const express = require('express');
const bodyParser = require('body-parser');
const session = require('express-session');
const app = express();


app.set('view engine', 'ejs');


app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({
    secret: 'tajne_haslo',
    resave: false,
    saveUninitialized: true
}));


app.get('/', (req, res) => {

    const error = req.session.error;
    const formData = req.session.formData || {};
    req.session.error = null;
    
    res.render('index', { error, formData });
});


app.post('/submit', (req, res) => {
    const { firstname, lastname, course } = req.body;

    let tasks = [];
    for(let i=1; i<=10; i++) {
        let val = req.body[`task${i}`];
        tasks.push(val ? parseInt(val) : 0);
    }


    if (!firstname || !lastname || !course) {
        req.session.error = "Błąd: Imię, nazwisko i nazwa zajęć są wymagane!";
        req.session.formData = req.body; 
        return res.redirect('/');
    }


    req.session.printData = {
        firstname,
        lastname,
        course,
        tasks
    };
    
    res.redirect('/print');
});

app.get('/print', (req, res) => {
    const data = req.session.printData;
    if (!data) return res.redirect('/');
    
    res.render('print', { data });
});

app.listen(3000, () => {
    console.log('Aplikacja działa na http://localhost:3000');
});