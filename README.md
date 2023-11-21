# Django-CNLTHD
# clone project:
git clone url:project

# create env for python
python3 -m venv env

# Activate env
env\Scripts\activate

# migrations
python3 manage.py makemigrations
python3 manage.py migrate

# create admin account
python3 manage.py createsuperuser

# run server
python3 manage.py runserver

