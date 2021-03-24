## Week 5 mysql code

Q2

1. create database called website

   create database website;

   use website;

2. create table user ( id bigint primary key auto_increment,

   ​    name varchar(255) not null,

   ​    username varchar(255) not null,

   ​    password varchar(255) not null,

   ​    time datetime not null DEFAULT CURRENT_TIMESTAMP);

   describe user;

3. sql command

   * insert data to user table

     insert into user (name, username ,password) values ('u1','ply','ply');

     insert into user (name, username ,password) values ('u2','super','123');

     insert into user (name, username ,password) values ('u3','super3','abc');

     insert into user (name, username ,password) values ('u4','tim','abc@123');

     insert into user (name, username ,password) values ('u5','tom','123@pig');

   * 使用 SELECT 指令取得所有在 user 資料表中的使用者資料

     select * from user;

     ![1](https://github.com/chloe0730000/chloe0730000.github.io-assignment/blob/main/Assignment5%20-%20mysql/screenshots/1.png)

   * 使用 SELECT 指令取得 user 資料表中總共有幾筆資料 

     select count(*) from user;

     ![2](https://github.com/chloe0730000/chloe0730000.github.io-assignment/blob/main/Assignment5%20-%20mysql/screenshots/2.png)

   * 使用 SELECT 指令取得所有在 user 資料表中的使用者資料，並按照 time 欄位，由近 

     到遠排序。 

     select * from user order by time desc;

     ![3](https://github.com/chloe0730000/chloe0730000.github.io-assignment/blob/main/Assignment5%20-%20mysql/screenshots/3.png)

     

   * 使用 SELECT 指令取得 user 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近 

     到遠排序。 

     select *

     from

     ​	(select *, row_number() over(order by time desc) as rn

     ​	from user) as temp

     where rn in (2,3,4);

     ![4](https://github.com/chloe0730000/chloe0730000.github.io-assignment/blob/main/Assignment5%20-%20mysql/screenshots/4.png)

   * 使用 SELECT 指令取得欄位 username 是 ply 的使用者資料。 

     select * from user where username='ply';

     ![5](https://github.com/chloe0730000/chloe0730000.github.io-assignment/blob/main/Assignment5%20-%20mysql/screenshots/5.png)

   * 使用 SELECT 指令取得欄位 username 是 ply、且欄位 password 也是 ply 的資料。 

     select * from user where username='ply' and password='ply';

     ![6](https://github.com/chloe0730000/chloe0730000.github.io-assignment/blob/main/Assignment5%20-%20mysql/screenshots/6.png)

   * 使用 UPDATE 指令更新欄位 username 是 ply 的使用者資料，將資料中的 name 欄位 

     改成【丁滿】。 

     update user set name='丁滿' where username='ply';

     ![7](https://github.com/chloe0730000/chloe0730000.github.io-assignment/blob/main/Assignment5%20-%20mysql/screenshots/7.png)

   * 使用 DELETE 指令刪除所有在 user 資料表中的資料 

     delete from user;







Q4

* create message table

  create table message (id bigint primary key auto_increment, 

  ​	user_id bigint not null, 

  ​	content varchar(255) not null, 

  ​	time datetime not null default current_timestamp,

  ​	foreign key (user_id) references user(id));

* insert value

  insert into message (user_id, content) values (1,"testing");

  insert into message (user_id, content) values (2,"testing");

  insert into message (user_id, content) values (3,"testing");

  insert into message (user_id, content) values (4,"testing");

  insert into message (user_id, content) values (5,"testing");

  insert into message (user_id, content) values (5,"abc”);

* select * from message;

  ![8](https://github.com/chloe0730000/chloe0730000.github.io-assignment/blob/main/Assignment5%20-%20mysql/screenshots/8.png)

  

* 使用 SELECT 搭配 JOIN 的語法，取得所有留言，資料中須包含留言會員的姓名 

  select u.*, m.content

  from user as u

  join message as m on u.id = m.user_id;

  ![9](https://github.com/chloe0730000/chloe0730000.github.io-assignment/blob/main/Assignment5%20-%20mysql/screenshots/9.png)

* 使用 SELECT 搭配 JOIN 的語法，取得 user 資料表中欄位 username 是 ply 的所有留 

  言，資料中須包含留言會員的姓名 

   select u.*, m.content 

  from user as u join message as m on u.id = m.user_id 

  where username='ply';

  ![10](https://github.com/chloe0730000/chloe0730000.github.io-assignment/blob/main/Assignment5%20-%20mysql/screenshots/10.png)



* dump the file

  usr/local/mysql/bin/mysqldump -u root -p website > data.sql

* import the file

   /usr/local/mysql/bin/mysql -u root -p website < data.sql

