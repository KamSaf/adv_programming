#!/bin/bash

PYTHON_SCRIPT="src/consumer.py"
PIDS=$(pgrep -f "python3 $PYTHON_SCRIPT")

if [ -z "$PIDS" ]; then
    echo "No running consumer found: $PYTHON_SCRIPT"
    exit 0
fi

echo "Shutting down consumers...:"
echo "$PIDS"
kill $PIDS

if [ $? -eq 0 ]; then
    echo "All consumers have been shutted down."
else
    echo "An error occured while trying to shut down consumers."
fi
