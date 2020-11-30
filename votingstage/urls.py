from django.urls import path
from votingstage import views


app_name = 'votingstage'

urlpatterns = [
    path('<int:pk>', views.choice, name='cast/choice'),
    path('<int:pk>/cast', views.vote, name='vote')
]