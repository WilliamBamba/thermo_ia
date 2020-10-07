const sequelize = require('./db');
const models = require('./models');
models.init(sequelize);

let syncDb = async () => {
    await sequelize.sync();
    console.log('db migrated successfully');
};

syncDb();