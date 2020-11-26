from django.shortcuts import render, redirect
import csv, io
import cx_Oracle
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
connection = cx_Oracle.connect(user='cricinfo', password='cricinfo', dsn=dsn_tns)
# Create your views here.


def addmatch(request):
    if request.method == 'GET':
        if request.session['loginstatus']:
            return render(request, 'addmatch/index.html')
        else:
            return redirect('login')

    else:
        # name = request.POST['name']
        # country = request.POST['country']
        # Address = request.POST['address']
        # street_no = request.POST['street_no']
        # zip_code = request.POST['pincode']
        # city = request.POST['city']

        promot = {
            'order': 'MATCH_ID,	PERSON_ID,	SCORED_RUNS,	NUM_OF_BALLS_BATTED,	NUM_OF_FOURS,	NUM_OF_SIXES,	NOT_OUT,	NUM_OF_OVERS_BOWLED,	GIVEN_RUNS,	NUM_OF_WICKETS'

        }
        file = request.FILES['player_score']
        dataset=file.read().decode('UTF-8')
        io_string=io.StringIO(dataset)
        next(io_string)
        for col in csv.reader(io_string, delimiter='.', quotechar="|"):
            match_id=col[0];
            print(match_id)

        print(file.name)
        # print(name, country, Address, street_no, zip_code, city)
        # return HttpResponse("File uploaded successfuly")
        return render(request, 'adminpage/index.html')
