// 01. comment in javascript

// this is in-line comment.

/*
This is a
multi line comment.
*/

// 02. how to declare variables in javascript

var ourName;

// 03. storing values with the Assignment operator

myVariable = 5;

myVar = 5;
myNum = myVar;

// 04. initializing variables with the assignment operator.
var myVar = 0;
console.log(myVar);

// 05. understanding uninitialized variables
var a = 5;
var b = 10;
var c = "I am a";

a = a + 1;
b = b + 5;
c = c + "String!";

console.log(a);
console.log(b);
console.log(c);

// 06. Understanding Case sensitivity in Variables.

// undefined Variables output because its doesn't contain any values
var someVariable;
var anotherVariable;
var thisVariableNameIsSoLong;

var studlyCapVar = 10;
var properCamelCase = "A String";
var titleCaseOver = 9000;

console.log(someVariable);
console.log(anotherVariable);
console.log(thisVariableNameIsSoLong);

console.log(studlyCapVar);
console.log(properCamelCase);
console.log(titleCaseOver);

// 07. add two numbers in javascript

myVar = 5 + 10;
console.log(myVar);

var sum = 10 + 10;
console.log(sum);

// 08. subtract one number from another with javascript

var diff = 12 - 6;
console.log(diff);

// 09. multiply numbers with javascript

var multiply = 13 * 13;
console.log(multiply);

/*
data types:
undefined, null, boolean, string, number, symbol, add object
*/

var myName = "rachamt";
var myFloat = true;
var myNumber = 10000;
var myArray = ["Global", 100];
var myArrayNested = [
  ["global", 1000],
  ["universe", 2000],
];

console.log(myName);
console.log(myFloat);
console.log(myNumber);
console.log(myArray);
console.log(myArrayNested);

// 3 types of declaring variables

var a = 10000;
var b = 2;

let e = "string";

const pi = 3.14;

console.log(a, b);
console.log(e);
console.log(pi);

// initializing variable to initial value

var f = 9;

// uninitialize variable

var a;
var b;
var c;

// declaration

var studlyCapVar;
var properCamelCase;
var titleCaseOver;

// assignment
studlyCapVar = 10;
properCamelCase = "A string";
titleCaseOver = 9000;

// adding numbers with +
var a = 10 + 10;
console.log(a);

// subtracting numbers with -
var b = 20 - 10;
console.log(b);

// multiply numbers with *
var c = 100 * 10.0;
console.log(c);

// deviding numbers with /
var d = 100 / 2;
console.log(d);

// reminder of numbers with %
var f = 10 % 4;
console.log(f);

// increment numbers with ++
var g = 10;
g++;
console.log(g);

// decrementing numbers with --
var h = 200;
h--;
console.log(h);

// decimal number with .
var ourDecimal = 5.7;
console.log(ourDecimal);

// operating decimal
console.log(ourDecimal + 10);
console.log(ourDecimal - 2);
console.log(ourDecimal * 10);
console.log(ourDecimal / 3);

// compound operator

console.log("\ncompund operator");
var ourNumber = 100;
ourNumber += 10;
console.log(ourNumber);

ourNumber -= 10;
console.log(ourNumber);

ourNumber *= 10;
console.log(ourNumber);

ourNumber /= 10;
console.log(ourNumber);

// declare string variable

var firstName = "Agus";
var lastName = "Roe";

var myFirstName = "Beau";
var myLastName = "folks";

// escape characters
var myStr = 'I am a "double quoted" string inside "double quoted"';
console.log(myStr);

var myStr = '<a href="http://www.example.com>" target="_blank">Link</a>';
console.log(myStr);

// escaping sequences in Strings
