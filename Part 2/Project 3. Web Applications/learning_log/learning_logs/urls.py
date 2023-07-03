""" Defines URL patterns for `learning_logs`. """
from django.urls import path
from . import views

app_name = "learning_logs"
urlpatterns = [
    # Home page:
    path("", views.index, name="index"),
    # All topics' page:
    path("topics/", views.topics, name="topics"),
    # A single topic's page:
    path("topics/<int:topic_id>/", views.topic, name="topic"),
]
