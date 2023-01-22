from django.shortcuts import render
from .models import Producer


def all_producers(request):
    """ A view to show all producers """

    producers = Producer.objects.all()

    context = {
        'producers': producers,
    }

    return render(request, 'producers/producers.html', context)
