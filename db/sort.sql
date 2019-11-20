use youke;
create table FirstClass
(
   id                   int not null,
   yk_FirstClassName    varchar(20),
   primary key (id)
);
create table SecondClass
(
   id                   int not null,
   yk_SecondClassName   varchar(20),
   yk_FirstClassID      int,
   yk_JumpLink          varchar(256),
   yk_LikeNumber        integer(20),
   primary key (id)
);
create table LessonList
(
   id                   int not null,
   yk_Clicks            integer,
   yk_AgeClass          int,
   yk_SecondClassID     int,
   yk_LessonListName    varchar(50),
   primary key (id)
);
create table Lesson
(
   id                   int not null auto_increment,
   yk_video_jump_link   varchar(200) not null,
   yk_lesson_name       varchar(50),
   yk_lesson_price      float,
   yk_lesson_describe   varchar(200),
   yk_teacher_describe  varchar(100),
   yk_lesson_contents   varchar(50) not null,
   yk_lesson_contents_mark int not null,
   yk_lesson_image      varchar(256),
   yk_rotation_id       int,
   yk_recommend_lesson_id int,
   yk_price_class       int,
   yk_discount_price    float,
   yk_lesson_list_id    int,
   primary key (id)
);