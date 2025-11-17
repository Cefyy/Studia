function Person(name) {
    this.name = name;
}
Person.prototype.sayHello = function() {
    console.log("Hello, I'm " + this.name);
}

function Worker(name, job) {
    Person.call(this, name);
    this.job = job;
}

//Worke.prototype = Person.prototype /zle bo worker.prototype i person.prototype maja to samo miejsce w pamieci wiec modyfikuja sie oba obiekty
function Worker1(name, job) {
    Person.call(this, name);
    this.job = job;
}
Worker1.prototype = Person.prototype;
Worker1.prototype.work = function() { console.log("Working..."); }

var p1 = new Person("Jan");
p1.work(); 

// Worker.prototype = new Person()
// wywołujemy konstruktor bez parametrów moze pojawic sie blad
// nie dziedziczy tylko metod ale tez wartosci typu person.name ktore i tak zostaną nadpisane
// jesli konstruktor ma jakie console logi zapisy itd to tez je niepotrzebnie wywolamy
// tworzymy obiekt tylko po to zeby uzyc go jako prototypu wiec marnujemy pamiec
// zeby stworzyc lancuch prototypow nie musimy robic instancji obiektu
function Worker2(name, job) {
    Person.call(this, name);
    this.job = job;
}
Worker2.prototype = new Person();
console.log(Worker2.prototype.name);

// Object.create(person.prototype) //nie ma takiej sytuacji jak w 1. ani w 2.
function Worker3(name, job) {
    Person.call(this, name);
    this.job = job;
}
Worker3.prototype = Object.create(Person.prototype);
Worker3.prototype.work = function() { console.log("Working as " + this.job); }

var w = new Worker3("Anna", "developer");
w.sayHello();
w.work();
console.log(w.name);