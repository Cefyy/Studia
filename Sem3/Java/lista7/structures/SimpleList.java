package structures;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class SimpleList<T extends Comparable<T>> implements SimpleSequence<T>, Iterable<T> {
    
    private class SimpleNode {
        private SimpleNode prev, next;
        T data;
        
        SimpleNode(T data) {
            this.data = data;
            this.prev = null;
            this.next = null;
        }
        
        void insert(T el, int pos) {
            if (pos == 0) {
                SimpleNode newNode = new SimpleNode(el);
                newNode.next = this;
                if (this.prev != null) {
                    this.prev.next = newNode;
                    newNode.prev = this.prev;
                }
                this.prev = newNode;
                return;
            }
            
            if (this.next == null) {
                if (pos == 1) {
                    SimpleNode newNode = new SimpleNode(el);
                    this.next = newNode;
                    newNode.prev = this;
                } else {
                    throw new IndexOutOfBoundsException("Position out of bounds: " + pos);
                }
            } else {
                this.next.insert(el, pos - 1);
            }
        }
        
        boolean remove(T el) {
            if (this.data.equals(el)) {
                if (this.prev != null) {
                    this.prev.next = this.next;
                }
                if (this.next != null) {
                    this.next.prev = this.prev;
                }
                return true;
            }
            
            if (this.next == null) {
                return false;
            }
            
            return this.next.remove(el);
        }
        
        SimpleNode removeAt(int pos) {
            if (pos == 0) {
                if (this.prev != null) {
                    this.prev.next = this.next;
                }
                if (this.next != null) {
                    this.next.prev = this.prev;
                }
                return this.next;
            }
            
            if (this.next == null) {
                throw new IndexOutOfBoundsException("Position out of bounds: " + pos);
            }
            
            this.next = this.next.removeAt(pos - 1);
            return this;
        }
        
        T min() {
            T minVal = this.data;
            if (this.next != null) {
                T nextMin = this.next.min();
                if (nextMin.compareTo(minVal) < 0) {
                    minVal = nextMin;
                }
            }
            return minVal;
        }
        
        T max() {
            T maxVal = this.data;
            if (this.next != null) {
                T nextMax = this.next.max();
                if (nextMax.compareTo(maxVal) > 0) {
                    maxVal = nextMax;
                }
            }
            return maxVal;
        }
        
        boolean search(T el) {
            if (this.data.equals(el)) {
                return true;
            }
            if (this.next == null) {
                return false;
            }
            return this.next.search(el);
        }
        
        T at(int pos) {
            if (pos == 0) {
                return this.data;
            }
            if (this.next == null) {
                throw new IndexOutOfBoundsException("Position out of bounds: " + pos);
            }
            return this.next.at(pos - 1);
        }
        
        int index(T el, int currentPos) {
            if (this.data.equals(el)) {
                return currentPos;
            }
            if (this.next == null) {
                return -1;
            }
            return this.next.index(el, currentPos + 1);
        }
        
        int size() {
            if (this.next == null) {
                return 1;
            }
            return 1 + this.next.size();
        }
    }
    
    private class SimpleListIterator implements Iterator<T> {
        private SimpleNode current;
        private int expectedModCount;
        
        SimpleListIterator() {
            this.current = head;
            this.expectedModCount = modCount;
        }
        
        @Override
        public boolean hasNext() {
            if (expectedModCount != modCount) {
                throw new IllegalStateException("List was modified during iteration");
            }
            return current != null;
        }
        
        @Override
        public T next() {
            if (!hasNext()) {
                throw new NoSuchElementException("No more elements in the list");
            }
            T data = current.data;
            current = current.next;
            return data;
        }
    }
    
    private SimpleNode head;
    private int modCount;
    
    public SimpleList() {
        this.head = null;
        this.modCount = 0;
    }
    
    @Override
    public void insert(T el, int pos) {
        if (el == null) {
            throw new NullPointerException("Cannot insert null element");
        }
        if (pos < 0) {
            throw new IndexOutOfBoundsException("Position cannot be negative: " + pos);
        }
        
        if (head == null) {
            if (pos != 0) {
                throw new IndexOutOfBoundsException("Position out of bounds: " + pos);
            }
            head = new SimpleNode(el);
        } else {
            if (pos == 0) {
                SimpleNode newNode = new SimpleNode(el);
                newNode.next = head;
                head.prev = newNode;
                head = newNode;
            } else {
                head.insert(el, pos);
            }
        }
        modCount++;
    }
    
    @Override
    public void remove(T el) {
        if (el == null) {
            throw new NullPointerException("Cannot remove null element");
        }
        if (head == null) {
            return;
        }
        
        if (head.data.equals(el)) {
            head = head.next;
            if (head != null) {
                head.prev = null;
            }
            modCount++;
            return;
        }
        
        if (head.remove(el)) {
            modCount++;
        }
    }
    
    @Override
    public void remove(int pos) {
        if (pos < 0) {
            throw new IndexOutOfBoundsException("Position cannot be negative: " + pos);
        }
        if (head == null) {
            throw new IndexOutOfBoundsException("List is empty");
        }
        
        if (pos == 0) {
            head = head.next;
            if (head != null) {
                head.prev = null;
            }
        } else {
            head = head.removeAt(pos);
        }
        modCount++;
    }
    
    @Override
    public T min() {
        if (head == null) {
            throw new NoSuchElementException("List is empty");
        }
        return head.min();
    }
    
    @Override
    public T max() {
        if (head == null) {
            throw new NoSuchElementException("List is empty");
        }
        return head.max();
    }
    
    @Override
    public boolean search(T el) {
        if (el == null) {
            throw new NullPointerException("Cannot search for null element");
        }
        if (head == null) {
            return false;
        }
        return head.search(el);
    }
    
    @Override
    public T at(int pos) {
        if (pos < 0) {
            throw new IndexOutOfBoundsException("Position cannot be negative: " + pos);
        }
        if (head == null) {
            throw new IndexOutOfBoundsException("List is empty");
        }
        return head.at(pos);
    }
    
    @Override
    public int index(T el) {
        if (el == null) {
            throw new NullPointerException("Cannot find index of null element");
        }
        if (head == null) {
            return -1;
        }
        return head.index(el, 0);
    }
    
    @Override
    public int size() {
        if (head == null) {
            return 0;
        }
        return head.size();
    }
    
    @Override
    public boolean empty() {
        return head == null;
    }
    
    @Override
    public Iterator<T> iterator() {
        return new SimpleListIterator();
    }
    
    @Override
    public String toString() {
        if (head == null) {
            return "[]";
        }
        
        StringBuilder sb = new StringBuilder("[");
        SimpleNode current = head;
        while (current != null) {
            sb.append(current.data);
            if (current.next != null) {
                sb.append(", ");
            }
            current = current.next;
        }
        sb.append("]");
        return sb.toString();
    }
}
