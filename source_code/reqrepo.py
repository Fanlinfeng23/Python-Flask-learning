from flask import Flask
from flask import request

app=Flask(__name__)


@app.route('/user/<password>')

def user_password(password):

# 打印计算机用户信息，如：User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/XXXXX (KHTML, like Gecko) Version/17.2.1 Safari/XXXXXX
    print('User-Agent:',request.headers.get('User-Agent'))

#从URL中获取time和q的值，变量之前需要加“？“ ，变量之间加&链接
    print('time:',request.args.get('time'))
    print('q:',request.args.get('q'))

    return 'password is {}'.format(password)

if __name__ == '__main__':
    app.run()
