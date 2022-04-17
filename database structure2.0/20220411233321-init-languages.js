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
      },//language id
      languageName: STRING,//(such as franch)
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