const { Model, DataTypes } = require('sequelize');


class SensorData extends Model {}
class UserProfile extends Model {}

exports.SensorData = SensorData;
exports.UserProfile = UserProfile;

exports.init = (sequelize) => {

    UserProfile.init({
        desiredTemp: DataTypes.FLOAT,
        location: DataTypes.STRING
    }, {sequelize, modelName: 'user_profile'});

    SensorData.init({
        ctemp: DataTypes.FLOAT,
        fan: DataTypes.FLOAT,
        heat: DataTypes.FLOAT
    }, {sequelize, modelName: 'sensor_data'});

}