from django.contrib.auth import logout
from django.shortcuts import render, redirect
import random, cx_Oracle, json

dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
connection = cx_Oracle.connect(user='cricinfo', password='cricinfo', dsn=dsn_tns)


# Create your views here.
def home(request):
    request.session['loginstatus'] = False
    logout(request)
    cursor = connection.cursor()
    sql = "SELECT * FROM TEAM"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    teams = []
    for r in result:
        id = r[0]
        name = r[1]
        image_link = r[2]
        row = {'id': id, 'name': name, 'image_link': image_link}
        teams.append(row)

    curs = connection.cursor()
    sql = "SELECT * FROM SERIES"
    curs.execute(sql)
    result = curs.fetchall()
    curs.close()
    series = []

    for r in result:
        id = r[0]
        name = r[1]
        host = r[2]
        motm = r[3]
        cur = connection.cursor()
        sql = "SELECT * from PERSON WHERE PERSON_ID='"+motm+"'"
        cur.execute(sql)
        re = cur.fetchall()
        cur.close()
        for d in re:
            fn = d[1]
            ln = d[2]
            fullname = fn+" "+ln
        winner = r[4]
        image_link = r[5]
        if image_link is None:
            image_link = "default.jpg"
        row = {'id': id, 'name': name, 'host': host, 'motm': fullname, 'winner': winner, 'image_link': image_link}
        series.append(row)

    return render(request, 'homepage/index.html', {'teams': teams, 'series': series})


def series_details(request):
    series_name = request.GET.get('name')
    cursor = connection.cursor()
    sql = "SELECT * FROM SERIES WHERE NAME='"+series_name+"'"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()

    dict_result = []

    for r in result:
        id = r[0]
        name = r[1]
        host = r[2]
        motm = r[3]
        cur = connection.cursor()
        sql = "SELECT * from PERSON WHERE PERSON_ID='" + motm + "'"
        cur.execute(sql)
        re = cur.fetchall()
        cur.close()
        for d in re:
            fn = d[1]
            ln = d[2]
            fullname = fn + " " + ln
        winner = r[4]
        image_link = r[5]
        if image_link is None:
            image_link = "default.jpg"
        row = {'id': id, 'name': name, 'host': host, 'motm': fullname, 'winner': winner, 'image_link': image_link}
        dict_result.append(row)
    return render(request, 'homepage/speaker-details.html', {'name': series_name, 'series': dict_result[0]})


def teams(request):
    all_team = []
    if request.method=="GET":
        cursor = connection.cursor()
        sql = "SELECT * FROM TEAM"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()

        dict_result = []
        all_team.clear()
        for r in result:
            id = r[0]
            name = r[1]
            all_team.append(name)
            image_link = r[2]
            row = {'id': id, 'name': name, 'image_link': image_link}
            dict_result.append(row)

        json_teams = json.dumps(all_team)

        return render(request, 'homepage/teams.html', {'results': dict_result, 'allteam': json_teams})
    else:
        name = request.POST['search2']
        return redirect('teams')
