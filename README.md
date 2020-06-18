### Contains the Restful API's for Beats Allocation, and also to handle the admin page of the app
Django Rest Framework is used for the same.

The API can be viewed on : http://aman28.pythonanywhere.com/

### API endpoints :
- `'/'` , Defualt page, contains the landing page
- `'/police'` , fetches the list of all policemen
- `'/zone'`, fetches the list of all zones
- `'/allocation'`, fetches the allocation details like zone, police assigned to that zone and the time slot

#### Note that, to fetch the details of the exact policeman / zone / allocation :
The ID can be spcified after the url like :
`/police/1`
`/zone/4`
`/allocation/2`

