public class Pair implements Cloneable {
    public final String key;
    private double value;

    public Pair(String key, double value)
    {
        if(key == null || key.equals(""))
        {
            throw new IllegalArgumentException("Key can't be empty or null");
        }
        this.key = key.toLowerCase();
        this.value = value;
    }
    public double get()
    {
        return value;
    }
    
    public void set(double value)
    {
        this.value = value;
    }
    @Override
    public String toString()
    {
        return ("(" + key + ": " + value + ")");
    }
    
    @Override
    public boolean equals(Object obj)
    {
        if (this == obj) return true;
        if (obj == null || !(obj instanceof Pair)) return false;
        
        Pair other = (Pair) obj;
        return this.key.equals(other.key);
    }
    
    @Override
    protected Object clone() throws CloneNotSupportedException {
        
        return super.clone();
    }
    

}
