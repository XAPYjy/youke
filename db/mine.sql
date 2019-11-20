/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2019/11/19 21:45:36                          */
/*==============================================================*/
use youke;

drop table if exists billing_details;

drop table if exists downloadRecord;

drop table if exists information;

drop table if exists mycourse;

drop table if exists order;

drop table if exists user;

drop table if exists wallet;

drop table if exists yk_lesson;

/*==============================================================*/
/* Table: billing_details                                       */
/*==============================================================*/
create table billing_details
(
   id                   int not null auto_increment,
   yk_wallet_id         int,
   yk_user_id           int,
   yk_recharge_time     time,
   yk_recharge_amount   float,
   yk_consumption_time  time,
   yk_consumption_amount float,
   primary key (id)
);

/*==============================================================*/
/* Table: downloadRecord                                        */
/*==============================================================*/
create table downloadRecord
(
   id                   int not null auto_increment,
   yk_dowTime           time,
   yk_dowContent        char(50),
   yk_u_id              int,
   primary key (id)
);

/*==============================================================*/
/* Table: information                                           */
/*==============================================================*/
create table information
(
   id                   int not null auto_increment,
   yk_nickname          varchar(50),
   yk_name              varchar(50),
   yk_avatar            varchar(256),
   yk_sex               varchar(10),
   yk_age               int,
   yk_Career            varchar(50),
   yk_hobby             char(50),
   yk_IDnumber          varchar(50),
   yk_signature         varchar(500),
   yk_user_id           int,
   primary key (id)
);

/*==============================================================*/
/* Table: mycourse                                              */
/*==============================================================*/
create table mycourse
(
   id                   int not null auto_increment,
   yk_user_id           int,
   yk_class_id          int,
   primary key (id)
);

/*==============================================================*/
/* Table: "order"                                               */
/*==============================================================*/
create table user_order
(
   id                   int not null auto_increment,
   yk_goods_id          int,
   yk_isorderStatus     bool,
   yk_total_price       float,
   yk_user_id           int,
   primary key (id)
);

/*==============================================================*/
/* Table: user                                                  */
/*==============================================================*/
create table user
(
   id                   int not null,
   yk_nume              varchar(50) not null,
   yk_auto_string       varchar(50) not null,
   yk_phone             int not null,
   sys_auth             bool,
   primary key (id)
);

/*==============================================================*/
/* Table: wallet                                                */
/*==============================================================*/
create table wallet
(
   id                   int not null auto_increment,
   yk_balance           char(50),
   yk_pay_pwd           char(50),
   yk_user_id           int,
   yk_bank_card         int,
   yk_integral          int,
   yk_member            char(50),
   yk_discount          char(10),
   primary key (id)
);

/*==============================================================*/
/* Table: yk_lesson                                             */
/*==============================================================*/
create table yk_lesson
(
   id                   int not null auto_increment,
   yk_video_jump_link   varchar(200),
   yk_lesson_name       varchar(50),
   yk_lesson_price      float,
   yk_lesson_describe   varchar(200),
   yk_teacher_describe  varchar(100),
   yk_lesson_contents   varchar(50),
   yk_lesson_contents_mark int,
   yk_lesson_img        varchar(200),
   yk_rotaion_id        int,
   yk_recommend_id      int,
   yk_lesson_price_type varchar(50),
   yk_lesson_dis_price  float,
   yk_lesson_list       int,
   yk_user_id           int,
   yk_buy_amount        int,
   yk_watch_amount      int,
   yk_course_chapter    char(20),
   yk_one_list_id       int,
   yk_tow_list_id       int,
   primary key (id)
);




