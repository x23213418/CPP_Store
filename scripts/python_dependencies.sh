#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install -r /home/ubuntu/furniture/requirements.txt
sudo chmod 777 /home/ubuntu/furniture
sudo chmod 777 /home/ubuntu/furniture/db.sqlite3