# Smartphone Management Web Application 📱

A full-stack web application built with Python (Flask) and SQLite for managing smartphone inventory and information. 

This project provides a clean user interface to browse, add, edit, and delete smartphone records with a relational SQLite database integration.

---

## 🚀 Features

- Inventory Management: View, add, and delete smartphone records[span_0](start_span)[span_0](end_span).
- Authentication: User login functionality[span_1](start_span)[span_1](end_span).
- Templating: Built using Flask's Jinja2 template inheritance (layout.html) for consistent UI layout[span_2](start_span)[span_2](end_span).
- Database Integration: SQLite integration (smart_db.db) managed via custom Python database helper scripts (smart_sqlite.py)[span_3](start_span)[span_3](end_span).
- Error Handling: Custom error page to gracefully handle runtime issues[span_4](start_span)[span_4](end_span).

---

## 🛠️ Tech Stack & Structure

- Backend: Python (Flask)[span_5](start_span)[span_5](end_span)
- Database: SQLite[span_6](start_span)[span_6](end_span)
- Frontend: HTML5, CSS3 (main.css), JavaScript[span_7](start_span)[span_7](end_span)
- Template Engine: Jinja2[span_8](start_span)[span_8](end_span)

### Project Structure
`text
smartphone/
├── static/
│   ├── css/main.css      # Styling files
│   ├── img/              # Product and static images
│   └── js/               # Frontend scripts
├── templates/
│   ├── layout.html       # Base HTML template
│   ├── index.html        # Home page
│   ├── phoneslist.html   # List of smartphones
│   ├── newphone.html     # Add smartphone form
│   ├── deletephone.html  # Delete confirmation
│   ├── login.html        # Login page
│   ├── about.html        # About page
│   └── error.html        # Error handling page
├── smart_db.db           # SQLite database
├── smart_sqlite.py       # Database helper
├── smartphone.py         # App script / routes
└── PhoneWeb.py           # Main server execution entry point
