# Error Handle 
## Firstly，you need to edit a server's code to build a server environment, and it will return a url.

[examplecode](/source_code/errorhandling.py)

## Secondly, we need to change our dir to the "templates" where we store our HTML code.
You can run the following command line on your terminal.
> makedir templates

>cd templates

## Thirdly, we could code our HTML file
Then you will see your dir is changed from 'flask' to 'templates', in this dir you could begin to code like 
[this](/source_code/404.html)

## Never forget to change dir back to 'flask', otherwise it could not found your python file'errorhandling.py'
using the following command line
> cd ..

## Then, just run the python file. And try any route on the website.


