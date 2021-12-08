1. In first step we have created a table (allowed_fields)in Model.py file.
2. Now in second step we created a function "def parse_search_phrase(allowed_fields, search_phrase)" as you want. And we are passing two arguments first one is 'allowed_fields' and second one is 'search_phrase'.
3. In above created function we have added functionality according to passed arguments (allowed_fields, search_phrase) to get data from Django model.
4. We have added "if" condition to match allowed_fields exists in database table or not. If fields don't exist then it returns error "Allowed Fields does not match".
5. We have changed search_phrase string according to cursor query and filter data accordingly.
6. we have another function " def index" which call the "parse_search_phrase(allowed_fields, search_phrase)" function to give results
