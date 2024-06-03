from django.shortcuts import render

def simple(request):
    
    return render(request, 'simple.html',{})


def dinamico(request,name):
    categories=["code","design","marketing"]
    context={"name":name,"categories":categories} 
    return render(request, 'dinamico.html',context)


# from django.http import HttpResponse
# def home(request):
#     return HttpResponse("tuki, esto funca papá")
