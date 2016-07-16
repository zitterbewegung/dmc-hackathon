from flask import Flask
import requests
import json
app = Flask(__name__)

{ "_id" : { "$oid" : "4f6abdbef437c071d940a3be" },
        "begin_dt_tm" : 1332395453,
        "category" : "Utilization",
        "component" : "Controller",
        "dataitemid" : "",
        "department" : [ 31, 37 ],
        "duration_in_seconds" : null,
        "end_dt_tm" : 1332395473,
        "instance_id" : 1331140867,
        "machine_id" : 49,
        "mt_name" : null,
        "mt_value" : "INTERRUPTED",
        "sequence" : 2302,
        "subtype" : null,
        "type" : "Execution",
        "virtual_flag" : "N" }

@app.route('/')
def admin():
    return "hello"

@app.route('/get/<int:machine_id>/id')
def get_by_id(machine_id):
    with open('itamcojson2012.json') as f:
        things = [json.loads(line) for line in f]
        

@app.route('/get/<string:name>/name')
def get_by_name(name):
    return name

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
