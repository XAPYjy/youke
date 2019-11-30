# 向目标地址下载最新的ubuntu
FROM 47.92.132.161:8888/ubuntu-dev
## 添加一个作者(自定义)
MAINTAINER cys
## 目标路径
WORKDIR /usr/src/
## 从Git上克隆文件到项目的目标地址中
ADD . /usr/src/youke
## 做一个数据卷, 将上面的目录映射出去(地址暴露出去)
WORKDIR /usr/src/youke
VOLUME /usr/src/youke
## 从阿里云仓库安装gunicorn
RUN pip install gunicorn -i https://mirrors.aliyun.com/pypi/simple
## 从阿里云仓库安装requirements.txt文件中的各种库和插件
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
## 运行runn.sh脚本, 并给他加可执行权限
RUN chmod +x run.sh
CMD /usr/src/youke/run.sh
