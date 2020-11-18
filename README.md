# codeshare
```
python -m venv venv
source venv/bin/activate
pip install Django
pip install djangorestframework
cd codeshare
mkdir sources
echo '{secretkey}' > secretkey.txt
python manage.py makemigrations api
python manage.py makemigrations notes
python manage.py migrate
docker run -p 6379:6379 -d redis:5
python manage.py runserver
```
