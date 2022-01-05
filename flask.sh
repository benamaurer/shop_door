#!/bin/bash

export FLASK_APP=responses
screen -S flask -d -m bash -c "cd ~/;flask run"
