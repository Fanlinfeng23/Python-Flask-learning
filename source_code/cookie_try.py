from flask import Flask
from flask import make_response
from flask import request
from flask import render_template


app=Flask(__name__)

@app.route('/set_cookie/<username>')

def set_cookie(username):


#make_response函数可对对象进行封装，使其变成一个相应对象
#make_response既可返回内容，如resp=make_response('<h1>Marveric</h1>')
#该函数也可以返回页面，但必须用页面渲染（render_template),例子如下
    resp=make_response(render_template('user_index.html',username=username))



#从resp中获取username参数并设置cookie
    resp.set_cookie('username',username)


#将页面渲染结果显示
    return resp


@app.route('/get_cookie')
def get_cookie():


    #获取cookies中的某一参数值采用request.cookies.get()
    username=request.cookies.get('username')
    return 'Hello {}'.format(username)

if __name__ == '__main__':
    app.run()

