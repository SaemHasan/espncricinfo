from django.shortcuts import render
import cx_Oracle
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
connection = cx_Oracle.connect(user='cricinfo', password='cricinfo', dsn=dsn_tns)


# Create your views here.

def teamsingle(request):
    name = request.GET.get('name')
    cursor = connection.cursor()
    sql = "SELECT TEAM_ID FROM TEAM WHERE NAME = '" + name + "'"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()

    team = []

    for r in result:
        team_id = r[0]
        row = {'team_id': team_id}
        team.append(row)
    team_id=team[0]['team_id']
    cursor = connection.cursor()
    sql = "SELECT * FROM PERSON WHERE PERSON_ID=ANY(SELECT COACH_ID FROM COACH WHERE TEAM_ID= '" + team_id + "')"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()

    coach = []

    for r in result:
        first_name = r[1]
        last_name = r[2]
        fullname=first_name + " " + last_name
        row = {'fullname': fullname}
        coach.append(row)

    cursor = connection.cursor()
    sql = "SELECT TEAM1_ID, TEAM2_ID FROM MATCH WHERE WINNER= '" + name + "'"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()

    details = []

    for r in result:
        team1_id=r[0]
        team2_id = r[1]
        row = {'team1_id': team1_id, 'team2_id': team2_id}
        details.append(row)


    return render(request, 'teamsingle/index.html', {'name':name, 'details': details, 'coach':coach})
