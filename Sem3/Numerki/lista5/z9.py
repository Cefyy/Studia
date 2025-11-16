import math

def ouern_method(f, f_prime, f_double_prime, x0, tol=1e-15, max_iter=1000):
    x = x0
    iterations = [x]
    
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        fppx = f_double_prime(x)
        
        if abs(fpx) < 1e-15:
            break
            
        delta_n = fx / fpx
        correction = 0.5 * (fppx / fpx) * (delta_n ** 2)
        x_new = x - delta_n - correction
        
        iterations.append(x_new)
        
        if abs(x_new - x) < tol:
            break
            
        x = x_new
    
    return iterations

def calculate_convergence_order(iterations):
    p_values = []
    n = len(iterations)
    
    if n < 4:
        return p_values
    
    for i in range(2, n-1):
        diff1 = abs(iterations[i+1] - iterations[i])
        diff2 = abs(iterations[i] - iterations[i-1])
        diff3 = abs(iterations[i-1] - iterations[i-2])
        
        if diff2 < 1e-15 or diff3 < 1e-15:
            continue
            
        ratio1 = diff1 / diff2
        ratio2 = diff2 / diff3
        
        if ratio1 > 0 and ratio2 > 0:
            p = math.log(ratio1) / math.log(ratio2)
            p_values.append(p)
    
    return p_values

def f1(x): return x**2 - 2
def f1_prime(x): return 2*x
def f1_double_prime(x): return 2

def f2(x): return x**3 - 2*x - 5
def f2_prime(x): return 3*x**2 - 2
def f2_double_prime(x): return 6*x

def f3(x): return math.sin(x) - x/2
def f3_prime(x): return math.cos(x) - 0.5
def f3_double_prime(x): return -math.sin(x)

def f4(x): return math.exp(x) + x - 2
def f4_prime(x): return math.exp(x) + 1
def f4_double_prime(x): return math.exp(x)

# Test 1
iterations1 = ouern_method(f1, f1_prime, f1_double_prime, 1.5)
p_values1 = calculate_convergence_order(iterations1)
print(f"p={p_values1[0]:.50f}")

# Test 2
iterations2 = ouern_method(f2, f2_prime, f2_double_prime, 2.0)
p_values2 = calculate_convergence_order(iterations2)
print(f"p={p_values2[0]:.50f}")

# Test 3
iterations3 = ouern_method(f3, f3_prime, f3_double_prime, 2.0)
p_values3 = calculate_convergence_order(iterations3)
print(f"p={p_values3[0]:.50f}")

# Test 4
iterations4 = ouern_method(f4, f4_prime, f4_double_prime, 1.0)
p_values4 = calculate_convergence_order(iterations4)
print(f"p={p_values4[0]:.50f}")