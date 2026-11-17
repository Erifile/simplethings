const listDiv = document.querySelector("#booksList");
const addForm = document.querySelector("#add-book");
const inputSearch = document.querySelector("#search");
const searchBtn = document.querySelector("#searchBtn");
const searchStatus = document.querySelector("#search-status");



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
    });
}