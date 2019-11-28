/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2019/11/25 9:11:26                           */
/*==============================================================*/

drop table if exists sys_role;

drop table if exists sys_user;

drop table if exists sys_user_role;

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
