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

for ( var f of foo )
console.log(f);
