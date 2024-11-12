# 打包镜像
docker-compose build 

# 启动服务
docker-compose up -d     

# 请求示例
# signup
```
# 终端请求
curl --location --request POST 'http://127.0.0.1:8000/api/signup/' \
--header 'Content-Type: application/json' \
--data '{"email": "test@test.com", "password": "123"}'

# 返回
{"email":"test@test.com","password":"pbkdf2_sha256$600000$nWlqp8binLUMT7ff5S7dSG$LM7q2wp2Gwvuh4z0yWJZU6RkeNTnWu5AiGLyDcg/X9g="}% 

```

# singin
```
curl --location --request POST 'http://127.0.0.1:8000/api/signin/' \
--header 'Content-Type: application/json' \
--data '{"email": "test@test.com", "password": "123"}'

# 返回
{"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNDIwODk3LCJqdGkiOiJlYjBkMzE3OWY5ZGQ0MDExOWU5M2JlNGNmYWRjNWJlZSIsInVzZXJfaWQiOjF9.pC3GGG9aS8uACL6E2VoKVJwBHAA3GYxkpmxp8jLs3RM","refresh_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTUwNjk5NywianRpIjoiZmFhM2RiMWU3YmI3NGFlNDk0N2QyNmJkY2JiNGIxNWUiLCJ1c2VyX2lkIjoxfQ.zooSar9zSOtqjw3GfJsPiSKsHCPPFDYQDC-ky71Xi3c"}%  
```

# me
```
# 请求
curl --location --request GET 'http://127.0.0.1:8000/api/me/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNDIwODk3LCJqdGkiOiJlYjBkMzE3OWY5ZGQ0MDExOWU5M2JlNGNmYWRjNWJlZSIsInVzZXJfaWQiOjF9.pC3GGG9aS8uACL6E2VoKVJwBHAA3GYxkpmxp8jLs3RM' \
--form 'email="test@test.com"' \
--form 'password="123"'

# 返回
{"id":1,"email":"test@test.com"}% 
```

# 重置数据
## 删除 db.sqlite3 文件并重建数据库
1. 删除根目录 db.sqlite3文件 -> 执行 python manage.py migrate -> 重新部署docker
```
# 查询容器id
docker ps
CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS          PORTS                    NAMES
7d535ce7dd22   jwt_project-web   "python manage.py ru…"   46 minutes ago   Up 46 minutes   0.0.0.0:8000->8000/tcp   jwt_project-web-1

# 进入docker shell
docker exec -it 7d535ce7dd22 /bin/bash

# 删除db.sqlite3文件
rm /app/db.sqlite3

# 重新运行数据库迁移命令
python manage.py migrate
```

1.2 
   


