from django.shortcuts import render
from django.http import HttpResponse

clicked =0
name_2='Akhil'
fruits = ['mango','banana','apple','guava']
def index(request) :
    global clicked
    my_dict = { 'inject_var' : clicked }
    clicked +=1
    return render(request, 'index.html', context=my_dict)

def help(request) :
    return render(request, 'help.html')

def name(request) :
    name_1 = { 'name_3' : name_2 }
    return render(request, 'index.html', context=name_1)

def loop(request) :
    loop_1 = { 'fruit' : fruits}
    return render(request, 'index.html',context=loop_1)
