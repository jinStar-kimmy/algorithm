-- MariaDB dump 10.18  Distrib 10.5.8-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: awsdjangodb
-- ------------------------------------------------------
-- Server version	10.5.8-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add board categories',7,'add_boardcategories'),(26,'Can change board categories',7,'change_boardcategories'),(27,'Can delete board categories',7,'delete_boardcategories'),(28,'Can view board categories',7,'view_boardcategories'),(29,'Can add boards',8,'add_boards'),(30,'Can change boards',8,'change_boards'),(31,'Can delete boards',8,'delete_boards'),(32,'Can view boards',8,'view_boards'),(33,'Can add board replies',9,'add_boardreplies'),(34,'Can change board replies',9,'change_boardreplies'),(35,'Can delete board replies',9,'delete_boardreplies'),(36,'Can view board replies',9,'view_boardreplies'),(37,'Can add board likes',10,'add_boardlikes'),(38,'Can change board likes',10,'change_boardlikes'),(39,'Can delete board likes',10,'delete_boardlikes'),(40,'Can view board likes',10,'view_boardlikes');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `username` varchar(150) NOT NULL,
  `is_superuser` int(11) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `date_of_birth` datetime(6) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_staff` int(11) DEFAULT NULL,
  `is_active` int(11) DEFAULT NULL,
  `first_name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$260000$JnF9ErWrKrplMUgTGbWWQu$akPPbw2pJNJ4VUHN+vFUEMNhjTTMnYP71YHqAywerpc=','gen2',1,'chanwong','010','123','2019-12-31 15:00:00.000000','2021-06-28 13:59:15.092919','2021-06-28 17:01:16.026668',1,1,NULL),(2,'pbkdf2_sha256$216000$tU1Mebg2gJwE$Lk3Exd5f/idNFtXlCA5WMxTkEr0HC2aajQ/LJO0V5YI=','gen3',1,'서찬웅','010-9021-2357','genlux@gmail.com','1982-10-03 15:00:00.000000','2021-08-05 08:34:00.279380','2021-08-05 16:27:25.817698',0,1,NULL);
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `board_categories`
--

DROP TABLE IF EXISTS `board_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `board_categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_type` varchar(45) NOT NULL,
  `category_code` varchar(100) NOT NULL,
  `category_name` varchar(100) NOT NULL,
  `category_desc` varchar(100) NOT NULL,
  `list_count` int(11) DEFAULT NULL,
  `authority` int(11) DEFAULT NULL,
  `creation_date` datetime(6) NOT NULL,
  `last_update_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `board_categories`
--

