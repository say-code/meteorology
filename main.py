from flask import Flask
import dao.data
import dao.serial_set_dao
from flask import request
from flask import render_template
from flask import abort, redirect, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
    # print(data_select_service())
    return render_template("index.html", data=data_select_service(), serial=serial_set_select_service())


@app.route("/sql/data/insert", methods=["post"])
def data_insert_service():
    data = request.form["data"]
    dao.data.data().insert(data)


@app.route("/sql/data/select")
def data_select_service():
    data = dao.data.data().selectAll()
    return data


@app.route("/sql/serial_set/update", methods=["post"])
def serial_set_update_service():
    data = dict(request.form)
    dao.serial_set_dao.serial_set().update(data)
    return redirect("/")


@app.route("/sql/serial_set/selectAll")
def serial_set_select_service():
    data = dao.serial_set_dao.serial_set().selectAll()[0]
    return list(data)
