const express = require('express');
const app = express();

const bodyParser = require('body-parser');
const port = 8080;

require('./migrate');


app.use(bodyParser.json());

const weather = require('./routes/weather');
const sensors = require('./routes/sensors');

app.use('/weather', weather);
app.use('/sensors', sensors);


app.listen(port, () => {
    console.log(`connected to ${port}`);
});