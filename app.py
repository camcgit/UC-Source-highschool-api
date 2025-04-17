
from flask import Flask, request, jsonify, abort, render_template
import os
import pandas as pd

app = Flask(__name__)


#TODO 1: Create an API key
API_KEY = ""


#load data
uc_all_df = pd.read_csv("data/UC_Source_HS_system.csv")
uc_campus_df = pd.read_csv("data/UC_Source_HS_by_uc_campus.csv")


def require_api_key():
    key = request.args.get("key")
    if key != API_KEY:
        abort(403, description="Forbidden: Invalid API key")

#TODO 2: Finish endpoint to return all HS data for UC system
@app.route('/api/v1/systemwide/all_hs_totals')
def all_hs_data_systemwide():

    require_api_key()  # key protection

    #Include all the relevant columns
    result = uc_all_df[[
         
    ]]

    #Convert the dataframe into JSON 
    return jsonify(result.to_dict(orient="records"))


# TODO 3: Return all High Schools in the data, incl. location and ID.
@app.route('/api/v1/systemwide/highschools')
def list_all_highschools():

    require_api_key()

    #build result from required dataframe columns. drop duplicates and sort by school name.
    result = ...
   
    #fix return so it serves JSON
    return result

@app.route('/')
def home():

    #Home page with basic info about API
    return render_template('index.html')
     
