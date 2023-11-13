# Alx School - 0x12-javascript-warm_up
Introduction to Javascript

## Project Description
Learn how to run a JavaScript script.
How to create variables and constants.
What are differences between `var`, `const` and `let`.
What are all the data types available in JavaScript.
How to use the `if`, `if ... else` statements.
How to use comments.
How to affect values to variables.
How to use `while` and `for` loops.
How to use `break` and `continue` statements.
What is a function and how do you use functions.print?
What does a function that does not use any `return` statement return.
Scope of variables.
What are the arithmetic operators and how to use them.
How to manipulate dictionary.
How to import a file.

## New Methods and strucutres
* ``for i in array`` -- returns index,
* ``for i of array`` -- returns value of array item
* ``array.forEach()`` -- applies a method on each item in the array
* ``console.log("hello").repeat``

## Helpful Links
* [Javascript Fundamentals](https://docs.microsoft.com/en-us/scripting/javascript/javascript-fundamentals)
* [Writing JS Code](https://docs.microsoft.com/en-us/scripting/javascript/writing-javascript-code)
* [Variables in Javascript](https://docs.microsoft.com/en-us/scripting/javascript/variables-javascript)
* [JS Datatypes](https://docs.microsoft.com/en-us/scripting/javascript/data-types-javascript)
* [Javascript Operators](https://docs.microsoft.com/en-us/scripting/javascript/operators-javascript)
* [Subtract operator precedence](https://docs.microsoft.com/en-us/scripting/javascript/operator-subtractprecedence-javascript)
* [Controlling program flow](https://docs.microsoft.com/en-us/scripting/javascript/controlling-program-flow-javascript)
* [JS functions](https://docs.microsoft.com/en-us/scripting/javascript/functions-javascript)
* [Objects and arrays](https://docs.microsoft.com/en-us/scripting/javascript/objects-and-arrays-javascript)
* [Intrinsic Objects](https://docs.microsoft.com/en-us/scripting/javascript/intrinsic-objects-javascript)
* [Module patterns Github](http://darrenderidder.github.io/talks/ModulePatterns/#/)
* [Youtube: JS tutorial](https://www.youtube.com/watch?v=sjyJBL5fkp8)
* [Youtube: Var, Let and Const](https://www.youtube.com/watch?v=vZBCTc9zHtI)
* [Var vs Const vs Let](https://medium.com/javascript-scene/javascript-es6-var-let-or-const-ba58b8dcde75)
* [Node Require and Exports](http://openmymind.net/2012/2/3/Node-Require-and-Exports/)

##  Requirements

### JavaScript Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x).
*   All your files should end with a new line.
*   The `main.js` files are used to test your functions, but you don’t have to push them to your repo.
*   The first line of all your files should be exactly `#!/usr/bin/node`.
*   Your code should be `semistandard` compliant (version 16.x.x).
*   All your files must be executable.
*   The length of your files will be tested using `wc`.

## More Info
### Install Node 14
```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard
[Documentation](https://github.com/standard/semistandard)
```
$ sudo npm install semistandard --global
```


* **0. First constant, first print** - Write a script that prints “JavaScript is amazing”. - `0-javascript_is_amazing.js`.
* **1. 3 languages** - Write a script that prints 3 lines. - `1-multi_languages.js`.
* **2. Arguments** - Write a script that prints a message depending of the number of arguments passed. - `2-arguments.js`.
* **3. Value of my argument** - Write a script that prints the first argument passed to it. - `3-value_argument.js`.
* **4. Create a sentence** - Write a script that prints two arguments passed to it, in the following format: “is”. - `4-concat.js`.
* **5. An Integer** - Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer. - `5-to_integer.js`.
* **6. Loop to languages** - Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop. - `6-multi_languages_loop.js`.
* **7. I love C** - Write a script that prints `x` times “C is fun”. - `7-multi_c.js`.
* **8. Square** - Write a script that prints a square. - `8-square.js`.
* **9. Add** - Write a script that prints the addition of 2 integers. - `9-add.js`.
* **10. Factorial** - Write a script that computes and prints a factorial. - `10-factorial.js`.
* **11. Second biggest!** - Write a script that searches the second biggest integer in the list of arguments. - `11-second_biggest.js`.
* **12. Object** - Update this script to replace the value `12` with `89`. - `12-object.js`.
* **13. Add file** - Write a function that returns the addition of 2 integers. - `13-add.js`.
* **14. Const or not const** - Write a file that modifies the value of `myVar` to `333`. - `100-let_me_const.js`.
* **15. Call me Moby** - Write a function that executes `x` times a function. - `101-call_me_moby.js`.
* **16. Add me maybe** - Write a function that increments and calls a function. - `102-add_me_maybe.js`.
* **17. Increment object** - Update this script by adding a new function `incr` that increments the integer `value`. - `103-object_fct.js`.
