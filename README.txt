Little Lemon Restaurant API - Capstone Project

SETUP
1. Install Python 3.10+ and MySQL.
2. Extract this ZIP and open the extracted folder in VS Code.
3. Create and activate a virtual environment:
   Windows: py -m venv .venv
   Windows PowerShell: .venv\Scripts\Activate.ps1
   macOS/Linux: python3 -m venv .venv && source .venv/bin/activate
4. Install dependencies: pip install -r requirements.txt
5. Create a MySQL database named littlelemon.
6. Set database environment variables (or update config/settings.py):
   DB_NAME=littlelemon
   DB_USER=your_mysql_user
   DB_PASSWORD=your_mysql_password
   DB_HOST=127.0.0.1
   DB_PORT=3306
7. Run: python manage.py makemigrations restaurant
8. Run: python manage.py migrate
9. Create an admin user: python manage.py createsuperuser
10. Start: python manage.py runserver
11. Open http://127.0.0.1:8000/

IMPORTANT
This is a starter project. Configure and test it with your own MySQL credentials before submitting.
Commit and push the complete project to GitHub. In the course submission, paste the GitHub repository URL if the assignment asks for it.

API PATHS FOR PEER REVIEW
GET     /restaurant/menu/
POST    /restaurant/menu/
GET     /restaurant/menu/<id>/
PUT     /restaurant/menu/<id>/
DELETE  /restaurant/menu/<id>/
GET     /restaurant/booking/tables/
POST    /restaurant/booking/tables/
GET     /restaurant/booking/tables/<id>/
PUT     /restaurant/booking/tables/<id>/
DELETE  /restaurant/booking/tables/<id>/
POST    /api-token-auth/          (DRF token authentication; create a user first)
GET     /admin/                   (Django admin)

Testing
Run: python manage.py test
Use Insomnia to send requests to http://127.0.0.1:8000/restaurant/menu/ and
http://127.0.0.1:8000/restaurant/booking/tables/.
