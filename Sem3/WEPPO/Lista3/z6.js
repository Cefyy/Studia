function createIterator()
{
    var f1=0;
    var f2=1;
    return {
        next : function()
        {
            const value = f2 + f1;
            var temp = f2;
            f2 = value;
            f1 = temp;
            const done = false
            return {
                value,done
            }
        }
    }
}
function* createGenerator(){
   var f1 = 0
   yield f1
   var f2 = 1
    yield f2
   while(true)
   {
     var temp = f2
     f2 = f2+f1
     f1 = temp
     yield f2
   }
}

var it = createGenerator();
var i = 1
while (i<=10) {
  const { value, done } = it.next();
  if (done) break;
    i++
  console.log(value);
}

for ( var i of createGenerator() ) {
    console.log( i );
}