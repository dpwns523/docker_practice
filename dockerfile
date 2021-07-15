# syntax=docker/dockerfile:1

# 공식 파이썬 이미지사용
FROM python:3.6-slim-buster 
# 최소한의 패키지만

#프로젝트가 들어가는 Working Directory
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# 소스코드를 이미지에 추가하는 것 위의 카피와 같은 파일을 복사한다는뜻
COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# EXPOSE 8000 
# 포트를 열어주겠다

# CMD 
# 서버구성을 뭐로하느냐
