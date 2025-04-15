#!/bin/bash
cd /home/ubuntu/flask-app
source venv/bin/activate
nohup python3 app.py > app.log 2>&1 &
