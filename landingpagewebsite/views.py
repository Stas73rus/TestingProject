from django.shortcuts import render

def test(request):
    name = 'Stas'
    text = 'ferfer'
    return render(request, './index.html', {
        'myyytest': name,
        'moo': text,
    })