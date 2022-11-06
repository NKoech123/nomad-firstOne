# nomad
# Backend

cd backend
python3 -m venv env
source env/bin/activate

#migrations
python manage.py makemigrations
python manage.py migrate

#run server
python manage.py runserver


# Frontend
at root `nomad`
start with `yarn install`
then Run `yarn start`
