module.exports.server = 'http://localhost:8000';
module.exports.routes = {
    weather: {
        get: '/weather/'
    },
    sensor: {
        get: '/sensors/'
    }, 
    profile: {
        post: '/profiles/',
        get: '/profiles/'
    }
};

