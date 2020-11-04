from django.shortcuts import render

# Create your views here.


def addteam(request):
    # return render(request, 'addteam/index.html')
    if request.method == 'GET':
        return render(request, 'addteam/index.html')
    else:
        # name = request.POST['name']
        # country = request.POST['country']
        # Address = request.POST['address']
        # street_no = request.POST['street_no']
        # zip_code = request.POST['pincode']
        # city = request.POST['city']
        file = request.FILES['file_image']
        print(file.name)
        # print(name, country, Address, street_no, zip_code, city)
        handle_uploaded_file(file)
        # return HttpResponse("File uploaded successfuly")
        return render(request, 'adminpage/index.html')


def handle_uploaded_file(f):
    with open('static/homepage/img/speakers/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)