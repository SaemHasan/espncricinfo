from django.shortcuts import render, redirect
from loginpage.views import getlogin
# Create your views here.



def addground(request):
    if request.method == 'GET':
        if True:
            return render(request, 'addground/index.html')
        else:
            return redirect('login')
    else:
        name = request.POST['name']
        country = request.POST['country']
        Address = request.POST['address']
        street_no = request.POST['street_no']
        zip_code = request.POST['pincode']
        city = request.POST['city']
        file = request.FILES['image']
        print(file.name)
        print(name, country, Address, street_no, zip_code, city)
        handle_uploaded_file(request.FILES['image'])
        # return HttpResponse("File uploaded successfuly")
        return render(request, 'adminpage/index.html')

def handle_uploaded_file(f):
    with open('static/grounds/images/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


