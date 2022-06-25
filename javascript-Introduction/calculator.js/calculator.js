// program for a simple calculator in javascript without the frontend



//const prompt = require('prompt-sync')();

// take operator input
const startCalculator = () => {
	const operator = prompt('Please type in the math operation you would like to complete:\n'+
	'+ for addition\n' + '- for subtraction\n' + '* for multiplication\n' + '/ for division\n' +
	'% for modulus\n ');

	// take the operand input
	const number1 = parseFloat(prompt('Enter first number: '));
	const number2 = parseFloat(prompt('Enter second number: '));

	let result;

	if (operator == '+') {
    		result = number1 + number2;
	}
	else if (operator == '-') {
    		result = number1 - number2;
	}
	else if (operator == '*') {
    		result = number1 * number2;
	}
	else if (operator == '/') {
    		result = number1 / number2;
	}
	else if (operator == '%') {
    		result = number1 % number2;
	}
	else {
		console.log("You have not typed a valid operator, please run the program again.");
                alert("You have not typed a valid operator, please run the program again.");
		return "wrong operator !!";
	}
        alert(`${number1} ${operator} ${number2} = ${result}`);
	console.log(`${number1} ${operator} ${number2} = ${result}`);
}

//Add event to button
const button = document.querySelector('button');
button.addEventListener('click',e =>{
    startCalculator();
});

//call function
startCalculator();