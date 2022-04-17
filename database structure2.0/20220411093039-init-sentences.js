'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    const {
      INTEGER,
      DATE,
      STRING
    } = Sequelize;
    await queryInterface.createTable('sentences', {
      id: {
        type: INTEGER,
        primaryKey: true,
        autoIncrement: true
      },//sentence Id
      pageNumber: INTEGER,
      dateId: STRING,
      originSentences: STRING,
      english: STRING,
      created_at: DATE,
      updated_at: DATE,
    }, {
      charset: 'utf8'
    });
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('sentences');
  }
};