from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    name = request.GET.get('name', '匿名')
    return HttpResponse(f'Hello {name}!!!')

def books(request, id):
    return render(request, 'books.html', {'id': id})

def books_list(request):
    try:
        count = int(request.GET.get('count', 10))
    except ValueError:
        # TODO: 不是數字的話，錯誤處理
        return render(request, 'books_error.html')
    items = range(1, count+1)
    return render(request, 'books_list.html', {'items': items, 'message':'訊息！！！'})