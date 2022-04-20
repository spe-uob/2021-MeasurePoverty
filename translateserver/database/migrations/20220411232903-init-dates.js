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
      },//日期id
      value: STRING,//时间字符串 例如 2019 2020
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