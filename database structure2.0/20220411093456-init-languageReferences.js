'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    const {
      INTEGER,
      DATE,
      STRING
    } = Sequelize;
    await queryInterface.createTable('languageReferences', {
      id: {
        type: INTEGER,
        primaryKey: true,
        autoIncrement: true
      },
      sentenceId: STRING,
      languageId: STRING，
      languageContent: STRING,
      created_at: DATE,
      updated_at: DATE,
    }, {
      charset: 'utf8'
    });
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('languageReferences');
  }
};