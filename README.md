# Flask Lesson: Rendering an HTML Website

This repository contains a simple Flask project demonstrating how to render an HTML website using Flask. It is intended as a lesson for beginners to understand the basics of Flask routing, templates, and static files.

## Project Structure

yourproject/
│
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── index.html         # Home page
│   ├── about.html         # About page
│   └── contact.html       # Contact page
│
└── static/                # Static files (CSS, JS, Images, Libraries)
    ├── css/style.css
    ├── img/
    │   ├── somakodi logo.png
    │   └── favicon.ico
    ├── lib/
    │   └── owlcarousel/assets/owl.carousel.min.css
    └── js/main.js

## Prerequisites

* Python 3.7+
* Flask (`pip install flask`)


## How to Run the Project

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/flask-html-lesson.git
cd flask-html-lesson
```

2. **Install Flask**:

```bash
pip install flask
```

3. **Run the Flask app**:

```bash
python app.py
```

4. **Open your browser** and go to:

```
http://127.0.0.1:5000/
```

You should see the home page rendered. Navigate to `/about` and `/contact` to view other pages.

---

## Learning Objectives

By completing this lesson, students will learn:

* How to set up a Flask project
* How to render HTML templates using `render_template()`
* How to serve static files (CSS, JS, images)
* How to create multiple routes for different pages
* How to integrate front-end templates into a Flask application

---

## Next Steps

Students can enhance this project by:

* Adding a functional registration form using Flask back-end
* Using Jinja2 templating for dynamic content
* Adding more pages and navigation links
* Learning to deploy Flask apps to platforms like Heroku, Railway, or Render

---

## Author

**Somakodi School** – [https://somakodi.ke](https://somakodi.ke)

---

## License

This project is open source and available for educational purposes.
