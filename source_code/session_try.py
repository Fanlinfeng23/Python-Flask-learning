from flask import Flask
from flask import session

app=Flask(__name__)


#若没有安全密钥，session会自动报错，因此需在此设置安全码
app.secret_key='12345678'


@app.route('/set_session')
def set_session():

#设置session的持久化
    session.permanent =True
    session['username']='Marveric'
    return '成功设置session'




@app.route('/get_session')

def get_session():
    value = session.get('username')
    return '成功获取session值为{}'.format(value)


if __name__ == '__main__':
    app.run()

