'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    const {
      INTEGER,
      DATE,
      STRING
    } = Sequelize;
    await queryInterface.createTable('languages', {
      id: {
        type: INTEGER,
        primaryKey: true,
        autoIncrement: true
      },//语言id
      languageName: STRING,//语言名称：例如 English,日语等等
      created_at: DATE,
      updated_at: DATE,
    }, {
      charset: 'utf8'
    });
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('languages');
  }
};