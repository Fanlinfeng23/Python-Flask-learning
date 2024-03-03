from flask import Flask


#初始化,创建一个应用程序的实例
app = Flask(__name__)

#对URL进行路由，当访问到根目录时执行index函数
@app.route('/')

#一个视图函数可以绑定多个URL
@app.route('/hello')
#在terminal返回URL后加'/hello'也可以返回该函数


#index为视图函数，即对客户端请求进行处理的函数
def index():
    return 'Hello World'

#变量也能传入路由，格式为<>
@app.route('/user/<username>')

def usser_index(username):
    return 'Hello {}'.format(username)


@app.route('/post/<int:post_id>')

def show_post(post_id):
    return 'post {}'.format(post_id)




if __name__=='__main__':
    app.run(debug=True)

#debug=True可不加，加的目的是为了不用退出路由环境就可以修改代码

