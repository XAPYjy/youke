#!/bin/sh

echo 'staring project'
cd /usr/src/youke
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
cd /usr/src/youke
python manage runserver 47.92.132.161