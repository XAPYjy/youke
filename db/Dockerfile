FROM 47.92.132.161/ubtu:latest
MAINTAINER cys 724553598@qq.com
WORKDIR /usr/src
ADD . /usr/src/youke
VOLUME /usr/src/youke
WORKDIR /usr/src/youke
RUN pip install gunicorn -i https://mirrors.aliyun.com/pypi/simple
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN chmod +x run.sh
CMD /usr/src/youke/run.sh
