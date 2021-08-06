# URL patterns allow you to map URLs to views. A URL pattern is composed of a
# string pattern, a view, and, optionally, a name that allows you to name the URL
# project-wide. Django runs through each URL pattern and stops at the first one
# that matches the requested URL. Then, Django imports the view of the matching
# URL pattern and executes it, passing an instance of the HttpRequest class and
# the keyword or positional arguments

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    #post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]

