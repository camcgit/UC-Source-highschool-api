
# UC High School Insights API: Starter branch

This is the starting point for Day 7 of the  SMASH Python for Data Powered applications course. A basic Flask project is ready with two datasets in the `/data` folder ready to use.

Data was obtained and compiled from the [University of California's Information Center](https://www.universityofcalifornia.edu/about-us/information-center/admissions-source-school)

---

### Todos:

1. Create and secure an API key and require it for access to endpoints.
2. Finish the first endpoint `/api/v1/systemwide/all_hs_totals` to return all HS data for UC system.
3. Return all High Schools in the data, including location and ID for this endpoint: `@app.route('/api/v1/systemwide/highschools')`
4. Test and validate on clients.

###  Run in GitHub Codespaces

This project is preconfigured for GitHub Codespaces. Just open the Codespace and the Flask server will automatically run on port `5000`.

Make sure to set the port visibility to **public** if you want to test the API in your browser.

### Option: Run Locally

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



## 📜 License

MIT — free to use and modify for educational and civic data projects.

---

Built by *vivertido* for learning, teaching, and open data.