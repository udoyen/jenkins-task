import sys
sys.path.append("/var/www/html/app/myprojectenv")

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>George Udosen's Docker Task</h1>"

if __name__ == "__main__":
    app.run(host='127.0.0.1')