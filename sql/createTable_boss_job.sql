/*
Navicat MySQL Data Transfer

Source Server         : Local
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : python_conn

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2018-04-27 01:02:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for boss_job
-- ----------------------------
DROP TABLE IF EXISTS `boss_job`;
CREATE TABLE `boss_job` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_name` varchar(255) DEFAULT NULL,
  `job_pay` varchar(255) DEFAULT NULL,
  `job_age` varchar(255) DEFAULT NULL,
  `job_area` varchar(255) DEFAULT NULL,
  `education` varchar(255) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `company_url` varchar(255) DEFAULT NULL,
  `company_description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=301 DEFAULT CHARSET=utf8;
