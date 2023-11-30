#!/bin/bash
# Check if the script is provided with a URL argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# send a resquest and display the size of the response body
curl -sI "http://$1" | grep -i Content-length | awk '{print $2}'