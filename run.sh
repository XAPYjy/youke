#!/bin/bash

echo 'staring project'
cd /usr/src/youke
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
gunicorn -w 1 -b 0.0.0.0:5000 manage:app