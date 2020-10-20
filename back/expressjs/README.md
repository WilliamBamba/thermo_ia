### Get started :
- install nodejs, yarn
- `yarn install` to install dependencies
- `node index.js` to start the server

### Database migration
To run database migration run the following command `node migratge.js`. When the migrations has been run the tables should have been created on the database. for our small application we don't need more sufisticated system. So, every migration erase the database beforehand for avoiding any unwanted behaviour.

### Routes
The `index.js` is the main entry point of the app. And, others routes are separated in `routes` folder and included in the index file.
Here is breaf description of the routes.

- weather routes
    GET: `/weather/:city/:days/` `=>` `200`
    for example `/weather/lyon/1` will give <a href='http://api.weatherapi.com/v1/forecast.json?key=e14c95d7a1d6456e8f4125239201010&q=lyon&days=1'>this result</a>. for more details checkout weatherapi.com.
    <br>

- sensors routes
    POST: `/sensors/` `=>` `201`
    will create a sensor data. the required parameters are `ctemp: FLOAT`, `fan: FLOAT`, `heat: FLOAT`. be carefull the are no data validation at this stage.
    <br>

    GET: `/sensors/:day-:month/` `=>` `200`
    will give a list of sensor data for the given date.
    <br>

- profile routes
    GET: `/profile/` `=>` `200`