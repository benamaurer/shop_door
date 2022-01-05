#!/bin/bash

screen -S ngrok -d -m bash -c "cd ~/;ngrok http 5000"
