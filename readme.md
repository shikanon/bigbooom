# 一个泛资讯网站

----------------

这是一个用Django写的泛资讯网站。通过scrapy整合了热门资讯信息，并专注个性化推荐。

文档架构：
```

```

### 运行
安装好Python，通过pip 安装库:

```pip install -r requirements.txt```

安装完成，运行：

```python manage.py runserver```

通过docker容器运行：

构建容器
```
docker build -t bigbooom .
```

运行：
```
docker run -it bigbooom
```