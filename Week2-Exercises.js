console.log("Hello World!");
// single line comment 

/*
This is a
Multi line comment
*/

var aVariable = 'Hello World from our variable!';
console.log(aVariable);
// variable assignments


console.log(2 * 3 + 5);
console.log(2 * (3 + 5));
//arthiemetic operators


var greeting = function(){
    // any function instruction we want
    var number1 = 6;
    var numnber2 = 7;
    var total = number1 + numnber2;
    console.log("Our total is:" + total);

}

greeting();


var foo = "Hello";
var bar = "world";

console.log(foo + " " + bar + "!");

console.log(2*3);
console.log(2/3);

var i = 1;
var j = ++i;
var k = i++;
// increments and decrements

console.log("i:" + i, "\n", "j:" + j, "\n", "k:" + k);
// introduced \n for new lines and used , to seperate the print lines

var aNumber = 1;
var anotherNumber = '2';

console.log(aNumber + anotherNumber); //12

console.log(aNumber + Number(anotherNumber)); //3
// conversions from one data type to another


//boolean values
var a = 1;
var b = 0;
var c = 2;

console.log(a || b); // 1 is true 
// || is 'or' operator
console.log(c && b); // 0 is false
// && is 'and' operator
console.log(!a || b); // 0 is false
// ! is 'not' operator

/* 
== represents equal to 
!= represents not equal to
> represents greater than
>= represents greater than or equal to
< represents less than
<= represents less than or equal to
*/

var jeff;
jeff = 5;

if (jeff < 5)
{
    console.log("Jeff is less than 5");
} else if (jeff > 5){
    console.log("Jeff is greater than 5");
}
    else {
    console.log("Jeff is 5!");
}



var anArray = [];
var anObject = {};
// initializing an empty array and an empty object

let aChoice = "choice 3";
switch(aChoice){
    case 'choice 2':
        console.log("choice 2 was selected");
    break;

    case 'choice 1':
        console.log("choice 1 was selected");
    break;

    default:
        console.log("default choice was executed");
    break;

}


