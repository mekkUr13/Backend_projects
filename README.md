# 🚀 Backend Projects

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688)](https://fastapi.tiangolo.com/)
[![Flask](https://img.shields.io/badge/Flask-000000)](https://flask.palletsprojects.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-e92063)](https://docs.pydantic.dev/)

A collection of backend / API projects showcasing my work in **RESTful API design, data validation, and
clean, modular service architecture**. Each project lives in its own self-contained subfolder with its own
source, configuration and docs.

---

## 📂 Projects

### `Courses_fastapi_backend` — Culinary Institute Management API

A fast, responsive **RESTful API built with FastAPI** for administering a culinary training institute —
managing its courses, instructors and students.

**Tech stack:** Python · FastAPI · Uvicorn · Pydantic · Starlette
**Concepts:** REST API design · request/response validation · exception handling · endpoint routing · file-based persistence · modular architecture

**Highlights**

- **Course management** — tracks course IDs, names, type (lecture/practice), year, schedule, location,
  the assigned instructor, enrolled students and maximum capacity.
- **People management** — instructor and student profiles (names, IDs, emails).
- **Strong typing & validation** — all payloads are modeled and validated with Pydantic, so malformed
  requests are rejected with clear errors.
- **Persistent storage** — reads from and writes to a JSON store (`kurzusok.json`).
- **Clean separation of concerns**
  - `modellek.py` — Pydantic data models
  - `fajl_kezeles.py` — JSON read/write persistence layer
  - `utvonalak.py` — API routes and endpoint logic
- **Interactive docs** — auto-generated Swagger UI for exploring and testing every endpoint.

> The domain vocabulary (courses, roles) is in Hungarian, reflecting the institute it models; the
> architecture and API design are language-agnostic.

**Run it**

```bash
cd Courses_fastapi_backend
pip install fastapi uvicorn
python app_sz/main.py
# then open http://127.0.0.1:8000/docs
```

---

### `Flaskprojekt` — Flask Fundamentals: A Message-Board App, Built Step by Step

A progressive, hands-on tour of **server-side web development with Flask**, building the same message-board
(*üzenőfal*) application up from a single route to a full authenticated CRUD app. Each numbered folder
(`01`–`09`) is a self-contained stage that adds one new capability.

**Tech stack:** Python · Flask · Jinja2 · Flask-WTF / WTForms · Flask-SQLAlchemy · Flask-Bcrypt · Flask-Login
**Concepts:** routing & views · templating · form handling & validation · ORM/database modelling · app packaging (blueprints & app factory) · authentication · full CRUD

**What each stage covers**

- **`01-Flask-Alapok`** — Flask basics: the app object, routes and returning responses.
- **`02-Templates` / `03-Jinja`** — server-side rendering with Jinja2 templates and template logic.
- **`04-Form` / `04-Form-Advanced`** — HTML forms with Flask-WTF / WTForms and server-side validation.
- **`05-Database`** — persistence with Flask-SQLAlchemy (models, queries, migrations).
- **`06-Package`** — restructuring into a proper Python package with an app factory and config.
- **`07-User-Registration` / `08-Login`** — user accounts with Flask-Bcrypt password hashing and
  Flask-Login sessions.
- **`09-CRUD`** — the finished app: authenticated create / read / update / delete on message-board posts.

> Built by following a Flask tutorial series to solidify web-backend fundamentals; each stage has its own
> `requirements.txt` so it can be run in isolation.

**Run it** (example — the final CRUD stage)

```bash
cd Flaskprojekt/09-CRUD
pip install -r requirements.txt
python run.py
```

---

## 🛠️ Skills demonstrated

- **Language:** Python
- **Frameworks & libraries:** FastAPI, Pydantic, Starlette, Uvicorn · Flask, Jinja2, Flask-WTF/WTForms,
  Flask-SQLAlchemy, Flask-Bcrypt, Flask-Login
- **Concepts:** RESTful API design, server-side rendering, form handling & validation, ORM/database
  modelling, authentication, error handling (`HTTPException`), file I/O, modular programming and app
  packaging, object-oriented design.
