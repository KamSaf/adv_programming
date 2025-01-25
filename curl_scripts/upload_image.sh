#!/bin/bash

curl -i -X POST http://127.0.0.1:5000/api/upload -F "file=@../examples/example.jpg"
