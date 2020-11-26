from django.shortcuts import render
import cx_Oracle
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
connection = cx_Oracle.connect(user='cricinfo', password='cricinfo', dsn=dsn_tns)


# Create your views here.

def groundsingle(request):
    ground_name = request.GET.get('name')

    cursor = connection.cursor()
    sql = "SELECT TEAM1_ID, TEAM2_ID, WINNER, WEATHER FROM MATCH WHERE GROUND_ID = ANY(SELECT GROUND_ID FROM GROUND WHERE NAME='"+ground_name+"')"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()

    details = []
    for r in result:
        team1_id=r[0]
        team2_id = r[1]
        winner=r[2]
        weather=r[3]
        row = {'team1_id': team1_id, 'team2_id': team2_id, 'winner': winner,
               'weather': weather}
        details.append(row)

    return render(request, 'groundsingle/index.html', {'details': details})
