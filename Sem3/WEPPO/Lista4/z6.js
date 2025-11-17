class Queue {
  constructor() {
    this.items = [];
  }

  push(element) {
    this.items.push(element); 
  }

  dequeue() {
    return this.isEmpty() ? "Queue is empty" : this.items.shift();
  }

  isEmpty() {
    return this.items.length === 0;
  }

  size() {
    return this.items.length;
  }

}

function Tree(val, left, right) {
this.left = left;
this.right = right;
this.val = val;
}


Tree.prototype[Symbol.iterator] = function*() {
    const queue = new Queue();
    queue.push(this);
    while(!queue.isEmpty())
    {
        const node = queue.dequeue();

        if(node.left) queue.push(node.left);
        if(node.right) queue.push(node.right);

        yield node.val
    }
}

var root = new Tree( 1,
new Tree( 2, new Tree( 3 ) ), new Tree( 4 ));
for ( var e of root ) {
console.log( e );
}
