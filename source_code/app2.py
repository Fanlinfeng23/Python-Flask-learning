from flask import Flask

from flask import redirect

from flask import url_for

app=Flask(__name__)

@app.route('/')

def index():
    return 'Welcome to my website'

@app.route('/<username>')

def redirection(username):
    if username =='Marveric':
        return 'Hello {}'.format(username)
    else:
        return redirect(url_for('index'))

 # redirect字面意思重定向，本文指若名字非‘Marveric’，其他均回到首页
if __name__=='__main__':
    app.run()

