#manage.py
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projecthasen.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#urls.py
from django.urls import path
from . import views

#http://127.0.0.1:8000/           =>homepage
#http://127.0.0.1:8000/index      =>homepage
#http://127.0.0.1:8000/blogs      =>blogs
#http://127.0.0.1:8000/blogs/3    =>blog-details

urlpatterns = [
    path("",views.home),
]


#vievs.py
from django.http.response import HttpResponse
from django.shortcuts import render


#create your views here sena
def index(request):
    return HttpResponse('<h1>Home Page</h1>')
