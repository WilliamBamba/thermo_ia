const express = require('express');
const app = express();

const bodyParser = require('body-parser');
const port = 8080;

require('./migrate');

const models = require('./models');
const SensorData = models.SensorData;

app.use(bodyParser.json());

const weather = require('./routes/weather');
const sensors = require('./routes/sensors');

app.use('/weather', weather);
app.use('/sensors', sensors);


app.listen(port, () => {
    console.log(`connected to ${port}`);
});