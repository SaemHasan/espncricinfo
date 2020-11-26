from django.shortcuts import render, redirect
import cx_Oracle
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
connection = cx_Oracle.connect(user='cricinfo', password='cricinfo', dsn=dsn_tns)
# Create your views here.


def addseries(request):
    # return render(request, 'addteam/index.html')
    if request.method == 'GET':
        if request.session['loginstatus']:
            return render(request, 'addseries/index.html')
        else:
            return redirect('login')
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