from django.shortcuts import render, redirect
from .models import Terms
from .forms import TermsForm

def create_term(request):
    if request.method == 'POST':
        form = TermsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("term_list")
    else:
        form = TermsForm()
    
    context = {
        'form': form
    }
    return render(request, 'evaluation/term/create.html', context)

def terms_list(request):
    terms = Terms.objects.all()
    context = {
        'terms': terms,
    }
    return render(request, 'evaluation/term/list.html', context)