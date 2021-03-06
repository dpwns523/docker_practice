# syntax=docker/dockerfile:1

# 공식 파이썬 이미지사용
FROM python:3.6-alpine
# 최소한의 패키지만

#프로젝트가 들어가는 Working Directory
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# 소스코드를 이미지에 추가하는 것
# 도커파일이 있는 폴더의 모든 파일 복사하여 이미지에 추가
COPY . .

# exec방식으로 명령을json으로 지정하여 실행
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# EXPOSE 8000 
# 포트를 열어주겠다

