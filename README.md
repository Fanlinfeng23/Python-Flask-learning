# Python-Flask-learning
In this part, I will lead you to learn the application of Flask, and it's along with some basic web learning. Never miss this project!
## Build a virtual environment
If you haven't built a virtual environment,click [this](/教学内容/虚拟环境.md)
## install Flask
Using this command line:
> pipenv isntall flask

## the first app:
 [example code](source_code/app.py)
> when you run this code on your own computer,it will return a URL，you put it on your browser,you will get the word‘hello world’

>the URL is like that"Running on http://127.0.0.1:5000", put "http://127.0.0.1:5000" on your browser

## Use url_for() to create a dynamic function
url_for('name of func',parameters)
[example code](source_code/app1.py)

And use url_for can also help you to redirect the route
[example code](source_code/app2.py)


## In the real application, we use html, CSS, Javascript and so on.
> in this part, we will learn some basic knowledge about website and front-end infrastrcture.

## to render our template, we will use render_template

To learn more thing about this module, click [this](http://t.csdnimg.cn/MjOcr)

And to get the source code, click [here](/source_code/renderTemplate.py). And [this](/source_code/user_index.html) is the HTML file.
> Remember one thing is important, If your IDLE cannot 'mkdir templates' for you, you should put this in your command line and then in it you could edit your HTML file.


## in the request repo, we could use the function: get() and post()
[code about how to use get](source_code/reqrepo.py)

> Then open the browser, and put the url on it .
> Then add the arguments as i said in the python code, you may get "your password is XXXXXXX", which means your code is  correct!

Since the usage of Post() is a little compilcated, click [thisfile](/教学内容/Post的使用说明.md) to learn more about that. 


## Session and Cookie
But in reality, we always see almost all website using cookie or session to store the user's data. Because some of the reasons, not all data is suitable to store in the server, so we well use cookie to store some datas like username, userID, and that's also the reason why we could sometimes automatically login.  
Please have a look at the [examplecode](/source_code/session_try.py)
> the upper code has two route: one is set_session, and the other one is get_session, you should put the URL:  XXXXXXXXX/set_session first to set session.
> And then you could get the session you set before.
