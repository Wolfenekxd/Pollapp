from django.urls import path
from votingbooth import views


app_name = 'votingbooth'

urlpatterns = [
    path('', views.avalaible, name='polls/avalaible'),
    #path('<int:id>/vote', views.vote, name='vote'),
    path('<int:pk>/', views.detail, name='polls/detail'),
    path('<int:pk>/results', views.results, name='polls/results'),
    path('createpoll/', views.create_poll, name='polls/create')
]
