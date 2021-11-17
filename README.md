# real-estate-app

To run ->
Run CMD (Windows - in Admin mode) or Terminal (Unix/Mac)
1) cd (change directory) to parent "realestate" directory. Notice there are two, navigate to the first one
2) python -m pip install Django
3) python -m pip install requests
4) python -m pip install boto3
5) python manage.py runserver
6) Enter url as the following -> http://localhost:8000/clientservices/chicago/illinois/

URL variations can be any variation:

City - can be any variation, api will lowercase all letters and then uppercase first letter

State - can be any variation, api will convert any lowercase abbvreviation to uppercase, and convert any full length states to abbvreviations

Available URLS:

1) /clientservices/salelistings/{city}/{state}
2) /clientservices/nearbystations/{latitude}/{longitude}
