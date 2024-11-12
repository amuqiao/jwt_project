# 打包镜像
docker-compose build 

# 启动服务
docker-compose up -d     

# 请求示例
# signup
```
curl --location --request POST 'http://127.0.0.1:8000/api/signup/' \
--header 'Content-Type: application/json' \
--data '{"email": "test3@test.com", "password": "123456"}'

```

# singin
```
curl --location --request POST 'http://127.0.0.1:8000/api/signin/' \
--header 'Content-Type: application/json' \
--data '{"email": "test3@test.com", "password": "123456"}'

```

# 返回 
```
{"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNDE5NzI0LCJqdGkiOiJlNjAxZDAwMjQ2ZDQ0ZTI2YmMyNzkzMmUzYTVhMzdkZSIsInVzZXJfaWQiOjR9.l_gSUPK-pjNno43wsZERdPVrNrlaXpQccyyERcWpsK4","refresh_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTUwNTgyNCwianRpIjoiMzM3N2JkZjE0NWVhNDNlMGEwMTU4ODJiMWQ3M2JiZGEiLCJ1c2VyX2lkIjo0fQ.xayyJZ6fyYmk9m1p44N5pkzTkQDi4S5YdPkDR6bnzik"}%  
```

# me
```
curl --location --request GET 'http://127.0.0.1:8000/api/me/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNDE5NjcyLCJqdGkiOiI5NGJmNDFkMGU0ZjU0ODg0ODA5YzkyNzVjYjlhMzdkNyIsInVzZXJfaWQiOjR9.I7a4vBLtz9mLYefGESKg3j68KVHGroykbRcS0CYrY78' \
--form 'email="test1@test.com"' \
--form 'password="1234"'
```

# 重置数据
1. 删除 db.sqlite3 文件并重建数据库
1.1 删除根目录 db.sqlite3文件 -> 执行 python manage.py migrate -> 重新部署docker

1.2 
   


