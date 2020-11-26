from django.shortcuts import render
import cx_Oracle
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
connection = cx_Oracle.connect(user='cricinfo', password='cricinfo', dsn=dsn_tns)


# Create your views here.

def playersingle(request):
    name = request.GET.get('name')
    part = name.split(" ")
    first_name = part[0]
    last_name = part[1]
    cursor = connection.cursor()
    sql = "SELECT * FROM PERSON WHERE FIRST_NAME='" + first_name + "' AND LAST_NAME='" + last_name + "'"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()

    dict_result = []

    for r in result:
        id = r[0]
        first_name = r[1]
        last_name = r[2]
        full_name = first_name + " " + last_name
        nationality = r[3]
        dob = r[4]
        image_link = r[5]
        if image_link is None:
            image_link = "default.jpg"
        row = {'id': id, 'first_name': first_name, 'last_name': last_name, 'full_name': full_name,
               'nationality': nationality, 'date_of_birth': dob, 'image_link': image_link}
        dict_result.append(row)

    return render(request, 'playersingle/playersingle.html', {'name': name, 'details': dict_result[0]})
