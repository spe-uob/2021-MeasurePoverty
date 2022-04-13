'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    const {
      INTEGER,
      DATE,
      STRING
    } = Sequelize;
    await queryInterface.createTable('dates', {
      id: {
        type: INTEGER,
        primaryKey: true,
        autoIncrement: true
      },//dateid
      value: STRING,//（such as2009,2010）
      created_at: DATE,
      updated_at: DATE,
    }, {
      charset: 'utf8'
    });
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('dates');
  }
};