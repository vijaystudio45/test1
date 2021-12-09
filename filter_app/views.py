from django.http import HttpResponse, JsonResponse
from .models import dbFileds
import re
from django.db import connection

def cursor_data(request):
    allowed_fields = ['distance', 'run_date']
    search_phrase = "(run_date eq '2021-12-08') AND ((distance gt 0) OR (distance lt 10))"
    search_filter = search_phrase_method(allowed_fields, search_phrase)
    Queryset = "SELECT * from allowed_fields where " + search_filter + ""
    cursor = connection.cursor()
    cursor.execute(Queryset)
    records = cursor.fetchall()
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in records:
        insertObject.append(dict(zip(columnNames, record)))

    if len(insertObject) != 0:
        data = {
            'status': 'success',
            'data': insertObject
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'status': 'Fail', 'message': "Data not found"})


def raw_data(request):
    allowed_fields = ['distance', 'run_date']
    search_phrase = "(run_date eq '2021-12-08') AND ((distance gt 0) OR (distance lt 10))"
    search_filter = search_phrase_method(allowed_fields, search_phrase)
    Queryset = "SELECT * from allowed_fields where " + search_filter + ""
    data = dbFileds.objects.raw(Queryset)
    columns = tuple(data.columns)
    dataFinal = []
    for row in data:
        finalData = tuple(getattr(row, col) for col in columns)
        mapped = list(zip(columns, finalData))
        dataFinal.append(dict(mapped))
    if len(dataFinal) != 0:
        data = {
            'status': 'success',
            'data': dataFinal
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'status': 'Fail', 'message': "Data not found"})


def search_phrase_method(allowed_fields, search_phrase):
    dbFields = dbFileds._meta.get_fields()
    dbFieldsList = []
    for field in dbFields:
        dbFieldsList.append(field.name)
        
    matchedFields = all(item in dbFieldsList for item in allowed_fields)
    if matchedFields is True:
        string = search_phrase
        string = string.replace("eq", "=", )
        string = string.replace("gt", ">")
        string = string.replace("lt", "<")
        string = string.replace("ne", "!=")
        string = string.replace("lte", "<=")
        string = string.replace("gte", ">=")
        return string
    else:
        return JsonResponse({'status': 'Fail', 'message': "Fields not matched"})

# Create your views here.
