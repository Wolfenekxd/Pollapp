from django.shortcuts import render,Http404,get_object_or_404
from votingbooth.models import Election, Answers
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.urls import reverse
# Create your views here.

def choice(request, pk):
    Question = Election.objects.get(pk=pk)
    answers = Answers.objects.filter(Election_Id=pk)
    context = {
        'Question':Question,
        'Answers':answers
    }
    return render(request, 'cast/choice.html', context)   


'''def vote(request, pk):
    question = get_object_or_404(Election, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, ObjectDoesNotExist):
        return render(request, 'cast/choice.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.Result += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:polls/results', args=(question.id,)))'''

