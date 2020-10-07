const express = require('express');
const app = express();

const bodyParser = require('body-parser');
const port = 8080;

require('./migrate');

const models = require('./models');
const SensorData = models.SensorData;

app.use(bodyParser.json());


app.post('/sensors', async (req, res) => {
    let data = {
        ctemp: req.body.ctemp,
        fan: req.body.fan,
        heat: req.body.heat
    };
    data = await SensorData.create(data);
    res.send(data);
});

app.get('/sensors/{date}', (req, res) => {

});

app.listen(port, () => {
    console.log(`connected to ${port}`);
});