import data
from flask import Flask, request

app = Flask(__name__)


@app.route("/sign_in", methods=["POST"])
def sign_in():
    print(request.get_json()["user"])
    return "Success!"


@app.route("/get_name", methods=["POST"])
def get_name():
    print(data.user_list)
    return data.user_list[request.get_json()["id"]]
