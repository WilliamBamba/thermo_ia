const express = require('express');
const app = express();

const bodyParser = require('body-parser');
const { Sequelize } = require('sequelize');
const sequelize = new Sequelize('sqlite::memory:');
const port = 8080;

const models = require('./models');
models.init(sequelize);

const SensorData = models.SensorData;

app.use(bodyParser.json());


let test = async () => {
    await sequelize.sync();
};

test();

app.post('/save/sensor/data', async (req, res) => {
    let data = {
        ctemp: req.body.ctemp,
        fan: req.body.fan,
        heat: req.body.heat
    };
    data = await SensorData.create(data);
    res.send(data);
});

app.get('/fetch/data/', (req, res) => {

});

app.listen(port, () => {
    console.log(`connected to ${port}`);
});