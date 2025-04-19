## Django REST Framework Complete Authentication API with Simple JWT


## To Run this Project follow below:

```bash
mkvirtualenv authenv
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### There is a File "DjangoAuthAPI.postman_collection" which has Postman Collection You can import this file in your postman to test this API

### Live Api's of Authentication

## Registeration
# Endpoint: `https://inaampython123.pythonanywhere.com/api/user/register/`
# Method: `POST`
# Payload: 
`{
    "email":"itsinaam89@gmail.com",
    "name":"inaam ullah",
    "password":"inaam@123",
    "password2":"inaam@123",
    "tc":"True"   
}`
