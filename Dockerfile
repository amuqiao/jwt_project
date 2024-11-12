# 使用 Python 官方的轻量级基础镜像
FROM python:3.11-slim

# 设置工作目录为 /app
WORKDIR /app

# 将当前目录下的所有文件复制到 /app 目录
COPY . /app/

# 安装 requirements.txt 中列出的所有依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置环境变量，禁用 Django 的调试模式
ENV DJANGO_SETTINGS_MODULE=jwt_project.settings

# 在容器启动时运行数据库迁移
RUN python manage.py migrate

# 设置容器启动时运行的命令，使用 Django 开发服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
