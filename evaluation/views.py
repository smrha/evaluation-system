from django.shortcuts import render, redirect, get_object_or_404
from .models import Terms
from .forms import TermsForm

def edit_term(request, id):
    term = get_object_or_404(Terms, id=id)

    if request.method == 'POST':
        form = TermsForm(request.POST, instance=term)

        if form.is_valid():
            form.save()
            return redirect("term_list")
    else:
        form = TermsForm(instance=term)
    
    context = {
        'form': form,
        'term': term,
    }
    return render(request, 'evaluation/term/edit.html', context)

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