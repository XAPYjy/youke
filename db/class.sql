# drop table if exists FirstClass;
# create table FirstClass
# (
#    id                   int not null auto_increment,
#    yk_FirstClassID      int not null,
#    yk_FirstClassName    varchar(20),
#    primary key (id)
# );
# drop table if exists SecondClass;
#
#
# create table SecondClass
# (
#    id                   int not null auto_increment,
#    yk_SecondClassID     int not null,
#    yk_SecondClassName   varchar(20),
#    yk_FirstClassID      int,
#    secondimage                varchar(256),
#    secondurl                  varchar(256),
#    primary key (id)
# );
# drop table if exists lessonlist;
#
#
# create table lessonlist
# (
#    id                   int not null,
#    yk_LessonName        varchar(20),
#    yk_LessonImage       varchar(256),
#    yk_LessonClassID     int,
#    yk_PriceClassID      int,
#    yk_Price             float,
#    yk_JumpLink          varchar(256),
#    yk_Clicks            integer,
#    yk_AgeClass          varchar(20),
#    primary key (id)
# );

# insert into FirstClass (yk_FirstClassID, yk_FirstClassName) values (1,'少儿童书');
# insert into FirstClass (yk_FirstClassID, yk_FirstClassName) values (2,'文化教育');
# insert into FirstClass (yk_FirstClassID, yk_FirstClassName) values (3,'文学小说');
# insert into FirstClass (yk_FirstClassID, yk_FirstClassName) values (4,'人文社科');
# insert into FirstClass (yk_FirstClassID, yk_FirstClassName) values (5,'科技教育');
# insert into FirstClass (yk_FirstClassID, yk_FirstClassName) values (6,'艺术教育');
# insert into FirstClass (yk_FirstClassID, yk_FirstClassName) values (7,'休闲文化');
# insert into FirstClass (yk_FirstClassID, yk_FirstClassName) values (8,'舌尖文化');

insert into SecondClass(yk_secondclassid,yk_SecondClassName,yk_FirstClassID,secondimage,secondurl)values (1,'0-2岁',1,'','http://47.92.132.161:8003/gate/lesson/?secondid=1');
insert into SecondClass(yk_secondclassid,yk_SecondClassName,yk_FirstClassID,secondimage,secondurl)values (2,'3-6岁',1,'','http://47.92.132.161:8003/gate/lesson/?secondid=2');
insert into SecondClass(yk_secondclassid,yk_SecondClassName,yk_FirstClassID,secondimage,secondurl)values (3,'7-9岁',1,'','http://47.92.132.161:8003/gate/lesson/?secondid=3');
insert into SecondClass(yk_secondclassid,yk_SecondClassName,yk_FirstClassID,secondimage,secondurl)values (4,'10-12岁',1,'','http://47.92.132.161:8003/gate/lesson/?secondid=4');
insert into SecondClass(yk_secondclassid,yk_SecondClassName,yk_FirstClassID,secondimage,secondurl)values (5,'13-15岁',1,'','http://47.92.132.161:8003/gate/lesson/?secondid=5');
insert into SecondClass(yk_secondclassid,yk_SecondClassName,yk_FirstClassID,secondimage,secondurl)values (6,'小学教材',2,'','http://47.92.132.161:8003/gate/lesson/?secondid=6');
insert into SecondClass(yk_secondclassid,yk_SecondClassName,yk_FirstClassID,secondimage,secondurl)values (7,'初中教材',2,'','http://47.92.132.161:8003/gate/lesson/?secondid=7');
insert into SecondClass(yk_secondclassid,yk_SecondClassName,yk_FirstClassID,secondimage,secondurl)values (8,'高中教材',2,'','http://47.92.132.161:8003/gate/lesson/?secondid=8');
insert into SecondClass(yk_secondclassid,yk_SecondClassName,yk_FirstClassID,secondimage,secondurl)values (9,'大学教材',2,'','http://47.92.132.161:8003/gate/lesson/?secondid=9');
insert into SecondClass(yk_secondclassid,yk_SecondClassName,yk_FirstClassID,secondimage,secondurl)values (10,'外语教材',2,'','http://47.92.132.161:8003/gate/lesson/?secondid=10');
