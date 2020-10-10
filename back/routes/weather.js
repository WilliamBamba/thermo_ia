var express = require('express');
var router = express.Router();
const configs = require('../configs');
const fetch = require('node-fetch');

// http://api.weatherapi.com/v1/forecast.json?key=e14c95d7a1d6456e8f4125239201010&q=lyon&days=1
// define the home page route
router.get('/:city/:days/', async (req, res) => {

  const url = `${configs.weatherApi}?key=${configs.apiKey}&q=${req.params.city}&days=${req.params.days}`;
  let status = 200;
  const weatherForcast = await fetch(url).then(r => {
    status = r.status;
    return r.json();
  });

  res.status(status).send(weatherForcast);
});

module.exports = router;