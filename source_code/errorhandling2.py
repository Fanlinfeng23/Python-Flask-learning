from flask import Flask , abort , render_template

app=Flask(__name__)


app.route('/user/<username>')

def errorhandling2(username):
    if username == 'invalid':

#abort 可直接进入404 page
        abort(404)


#真实场景中可加入其他内容包括return


if __name__ == '__main__':
    app.run()
