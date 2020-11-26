from django.shortcuts import render
import cx_Oracle
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
connection = cx_Oracle.connect(user='cricinfo', password='cricinfo', dsn=dsn_tns)


# Create your views here.

def matchsingle(request):
    match_id = request.GET.get('id')
    id2=request.GET.get('name')
    print(match_id)
    print(id2)
#############################Teams
    cursor = connection.cursor()
    sql = "SELECT NAME, TEAM_ID FROM MATCH M JOIN TEAM T ON(M.TEAM1_ID=T.TEAM_ID OR M.TEAM2_ID=T.TEAM_ID) WHERE M.MATCH_ID='"+match_id+"'"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()

    teams = []
    c=0

    for r in result:
        team_x=r[0]
        team_id=r[1]
        c=c+1;
        t="team"+str(c)
        id = "teamID" + str(c)
        rowTeam={t:team_x, id:team_id}
        teams.append(rowTeam)

#############################Team1_bat
    team1_id = teams[0]['teamID1']
    print(team1_id)
    print(match_id)
    team2_id = teams[1]['teamID2']

    cursor = connection.cursor()
    sql = "SELECT * FROM PLAYER_SCORE WHERE MATCH_ID='"+match_id+"'  AND PLAYER_ID=ANY(SELECT PLAYER_ID FROM TEAM_PLAYER WHERE TEAM_ID='"+team1_id+"')"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()

    team1_bat = []
    for r in result:
        m_id = r[0]
        person_id=r[1]
        scored_run = r[2]
        balls_batted = r[3]


        fours = r[4]
        sixes = r[5]
        not_out = r[6]
        balls_bowled=r[7]
        given_runs=r[8]
        wickets=r[9]

        cursor = connection.cursor()
        sql = "SELECT * FROM PERSON WHERE PERSON_ID='" + person_id + "'"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        fullname=""
        for r in result:
            first_name=r[1]
            last_name=r[2]
            fullname=""+first_name+" "+last_name

        row = {'m_id': m_id, 'player_name': fullname, 'scored_run': scored_run, 'balls_batted': balls_batted,
               'fours': fours, 'sixes': sixes, 'not_out': not_out,
               'balls_bowled': balls_bowled, 'given_runs': given_runs, 'wickets': wickets}
        team1_bat.append(row)
###################team2_bat
    cursor = connection.cursor()
    sql = "SELECT * FROM PLAYER_SCORE WHERE MATCH_ID='"+match_id+"'  AND PLAYER_ID=ANY(SELECT PLAYER_ID FROM TEAM_PLAYER WHERE TEAM_ID='"+team2_id+"')"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()

    team2_bat = []
    for r in result:
        m_id = r[0]
        person_id=r[1]
        scored_run = r[2]
        balls_batted = r[3]
        fours = r[4]
        sixes = r[5]
        not_out = r[6]
        balls_bowled=r[7]
        given_runs=r[8]
        wickets=r[9]

        cursor = connection.cursor()
        sql = "SELECT * FROM PERSON WHERE PERSON_ID='" + person_id + "'"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        fullname=""
        for r in result:
            first_name=r[1]
            last_name=r[2]
            fullname=""+first_name+" "+last_name

        row = {'m_id': m_id, 'player_name': fullname, 'scored_run': scored_run, 'balls_batted': balls_batted,
               'fours': fours, 'sixes': sixes, 'not_out': not_out,
               'balls_bowled': balls_bowled, 'given_runs': given_runs, 'wickets': wickets}
        team2_bat.append(row)
###################team1_bowl
        cursor = connection.cursor()
        sql = "SELECT * FROM PLAYER_SCORE WHERE MATCH_ID='" + match_id + "' AND PLAYER_ID=ANY(SELECT PLAYER_ID FROM TEAM_PLAYER WHERE TEAM_ID='" + team1_id + "') AND NUM_OF_OVERS_BOWLED IS NOT NULL"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()

        team1_bowl = []
        for r in result:
            m_id = r[0]
            person_id = r[1]
            scored_run = r[2]
            balls_batted = r[3]
            fours = r[4]
            sixes = r[5]
            not_out = r[6]
            balls_bowled = r[7]
            given_runs = r[8]
            wickets = r[9]

            cursor = connection.cursor()
            sql = "SELECT * FROM PERSON WHERE PERSON_ID='" + person_id + "'"
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            fullname = ""
            for r in result:
                first_name = r[1]
                last_name = r[2]
                fullname = "" + first_name + " " + last_name

            row = {'m_id': m_id, 'player_name': fullname, 'scored_run': scored_run, 'balls_batted': balls_batted,
                   'fours': fours, 'sixes': sixes, 'not_out': not_out,
                   'balls_bowled': balls_bowled, 'given_runs': given_runs, 'wickets': wickets}
            team1_bowl.append(row)
###################team2_bowl
        cursor = connection.cursor()
        sql = "SELECT * FROM PLAYER_SCORE WHERE MATCH_ID='" + match_id + "' AND PLAYER_ID=ANY(SELECT PLAYER_ID FROM TEAM_PLAYER WHERE TEAM_ID='" + team2_id + "') AND NUM_OF_OVERS_BOWLED IS NOT NULL"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()

        team2_bowl = []
        for r in result:
            m_id = r[0]
            person_id = r[1]
            scored_run = r[2]
            balls_batted = r[3]
            fours = r[4]
            sixes = r[5]
            not_out = r[6]
            balls_bowled = r[7]
            given_runs = r[8]
            wickets = r[9]

            cursor = connection.cursor()
            sql = "SELECT * FROM PERSON WHERE PERSON_ID='" + person_id + "'"
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            fullname = ""
            for r in result:
                first_name = r[1]
                last_name = r[2]
                fullname = "" + first_name + " " + last_name

            row = {'m_id': m_id, 'player_name': fullname, 'scored_run': scored_run,
                   'balls_batted': balls_batted,
                   'fours': fours, 'sixes': sixes, 'not_out': not_out,
                   'balls_bowled': balls_bowled, 'given_runs': given_runs, 'wickets': wickets}
            team2_bowl.append(row)
###################Umpires
            cursor = connection.cursor()
            sql = "SELECT * FROM PERSON WHERE PERSON_ID=ANY(SELECT UMPIRE_ID FROM UMPIRE_MATCH WHERE MATCH_ID='"+match_id+"')"
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()

            umpire = []
            fullname = ""
            for r in result:
                first_name = r[1]
                last_name = r[2]
                fullname = "" + first_name + " " + last_name

                row = {'umpire_name': fullname}
                umpire.append(row)


    return render(request, 'matchsingle/index.html', {'team1_bat': team1_bat,'team2_bat': team2_bat,'team1_bowl': team1_bowl,'team2_bowl': team2_bowl,'teams':teams, 'umpire':umpire})
