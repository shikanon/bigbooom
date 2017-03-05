FROM python:2-onbuild
MAINTAINER shikanon <shikanon@foxmail.com>

# 安装python库
ADD requirements.txt /opt/pyspider/requirements.txt
RUN pip install -r requirements.txt

# 添加项目/工作路径
ADD ./ /home/bigbooom
WORKDIR /home/bigbooom

CMD ["python", "manage.py", "runserver"]

EXPOSE 8000

