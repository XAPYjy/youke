#!/bin/sh

echo 'staring project'
cd /usr/src/youke
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
cd /usr/src/youke
gunicorn -w 1 -b 0.0.0.0:8888 youke.wsgi:application