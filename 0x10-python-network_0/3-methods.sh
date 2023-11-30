#!/bin.bash
# send an OPTIONS request and display the allowed HTTP methods
curl -sI "$1" -X OPTIONS | grep "Allow:" | cut -f2- -d" "
