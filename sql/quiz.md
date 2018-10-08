# SQL Test

*the question got from [what-the-sql](http://wts.jmoiron.net)*

## data prepare
```sql
-- MySQL dump 10.16  Distrib 10.1.35-MariaDB, for Linux (x86_64)
--
-- Host: 172.16.154.26    Database: test_1024_sign
-- ------------------------------------------------------
-- Server version	5.5.25a-r5436-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `departments` (
  `departmentid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL DEFAULT '',
  PRIMARY KEY (`departmentid`),
  UNIQUE KEY `departments_id_uindex` (`departmentid`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` (`departmentid`, `name`) VALUES (1,'Interdum Enim Non Foundation'),(2,'Pede Nunc Ltd'),(3,'Et Libero Foundation'),(4,'Nascetur Ridiculus Mus Associate'),(5,'Nam Industries'),(6,'Feugiat Non Inc.'),(7,'Eget Mollis Lectus Limited'),(8,'Duis Incorporated'),(9,'Eu Placerat Institute'),(10,'Sociis Natoque Limited'),(11,'Nonummy PC'),(12,'Mattis Semper Dui Foundation'),(13,'Pharetra Sed PC'),(14,'Curae; Incorporated');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employees` (
  `employeeid` int(11) NOT NULL AUTO_INCREMENT,
  `departmentid` int(11) NOT NULL DEFAULT '0',
  `bossid` int(11) NOT NULL DEFAULT '0',
  `name` varchar(16) NOT NULL DEFAULT '',
  `salary` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`employeeid`),
  UNIQUE KEY `employees_id_uindex` (`employeeid`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` (`employeeid`, `departmentid`, `bossid`, `name`, `salary`) VALUES (1,8,0,'Jade Buchanan',253789),(2,9,1,'Gretchen Benton',232873),(3,4,1,'Desiree Reid',190374),(4,2,2,'Deborah Mills',203148),(5,4,4,'Claudia House',293193),(6,7,5,'Mechelle Kramer',164555),(7,8,2,'Barrett Pruitt',248567),(8,4,1,'Kyra Harrell',88734),(9,4,2,'Shad Chapman',284941),(10,3,5,'Dahlia Wiggins',217431),(11,5,7,'Oliver Pena',88653),(12,10,4,'Gavin Cardenas',227669),(13,6,3,'Leo Chen',273135),(14,3,1,'Montana Clayton',227003),(15,8,2,'Uma Daugherty',176748),(16,5,13,'Lunea Cole',147576),(17,5,11,'Germane Bartlett',186167),(18,6,2,'Adrian Cleveland',211932),(19,8,13,'Tasha Reyes',213184),(20,3,15,'Teagan Alston',159882),(21,5,15,'Channing York',151167),(22,9,14,'Cecilia Preston',296823),(23,1,13,'Wyatt Richmond',151951),(24,6,1,'Willa Hayes',72705),(25,4,22,'Ishmael Pace',256135),(26,5,5,'Stuart White',133126),(27,8,1,'Odette Underwood',102573),(28,7,4,'Ursa Ruiz',179185),(29,2,28,'Reuben Snider',227786),(30,10,2,'Levi Mcleod',235048),(31,6,4,'Hall Morrow',118401),(32,4,20,'Amethyst Cervant',273802),(33,5,31,'Shelly Le',126729),(34,8,17,'John Carrillo',221224),(35,3,29,'Aquila Lane',239008),(36,10,4,'Ferdinand Webb',175668),(37,2,4,'Roanna Benton',232190),(38,5,36,'Mia Cash',128522),(39,1,15,'Rhonda Bowman',254525),(40,9,14,'Dawn Alston',291871),(41,2,34,'Kennan Flowers',65410),(42,1,10,'Isadora Gilliam',78907),(43,6,21,'Sigourney Black',259164),(44,2,13,'Alexa Mccormick',55258),(45,9,11,'Marvin Hansen',255638),(46,4,17,'Kennedy Contrera',220784),(47,4,9,'Edan Preston',71886),(48,6,30,'Petra Levy',249277),(49,3,16,'Samson Jenkins',280726),(50,3,39,'Rose Macdonald',197879),(51,7,43,'Magee Espinoza',141836),(52,7,25,'Sierra Carpenter',281803),(53,6,43,'Keely Peterson',275559),(54,1,22,'Ulric Colon',58198),(55,3,40,'Vaughan Mckay',155698),(56,7,54,'Bruce Guzman',285929),(57,10,14,'Shana Finch',252513),(58,7,20,'Selma Alvarez',229558),(59,5,7,'Edward Collins',261885),(60,2,39,'Gail Mckinney',231011),(61,9,57,'Fletcher Jensen',217784),(62,3,28,'Melyssa Glenn',85336),(63,6,18,'Wade Cline',213351),(64,1,3,'Kitra Dotson',140959),(65,5,5,'Kelsey Everett',124117),(66,4,55,'Elijah Head',187126),(67,6,48,'Lester Wells',281162),(68,10,54,'Kylan Guerra',235590),(69,9,9,'Seth Pope',242200),(70,6,8,'August Maxwell',98902),(71,1,7,'Phillip Hansen',84435),(72,4,51,'Malachi Campbell',216728),(73,2,40,'Howard Roberts',183538),(74,8,21,'Charde Hanson',128179),(75,8,53,'Garth Young',270469),(76,10,59,'Griffin Kirkland',102531),(77,3,55,'Daniel Valdez',129869),(78,4,26,'Joan Schroeder',134816),(79,3,43,'Cleo Holland',290718),(80,9,1,'Lana Eaton',165740),(81,10,56,'Amaya Lynn',194349),(82,3,2,'Vernon Whitehead',77064),(83,3,17,'Wylie Paul',139793),(84,4,46,'Colorado Whitley',278346),(85,5,65,'Susan Dunlap',80447),(86,4,53,'Ava Britt',75522),(87,3,13,'Kelsie Carver',209091),(88,2,10,'Hunter Cameron',251679),(89,5,61,'Myles Rivers',85918),(90,7,81,'Palmer Oneil',240424),(91,8,5,'Henry Blanchard',165394),(92,7,9,'Amela Martinez',262512),(93,10,28,'Rylee Shaw',62180),(94,10,20,'Violet Sykes',104213),(95,5,56,'Amela Galloway',146457),(96,5,88,'James Nolan',129572),(97,2,75,'Ivory Mckenzie',260720),(98,2,87,'Eliana Nichols',125917),(99,7,32,'Patricia Vargas',253456),(100,8,71,'Jocelyn Guy',191937);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-08  8:41:11
```

## Q&A:
1. List the top 10 employee names by salary. <br/>
```select name from employees order by salary desc limit 10```
2. List employee names who have a bigger salary than their boss.<br/>
```select a.name from employees a left join employees b on a.bossid=b.employeeid where a.salary>b.salary```
3. List employee names who have the biggest salary in their departments.<br/>
```select a.name from employees a where not exists (select 1 from employees b where a.departmentid=b.departmentid and a.salary<b.salary)```
4. List department names that have less than 10 people in it.<br/>
```select name from departments where departmentid not in (select departmentid from employees group by departmentid having count(*) >=10)```
5. List employees who have a boss in a different department from them.<br/>
```select a.name from employees a left join employees b on a.bossid=b.employeeid where a.departmentid!=b.departmentid```
6. List all department names along with the total salary there.<br/>
```select d.name, IFNULL(e.salary,0) from departments d left join (select departmentid, sum(salary) as salary from employees group by departmentid) as e on e.departmentid=d.departmentid```

## Reference
1. [数据库分组查询最大值的问题](https://segmentfault.com/a/1190000004157112)
2. [The Rows Holding the Group-wise Maximum of a Certain Column](https://dev.mysql.com/doc/refman/5.7/en/example-maximum-column-group-row.html)