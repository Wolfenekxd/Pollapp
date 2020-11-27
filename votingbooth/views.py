from django.shortcuts import render, get_object_or_404,redirect
from .models import Election,Answers
from django.views.generic import ListView , DetailView
from .forms import ElectionForm, AnswerForm
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib import messages 
# Create your views here.

def avalaible(request):
    question_list = Election.objects.all()
    context = {'question_list': question_list}
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
            election = election_form.save(commit=False)
            election.Owner_Id_id = request.user.id
            election.save()
        else:
            print(election_form)
    else:
        election_form = ElectionForm()

    return render(request, 'polls/polls_form.html', {'election_form':election_form})    

def create_answers(request):
    
    if request.method == 'POST':
        answer_form = AnswerForm(data=request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.Election_Id_id = 1
            answer.save()
            messages.info(request, 'Answer ' + str(answer) + ' added')
        else:    
            print(answer_form)
    else:
        answer_form = AnswerForm()

    return render(request, 'polls/answers_form.html', {'answer_form':answer_form})    


def success(request):
    return render(request, 'polls/success.html')    