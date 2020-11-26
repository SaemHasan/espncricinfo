from django.shortcuts import render, redirect
import cx_Oracle, json

dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
connection = cx_Oracle.connect(user='cricinfo', password='cricinfo', dsn=dsn_tns)
# Create your views here.

players_fullname = []


def umpiresall(request):
    if request.method == "GET":
        players_fullname.clear()
        cursor = connection.cursor()
        sql = "SELECT * FROM PERSON P JOIN UMPIRE U ON(P.PERSON_ID=U.UMPIRE_ID)"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        dict_result = []
        first_name_list = []
        last_name_list = []
        for r in result:
            id = r[0]
            first_name = r[1]
            last_name = r[2]
            full_name = first_name + " " + last_name
            players_fullname.append(full_name)
            first_name_list.append(first_name)
            last_name_list.append(last_name)
            nationality = r[3]
            dob = r[4]
            image_link = r[5]
            if image_link is None:
                image_link = "default.jpg"
            row = {'id': id, 'first_name': first_name, 'last_name': last_name, 'full_name': full_name,
                   'nationality': nationality, 'date_of_birth': dob, 'image_link': image_link}
            dict_result.append(row)

        json_names = json.dumps(players_fullname)
        json_fname = json.dumps(first_name_list)
        json_lname = json.dumps(last_name_list)
        return render(request, 'umpiresall/index.html',
                      {'persons': dict_result, 'names': json_names, 'fname': json_fname, 'lname': json_lname})

    else:
        name = request.POST['search2']
        # print(players_fullname)
        if str(name) in players_fullname:
            part = name.split(" ")
            first_name = part[0]
            last_name = part[1]
            cursor = connection.cursor()
            sql = "SELECT * FROM PERSON P JOIN UMPIRE U ON(P.PERSON_ID=U.UMPIRE_ID) WHERE FIRST_NAME='" + first_name + "' AND LAST_NAME='" + last_name + "'"
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

            return render(request, 'umpiresingle/index.html', {'name': name, 'details': dict_result[0]})
        else:
            return redirect('umpiresall')