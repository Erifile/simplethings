// let total = 500;


// function applyDiscount(sum) 
// {
//   return sum - (sum * 0.15); // Скидка 15% от текущей суммы
// }

// function addDelivery(sum) 
// {
//   return sum + 350; // Добавляем доставку
// }

// function showResult(result) 
// {
//   console.log("Итоговая сумма заказа: " + result);
// }

// // Цепочка: берем total -> считаем скидку -> добавляем доставку -> выводим
// let step1 = applyDiscount(total);
// let step2 = addDelivery(step1);
// showResult(step2); 

let price = prompt();

function addDelivery(sum)
{
    if (sum < 3000) sum = sum + 350;
    if (sum >= 3000) sum = sum - (sum*0.10);
    return sum;
}
withDelivery = addDelivery(price);
console.log(withDelivery)