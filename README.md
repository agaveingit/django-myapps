# Django Web Application Project

This project is a collection of simple web applications built with Django. It provides two main utilities: a number-to-text converter and a QR code generator.

## Features

1.  **Number to Text Converter**

    - Converts numeric input into its text representation in Indonesian.
    - Example: `123` becomes `seratus dua puluh tiga`.
    - URL: `/konversi/`

2.  **QR Code Generator**
    - Creates a QR code from text or URL input.
    - Provides a live preview of the QR code on the page.
    - Allows users to download the QR code in **PNG** or **SVG** format.
    - URL: `/qrgen/`

## Technologies Used

- **Backend**: Python, Django
- **Library**: `qrcode[pil]` for QR code generation.

## Installation and Setup

1.  **Clone this repository.**

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Django development server:**

    ```bash
    python manage.py runserver
    ```

5.  **Open your browser and access the application:**
    - **Home Page**: http://127.0.0.1:8000/
    - **Number Converter**: http://127.0.0.1:8000/konversi/
    - **QR Generator**: http://127.0.0.1:8000/qrgen/

- **Or if you have docker**
  ```bash
  docker compose up --build
  ```
  - Open localhost:8080

---
