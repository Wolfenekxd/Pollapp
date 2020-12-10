from django.urls import path
from votingbooth import views


app_name = 'votingbooth'

urlpatterns = [
    path('', views.avalaible, name='polls/avalaible'),
    path('user_polls', views.user_polls, name='polls/user_polls'),
    path('<int:pk>/', views.detail, name='polls/detail'),
    path('<int:pk>/results', views.results, name='polls/results'),
    path('createpoll/', views.create_poll, name='polls/create'),
    path('polldate/', views.PollCreateView.as_view(), name='poll_add'),
    path('answers/<int:pk>', views.create_answers, name='answers'),
    path('success', views.success, name='polls/success')
]
