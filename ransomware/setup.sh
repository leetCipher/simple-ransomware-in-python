#!/bin/bash
apt-get update -y
apt-get install build-essential python3-dev -y
apt-get install python3-pip -y
pip3 install -r requirements.txt
