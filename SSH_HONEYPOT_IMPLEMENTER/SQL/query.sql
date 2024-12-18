create database honeypot_logs;

use honeypot_logs;

create table logs(
id int auto_increment primary key,
timestamp datetime default current_timestamp,
ip_address varchar(66),
username varchar(255),
password varchar(255),
message text
);
