var express = require('express');
var router = express.Router();
const models = require('../models');

const SensorData = models.SensorData;

router.post('/', async (req, res) => {
    let data = {
        ctemp: req.body.ctemp,
        fan: req.body.fan,
        heat: req.body.heat
    };
    data = await SensorData.create(data);
    res.send(data);
});

router.get('/{date}', (req, res) => {

});

module.exports = router;