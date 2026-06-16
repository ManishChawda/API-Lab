# API-Lab

Hands-on Python labs for learning REST APIs, API consumption, and API development using FastAPI.

---

## Overview

This repository contains beginner-friendly API projects designed to practice:

- REST API fundamentals
- API consumption using Python Requests
- JSON parsing
- FastAPI development
- Linux system information retrieval
- Custom API creation

---

## Project Structure

```text
API-Lab
│
├── lab1_callgithub_api.py
├── lab2_createyourown_api.py
└── .gitignore
```

---

## Lab 1 – Calling the GitHub API

File:

```text
lab1_callgithub_api.py
```

### Objectives

Learn how to consume public REST APIs using Python.

### Features

- Connects to GitHub REST API
- Retrieves API metadata
- Parses JSON responses
- Searches GitHub repositories using API endpoints

### Technologies

- Python Requests
- JSON

### Run

```bash
python3 lab1_callgithub_api.py
```

### Example Concepts Covered

- HTTP GET requests
- JSON responses
- API endpoints
- Response parsing

---

## Lab 2 – Creating Your Own API

File:

```text
lab2_createyourown_api.py
```

### Objectives

Learn how to create REST APIs using FastAPI.

### Endpoint

```http
GET /system-info
```

### Information Returned

- Hostname
- Kernel Version
- System Uptime
- CPU Information
- Memory Usage

### Technologies

- FastAPI
- Python
- Linux Commands

### Run

```bash
uvicorn lab2_createyourown_api:app --reload
```

### Open Browser

```text
http://127.0.0.1:8000/system-info
```

### Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Requirements

Install dependencies:

```bash
pip install fastapi uvicorn requests
```

---

## Learning Objectives

This repository demonstrates:

- REST API fundamentals
- API consumption
- API development
- JSON handling
- FastAPI framework
- Linux automation
- Backend development basics

---

## Author

Manish Chawda

Learning Python APIs and FastAPI through hands-on labs.
