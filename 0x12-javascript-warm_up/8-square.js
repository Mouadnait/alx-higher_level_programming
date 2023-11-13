#!/usr/bin/node
const firstArgument = process.argv[2];
const number = parseInt(firstArgument);
if (!isNaN(number)) {
    for (let i = 0; i < number; i++) {
        let row = '';
        for (let j = 0; j < number; j++){
            row += 'X';
        }
        console.log(row);
    }
} else {
    console.log('Missing size');
}
