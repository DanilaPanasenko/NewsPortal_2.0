from django.urls import path
from news.views import PostUpdate

urlpatterns = [
    path('', PostUpdate.as_view()),
]
