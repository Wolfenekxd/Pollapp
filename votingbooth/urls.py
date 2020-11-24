from django.urls import path
from votingbooth import views


app_name = 'votingbooth'

urlpatterns = [
    path('', views.avalaible, name='polls/avalaible'),
    #path('<int:id>/vote', views.vote, name='vote'),
    path('<int:election_id>/', views.election_detail, name='results'),
]
