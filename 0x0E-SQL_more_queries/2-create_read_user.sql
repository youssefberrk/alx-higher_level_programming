-- script that creates the database hbtn_0d_2 and the user user_0d_2.
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
--create user wit pwd
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- grant privilege
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
