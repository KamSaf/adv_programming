#!/bin/bash

curl -i -X POST http://127.0.0.1:5000/api_alt/upload -F "file=@../examples/example.jpg"
