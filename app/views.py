from django.shortcuts import render

from app.models import ScrabbleWord
from app.forms import RackForm
from app import utils


def index(request):
    DICTIONARY = ScrabbleWord.objects.all()
    valid_words = []
    if request.method == 'POST':
        form = RackForm(request.POST)
        if form.is_valid():
            rack = form.cleaned_data['rack']

            for word in DICTIONARY.iterator():
                if utils.is_subset(word.word, rack.upper()):
                    valid_words.append(word)
    else:
        form = RackForm()

    context = {
        'form': form,
        'valid_words': valid_words
    }
    return render(request, 'app/index.html', context)
