from django.shortcuts import render, redirect
import cx_Oracle
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
connection = cx_Oracle.connect(user='cricinfo', password='cricinfo', dsn=dsn_tns)
# Create your views here.


def addumpire(request):
    if request.method == 'GET':
        if request.session['loginstatus']:
            return render(request, 'addumpire/index.html')
        else:
            return redirect('login')

    else:
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        country = request.POST['company']
        dob = request.POST['phone_number']
        file = request.FILES['image']
        uid = country+"_"+lname+"_"+dob
        print(file.name)
        print(fname, lname, country, dob)
        handle_uploaded_file(file)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO PERSON VALUES(:UmID,:FNAME,:LNAME,:uCOUNTRY,TO_DATE(:DOB,'YYYY-MM-DD'),:uIMAGE)", UmID=uid, FNAME=fname, LNAME=lname, uCOUNTRY=country, DOB=dob, uIMAGE=file.name)
        cursor.execute("INSERT INTO UMPIRE VALUES (:UmID,NULL)", UmID=uid)
        connection.commit()
        cursor.close()
        # return HttpResponse("File uploaded successfuly")
        return render(request, 'adminpage/index.html')


def handle_uploaded_file(f):
    with open('static/umpiresingle/images/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)