from django.shortcuts import render, get_object_or_404
from .models import Election,Answers
from .db import election_data
from django.views.generic import ListView , DetailView
# Create your views here.

def avalaible(request):
    question_list = Election.objects.all()
    context = {'question_list': question_list}
    return render(request, 'polls/avalaible.html',context)


class PollsListView(ListView):
    queryset = Election.objects.all()
    context_object_name = 'Election'
    template_name = 'polls/avalaible.html'

def election_detail(request, election):
    election = get_object_or_404(election)
    return render(request, 'polls/detail.html', {'election':election})

def results(request, election_id):
    answers = Answers.objects.all(election_id=election_id)
    election = Election.objects.all(id=election_id)
    return render(request,'polls/results.html', {'answers':answers,'election':election})


'''def results(request, id):
    context = election_data(id)
    return render(request, 'polls/results.html', context)'''