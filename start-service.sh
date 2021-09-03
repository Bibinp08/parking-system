#!/bin/bash

python receive.py &
flask run --host=0.0.0.0
