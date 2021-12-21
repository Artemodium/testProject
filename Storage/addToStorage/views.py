from django.shortcuts import render
from .forms import AddEqiupmentsForm
from .services import  parsingSerials, insertTobase


def index(request):
    return render(request, 'addToStorage/main.html')

def store(request):
    parsedData={'correct':[], 'incorrect':[], 'doubles':[]}
    if request.method == 'POST':
        form = AddEqiupmentsForm(request.POST)
        if form.is_valid():
            parsedData = parsingSerials(form.cleaned_data)
            insertTobase(form.cleaned_data, parsedData['correct'])
            form = AddEqiupmentsForm()
    else:
        form = AddEqiupmentsForm()

    return render(request, 'addToStorage/store.html', {'form': form,
                                                       'parsedData': parsedData,
                                                       'doubles_len': len(parsedData['doubles']),
                                                       'doubles': ', '.join(parsedData['doubles']),
                                                       'correct': ', '.join(parsedData['correct']),
                                                       'correct_len': len(parsedData['correct']),
                                                       'incorrect_len': len(parsedData['incorrect']),
                                                       'incorrect': ', '.join(parsedData['incorrect'])})

