input1 = document.querySelector("#num1");
input2 = document.querySelector("#num2");
operationBtns = document.querySelectorAll(".operation");
resultTxt = document.querySelector("#result");

let result = 0;

operationBtns.forEach(btn => {
    btn.addEventListener('click', (e) =>
        {

            let btnId = e.target.id;
            let num1 = Number(input1.value);
            let num2 = Number(input2.value);

            calculate(num1, num2, btnId);

            resultTxt.textContent = `Результат: ${calculate()}`;
        })
});
function calculate(num1, num2, operation)
{
    switch (operation) 
    {
        case 'plus':
            result = result + num1 + num2;
            break;
        case 'minus':
            result = num1 - num2;
            break;
        case 'multiply':
            result = num1 * num2;
            break;
        case 'divide':
            if (num2 == 0)
                {
                    result = 'Ошибка. Деление на ноль.';
                    break;
                } 
            result = num1 / num2;
            break;
        case 'power':
            result = num1 ** num2;
            break; 
        
    }
    return result;
    
}
