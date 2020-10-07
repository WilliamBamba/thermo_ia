const { Model, DataTypes } = require('sequelize');


class User extends Model {}
class SensorData extends Model {}

exports.SensorData = SensorData;

exports.init = (sequelize) => {

    SensorData.init({
        ctemp: DataTypes.FLOAT,
        fan: DataTypes.FLOAT,
        heat: DataTypes.FLOAT
    }, {sequelize, modelName: 'sensor_data'});

}