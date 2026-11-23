let object = {name: "Фывфыв", age: 631, active: true};
let json = '{"name": "Фывфыв", "age": 631, "active": true}';

// тот же объект но в текстовом виде с '' кавычками
// названия свойств в "" кавычках


console.log(typeof(object)); // object
console.log(typeof(json)); // string


// JSON.stringify() принимает объект и превращает в json


let object1 = {name: "Фывфыввфывфв", age: 631, active: true}

JSON.stringify(object1);

user = '{"name": "Bob", "age": 13, "isAdmin": false, "hasGTA6": true}'

// если преобр. объект с особенными значениями в JSON некоторые не будут сохранены/преобразованны в null
// в силу ограничения других языков


// JSON.parse() принимает json и превращает в объект JS
console.log(typeof user);
userJS = JSON.parse(user);
console.log(typeof userJS);



//  LOCAL STORAGE - объект. все значения хранятся в самом браузере на ПК пользователя

// принимает ключ и значение
// привязываются к ПОРТУ и ДОМЕНУ (адресу страницы)
localStorage.setItem("theme", 'light');

let currentTheme = localStorage.getItem("theme");
// localStorage.removeItem('theme');
// очистка всего localStorage
// localStorage.clear()

localStorage.setItem("user", JSON.stringify(userJS));


const selectTheme = document.querySelector("#theme");
const body = document.querySelector("body");
selectTheme.addEventListener('change', () =>
    {
        if (localStorage.getItem('theme') == 'light') {localStorage.setItem('theme', 'dark'); body.style.backgroundColor = 'black'; return;}
        if (localStorage.getItem('theme') == 'dark') {localStorage.setItem('theme', 'light'); body.style.backgroundColor = 'white'; return;}
    })

