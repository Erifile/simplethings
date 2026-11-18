const listDiv = document.querySelector("#booksList");
const addForm = document.querySelector("#add-book");
const inputSearch = document.querySelector("#search");
const searchBtn = document.querySelector("#searchBtn");
const searchStatus = document.querySelector("#search-status");
const availableCheckbox = document.querySelector("#isAvailable");

// books меняется формой и явл. полным списком книг в текущей сессии до ф5
// currentList - текущий отфильтрованный books, которое ищет пользователь

let currentList;

let books = [
 { id: 1, title: "Мастер и Маргарита",
 author: "Михаил Булгаков", year: 1967, available: true },
 { id: 2, title: "Преступление и наказание",
 author: "Фёдор Достоевский", year: 1866, available: false },
 { id: 3, title: "Евгений Онегин",
 author: "Александр Пушкин", year: 1833, available: true }
];

// принимает аргумент - массив с объектами.
loadList(books);

addForm.addEventListener("submit", (e) =>
    {
        e.preventDefault();

        // нахожд. input-ов через автом. массив формы elements
        let inputTitle = addForm.elements.title.value;
        let inputAuthor = addForm.elements.author.value;
        let inputYear = addForm.elements.year.value;

        let book = 
        {
            id: books.length+1,
            title: inputTitle,
            author: inputAuthor,
            year: inputYear,
            available: true // по умолч.
        }
        books.push(book);
        loadList(books);
    })


searchBtn.addEventListener("click", () =>
    {
        let inputTitle = inputSearch.value.toLowerCase();
        
        foundedBooks = books.filter(b => b.title.toLowerCase().includes(inputTitle));
        // передаем массив с запрошенными названиями
        if (foundedBooks.length > 0) {loadList(foundedBooks); searchStatus.textContent = "";}
        if (foundedBooks.length == 0) searchStatus.textContent = "Книг не найдено"
    })
availableCheckbox.addEventListener("change", () =>
    {
        if (availableCheckbox.checked)
            {
                // loadList() хранит list (т.к return)
                availableBooks = currentList.filter(b => b.available == true);

                if (availableBooks.length > 0) {loadList(availableBooks); searchStatus.textContent = "";}
                if (availableBooks.length == 0) searchStatus.textContent = "Книг в наличии нет";
            }
        if (!availableCheckbox.checked) {currentList = books; loadList(currentList);}
    })



function loadList(list)
{
    listDiv.innerHTML = "";
    
    list.forEach(b => {
        let bookDiv = document.createElement('div');
        bookDiv.classList.add("book");
        listDiv.appendChild(bookDiv);

        let title = document.createElement('p');
        title.classList.add("title");
        title.textContent = b.title;
        bookDiv.appendChild(title);
        
        let author = document.createElement('p');
        author.classList.add("author");
        author.textContent = b.author;
        bookDiv.appendChild(author);

        let year = document.createElement('p');
        year.classList.add("year");
        year.textContent = b.year;
        bookDiv.appendChild(year);

        let status = document.createElement('p');
        status.classList.add("status");
        if (b.available) {status.textContent = "В наличии"; status.style.color = "green";}
        if (!b.available) {status.textContent = "Выдана"; status.style.color = "red";}
        bookDiv.appendChild(status);

        let statusBtn = document.createElement('button');
        statusBtn.classList.add("statusBtn");
        statusBtn.textContent = "Изменить статус"
        statusBtn.addEventListener('click', (e) =>
            {
                e.preventDefault();

                if (b.available) {b.available = false; status.textContent = "Выдана"; status.style.color = "red"; return;}
                if (!b.available) {b.available = true; status.textContent = "В наличии"; status.style.color = "green"; return;}
            })
        bookDiv.appendChild(statusBtn);
    });
    currentList = list;
}