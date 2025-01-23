#!/bin/bash

PYTHON_SCRIPT="run_consumer.py"
NUM_PROCESSES=3
DELAY=10

for ((i=1; i<=NUM_PROCESSES; i++)); do
    echo "Starting consumer $i..."
    python3 "$PYTHON_SCRIPT" --id=$i &
    sleep $DELAY
done

echo "All consumers have been started."
