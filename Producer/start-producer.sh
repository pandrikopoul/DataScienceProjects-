#!/bin/bash

set -e


USAGE="
Usage: run.sh <topic>

    topic: The topic where messages are to be produced.
"

if ! (( $# > 0 )); then
    echo $USAGE
    exit -1
fi

topic="$1"







for i in {1..3}; do
    docker run \
        --rm \
        -v $(pwd)/auth:/usr/src/cc-assignment-2023/experiment-producer/auth \
        experiment-producer \
        --topic "$topic" &
done
