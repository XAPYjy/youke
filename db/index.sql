/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2019/11/20 8:48:51                           */
/*==============================================================*/

use youke;
drop table if exists yk_discuss;

drop table if exists yk_lesson;

drop table if exists yk_recommend;

drop table if exists yk_rotation;

drop table if exists yk_viedo;

/*==============================================================*/
/* Table: yk_discuss                                            */
/*==============================================================*/
create table yk_discuss
(
   id                   int not null,
   yk_user_id           int not null,
   yk_discuss_contents  varchar(100) not null,
   yk_discuss_date      datetime not null,
   yk_discuss_outdate   datetime not null,
   yk_discuss_click_num int,
   yk_lesson_id         int not null,
   yk_discuss_authority bool not null,
   primary key (id)
);

/*==============================================================*/
/* Table: yk_lesson                                             */
/*==============================================================*/
create table yk_lesson
(
   id                   int not null auto_increment,
   yk_video_jump_link   varchar(200) not null,
   yk_lesson_name       varchar(50) not null,
   yk_lesson_price      float,
   yk_lesson_describe   varchar(200) not null,
   yk_teacher_describe  varchar(100),
   yk_lesson_contents   varchar(50) not null,
   yk_lesson_contents_mark int not null,
   yk_lesson_img        varchar(200) not null,
   yk_rotaion_id        int ,
   yk_recommend_id      int ,
   yk_lesson_price_type varchar(50) not null,
   yk_lesson_dis_price  float,
   yk_lesson_list       int not null,
   primary key (id)
);

/*==============================================================*/
/* Table: yk_recommend                                          */
/*==============================================================*/
create table yk_recommend
(
   id                   int not null auto_increment,
   yk_lesson_type       varchar(200) not null,
   yk_lesson_jump_link  varchar(200) not null,
   primary key (id)
);

/*==============================================================*/
/* Table: yk_rotation                                           */
/*==============================================================*/
create table yk_rotation
(
   id                   int not null auto_increment,
   yk_is_rotation       bool not null,
   primary key (id)
);

/*==============================================================*/
/* Table: yk_viedo                                              */
/*==============================================================*/
create table yk_viedo
(
   id                   int not null,
   yk_video_name        varchar(50),
   yk_lesson_id         int not null,
   yk_video_progress    float,
   yk_user_id           int not null,
   yk_crats_id          int,
   yk_video_authority   bool not null,
   yk_lesson_jump_link  varchar(200) not null,
   primary key (id)
);

