#!/bin.bash
# send an OPTIONS request and display the allowed HTTP methods
curl -sI -X OPTIONS "$1" | awk -F ": " '/Allow/{print $2}'
