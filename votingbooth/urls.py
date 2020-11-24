from django.urls import path
from votingbooth import views


app_name = 'votingbooth'

urlpatterns = [
    path('', views.avalaible, name='polls/avalaible'),
    #path('<int:id>/vote', views.vote, name='vote'),
    path('<int:election_id>/', views.results, name='results'),
    path('createpoll/', views.create_poll, name='polls/create')
]
