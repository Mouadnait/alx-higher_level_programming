#!/bin/bash
<<<<<<< HEAD
# send a resquest and display the size of the response body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
=======
# gets the length of the body of an html get request
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
>>>>>>> 4c3bdf2ca79087458f6394d56e4a70132fc706ca
