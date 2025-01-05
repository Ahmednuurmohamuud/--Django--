from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    data = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body bgcolor="navy"><br><br><br><br><br><br><br>
    <h1><center><span style="background-color: yellow;">WELCOME TO SOMALIA WEBSITE</span></center></h1>
</body>
</html>
    """
    return HttpResponse(data)