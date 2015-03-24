from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Question, Reponse


def index(request):
    questions = Question.objects.all()
    contexte = {
        'questions': questions
    }
    return render(request, 'sondages/index.html', contexte)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'sondages/detail.html'
    context_object_name = 'question'


def detail(request, id):
    question = get_object_or_404(Question, id=id)
    contexte = {
        'question': question
    }
    return render(request, 'sondages/detail.html', contexte)


def resultats(request, id):
    question = get_object_or_404(Question, id=id)
    contexte = {
        'question': question
    }
    return render(request, 'sondages/resultats.html', contexte)

    
def voter(request, id):
    if request.method == 'POST':
        reponse_id = request.POST.get("reponse")
        reponse = Reponse.objects.get(id=reponse_id)
        reponse.score = reponse.score + 1
        reponse.save()
        return redirect('sondages:resultats', id)
    return redirect('sondages:index')
