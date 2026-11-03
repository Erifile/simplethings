const input = document.querySelector("input");
const addBtn = document.querySelector(".add");
const tasksOl = document.querySelector(".tasks");
const status = document.querySelector(".status");
tasks = [];

addBtn.addEventListener('click', () =>
    {
        
        task = input.value;
        if (tasks.includes(task))
            {
                status.textContent = "Ошибка. Задача уже создана.";
                return;
            }
        if (task == '')
            {
                status.textContent = "Ошибка. Введите текст задачи.";
                return;
            }
        tasks.push(task);
        taskLi = document.createElement('li');
        taskLi.textContent = task;
        tasksOl.appendChild(taskLi);

        let delBtn = document.createElement('button');
        delBtn.textContent = 'Удалить';
        delBtn.classList.add("delBtn");
        taskLi.appendChild(delBtn);

        delBtn.addEventListener('click', (e) =>
        {
            e.preventDefault();
            let taskLi = delBtn.closest('li');
            console.log(taskLi);
            let taskText = taskLi.firstChild.textContent.trim();
            console.log(taskText);
            let index = tasks.indexOf(taskText);
            tasks.splice(index, 1);
            tasksOl.removeChild(taskLi);
        });
        status.textContent = "";
        input.value = '';
    })


