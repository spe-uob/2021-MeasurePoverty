/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table dates
# ------------------------------------------------------------
CREATE DATABASE translate CHARACTER SET utf8 COLLATE utf8_general_ci;

USE translate;
DROP TABLE IF EXISTS `dates`;

CREATE TABLE `dates` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `dates` WRITE;
/*!40000 ALTER TABLE `dates` DISABLE KEYS */;

INSERT INTO `dates` (`id`, `value`, `created_at`, `updated_at`)
VALUES
	(1,'2019',NULL,NULL),
	(2,'2020',NULL,NULL),
	(3,'2021',NULL,NULL),
	(4,'2022',NULL,NULL);

/*!40000 ALTER TABLE `dates` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table languageReferences
# ------------------------------------------------------------

DROP TABLE IF EXISTS `languageReferences`;

CREATE TABLE `languageReferences` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sentenceId` varchar(255) DEFAULT NULL,
  `languageId` varchar(255) DEFAULT NULL,
  `languageContent` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `languageReferences` WRITE;
/*!40000 ALTER TABLE `languageReferences` DISABLE KEYS */;

INSERT INTO `languageReferences` (`id`, `sentenceId`, `languageId`, `languageContent`, `created_at`, `updated_at`)
VALUES
	(1,'1','1','apple',NULL,NULL),
	(2,'1','2','苹果',NULL,NULL),
	(3,'1','3','りんご ',NULL,NULL),
	(4,'2','1','banana',NULL,NULL),
	(5,'2','2','香蕉',NULL,NULL),
	(6,'2','3','バナナ',NULL,NULL);

/*!40000 ALTER TABLE `languageReferences` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table languages
# ------------------------------------------------------------

DROP TABLE IF EXISTS `languages`;

CREATE TABLE `languages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `languageName` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `languages` WRITE;
/*!40000 ALTER TABLE `languages` DISABLE KEYS */;

INSERT INTO `languages` (`id`, `languageName`, `created_at`, `updated_at`)
VALUES
	(1,'English',NULL,NULL),
	(2,'Chinese',NULL,NULL),
	(3,'Japanese',NULL,NULL),
	(4,'Italy',NULL,NULL);

/*!40000 ALTER TABLE `languages` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table sentences
# ------------------------------------------------------------

DROP TABLE IF EXISTS `sentences`;

CREATE TABLE `sentences` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pageNumber` int(11) DEFAULT NULL,
  `dateId` varchar(255) DEFAULT NULL,
  `originSentences` varchar(255) DEFAULT NULL,
  `english` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `sentences` WRITE;
/*!40000 ALTER TABLE `sentences` DISABLE KEYS */;

INSERT INTO `sentences` (`id`, `pageNumber`, `dateId`, `originSentences`, `english`, `created_at`, `updated_at`)
VALUES
	(1,5,'1','苹果','apple',NULL,NULL),
	(2,10,'1','香蕉','banana',NULL,NULL);

/*!40000 ALTER TABLE `sentences` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table SequelizeMeta
# ------------------------------------------------------------

DROP TABLE IF EXISTS `SequelizeMeta`;

CREATE TABLE `SequelizeMeta` (
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

LOCK TABLES `SequelizeMeta` WRITE;
/*!40000 ALTER TABLE `SequelizeMeta` DISABLE KEYS */;

INSERT INTO `SequelizeMeta` (`name`)
VALUES
	('20220411093039-init-sentences.js'),
	('20220411093456-init-languageReferences.js'),
	('20220411232903-init-dates.js'),
	('20220411233321-init-languages.js');

/*!40000 ALTER TABLE `SequelizeMeta` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
