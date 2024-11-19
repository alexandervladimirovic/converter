from django.shortcuts import render

import requests


def index(request):
    """
    A view for converting currency.
    
    If the request is GET, it will return a form with all the currencies.
    
    If the request is POST, it will convert the currency and return the result.
    """
    responce = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
    currencies = responce.get('rates')

    if request.method == 'GET':

        context = {
            'currencies': currencies
        }



 

        return render(request, 'exchance_app/index.html', context)
    
    if request.method == 'POST':
        from_amount = float(request.POST.get('amount'))
        from_curr = request.POST.get('from_curr')
        to_curr = request.POST.get('to_curr')

        converted_amount = round(currencies[to_curr] / currencies[from_curr] * float(from_amount), 2)

        context = {
            'from_curr': from_curr,
            'to_curr': to_curr,
            'from_amount': from_amount,
            'currencies': currencies,
            'converted_amount': converted_amount
        }

        return render(request, 'exchance_app/index.html', context)
        

