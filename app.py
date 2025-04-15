
from flask import Flask, request, jsonify, abort, render_template
import os
import pandas as pd

app = Flask(__name__)



#example: <my_app_base_URL>/api/v1/systemwide/all_hs_totals?key=a9YGOPPq2nCPSa2QT2EjgEjcDBd5iFV8j2MbAbNkA
API_KEY = "a9YGOPPq2nCPSa2QT2EjgEjcDBd5iFV8j2MbAbNkA"


#load data
uc_all_df = pd.read_csv("data/UC_Source_HS_systemwide.csv")
uc_campus_df = pd.read_csv("data/UC_Source_HS_by_campus.csv")



# TODO #1 Make an endpoint that returns all campus data.
# Similar to /api/v1/systemwide/all_hs_totals, but using
# uc_campus_df, to get each row in the dataframe.
#




# TODO #2 Make an endpoint that returns a list of all schools that match a query name
#  along with it's ID and location. There are schools that have the same name!
#




# TODO #3 Make an endpoint that returns individual school data by school_id
#  Use that to return all data from that school, by campus and systemwide.
# [including applications, acceptance, enrollment]





# TODO #4 Make an endpoint that takes a campus name <Berkeley> and returns
#  admissions data, including admissions: [total applicatns, acceptance and enrollments],
#  [top 10 feeder schools in terms of total enrollees], [top 10 schools with highest
#   acceptance rates], [demographic totals of applicants, acceptance, and enrollment by 
#   group], [demographic admission averages]
#







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
    return jsonify(result.to_dict(orient="records"))

@app.route('/api/v1/systemwide/highschools')
def list_all_highschools():

    #Returns a list of all highschools in the data, along with ID and location data.
    require_api_key()

    result = uc_all_df[[ "school_id", "school", "city", "countystate_territory"]].drop_duplicates().sort_values("school")

   
    return jsonify(result.to_list.to_dict(orient="records"))

@app.route('/')
def home():

    #Home page with basic info about API
    return render_template('index.html')
     
