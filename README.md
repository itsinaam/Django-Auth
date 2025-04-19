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
# Endpoint: https://inaampython123.pythonanywhere.com/api/user/register/
# Method: POST
# Payload: 
`{
    "email":"itsinaam89@gmail.com",
    "name":"inaam ullah",
    "password":"inaam@123",
    "password2":"inaam@123",
    "tc":"True"   
}`

## Login
# Endpoint: https://inaampython123.pythonanywhere.com/api/user/login/
# Method: POST
# Payload: 
`{
    "email":"itsinaam89@gmail.com",
    "password":"inaam@123"
}`


## Profile
# Endpoint: https://inaampython123.pythonanywhere.com/api/user/profile/
# Method: GET
# Header: Bearer {token}


## Change Password
# Endpoint: https://inaampython123.pythonanywhere.com/api/user/changepassword/
# Method: POST
# Payload: 
`{
    "password":"hello",
    "password2":"hello"
}`


## Send Reset Password Email
# Endpoint: https://inaampython123.pythonanywhere.com/api/user/send-reset-password-email/
# Method: POST
# Payload: 
`{
    "email":"itsinaam89@gmail.com"
}`



## Reset Password
# Endpoint: https://inaampython123.pythonanywhere.com/api/user/reset-password/NA/coi6if-7e209b758cfec9d334ac85d8e478a73f/
# Method: POST
# Payload:
`{
    "password":"hello123",
    "password2":"hello123"
}`

