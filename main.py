from flask import Flask
import dao.data
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/sql/data/insert", methods=["post"])
def data_insert_service():
    data = request.form["data"]
    service = dao.data.data().insert(data)

@app.route("/sql/data/select")
def data_select_service():
    return None

asdasdasd