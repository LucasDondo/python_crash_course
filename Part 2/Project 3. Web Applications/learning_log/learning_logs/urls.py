""" Defines URL patterns for `learning_logs`. """
from django.urls import path
from . import views

app_name = "learning_logs"
urlpatterns = [
    # Home page:
    path("", views.index, name="index"),
    # All topics' page:
    path("topics/", views.topics, name="topics"),
    # Creating new topic:
    path("topics/new/", views.new_topic, name="new_topic"),
    # A single topic's page:
    path("topics/<int:topic_id>/entries", views.topic, name="topic"),
    # Creating new entry:
    path("topics/<int:topic_id>/entries/new", views.new_entry, name="new_entry"),
    # Editing a previous entry:
    path(
        "topics/<int:topic_id>/entries/<int:entry_id>/",
        views.edit_entry,
        name="edit_entry",
    ),
]
