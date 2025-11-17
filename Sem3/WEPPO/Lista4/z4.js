var n = 1;

console.log( typeof Object.getPrototypeOf( n ) );

n.foo = "foo";
console.log( n.foo );

//liczby to prymitywy wiec nie są obiektami ale js tymczasowo wrappuje je w obiekty gdy chcemy ich uzyc jako obiekty
// int w Number string w String itd
// dlatego nie mozliwe jest dopisanie do niego czegokolwiek bo jest od razu usuwane

