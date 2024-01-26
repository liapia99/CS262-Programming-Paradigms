var myArray= ['hello', 'world'];
console.log(myArray[0]);

// arrays with info

//for loop
for (var i=0; i<5; i++) // starts counting at 0 and goes up to 4
{
    console.log(i);
}

//while loop
var j = 0;

while (j<100){
    console.log("currently at:" + j);
    j++;
}


//do while loop

var k = 0;

do{
    k--;
    console.log("k" + k);
    if (k==-15){
        break;
    }


} while (true);


var myObject = {
 sayHello : function(){
    console.log("hello has been said");
 },

 addNumber : function(number1, number2){
    total = number1 + number2;
    return total;
 },
 myName : 'julia',
 myLastName : 'piascik'
}

console.log(myObject.addNumber(1,2));
console.log(myObject.sayHello);
console.log(myObject.myName);
