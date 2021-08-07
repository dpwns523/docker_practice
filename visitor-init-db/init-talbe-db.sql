-- Database : 'visitors'

-- Table structure for table 'visitors'

CREATE TABLE IF NOT EXISTS 'visitors' (
	'id' bigint NOT NULL AUTO_INCREMENT,
	'mail' varchar(45) DEFAULT NULL,
	'region' varchar(45) DEFAULT NULL,
	'temperature' float DEFAULT NULL,
	PRIMARY KEY('id')
	) ENGINE=InnoDB DEFAULT CHARSET=utf8 ;

-- Dumping data ( init )
INSERT INTO 'visitors'(
	'id','mail','region','temperature')
	values
	(1,'dpwns523@naver.com','인천',36.5);

