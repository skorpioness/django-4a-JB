from django.urls import path
from . import views
from django.http import HttpResponse
from .models import Question

APP_NAME = "polls"
app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("counter/", views.counter, name="counter"),
    path("basic/", views.basic, name="basic"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote")
]