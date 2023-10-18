from django.shortcuts import render

from django.shortcuts import render


def main(request, pk=None):
    context = {}
    return render(request, 'page.html', context)
