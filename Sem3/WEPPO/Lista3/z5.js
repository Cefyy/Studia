function createGenerator(top) {
  var _state = 0;
  return {
    next: function () {
      return {
        value: _state,
        done: _state++ >= top
      };
    },
  };
}

var foo = {
[Symbol.iterator] : function()
{return createGenerator(10)}
};
var foo2 = {
    [Symbol.iterator] : function()
    {
        return createGenerator(42)
    }
}

for ( var f of foo )
console.log(f);
for ( var f of foo2 )
console.log(f);
