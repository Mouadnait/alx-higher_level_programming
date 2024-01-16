# Alx School - 0x15-javascript-web_jquery
Intro to JQUERY

## Project Description
Learn why JQuery makes front-end programming so easy.
How to select HTML elements in JavaScript.
How to select HTML elements with JQuery.
What are differences between `ID`, `class` and `tag name` selectors.
How to modify an HTML element style.
How to get and update an HTML element content.
How to modify the DOM.
How to make a GET request with JQuery Ajax.
How to make a POST request with JQuery Ajax.
How to listen/bind to DOM events.

## New commands / functions used:
* ``semistandard *.js --global $`` -- Check JQUERY style with this command
* ``document.querySelectorAll('header')`` -- Grabs all tags called header.
* ``$('header').toggleClass('red')`` -- Turns a class on or off
* ``$.each(data.results, (key, value) => { $('ul#list').append.$('<li></li>').text(data.results[key].title); } });`` -- operates on each JSON key-value pair.

## Helpful Links
* [What is Javascript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
* [JQuery: Using ids and classes](http://www.jquery-tutorial.net/selectors/using-elements-ids-and-classes/)
* [JQuery: Getting and setting Content](http://www.jquery-tutorial.net/dom-manipulation/getting-and-setting-content/)
* [JQuery: Getting and setting CSS Classes](http://www.jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/)
* [JQuery: Append and prepend methods](http://www.jquery-tutorial.net/dom-manipulation/the-append-and-prepend-methods/)
* [Intro to Ajax](http://www.jquery-tutorial.net/ajax/introduction/)
* [Ajax: Get and Post methods](http://www.jquery-tutorial.net/ajax/the-get-and-post-methods/)
* [What goes wrong in JS](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
* [JQuery website](https://jquery.com)
* [JQuery API](http://api.jquery.com)
* [JQuery / Ajax tutorial](https://learn.jquery.com/ajax/)

##  Requirements
### scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x).
*   All your files should end with a new line.
*   The `main.js` files are used to test your functions, but you don’t have to push them to your repo.
*   The first line of all your files should be exactly `#!/usr/bin/node`.
*   Your code should be `semistandard` compliant (version 16.x.x).
*   All your files must be executable.
*   The length of your files will be tested using `wc`.
*   You are not allowed to use `var`.

## More Info
### Import JQuery
```
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

### Install semi-standard
[Documentation](https://github.com/standard/semistandard)
```
$ sudo npm install semistandard --global
```

## Description of Tasks
* **0. Readme** - Write a script that reads and prints the content of a file.. - `0-script.js`.
* **1. With JQuery** - Write a script that updates the text color of the `<header>` element to red (`#FF0000`). - `1-script.js`.
* **2. Click and turn red** - Write a script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`. - `2-script.js`.
* **3. Add `.red` class** - Write a script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`. - `3-script.js`.
* **4. Toggle classes** - Write a script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`. - `4-script.js`.
* **5. List of elements** - Write a script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`. - `5-script.js`.
* **6. Change the text** - Write a script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header`. - `6-script.js`.
* **7. Star wars character** - Write a script that fetches the character name from this URL: `https://swapi-api.alx-tools.com/api/people/5/?format=json`. - `7-script.js`.
* **8. Star Wars movies** - Write a script that fetches and lists the `title` for all movies by using this URL: `https://swapi-api.alx-tools.com/api/films/?format=json`. - `8-script.js`.
* **9. Say Hello!** - Write a script that fetches from `https://fourtonfish.com/hellosalut/?lang=fr` and displays the value of `hello` from that fetch in the HTML tag `DIV#hello`. - `9-script.js`.
* **10. No jQuery - document loaded** - Write a script that updates the text color of the `<header>` element to red (`#FF0000`). - `100-script.js`.
* **11. List, add, remove** - Write a script that adds, removes and clears `LI` elements from a list when the user clicks. - `101-script.js`.
* **12. Say hello to everybody!** - Write a script that fetches and prints how to say “Hello” depending on the language. - `102-script.js`.
* **13. And press ENTER?** - Write a script that fetches and prints how to say “Hello” depending on the language. - `103-script.js`.
