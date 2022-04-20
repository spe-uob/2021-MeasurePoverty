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
      pageNumber: INTEGER,//页码
      dateId: STRING,//日期id
      originSentences: STRING,//原始句子
      english: STRING,//英文翻译
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