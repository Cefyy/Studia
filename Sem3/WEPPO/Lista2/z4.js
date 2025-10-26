/*typeof zwraca prymitywne typy -> number,string,boolean,object jako string 
instanceof zwraca boolean czy obiekt został stworzony przed dany konstruktor 
np. Array, Object, Date itd.
ale nie działa z prymitywnymi
*/

console.log(typeof 5)
console.log(typeof "abc")
console.log(typeof true)
console.log(typeof [])





console.log([] instanceof Array)
console.log([] instanceof Object)

console.log(5 instanceof Number)
console.log(true instanceof Boolean)