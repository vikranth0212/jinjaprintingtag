from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='This data is our assumption'
    d={'assumption':data}
    return render(request,'data_render.html',context=d)
def loginpage(request):
    name='vikranth'
    d={'user':name,'age':27}
    return render(request,'loginpage.html',context=d)