from django.urls import path
from votingbooth import views


app_name = 'votingbooth'

urlpatterns = [
    path('', views.avalaible, name='polls/avalaible'),
    path('<int:pk>/', views.detail, name='polls/detail'),
    path('<int:pk>/results', views.results, name='polls/results'),
    path('createpoll/', views.create_poll, name='polls/create'),
    path('polldate/', views.PollCreateView.as_view(), name='poll_add')
    path('answers', views.create_answers, name='polls/answers'),
    path('success', views.success, name='polls/success')
]
