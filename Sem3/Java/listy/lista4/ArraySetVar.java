public class ArraySetVar extends SetVar {
    protected Pair[] vars; 
    protected int size;   
    
    public ArraySetVar(int capacity) {
        this.vars = new Pair[capacity];
        this.size = 0;
    }
    
    @Override
    public void set(String k, double v) {
        for (int i = 0; i < size; i++) {
            if (vars[i].key.equals(k)) {
                vars[i].set(v);
                return;
            }
        }
        
        if (size >= vars.length) {
            Pair[] newVars = new Pair[vars.length * 2];
            for (int i = 0; i < size; i++) {
                newVars[i] = vars[i];
            }
            vars = newVars;
        }
        
        vars[size] = new Pair(k, v);
        size++;
    }
    
    @Override
    public double get(String k) {
        for (int i = 0; i < size; i++) {
            if (vars[i].key.equals(k)) {
                return vars[i].get();
            }
        }
        throw new IllegalArgumentException("Variable cannot be found");
    }
    
    @Override
    public boolean search(String k) {
        for (int i = 0; i < size; i++) {
            if (vars[i].key.equals(k)) {
                return true;
            }
        }
        return false;
    }
    
    @Override
    public String[] names() {
        String[] result = new String[size];
        for (int i = 0; i < size; i++) {
            result[i] = vars[i].key;
        }
        return result;
    }
    
    @Override
    public void del(String k) {
        for (int i = 0; i < size; i++) {
            if (vars[i].key.equals(k)) {
                for (int j = i; j < size - 1; j++) {
                    vars[j] = vars[j + 1];
                }
                vars[size - 1] = null;
                size--;
                return;
            }
        }
    }
    
    @Override
    public int size() {
        return size;
    }
    
    @Override
    public void clear() {
        for (int i = 0; i < size; i++) {
            vars[i] = null;
        }
        size = 0;
    }
    
    @Override
    public ArraySetVar clone() throws CloneNotSupportedException {
        ArraySetVar klon = new ArraySetVar(vars.length);
        
        for (int i = 0; i < size; i++) {
            klon.vars[i] = (Pair)vars[i].clone();
        }
        klon.size = size;
        
        return klon;
    }
    
    @Override
    public String toString() {
        return defaultToString();
    }
}