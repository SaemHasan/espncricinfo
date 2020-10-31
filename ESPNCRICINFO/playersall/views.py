from django.db import connection
from django.shortcuts import render

# Create your views here.


def playersall(request):
    cursor = connection.cursor()
    sql = "SELECT * FROM PERSON"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    dict_result = []

    for r in result:
        id = r[0]
        first_name = r[1]
        last_name = r[2]
        full_name = first_name+" "+last_name
        nationality = r[3]
        dob = r[4]
        row = {'id': id, 'first_name': first_name, 'last_name': last_name,'full_name': full_name, 'nationality': nationality,'date_of_birth': dob}
        dict_result.append(row)

    return render(request, 'playersall/index.html', {'persons': dict_result})