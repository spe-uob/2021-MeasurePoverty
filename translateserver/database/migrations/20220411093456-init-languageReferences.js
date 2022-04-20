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
      sentenceId: STRING,//所属句子id
      languageId: STRING,//语言id
      languageContent: STRING,//翻译内容
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