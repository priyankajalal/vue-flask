from flask import Flask
from flask import jsonify
from flask import request
import MySQLdb
import MySQLdb.cursors
import dbutil

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route("/symbol/<names>", methods=['POST', 'GET'])
def hello(names):
    list_dict_data = dbutil.getData(names.split(","))
    return jsonify(list_dict_data)

if __name__ == "__main__":
    app.run()
