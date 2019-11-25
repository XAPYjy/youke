/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2019/11/23 15:18:11                          */
/*==============================================================*/


drop table if exists yk_bank_card;

drop table if exists yk_billing_details;

drop table if exists yk_downloadRecord;

drop table if exists yk_information;

drop table if exists yk_my_class;

drop table if exists yk_order;

drop table if exists yk_user;

drop table if exists yk_wallet;

/*==============================================================*/
/* Table: yk_bank_card                                          */
/*==============================================================*/
create table yk_bank_card
(
   id                   int not null auto_increment,
   yk_id_card           varchar(30),
   name                 varchar(10),
   yk_user_id           int,
   yk_card_name         varchar(20),
   yk_card_type         varchar(10),
   yk_card_logo         varchar(256),
   primary key (id)
);

/*==============================================================*/
/* Table: yk_downloadRecord                                     */
/*==============================================================*/
create table yk_downloadRecord
(
   id                   int not null auto_increment,
   yk_dowTime           time,
   yk_dowContent        char(50),
   yk_u_id              int,
   primary key (id)
);

/*==============================================================*/
/* Table: yk_information                                        */
/*==============================================================*/
create table yk_information
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
/* Table: yk_my_class                                           */
/*==============================================================*/
create table yk_my_class
(
   id                   int not null auto_increment,
   yk_user_id           int,
   yk_class_id          int,
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
/* Table: yk_user                                               */
/*==============================================================*/
create table yk_user
(
   id                   int not null auto_increment,
   yk_name              varchar(50),
   yk_auto_string       varchar(100),
   yk_emil              varchar(50),
   yk_phone             varchar(20),
   sys_auth             bool,
   primary key (id)
);

/*==============================================================*/
/* Table: yk_wallet                                             */
/*==============================================================*/
create table yk_wallet
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
/* Table: yk_billing_details                                    */
/*==============================================================*/
create table yk_billing_details
(
   id                   int not null auto_increment,
   yk_wallet_id         int,
   yk_user_id           int,
   yk_bill_time         varchar(20),
   yk_amount            float,
   yk_integral          float,
   yk_paymenType        varchar(10),
   yk_transType         varchar(10),
   primary key (id)
);
