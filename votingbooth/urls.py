from django.urls import path
from votingbooth import views


urlpatterns = [
    path('', views.avalaible, name='polls/avalaible'),
    #path('<int:id>/vote', views.vote, name='vote'),
    path('results/<int:pk>/', views.result_view.as_view(), name='polls/results'),
]
