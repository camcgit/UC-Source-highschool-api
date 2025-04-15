
from flask import Flask, request, jsonify, abort, render_template
import os
import pandas as pd

app = Flask(__name__)



@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")



app = Flask(__name__)

API_KEY = "a9YGOPPq2nCPSa2-QT2EjgEjcD-Bd5iFV8j2MbAbNkA"


#load data
uc_all_df = pd.read_csv("data/uc_hs_enrollment_systemwide.csv")
uc_campus_df = pd.read_csv("data/uc_hs_enrollment_by_campus.csv")


def require_api_key():
    key = request.args.get("key")
    if key != API_KEY:
        abort(403, description="Forbidden: Invalid API key")

#returns all schools
@app.route('/api/v1/systemwide/all_hs_totals')
def all_hs_data_systemwide():

    require_api_key()  # key protection

    result = uc_all_df[[
        "school_", "city_", "countystate_territory_",
        "total_applied", "total_accepted", "total_enrolled",
        "pct_accepted", "pct_enrolled"
    ]]

    return result.to_json(orient="records")

@app.route('/api/v1/systemwide/highschools')
def list_all_highschools():
   # require_api_key()

    hs_list = uc_all_df[["school_", "city_", "countystate_territory_"]].drop_duplicates().sort_values("school_")

    return hs_list.to_json(orient="records")

@app.route('/')
def home():

    return render_template('index.html')
     
