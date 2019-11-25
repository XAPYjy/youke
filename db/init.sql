/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2019/11/25 9:11:26                           */
/*==============================================================*/


drop table if exists FirstClass;

drop table if exists SecondClass;

drop table if exists billing_details;

drop table if exists downloadRecord;

drop table if exists information;

drop table if exists mycourse;

drop table if exists sys_role;

drop table if exists sys_user;

drop table if exists sys_user_role;

drop table if exists wallet;

drop table if exists yk_discuss;

drop table if exists yk_lesson;

drop table if exists yk_lesson2;

drop table if exists yk_lesson3;

drop table if exists yk_lesson_list;

drop table if exists yk_order;

drop table if exists yk_recommend;

drop table if exists yk_rotation;

drop table if exists yk_tree;

drop table if exists yk_user;

drop table if exists yk_viedo;

/*==============================================================*/
/* Table: FirstClass                                            */
/*==============================================================*/
create table FirstClass
(
   yk_FirstClassID      int not null,
   yk_FirstClassName    varchar(20),
   primary key (yk_FirstClassID)
);

/*==============================================================*/
/* Table: SecondClass                                           */
/*==============================================================*/
create table SecondClass
(
   yk_SecondClassID     int not null,
   yk_SecondClassName   varchar(20),
   yk_FirstClassID      int,
   primary key (yk_SecondClassID)
);

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
/* Table: sys_role                                              */
/*==============================================================*/
create table sys_role
(
   id                   INTEGER not null auto_increment,
   name                 VARCHAR(50) not null,
   code                 VARCHAR(20) not null,
   primary key (id)
);

/*==============================================================*/
/* Table: sys_user                                              */
/*==============================================================*/
create table sys_user
(
   id                   INTEGER not null auto_increment,
   name                 VARCHAR(50),
   auth_string          VARCHAR(100) not null,
   email                VARCHAR(50),
   phone                VARCHAR(50),
   primary key (id)
);

/*==============================================================*/
/* Table: sys_user_role                                         */
/*==============================================================*/
create table sys_user_role
(
   id                   INTEGER not null auto_increment,
   user_id              INTEGER,
   role_id              INTEGER,
   primary key (id)
);

/*==============================================================*/
/* Table: wallet                                                */
/*==============================================================*/
create table wallet
(
   id                   int not null auto_increment,
   yk_balance           char(50),
   yk_pay_pwd           char(100),
   yk_user_id           int,
   yk_bank_card         int,
   yk_integral          int,
   yk_member            char(50),
   yk_discount          char(10),
   yk_paymenType        char(5),
   yk_transType         char(5),
   primary key (id)
);

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
   yk_rotaion_id        int,
   yk_recommend_id      int,
   yk_lesson_price_type varchar(50) not null,
   yk_lesson_dis_price  float,
   yk_lesson_list       int not null,
   primary key (id)
);

/*==============================================================*/
/* Table: yk_lesson2                                            */
/*==============================================================*/
create table yk_lesson2
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
   yk_class_size        char(20),
   primary key (id)
);

/*==============================================================*/
/* Table: yk_lesson3                                            */
/*==============================================================*/
create table yk_lesson3
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
   yk_class_size        char(20),
   primary key (id)
);

/*==============================================================*/
/* Table: yk_lesson_list                                        */
/*==============================================================*/
create table yk_lesson_list
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

/*==============================================================*/
/* Table: yk_order                                              */
/*==============================================================*/
create table yk_order
(
   id                   int not null auto_increment,
   yk_goods_id          int,
   yk_isorderStatus     bool,
   yk_total_price       float,
   yk_user_id           int,
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
/* Table: yk_tree                                               */
/*==============================================================*/
create table yk_tree
(
   id                   int not null auto_increment,
   yk_goods_type        bool not null,
   yk_list_id           int not null auto_increment,
   yk_lesson_id         int not null,
   yk_price             float not null,
   yk_authority         bool not null,
   yk_user_id           int not null,
   yk_time              time not null,
   primary key (id)
);

/*==============================================================*/
/* Table: yk_user                                               */
/*==============================================================*/
create table yk_user
(
   id                   int not null auto_increment,
   yk_name              varchar(50),
   yk_auto_string       varchar(100),
   yk_emil              varchar(50),
   yk_phone             int,
   sys_auth             bool,
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
   yk_lesson_jump_link  varchar(200) not null,
   primary key (id)
);

