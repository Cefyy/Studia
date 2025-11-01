from abc import ABC, abstractmethod

class Formula(ABC):
    @abstractmethod
    def oblicz(self,variables):
        pass
    @abstractmethod
    def uprosc(self):
        pass
    def __add__(self,other):
        return Or(self,other)
    def __mul__(self,other):
        return And(self,other)
    
    def tautologia(self):
        import itertools
        variables = sorted(self.get_variables())
        for values in itertools.product([False,True],repeat=len(variables)):
            env = dict(zip(variables,values))
            if not self.oblicz(env):
                return False
        return True

class And(Formula):
    def __init__(self,left,right):
        self.left=left
        self.right=right
    def oblicz(self, variables):
        return self.left.oblicz(variables) and self.right.oblicz(variables)
    def __str__(self):
        return f"({self.left} ∧ {self.right})"
    def get_variables(self):
        return self.left.get_variables() | self.right.get_variables()
    
    def uprosc(self):
        self.left = self.left.uprosc()
        self.right = self.right.uprosc()
        if isinstance(self.left,Stala) and not self.left.value:
            return Stala(False)
        if isinstance(self.right,Stala) and not self.right.value:
            return Stala(False)
        return self
        
class Or(Formula):
    def __init__(self,left,right):
        self.left=left
        self.right=right
        
    def oblicz(self, variables):
        return self.left.oblicz(variables) or self.right.oblicz(variables)
    
    def __str__(self):
        return f"({self.left} ∨ {self.right})"
    
    def get_variables(self):
        return self.left.get_variables() | self.right.get_variables()
    
    
    def uprosc(self):
        self.left = self.left.uprosc()
        self.right = self.right.uprosc()
        if isinstance(self.left,Stala) and not self.left.value:
            return self.right
        if isinstance(self.right,Stala) and not self.right.value:
            return self.left
        if isinstance(self.left,Stala) and self.left.value:
            return Stala(True)
        if isinstance(self.right,Stala) and self.right.value:
            return Stala(True)
        return self
class Zmienna(Formula):
    def __init__(self,name):
        self.name=name
        
    def oblicz(self,variables):
        if self.name not in variables:
            raise ValueError(f"No variable named {self.name}")
        else:
            return variables[self.name]
        
    def __str__(self):
        return self.name
    def get_variables(self):
        return {self.name}
    
    def uprosc(self):
        return self
    
class Not(Formula):
    def __init__(self,form):
        self.form = form
    
    def oblicz(self,variables):
        return not self.form.oblicz(variables)
    def __str__(self):
        return f"¬({self.form})"
    
    def get_variables(self):
        return self.form.get_variables()
    
    def uprosc(self):
        return self

        
class Stala(Formula):
    def __init__(self,value : bool):
        self.value = value  
    def oblicz(self,variables):
        return self.value
    def __str__(self):
        return "true" if self.value  else "false"
    def get_variables(self):
        return set()
    def uprosc(self):
        return self
        
          
if __name__ == "__main__":
    
    
    print("Test 1: ¬x ∨ x")
    f1 = Or(Not(Zmienna("x")), Zmienna("x"))
    print("Formuła:", f1)
    print("Tautologia:", f1.tautologia())
    print("-" * 40)

    # Test 2 – x ∧ ¬x (sprzeczność)
    print("Test 2: x ∧ ¬x")
    f2 = And(Zmienna("x"), Not(Zmienna("x")))
    print("Formuła:", f2)
    print("Tautologia:", f2.tautologia())
    print("-" * 40)

    # Test 3 – x ∨ (x ∧ y)
    print("Test 3: x ∨ (x ∧ y)")
    f3 = Or(Zmienna("x"), And(Zmienna("x"), Zmienna("y")))
    print("Formuła:", f3)
    print("Tautologia:", f3.tautologia())
    print("-" * 40)

    # Test 4 – p ∨ false (uproszczenie)
    print("Test 4: p ∨ false (uproszczenie)")
    f4 = Or(Zmienna("p"), Stala(False))
    print("Przed uproszczeniem:", f4)
    f4_simple = f4.uprosc()
    print("Po uproszczeniu:", f4_simple)
    print("-" * 40)

    # Test 5 – p ∧ true (uproszczenie)
    print("Test 5: p ∧ true (uproszczenie)")
    f5 = And(Zmienna("p"), Stala(True))
    print("Przed uproszczeniem:", f5)
    f5_simple = f5.uprosc()
    print("Po uproszczeniu:", f5_simple)
    print("-" * 40)
    
    f6 = f5 * f4 * f4
    print(f6)
    print(f6.uprosc())
    