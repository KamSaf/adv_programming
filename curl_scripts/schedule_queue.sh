#!/bin/bash

for ((i=1; i<=1000; i++))
do
  curl -i -X GET http://127.0.0.1:5000/api_alt/read/file/image.jpg
done
