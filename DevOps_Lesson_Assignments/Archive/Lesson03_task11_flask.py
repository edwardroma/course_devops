# 11. Create a Flask application which listens to port 30000

# INITIATE Flask
from flask import Flask
from flask import render_template

app = Flask(__name__)

# DEFINE the Url for testing conveniences
# hst = '127.0.0.1'
# prt = 4000
# my_url = "http://" + hst + ":" + str(prt)
# print(my_url)


# DEFINE Route App
@app.route("/")
def home():
    return render_template('home.html')


# DEFINE Content App
@app.route("/content/")
def content():
    return render_template('content.html')


@app.route("/content/<file_name>")
def content_file(file_name):
    file_content = [open(file_name, "r").readlines(), "status is 200"]
    return file_content


@app.route("/register/")
def register():
    return render_template('register.html')


@app.route("/register/<file_name>")
def register_file(file_name):
    open(file_name, "a+").write("\nhello")
    file_register = [open(file_name, "r").readlines(), "status is 201"]
    return file_register


# START App
app.run(host="127.0.0.1", port=4000, debug=True)
