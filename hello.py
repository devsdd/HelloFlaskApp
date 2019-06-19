import os
import socket
from flask import Flask, render_template

app = Flask(__name__, template_folder=os.getcwd())
 
@app.route("/")
def hello():
    return render_template("hello.html", hostname=socket.gethostname())
 
if __name__ == "__main__":
    app.run("0.0.0.0")

