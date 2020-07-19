### Contains the Restful API's for Beats Allocation, and also to handle the admin page of the app
Django Rest Framework is used for the same.

The API can be viewed on : http://aman28.pythonanywhere.com/

### API endpoints :
GET
- `'/'` , Default page, contains the landing page
- `'/policecount'` , fetches the number of total, alloted and unalloted police
- `'/zonecount'`, fetches the number of total, alloted and unalloted zones
- `'/allocation'`, fetches the allocation details like zone, police assigned to that zone and the time slot<br>

POST
`'/allocation'`
```
{
        "zone": "Chandni Chowk",
        "priority": "2",
        "police_allotted": "'Aman', 'Ishank', 'Ramu', 'Rahul'",
        "time_slot": "6-7 pm"
}
```
RESPONSE
```
{
    "id": 8,
    "zone": "Chandni Chowk",
    "priority": "2",
    "police_allotted": "'Aman', 'Ishank', 'Ramu', 'Rahul'",
    "date_posted": "2020-06-18T19:23:36.122904Z",
    "time_slot": "6-7 pm"
}
```
#### Note that, to fetch the details of the exact policeman / zone / allocation :
The ID can be spcified after the url like :
`'/allocation/2'`


