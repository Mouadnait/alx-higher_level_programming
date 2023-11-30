#!/bin/bash
# send a resquest and display the size of the response body
curl -sI $1 | grep -i Content-length | awk '{print $2}'