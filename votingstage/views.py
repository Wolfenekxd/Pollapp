from django.shortcuts import render,Http404,get_object_or_404
from votingbooth.models import Election, Answers
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.urls import reverse
from rsa_generate import generate_public_key, generate_private_key
from encryption import encryption
from decryption import decryption
# Create your views here.

def choice(request, pk):
    Question = Election.objects.get(pk=pk)
    answers = Answers.objects.filter(Election_Id=pk)
    context = {
        'Question':Question,
        'Answers':answers
    }
    return render(request, 'cast/choice.html', context)   


def vote(request, pk):
    question = get_object_or_404(Election, pk=pk)
    answer = str(question.answers_set.get(pk=request.POST['answer']))
    generate_private_key()
    generate_public_key()
    encryption(answer)
    decrypted_answer = decryption()
    answers_query = Answers.objects.filter(Election_Id=pk)
    for dbanswer in answers_query:
        if dbanswer.Answer == decrypted_answer:
            dbanswer.Result =+ 1
            dbanswer.save()
        else:
            dbanswer.Result = dbanswer.Result        
    return HttpResponseRedirect(reverse('votingbooth:polls/results', args=(question.id,)))


def succes(request, pk):
    election = Election.objects.get(pk=pk)
    answer = Answers.objects.get(pk=6)
    context = {
        'election':election,
        'answer':answer
    }
    return render(request, 'cast/success.html',context)