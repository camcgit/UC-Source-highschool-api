
from flask import Flask, request, jsonify, abort, render_template
import os
import pandas as pd

app = Flask(__name__)



#example: <my_app_base_URL>/api/v1/systemwide/all_hs_totals?key=a9YGOPPq2nCPSa2QT2EjgEjcDBd5iFV8j2MbAbNkA
API_KEY = "a9YGOPPq2nCPSa2QT2EjgEjcDBd5iFV8j2MbAbNkA"


#load data
uc_all_df = pd.read_csv("data/UC_Source_HS_systemwide.csv")
uc_campus_df = pd.read_csv("data/UC_Source_HS_by_campus.csv")


def require_api_key():
    key = request.args.get("key")
    if key != API_KEY:
        abort(403, description="Forbidden: Invalid API key")

#returns all schools
@app.route('/api/v1/systemwide/all_hs_totals')
def all_hs_data_systemwide():

    require_api_key()  # key protection

    #which columns to include
    result = uc_all_df[[
        "school_id", "school", "city", "countystate_territory",
        "total_applied", "total_accepted", "total_enrolled",
        "pct_accepted", "pct_enrolled"
    ]]

    #Convert the dataframe into JSON 
    return result.to_json(orient="records")

@app.route('/api/v1/systemwide/highschools')
def list_all_highschools():

    #Returns a list of all highschools in the data, along with ID and location data.
    require_api_key()

    hs_list = uc_all_df[[ "school_id", "school_", "city_", "countystate_territory_"]].drop_duplicates().sort_values("school_")

    return hs_list.to_json(orient="records")

@app.route('/')
def home():

    #Home page with basic info about API
    return render_template('index.html')
     
