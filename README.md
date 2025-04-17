
# UC High School Admissions API

This is a Flask-based RESTful API that serves structured data on applications, admissions, and enrollments from California public high schools to University of California campuses. It is designed as a teaching tool and a public resource.

---

## 🚀 Live Demo

Once deployed, students can query real-time UC admissions data using the API.

---

## 📁 Project Structure

```
.
├── app.py                      # Main Flask application
├── data/
│   ├── UC_Source_HS_system.csv
│   └── UC_Source_HS_by_uc_campus.csv
├── templates/
│   └── index.html              # Home route (optional)
│   └── api_docs.html           # API documentation page
├── requirements.txt
├── README.md
```

---

## 🔑 Authentication

Some endpoints require an API key passed as a query parameter:

```
?key=YOUR_API_KEY
```

---

## 📊 Endpoints

### `/api/v1/systemwide/all_hs_totals`
Returns totals (applied, accepted, enrolled) for each high school across the UC system.

### `/api/v1/systemwide/highschools`
Returns a list of all schools with IDs and locations.

### `/api/v1/systemwide/highschools/search?name=<name>&city=<city>`
Returns filtered list of schools by name and/or city.

### `/api/v1/school-detail/<school_id>`
Returns totals for a specific school, including breakdown by campus.

### `/api/v1/bycampus/all_hs`
Returns all school totals by UC campus.

### `/api/v1/campus/<campus_name>`
Returns total admissions stats and top schools for a campus.

---

## 📌 Data Suppression Policy

To protect student privacy, the following rules apply:

- If fewer than **5 students** applied in a category, that data is suppressed.
- If fewer than **3 students** enrolled or were admitted in a category, the count is shown as 0.
- If **100%** of a school's applicants belong to one category, that category is redacted.

---

## 📦 Installation

```bash
pip install -r requirements.txt
python app.py
```

---

## 🧠 Learning Goals

- Understand RESTful APIs
- Query and filter data using endpoints
- Explore real-world education data

---

## 🧑‍💻 Contributing

Please submit a pull request if you'd like to extend functionality, refactor endpoints, or improve docs.

---

## 🪪 License

MIT License – Open for educational use.