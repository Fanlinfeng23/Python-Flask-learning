from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/user/<username>')

def user_index(username):
    return render_template('user_index.html',username=username)



if __name__ == '__main__':
    app.run()
