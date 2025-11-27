# 🤰 Pregnancy Tracker – A Django Web Application

**Pregnancy Tracker** is a modern, responsive, and user-friendly Django application designed to help expecting mothers monitor their pregnancy journey—from the first day of their last menstrual period (LMP) to their baby’s birth and beyond, including immunization scheduling.

Built with care, security, and usability in mind, this app provides personalized insights, milestone tracking, and educational support—all while adhering to Django best practices and clean URL design principles.

---

## ✨ Features

- **Pregnancy Timeline Calculator**  
  Enter your Last Menstrual Period (LMP) to automatically calculate:
  - Weeks pregnant
  - Trimester
  - Estimated due date (EDD)

- **Immunization Schedule**  
  View a complete, medically aligned baby vaccination timeline based on birth date, with clear explanations for each vaccine.

- **Record Management**  
  Create, view, edit, and delete pregnancy records with ease.

- **Modern & Responsive UI**  
  Clean, vibrant design using Bootstrap 5, custom CSS, and mobile-first principles—works beautifully on phones, tablets, and desktops.

- **Educational Content**  
  Context-aware tips and vaccine information to empower informed decisions (no diagnostic AI—only supportive guidance).

- **Secure & Private**  
  Session-based record isolation ensures users only access their own data (extendable to user accounts).

- **Clean URL Design**  
  Follows Django’s URL dispatcher best practices (as per [Django 5.1 docs](https://docs.djangoproject.com/en/5.1/topics/http/urls/)) with named patterns and logical structure.

---

## 🛠️ Tech Stack

- **Backend**: Python 3 + Django 5.1
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Database**: SQLite (default; easily swappable to PostgreSQL/MySQL)
- **Static Assets**: Custom CSS with Google Fonts (`Inter` + `Poppins`)
- **Security**: CSRF protection, session-based data isolation

---

## 📁 Project Structure

```
ptracker/
├── ptracker/              # Main Django project
├── apps/
│   └── (future expansion)
├── templates/             # All HTML templates
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── pregnancy_list.html
│   ├── immunization_schedule.html
│   └── ...
├── static/
│   └── style/
│       ├── bootstrap/
│       └── style.css
├── models.py              # Pregnancy model with auto-calculated due date
├── views.py               # Clean, DRY views with form handling
├── forms.py               # ModelForm with validation
├── urls.py                # Clean, named URL patterns (no hardcoded paths)
└── manage.py
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/pregnancy-tracker.git
   cd pregnancy-tracker
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # OR
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Visit** `http://127.0.0.1:8000` in your browser!

---

## 📈 Future Enhancements

- User authentication & multi-device sync
- Weekly email/SMS reminders
- Journaling with AI summarization (opt-in)
- Exportable PDF records
- Multilingual support (via Django i18n)

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 💙 Inspired By

> *"Every pregnancy is a story. We’re here to help you write yours."*

---

**Made with ❤️ for expecting mothers everywhere.**  
*Empowering journeys, one week at a time.*
