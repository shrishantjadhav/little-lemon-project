LITTLE LEMON BOOKING ASSESSMENT STARTER

Requirements:
- Python 3.10+ (Pipfile currently targets Python 3.12)
- MySQL server
- Pipenv

SETUP (PowerShell or terminal)
1. Open a terminal in this folder.
2. Edit littlelemon/settings.py and set DATABASES['default']['PASSWORD'] to your local MySQL password.
3. Create the database in MySQL:
   CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
4. Install and activate dependencies:
   pipenv install
   pipenv shell
5. Create/apply migrations:
   python manage.py makemigrations restaurant
   python manage.py migrate
6. Run:
   python manage.py runserver
7. Visit:
   http://127.0.0.1:8000/
   http://127.0.0.1:8000/book/
   http://127.0.0.1:8000/reservations/
   http://127.0.0.1:8000/bookings?date=YYYY-MM-DD

Notes:
- This is a complete basic implementation, not the original Coursera starter website.
- If your course starter project includes supplied templates/assets, copy those into this project or merge the booking functionality into the starter before submitting.
- A database unique constraint and backend validation both help prevent duplicate date/time bookings.
- The MySQL password is a local placeholder and must be set for your computer.
