from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'home.html', { 'promenna1': 'tohle je hodnota ze slovníku',
                                         'promenna2': 'tohle je hodnota ze slovníku'})

def about(request):
    return HttpResponse('<h1>O nás</h1>')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1

    return render(request,'count.html', {'fulltext':fulltext, 'worddict':worddictionary, 'delkalistu':len(wordlist)})


slovnik = 'Hello'

def about_view(request):



    return render(request,'about.html',{'slovnik':slovnik})