LOCK TABLES `board_categories` WRITE;
/*!40000 ALTER TABLE `board_categories` DISABLE KEYS */;
INSERT INTO `board_categories` VALUES (2,'free','free','자유게시판','주식',10,1,'2021-06-28 14:01:13.000000','2021-06-28 14:01:13.000000'),(3,'notice','notice','notice','notice',10,1,'2021-06-28 14:02:43.000000','2021-06-28 14:02:43.000000'),(4,'comm','comm','comm','comm',10,1,'2021-06-28 14:49:16.000000','2021-06-28 14:49:16.000000');
/*!40000 ALTER TABLE `board_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `board_likes`
--

DROP TABLE IF EXISTS `board_likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `board_likes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `registered_date` datetime(6) NOT NULL,
  `article_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `board_likes_article_id_1caddaf3_fk_boards_id` (`article_id`),
  KEY `board_likes_user_id_bc0af575_fk_auth_user_id` (`user_id`),
  CONSTRAINT `board_likes_article_id_1caddaf3_fk_boards_id` FOREIGN KEY (`article_id`) REFERENCES `boards` (`id`),
  CONSTRAINT `board_likes_user_id_bc0af575_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `board_likes`
--

LOCK TABLES `board_likes` WRITE;
/*!40000 ALTER TABLE `board_likes` DISABLE KEYS */;
INSERT INTO `board_likes` VALUES (1,'2021-08-05 15:52:33.217964',4,2);
/*!40000 ALTER TABLE `board_likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `board_replies`
--

DROP TABLE IF EXISTS `board_replies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `board_replies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `level` int(11) DEFAULT NULL,
  `content` longtext NOT NULL,
  `registered_date` datetime(6) NOT NULL,
  `last_update_date` datetime(6) NOT NULL,
  `reference_reply_id` int(11) DEFAULT NULL,
  `article_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `board_replies_article_id_47a09eca_fk_boards_id` (`article_id`),
  KEY `board_replies_user_id_c1c4028a_fk_auth_user_id` (`user_id`),
  CONSTRAINT `board_replies_article_id_47a09eca_fk_boards_id` FOREIGN KEY (`article_id`) REFERENCES `boards` (`id`),
  CONSTRAINT `board_replies_user_id_c1c4028a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `board_replies`
--

LOCK TABLES `board_replies` WRITE;
/*!40000 ALTER TABLE `board_replies` DISABLE KEYS */;
/*!40000 ALTER TABLE `board_replies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boards`
--

DROP TABLE IF EXISTS `boards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `boards` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(300) NOT NULL,
  `content` longtext NOT NULL,
  `registered_date` datetime(6) NOT NULL,
  `last_update_date` datetime(6) NOT NULL,
  `view_count` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `category_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `boards_category_id_ec6bb4bf_fk_board_categories_id` (`category_id`),
  KEY `boards_user_id_67033f9a_fk_auth_user_id` (`user_id`),
  CONSTRAINT `boards_category_id_ec6bb4bf_fk_board_categories_id` FOREIGN KEY (`category_id`) REFERENCES `board_categories` (`id`),
  CONSTRAINT `boards_user_id_67033f9a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boards`
--

LOCK TABLES `boards` WRITE;
/*!40000 ALTER TABLE `boards` DISABLE KEYS */;
INSERT INTO `boards` VALUES (4,'안녕하세요','테스트입니다. ','2021-06-28 14:52:19.357889','2021-06-28 14:52:19.357889',13,'',2,1),(5,'adf','<h1> 하이 </h1>\r\n','2021-06-28 16:42:34.842682','2021-06-28 16:43:29.176254',5,'images/2021/06/29/KakaoTalk_20210429_105427775.jpg',2,1);
/*!40000 ALTER TABLE `boards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-06-28 14:00:33.860778','1','자유게시판 (1)',1,'[{\"added\": {}}]',7,1),(2,'2021-06-28 14:01:11.002561','1','자유게시판 (1)',3,'',7,1),(3,'2021-06-28 14:01:31.922262','2','free (free)',1,'[{\"added\": {}}]',7,1),(4,'2021-06-28 14:02:48.598722','3','notice (notice)',1,'[{\"added\": {}}]',7,1),(5,'2021-06-28 14:03:26.392469','1','[1] test',1,'[{\"added\": {}}]',8,1),(6,'2021-06-28 14:20:02.194909','2','[2] 안녕하세요',1,'[{\"added\": {}}]',8,1),(7,'2021-06-28 14:38:03.342525','3','[3] asfdasdf',1,'[{\"added\": {}}]',8,1),(8,'2021-06-28 14:45:31.592479','2','free (free)',2,'[{\"changed\": {\"fields\": [\"List count\"]}}]',7,1),(9,'2021-06-28 14:48:39.869836','3','[3] asfdasdf',3,'',8,1),(10,'2021-06-28 14:48:39.869836','2','[2] 안녕하세요',3,'',8,1),(11,'2021-06-28 14:48:39.869836','1','[1] test',3,'',8,1),(12,'2021-06-28 14:49:06.363336','3','notice (notice)',2,'[{\"changed\": {\"fields\": [\"List count\"]}}]',7,1),(13,'2021-06-28 14:49:24.642029','4','comm (comm)',1,'[{\"added\": {}}]',7,1),(14,'2021-06-28 14:50:03.740076','2','자유게시판 (free)',2,'[{\"changed\": {\"fields\": [\"Category name\"]}}]',7,1),(15,'2021-06-28 14:51:09.310159','2','자유게시판 (free)',2,'[{\"changed\": {\"fields\": [\"Authority\"]}}]',7,1),(16,'2021-06-28 14:53:48.880703','3','notice (notice)',2,'[{\"changed\": {\"fields\": [\"List count\", \"Authority\"]}}]',7,1),(17,'2021-06-28 14:53:59.957072','2','자유게시판 (free)',2,'[{\"changed\": {\"fields\": [\"Authority\"]}}]',7,1),(18,'2021-06-28 14:54:50.884185','4','comm (comm)',2,'[{\"changed\": {\"fields\": [\"Authority\"]}}]',7,1),(19,'2021-06-28 14:54:53.944135','3','notice (notice)',2,'[]',7,1),(20,'2021-06-28 14:54:57.013592','2','자유게시판 (free)',2,'[{\"changed\": {\"fields\": [\"Authority\"]}}]',7,1),(21,'2021-06-28 16:47:22.087449','2','자유게시판 (free)',2,'[{\"changed\": {\"fields\": [\"Category desc\"]}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(7,'boardapp','boardcategories'),(10,'boardapp','boardlikes'),(9,'boardapp','boardreplies'),(8,'boardapp','boards'),(6,'boardapp','user'),(4,'contenttypes','contenttype'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-06-28 13:14:51.295601'),(2,'boardapp','0001_initial','2021-06-28 13:14:51.483051'),(3,'admin','0001_initial','2021-06-28 13:14:51.529900'),(4,'admin','0002_logentry_remove_auto_add','2021-06-28 13:14:51.545812'),(5,'admin','0003_logentry_add_action_flag_choices','2021-06-28 13:14:51.545812'),(6,'contenttypes','0002_remove_content_type_name','2021-06-28 13:14:51.592903'),(7,'auth','0001_initial','2021-06-28 13:14:51.764353'),(8,'auth','0002_alter_permission_name_max_length','2021-06-28 13:14:51.780004'),(9,'auth','0003_alter_user_email_max_length','2021-06-28 13:14:51.780004'),(10,'auth','0004_alter_user_username_opts','2021-06-28 13:14:51.795880'),(11,'auth','0005_alter_user_last_login_null','2021-06-28 13:14:51.795880'),(12,'auth','0006_require_contenttypes_0002','2021-06-28 13:14:51.795880'),(13,'auth','0007_alter_validators_add_error_messages','2021-06-28 13:14:51.795880'),(14,'auth','0008_alter_user_username_max_length','2021-06-28 13:14:51.795880'),(15,'auth','0009_alter_user_last_name_max_length','2021-06-28 13:14:51.811146'),(16,'sessions','0001_initial','2021-06-28 13:14:51.842395');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-10 22:54:41
