from flask import Flask, render_template, request, redirect, session
import pymysql
app = Flask(__name__)

# db connect
def dbConnect():
    return pymysql.connect(host='database-2.cdcip60j3i41.ap-northeast-2.rds.amazonaws.com',
                            user='admin',
                            password='d363d363d363!',
                            db='sys',
                            charset='utf8')
def getData():
    conn = dbConnect()
    curs = conn.cursor()
    sql = "select * from visitors"
    curs.execute(sql) # 커서를 가져온 상태에서 select문을 실행
    rows = curs.fetchall() # 모든 레코드를 가져옴
    conn.close()
    return rows
def addData(name, mail, region, temperature):
    conn = dbConnect()
    curs = conn.cursor()
    sql = "INSERT INTO visitors(name, mail, region, temperature) VALUES ('%s', '%s', '%s', %.1f)" % (name, mail, region, temperature)
    ok = curs.execute(sql)
    conn.commit()
    conn.close()

# redirect() url주소를 여기로 연결해준다..
# GET = 페이지가 나오도록 요청. POST = 버튼을 눌렀을때 데이터를 가지고오는 요청
# 요청정보확인하려면 request 임포트 필요
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', data_list=getData())
    else:
        name = request.form.get('name')
        mail = request.form.get('mail')
        region = request.form.get('region')
        temperature = float(request.form.get('temperature'))
        addData(name, mail, region, temperature)
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
