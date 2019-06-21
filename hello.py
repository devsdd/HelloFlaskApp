import os
import socket
from flask import Flask, render_template

application = Flask(__name__, template_folder=os.getcwd())
 
@application.route("/")
def hello():
    return render_template("hello.html", hostname=socket.gethostname())
 
if __name__ == "__main__":
    application.run("0.0.0.0")

