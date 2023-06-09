// Задача 2: Получить от пользователя два числа и вывести 
// в диалоговое окно сумму значений, которые ввел пользователь, 
// вывод должен выглядеть так (пример): 
// Результат сложения чисел 5 и 2 равен 7.


// const num1 = +prompt("input first number: "); // Можно применять к flout
// const num2 = parseInt(prompt("input second number: "));
// const num3 = Number.parseInt(prompt("input second number: "));

// // alert("Result: " + (num1 + num2))

// alert(`Result ${num1} + ${num2} + ${num3}= ${num1 + num2 + num3}`)

// Создать функцию

// function sum(number1, number2){
//     return number1 + number2; 
// }

// const num1 = +prompt("input first number: ");
// const num2 = +prompt("input first number: ");

// alert(`Result ${sum(num1, num2)}`);


// Задача 4: вывести на экран в диалоговом окне текст с сообщением 
// “Вам хорошо живется?”
// и кнопками «ОК», «Отмена», для чего необходимо использовать 
// confirm.
// - При нажатии на кнопку “ОК” вывести в диалоговом окне текст 
// с сообщением “Тогда мы идем к вам!”.
// - При нажатии на кнопку “Отмена” вывести в диалоговом окне 
// текст с сообщением “Ну вы держитесь там!”.

// VAR 1
// if (confirm("Вам хорошо живется?")){
//     alert("Тогда мы идем к вам!")
// }
// else{
//     alert("Ну вы держитесь там!")
// }

// VAR 2
// confirm("Вам хорошо живется?")
//     ? alert("Тогда мы идем к вам!")
//     : alert("Ну вы держитесь там!")

// VAR3
// alert(confirm("Вам хорошо живется?")? "Тогда мы идем к вам!":"Ну вы держитесь там!")



// const product = prompt("введите фрукты:")


// const product = promt("input a fruct").toLowerCase();
// switch (product) {
//     case "мандарины":
//         alert('мандарины стоят 100 руб/кг.');
//         break;
//     case "бананы":
//     case "груши":
//         alert('Бананы и груши стоят 70 руб/кг.');
//         break
//     default:
//         alert('Нет такого продукта.');
// }

// function getMaxEvenElement(arr) {
//     let max = arr[0];
//     for (let index = 2; index < arr.length; index += 2) {
//         if (max < arr[index]) {
//             max = arr[index];
//         }
//     }
//     return max;

// }

// console.log(getMaxEvenElement([5, 7, -1, 12, 3, 0])); // 5
// console.log(getMaxEvenElement([4, -12, 29, 6, 31, 92, -50])); // 31

// function f(clockArr, money) {
//     for (let i = 0; i < clockArr.length - 1; i++) {
//         for (let j = i + 1; j < clockArr.length; j++) {
//             if (Math.floor((clockArr[i] + clockArr[j]) * 100) / 100 == money) {
//                 return true;
//             }
//         }
//     }
//     return false;
// }

// console.log(f([8.74, 3.12, 9.50, 2.35], 2.35)); // false
// console.log(f([1.1, 4.2, 7.5, 0.4], 8.4)); // false
// console.log(f([54.10, 20.00, 18.51, 97.75, 35.20, 76.42], 89.3)); // true