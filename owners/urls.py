from django.urls import path

from owners.views import login

app_name = 'owners'

urlpatterns = [
    path('login/', login, name='example')
]
