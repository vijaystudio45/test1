from django.http import HttpResponse, JsonResponse
from .models import dbFileds
import re
from django.db import connection

def index(request):
    allowed_fields = ['distance', 'run_date']
    #search_phrase = "(run_date eq 2021-12-08) AND ((distance gt 0) OR (distance lt 10))"
    search_phrase = "(distance lt 10)"
    search_filter = parse_search_phrase(allowed_fields, search_phrase)
    return search_filter


def parse_search_phrase(allowed_fields, search_phrase):
    dbFields = dbFileds._meta.get_fields()
    dbFieldsList = []
    for field in dbFields:
        dbFieldsList.append(field.name)

    matchedFields = all(item in dbFieldsList for item in allowed_fields)
    if matchedFields is True:
        string = re.sub("[()]", "", search_phrase)
        string = string.replace("eq", "=", )
        string = string.replace("gt", ">")
        string = string.replace("lt", "<")
        cursor = connection.cursor()
        cursorQuery = "SELECT * from allowed_fields where " + string + ""
        cursor.execute(cursorQuery)
        records = cursor.fetchall()
        insertObject = []
        columnNames = [column[0] for column in cursor.description]
        for record in records:
            insertObject.append(dict(zip(columnNames, record)))
        if len(insertObject) != 0:
            data = {
                'status': 'success',
                'data' : insertObject
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'status': 'Fail', 'message': 'Data not found.'})
    else:
        return JsonResponse("No, allowed fields does not matched")

# Create your views here.
