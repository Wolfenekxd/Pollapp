from django.shortcuts import render, get_object_or_404,redirect
from .models import Election,Answers
from .db import election_data, election_list,answer_list
from django.views.generic import ListView , DetailView
from .forms import ElectionForm
from django.contrib.auth.models import User
from django.http import Http404
# Create your views here.

def avalaible(request):
    question_list = Election.objects.all()
    context = {'question_list': question_list, }
    return render(request, 'polls/avalaible.html',context)


class PollsListView(DetailView):
    model = Election
    template_name = 'polls/detail.html'


def detail(request, pk):
    election = Election.objects.get(pk=pk)
    answers = Answers.objects.filter(Election_Id=pk)
    context = {
        'election':election,
        'answers':answers,     
    }
    return render(request, 'polls/detail.html', context)

def results(request, pk):
    answers = Answers.objects.filter(Election_Id=pk)
    election = Election.objects.get(pk=pk)
    labels = []
    data = []
    for answer in answers:
        labels.append(answer.Answer)
        data.append(answer.Result)

    context = {
        'answers':answers,
        'election':election,
        'labels':labels,
        'data':data
    }
    return render(request,'polls/results.html',context)


def create_poll(request):
    
    if request.method == 'POST':
        election_form = ElectionForm(data=request.POST)
        if election_form.is_valid():
            print(election_form)
            election_form.save()
            return redirect('answers_form.html')
        else:
            raise Http404    
    else:
        election_form = ElectionForm()

    return render(request, 'polls/polls_form.html', {'election_form':election_form})    


