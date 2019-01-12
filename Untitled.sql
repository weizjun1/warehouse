CREATE TABLE `student1` (
`id` int NOT NULL AUTO_INCREMENT,
`name` char(20) NOT NULL,
`age` int(3) NOT NULL,
`sex` char(2) NOT NULL,
`address` varchar(30) CHARACTER SET utf8 NOT NULL,
`classId` int NOT NULL,
PRIMARY KEY (`id`) 
)
DEFAULT CHARACTER SET = utf8;
CREATE TABLE `class1` (
`id` int NOT NULL AUTO_INCREMENT,
`name` char(20) CHARACTER SET utf8 NOT NULL,
PRIMARY KEY (`id`) 
)
DEFAULT CHARACTER SET = utf8;
CREATE TABLE `teacher1` (
`id` int NOT NULL AUTO_INCREMENT,
`name` char(20) CHARACTER SET ujis NOT NULL,
`age` int(3) NOT NULL,
`courseId` int NOT NULL,
PRIMARY KEY (`id`) 
)
DEFAULT CHARACTER SET = utf8;
CREATE TABLE `course1` (
`id` int NOT NULL AUTO_INCREMENT,
`name` char(0) CHARACTER SET utf8 NOT NULL,
`teacherId` int NOT NULL,
PRIMARY KEY (`id`) 
)
DEFAULT CHARACTER SET = utf8;
CREATE TABLE `grade` (
`id` int NOT NULL AUTO_INCREMENT,
`studentId` int NOT NULL,
`c_sId` int NOT NULL,
`score` int NOT NULL,
`typeId` int NOT NULL,
PRIMARY KEY (`id`) 
)
DEFAULT CHARACTER SET = utf8;
CREATE TABLE `type1` (
`id` int NOT NULL AUTO_INCREMENT,
`name` char(10) CHARACTER SET utf8 NOT NULL,
PRIMARY KEY (`id`) 
)
DEFAULT CHARACTER SET = utf8;
CREATE TABLE `c-s` (
`id` int NOT NULL AUTO_INCREMENT,
`classId` int NOT NULL,
`courseId` int NOT NULL,
PRIMARY KEY (`id`) 
)
DEFAULT CHARACTER SET = utf8;

ALTER TABLE `student1` ADD FOREIGN KEY (`classId`) REFERENCES `class1` (`id`);
ALTER TABLE `c-s` ADD FOREIGN KEY (`classId`) REFERENCES `class1` (`id`);
ALTER TABLE `c-s` ADD FOREIGN KEY () REFERENCES `course1` (`id`);
ALTER TABLE `grade` ADD FOREIGN KEY (`studentId`) REFERENCES `student1` (`id`);
ALTER TABLE `grade` ADD FOREIGN KEY (`c_sId`) REFERENCES `c-s` (`id`);
ALTER TABLE `grade` ADD FOREIGN KEY (`typeId`) REFERENCES `type1` (`id`);
ALTER TABLE `teacher1` ADD FOREIGN KEY (`courseId`) REFERENCES `course1` (`id`);
ALTER TABLE `course1` ADD FOREIGN KEY (`teacherId`) REFERENCES `teacher1` (`id`);

