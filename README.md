
# UC High School Insights API

This Flask-based API serves cleaned and enriched data about applications, admissions, and enrollments from California public high schools to the University of California system. It includes both systemwide and campus-level views of the data, designed for use in education, research, and civic data projects.

Data was obtained and compiled from the [University of California's Information Center](https://www.universityofcalifornia.edu/about-us/information-center/admissions-source-school)

---

## 🚀 Getting Started

### Option 1: Run in GitHub Codespaces

This project is preconfigured for GitHub Codespaces. Just open the Codespace and the Flask server will automatically run on port `5000`.

Make sure to set the port visibility to **public** if you want to test the API in your browser.

### Option 2: Run Locally

1. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install flask pandas
   ```

3. Start the server:
   ```bash
   flask run --host=0.0.0.0 --port=5000
   ```

---

## 🔐 API Key Access

All API endpoints require an API key to be passed as a query parameter:

```
?key=YOUR_API_KEY
```

> You can change the `API_KEY` inside `app.py`.

---

## 📊 Current Endpoints

### 🔹 General

| Method | Endpoint                                      | Description                             |
|--------|-----------------------------------------------|-----------------------------------------|
| GET    | `/`                                           | Home page with basic info               |

### 🔹 Systemwide Data

| Method | Endpoint                                           | Description                                              |
|--------|----------------------------------------------------|----------------------------------------------------------|
| GET    | `/api/v1/systemwide/all_hs_totals?key=...`         | All high schools with totals and percentages             |
| GET    | `/api/v1/systemwide/highschools?key=...`           | List of all high schools with IDs and locations          |
| GET    | `/api/v1/systemwide/highschool/id/<school_id>?key=...` | Data for a specific high school by ID               |

> All systemwide data comes from a pre-flattened CSV and includes total applied, accepted, enrolled, and percentages.

---

## 💡 Ideas for Extensions

- Add filters by county, city, or class year
- Add per-campus data views (`uc_campus_df`)
- Add demographic breakdowns (e.g., race/ethnicity)
- Secure the API key using headers instead of query parameters
- Build a Streamlit or React frontend to visualize the data

---

## 📁 Project Structure

```
.
├── app.py                  # Main Flask application
├── data/                   # Folder for uploaded data files
│   ├── UC_Source_HS_systemwide.csv
│   └── UC_Source_HS_by_campus.csv
├── templates/
│   └── index.html          # Optional landing page
├── .devcontainer/
│   └── devcontainer.json   # Configuration for Codespaces
└── README.md               # You’re reading it!
```

---

## 📜 License

MIT — free to use and modify for educational and civic data projects.

---

Built by *vivertido* for learning, teaching, and open data.