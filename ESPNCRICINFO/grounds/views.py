from django.shortcuts import render
import random
from django.db import connection


# Create your views here.


def grounds(request):
    cursor = connection.cursor()
    sql = "SELECT * FROM GROUND"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    dict_result = []

    for r in result:
        id = r[0]
        name = r[1]
        city = r[2]
        st_no = r[3]
        zip_code = r[4]
        image_link = r[5]
        row = {'id': id, 'name': name, 'city': city, 'street_no': st_no, 'zip_code': zip_code, 'image_link': image_link}
        dict_result.append(row)

    return render(request, 'grounds/index.html', {'results': dict_result})