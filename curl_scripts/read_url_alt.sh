#!/bin/bash

curl -i -X POST http://127.0.0.1:5000/api_alt/read/url -H "Content-Type: application/json" -d '{"url": "https://media.istockphoto.com/id/1052448556/vector/business-men-and-women-group-of-people-at-work-isolated-vector-silhouettes.jpg?s=612x612&w=0&k=20&c=yL8qENiPcN0lxqpFsw6l6llcjQbbixbS8KHAA6nDpzg="}'
