from flask import Flask, render_template
import pymysql
app = Flask(__name__)

# db connect
conn = pymysql.connect(host='database-2.cdcip60j3i41.ap-northeast-2.rds.amazonaws.com',
                        user='admin',
                        password='d363d363d363!',
                        db='sys',
                        charset='utf8')
curs = conn.cursor()
sql = "select * from visitors"
curs.execute(sql) # 커서를 가져온 상태에서 select문을 실행
rows = curs.fetchall() # 모든 레코드를 가져옴
conn.close()


@app.route('/')
def index():
    return render_template('index.html', data_list=rows)

if __name__ == '__main__':
    app.run()
#