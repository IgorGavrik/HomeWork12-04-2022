from django.urls import path
from my_app.views import MainView

urlpatterns = [
    path('', MainView.as_view(), name="form_profile")
]