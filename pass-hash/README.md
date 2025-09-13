# MLH Global Hack Week 2026: Password Hashing Web App

## Problem Statement
Build a secure, educational, and visually engaging password hashing web application for MLH Global Hack Week 2026. The app should:
- Stand out with original features and modern UI/UX.
- Demonstrate password hashing and security best practices.
- Educate users about password safety and hash storage.
- Be deployable on free hosting platforms (e.g., Render).

## What We Built
A full-stack password hashing web app with:
- **User Signup & Login:** Secure authentication using hashed passwords (bcrypt).
- **Password Strength Meter:** Real-time feedback on password strength during signup.
- **Password Visibility Toggle:** Show/hide password input for better UX.
- **Brute-force Protection:** Limits failed login attempts for security.
- **Hash Visualization:** Shows the actual hash stored in the database after signup.
- **Celebration Animation:** Confetti/firecracker animation on successful signup/login.
- **Modern Responsive UI:** Clean, mobile-friendly design with custom CSS.
- **Health Check Endpoint:** `/healthz` for deployment monitoring.

## How We Built It
- **Backend:** Python 3, Flask web framework
- **Password Hashing:** bcrypt library
- **Database:** SQLite for user storage
- **Frontend:** HTML, CSS, JavaScript (for strength meter, visibility toggle, animation)
- **Deployment:** Render.com (free tier)
- **Production Server:** gunicorn (recommended for deployment)

### Folder Structure
```
pass-hash/
├── app.py                # Main Flask app
├── requirements.txt      # Python dependencies
├── data.db               # SQLite database (auto-created)
├── static/
│   └── style.css         # Custom styles
└── templates/
    ├── signup.html       # Signup form
    ├── login.html        # Login form
    ├── done.html         # Signup success + hash
    └── welcome.html      # Login success + animation
```

## How to Access the Website
1. **Live Demo:**
   - Visit: [https://password-ing.onrender.com](https://password-ing.onrender.com)

2. **Local Setup:**
   - Clone the repo:
     ```bash
     git clone https://github.com/UNKN0WN006/mlh-events-submissions.git
     cd mlh-events-submissions/pass-hash
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run locally:
     ```bash
     python app.py
     ```
   - Access at: `http://localhost:10000` (or the port shown in terminal)

3. **Deployment (Render):**
   - Set root directory to `pass-hash`
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
   - Health check path: `/healthz`

## Features Explained
- **Signup:**
  - Enter username and password
  - Password strength meter guides user
  - Password is hashed and stored securely
  - Hash is shown after signup (educational)
  - Confetti animation celebrates success

- **Login:**
  - Enter credentials
  - Brute-force protection limits failed attempts
  - On success, user is welcomed with animation
  - Option to view stored hash

- **Security:**
  - Passwords are never stored in plain text
  - Hashing uses bcrypt with salt
  - Brute-force protection via session tracking

- **UI/UX:**
  - Responsive design for all devices
  - Modern color scheme and animations
  - Password visibility toggle for convenience

## Technologies Used
- Python 3
- Flask
- bcrypt
- SQLite
- HTML/CSS/JavaScript
- gunicorn (for deployment)

## Contributing
Pull requests and suggestions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
MIT

---

**Made for MLH Global Hack Week 2026.**
