from django.shortcuts import render
import cx_Oracle
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
connection = cx_Oracle.connect(user='cricinfo', password='cricinfo', dsn=dsn_tns)


# Create your views here.

def groundsingle(request):
    ground_name = request.GET.get('name')

    cursor = connection.cursor()
    sql = "SELECT TEAM1_ID, TEAM2_ID, WINNER, WEATHER,MATCH_ID FROM MATCH WHERE GROUND_ID = ANY(SELECT GROUND_ID FROM GROUND WHERE NAME='"+ground_name+"')"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()

    cursor = connection.cursor()
    cursor.execute("SELECT GROUND_ID FROM GROUND WHERE NAME=:GNAME", GNAME=ground_name)
    result1 = cursor.fetchall()[0]
    # print(result1[0])
    grid = result1[0]
    result2 = cursor.callfunc('HIGHESTWICKET_IN_GROUD', str, [grid])

    data = result2.split(" ")
    fullname = ""
    num_wickets = ""
    if(data[1] !='DATA' or data[1]!='MATCH'):
        cursor.execute("SELECT * FROM PERSON WHERE PERSON_ID=:PrID", PrID=data[1])
        result3 = cursor.fetchall()[0]
        # print(result3)
        fullname = result3[1]+" "+result3[2]
        num_wickets = data[2]
        print(fullname, num_wickets)

    highestWicketTaker ={'fullname': fullname, 'wickets': num_wickets}

    result4 = cursor.callfunc('HIGHESTRUN_IN_GROUD', str, [grid])
    cursor.execute("SELECT SUM(SCORED_RUNS) FROM PLAYER_SCORE WHERE MATCH_ID=:MID", MID=result4)
    scored_runs = cursor.fetchall()[0][0]
    cursor.execute("SELECT TEAM1_ID,TEAM2_ID FROM MATCH WHERE MATCH_ID=:MID", MID=result4)
    teams = cursor.fetchall()[0]
    team1 = teams[0]
    team2 = teams[1]

    cursor.execute("SELECT MATCH_DATE FROM TEAM_MATCH WHERE MATCH_ID=:MID", MID=result4)
    matchdate = cursor.fetchall()[0][0]
    print(team1, team2, scored_runs, matchdate)

    highestScoredRunsMatch = {'team1':team1, 'team2': team2, 'runs':scored_runs, 'date': matchdate}


    details = []
    for r in result:
        team1_id = r[0]
        team2_id = r[1]
        winner = r[2]
        weather = r[3]
        mid = r[4]
        row = {'mid': mid, 'team1_id': team1_id, 'team2_id': team2_id, 'winner': winner,
               'weather': weather}
        details.append(row)

    return render(request, 'groundsingle/index.html', {'details': details, 'highestwicket': highestWicketTaker, 'highestRunMatch': highestScoredRunsMatch})
