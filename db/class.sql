drop table if exists yk_firstClass;
create table yk_firstClass
(
   id                   int not null auto_increment,
   yk_FirstClassID      int not null,
   yk_FirstClassName    varchar(20),
   primary key (id)
);
drop table if exists yk_econdClass;


create table yk_econdClass
(
   id                   int not null auto_increment,
   yk_SecondClassID     int not null,
   yk_SecondClassName   varchar(20),
   yk_FirstClassID      int,
   secondimage                varchar(256),
   secondurl                  varchar(256),
   primary key (id)
);
drop table if exists yk_lessonlist;


create table yk_lessonlist
(
   id                   int not null,
   yk_LessonName        varchar(20),
   yk_LessonImage       varchar(256),
   yk_LessonClassID     int,
   yk_PriceClassID      int,
   yk_Price             float,
   yk_JumpLink          varchar(256),
   yk_Clicks            integer,
   yk_AgeClass          varchar(20),
   primary key (id)
);