from django.shortcuts import render

# Create your views here.


def addplayer(request):
    if request.method == 'GET':
        return render(request, 'addplayer/index.html')
    else:
        # name = request.POST['name']
        # country = request.POST['country']
        # Address = request.POST['address']
        # street_no = request.POST['street_no']
        # zip_code = request.POST['pincode']
        # city = request.POST['city']
        file = request.FILES['image']
        print(file.name)
        # print(name, country, Address, street_no, zip_code, city)
        handle_uploaded_file(file)
        # return HttpResponse("File uploaded successfuly")
        return render(request, 'adminpage/index.html')


def handle_uploaded_file(f):
    with open('static/playersingle/images/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)