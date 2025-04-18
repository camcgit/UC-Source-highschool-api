
from flask import Flask, request, jsonify, abort, render_template
import os
import pandas as pd
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()  # load from .env
API_KEY = os.environ.get("API_KEY")

#load data
uc_all_df = pd.read_csv("data/UC_Source_HS_system.csv")
uc_campus_df = pd.read_csv("data/UC_Source_HS_by_uc_campus.csv")


# TODO 1: returns all campus data by HS

@app.route('/api/v1/bycampus/all_hs')
def all_hs_data_by_campus():
    require_api_key()

    result = uc_campus_df[[
        "school_id", "school", "city", "countystate_territory", "university",
        "total_applied", "total_accepted", "total_enrolled"
    ]]
    return jsonify(result.to_dict(orient="records"))



# TODO #2 & 3: /api/v1/systemwide/highschools/search?name=academy&city=oakland&key=<thekey>
#   Can accept two optional parameters: name and/or city

@app.route('/api/v1/systemwide/highschools/search')
def search_highschools():
    require_api_key()

    #Get the name search term from the URL, no spaces, lowercased.
    query_name = request.args.get("name", "").strip().lower()
    query_city = request.args.get("city", "").strip().lower()

    # Start with a copy of the full dataset
    filtered = uc_all_df.copy()

    if query_name:
        filtered = filtered[filtered["school"].str.lower().str.contains(query_name)]

    if query_city:
        filtered = filtered[filtered["city"].str.lower() == query_city]

    if filtered.empty:
        return jsonify({"message": "No matching schools found"}), 404

    result = filtered[[
        "school_id", "school", "city", "countystate_territory"
    ]].drop_duplicates().sort_values("school")

    return jsonify(result.to_dict(orient="records"))



# TODO #4 Make an endpoint that returns individual school data by school_id

@app.route('/api/v1/school-detail/<school_id>')
def get_highschool_detail(school_id):

    require_api_key()

    school_id = int(school_id)

    #get systemwide data for school that match
    school_systemwide = uc_all_df[uc_all_df["school_id"]== school_id]
    print(type(school_id))
    print(type(uc_all_df["school_id"][0]))

    if school_systemwide.empty: 
        return jsonify({"error": f"{school_id} was not found"}), 404


    system_row = school_systemwide.iloc[0]

    # Build the base response
    response = {
        "school_id": school_id,
        "school": system_row["school"],
        "city": system_row["city"],
        "countystate_territory": system_row["countystate_territory"],
        "systemwide_totals": {
            "total_applied": system_row["total_applied"],
            "total_accepted": system_row["total_accepted"],
            "total_enrolled": system_row["total_enrolled"]
        }
    }

    # Add campus breakdowns
    campus_rows = uc_campus_df[uc_campus_df["school_id"] == school_id]

    response["by_campus"] = campus_rows[[
    "university",
    "total_applied", "total_accepted", "total_enrolled",
    "african_american_app", "african_american_adm", "african_american_enr",
    "american_indian_app", "american_indian_adm", "american_indian_enr",
    "asian_app", "asian_adm", "asian_enr",
    "domestic_unknown_app", "domestic_unknown_adm", "domestic_unknown_enr",
    "hispanic_latinx_app", "hispanic_latinx_adm", "hispanic_latinx_enr",
    "intl_app", "intl_adm", "intl_enr",
    "pacific_islander_app", "pacific_islander_adm",
    "white_app", "white_adm", "white_enr"
    ]].sort_values("university").to_dict(orient="records")

    return jsonify(response)



# TODO #5 Make an endpoint that takes a campus name <Berkeley> and returns
#  admissions data

@app.route('/api/v1/campus/<campus_name>')
def get_campus_profile(campus_name):
    require_api_key()

    campus_df = uc_campus_df[uc_campus_df["university"].str.lower() == campus_name.lower()]

    if campus_df.empty:
        return jsonify({"error": f"No data for campus '{campus_name}'"}), 404

    # ---- Admissions Summary
    total_applied = campus_df["total_applied"].sum()
    total_accepted = campus_df["total_accepted"].sum()
    total_enrolled = campus_df["total_enrolled"].sum()

    # ---- Top Feeder Schools by Enrollment
    top_feeders = (
        campus_df[["school", "school_id", "total_enrolled"]]
        .sort_values("total_enrolled", ascending=False)
        .head(10)
        .to_dict(orient="records")
    )

    

    # ---- Demographic Totals
    demo_prefixes = [
        "african_american", "american_indian", "asian", "white",
        "hispanic_latinx", "domestic_unknown", "intl", "pacific_islander"
    ]

    demographic_totals = {}
    

    for prefix in demo_prefixes:
        applied = campus_df.get(f"{prefix}_app", pd.Series(0)).sum()
        admitted = campus_df.get(f"{prefix}_adm", pd.Series(0)).sum()
        enrolled = campus_df.get(f"{prefix}_enr", pd.Series(0)).sum()

        demographic_totals[prefix] = {
            "applied": int(applied),
            "admitted": int(admitted),
            "enrolled": int(enrolled)
        }

       

    # ---- Response Structure
    return jsonify({
        "university": campus_name,
        "admissions": {
            "total_applied": int(total_applied),
            "total_accepted": int(total_accepted),
            "total_enrolled": int(total_enrolled)
        },
        "top_feeder_schools": top_feeders,
        "demographic_totals": demographic_totals,
    })


def require_api_key():
    key = request.args.get("key")
    if key != API_KEY:
        abort(403, description="Forbidden: Invalid API key")


#returns all schools
@app.route('/api/v1/systemwide/all_hs_totals')
def all_hs_data_systemwide():

    require_api_key()  # key protection

    #which columns to include
    result = uc_all_df[
        "school_id", "school", "city", "countystate_territory",
        "total_applied", "total_accepted", "total_enrolled"
    ]

    #Convert the dataframe into JSON 
    return jsonify(result.to_dict(orient="records"))

@app.route('/api/v1/systemwide/highschools')
def list_all_highschools():

    #Returns a list of all highschools in the data, along with ID and location data.
    require_api_key()

    result = uc_all_df[[ "school_id", "school", "city", "countystate_territory"]].drop_duplicates().sort_values("school")

   
    return jsonify(result.to_dict(orient="records"))

@app.route('/')
def home():

    #Home page with basic info about API
    return render_template('index.html')
     
@app.route('/docs')
def docs():
    return render_template('docs.html')