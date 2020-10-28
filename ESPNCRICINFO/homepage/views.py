from django.shortcuts import render
import random
from django.db import connection


# Create your views here.
def home(request):
    cursor = connection.cursor()
    sql = "SELECT * FROM PERSON"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    dict_result = []

    for r in result:
        job_id = r[0]
        job_title = r[1]
        min_salary = r[2]
        max_salary = r[3]
        row = {'job_id': job_id, 'job_title': job_title, 'min_salary': min_salary, 'max_salary': max_salary}
        dict_result.append(row)

    return render(request, 'index.html', {'jobs': dict_result})


def series_details(request):
    return render(request, 'speaker-details.html')

