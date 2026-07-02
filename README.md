# 🚀 Backend Projects

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688)](https://fastapi.tiangolo.com/)
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

## 🛠️ Skills demonstrated

- **Language:** Python
- **Frameworks & libraries:** FastAPI, Pydantic, Starlette, Uvicorn
- **Concepts:** RESTful API design, error handling (`HTTPException`), file I/O, modular programming,
  object-oriented design.
