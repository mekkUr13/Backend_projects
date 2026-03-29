# 🚀 Backend Projects Portfolio

Welcome to my Backend Projects repository! This repository serves as a portfolio of my personal programming projects and university assignments, demonstrating my skills in backend development, API design, and software architecture. 

---

## 📂 Repository Structure

Below is an overview of the projects currently included in this repository. Each project is contained within its own dedicated subfolder, complete with its own source code, configurations, and documentation.

### 1. `Courses_fastapi_backend` (Culinary Institute Management API)
**Technologies Used:** Python, FastAPI, Uvicorn, Pydantic
**Key Concepts:** RESTful APIs, JSON File Handling, Exception Handling, Data Validation, Endpoint Routing

**Description:**
This project is a fast and responsive RESTful API built with **FastAPI** to manage a Culinary Training Institute (Szakácsképző Intézmény). It handles the administration of courses, instructors, and students.
It was made for one of my university courses, so it is mainly written in hungarian.

**Features:**
- **Course Management:** Track course IDs, names (e.g., Soups, Roasts, Side Dishes, Salads, Desserts), types (lecture, practice), year, schedule, location, assigned instructor, enrolled students, and maximum capacity.
- **Instructor & Student Data:** Manage instructor and student profiles including names, IDs, and emails.
- **Persistent Storage:** Handles file-based data persistence reading from and writing to `kurzusok.json`.
- **Structured Architecture:** The logic is neatly separated into modules:
  - `modellek.py`: Defines the strictly typed Pydantic data models.
  - `fajl_kezeles.py`: Manages the underlying JSON read/write logic.
  - `utvonalak.py`: Hands the API routing and logic implementation.
- **Interactive Documentation:** Automatically generates interactive Swagger UI documentation for easy API testing and exploration.

**How to run it:**
1. Navigate to the `Courses_fastapi_backend` directory.
2. Install the required dependencies: `pip install fastapi uvicorn`
3. Run the application: `python app_sz/main.py`
4. Open your browser and go to `http://127.0.0.1:8000/docs` to interact with the API endpoints.

---

## 🛠️ Skills & Technologies Demonstrated
- **Languages:** Python
- **Frameworks & Libraries:** FastAPI, Pydantic, Starlette
- **Concepts:** RESTful API Design, Error Handling (`HTTPException`), File I/O, Modular Programming, Object-Oriented Principles.
