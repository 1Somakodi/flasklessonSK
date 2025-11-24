from flask import Flask, request, render_template, redirect, url_for, jsonify
import sqlite3

# Initialize Flask application
app = Flask(__name__)

# ------------------------------
# DATABASE CONNECTION FUNCTION
# ------------------------------
# This function opens a connection to our SQLite database.
# We call this every time we want to read/write data.
def get_db_connection():
    conn = sqlite3.connect("students.db")  # Connect to DB file
    conn.row_factory = sqlite3.Row         # Allows dictionary-like access to rows
    return conn


# ------------------------------
# HOME PAGE - SHOW APPLICATION COUNT
# ------------------------------
@app.route("/", methods=["GET"])
def home():
    # Step 1: Open database connection
    conn = get_db_connection()

    # Step 2: Query to count all applications in the table
    count = conn.execute(
        "SELECT COUNT(*) AS total FROM applications"
    ).fetchone()["total"]

    # Step 3: Close database connection
    conn.close()

    # Step 4: Render home page and pass the count to HTML
    return render_template("index.html", count=count)


# ------------------------------
# SUBMIT FORM DATA TO DATABASE
# ------------------------------
@app.route("/submit", methods=["POST"])
def submit():
    # Step 1: Collect form data from HTML page
    fullName = request.form.get("fullName")
    email = request.form.get("email")
    phone = request.form.get("phone")
    course = request.form.get("course")

    # Step 2: Open DB connection
    conn = get_db_connection()

    # Step 3: Insert this data into the database table
    conn.execute(
        "INSERT INTO applications (fullName, email, phone, course) VALUES (?, ?, ?, ?)",
        (fullName, email, phone, course)
    )

    # Step 4: Save the changes
    conn.commit()

    # Step 5: Close connection
    conn.close()

    # Step 6: Redirect back to home page
    return redirect(url_for("home"))


# ------------------------------
# API ENDPOINT - RETURN APPLICATION COUNT AS JSON
# ------------------------------
@app.route("/api/count")
def api_count():
    # Similar logic as home route, but we return JSON instead of HTML
    conn = get_db_connection()
    count = conn.execute("SELECT COUNT(*) AS total FROM applications").fetchone()["total"]
    conn.close()
    return jsonify({"total": count})  # Useful for JavaScript or external API calls


# ------------------------------
# STATIC PAGES (About, Contact)
# ------------------------------
@app.route("/about")
def about():
    # Render about page
    return render_template("about.html")


@app.route("/contact")
def contact():
    # Render contact page
    return render_template("contact.html")


# ------------------------------
# RUN THE FLASK APP
# ------------------------------
# debug=True helps show errors while coding (remove in production)
if __name__ == "__main__":
    app.run(debug=True)
