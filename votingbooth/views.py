from django.shortcuts import render, get_object_or_404
from .models import Election
from .db import election_data
from django.views.generic import ListView , DetailView
# Create your views here.

def avalaible(request):
    question_list = Election.objects.order_by('End_date')
    context = {'question_list': question_list}
    return render(request, 'polls/avalaible.html',context)


class result_view(DetailView):
    model = Election
    template_name = 'detail.html'


'''def results(request, id):
    context = election_data(id)
    return render(request, 'polls/results.html', context)'''