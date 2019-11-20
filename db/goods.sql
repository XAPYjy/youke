/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2019/11/19 19:14:18                          */
/*==============================================================*/

use youke;
drop table if exists bags;

/*==============================================================*/
/* Table: bags                                                  */
/*==============================================================*/
create table bags
(
   id                   int not null auto_increment,
   yk_goods_type        bool not null,
   yk_list_id           int,
   yk_lesson_id         int not null,
   yk_price             float not null,
   yk_authority         bool not null,
   yk_user_id           int not null,
   yk_time              time not null,
   primary key (id)
);

