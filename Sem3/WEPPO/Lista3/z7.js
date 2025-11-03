function createIterator()
{
    var f1=0;
    var f2=1;

    return {
        next : function()
        {
            var value = f2;
            var temp = f2;
            f2 = f2 + f1;
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
it = createIterator()
it1 = createGenerator()
function* take(it,top)
{
    while(top)
    {
        top--
        yield it.next()
    }
}

for (var i of take(it,10)) {
    console.log(i.value);
}
for(var i of take(it1,10))
{
    console.log(i.value)
}