# write all queries here

create_profile_query = ('CREATE TABLE IF NOT EXISTS profile ('
    'f_name varchar(20) NOT NULL,'
    'l_name varchar(20) NOT NULL,'
    'u_name varchar(20) NOT NULL,'
    'password varchar(20) NOT NULL,'
    'profile_id int NOT NULL,'
    'created_date varchar(20) NOT NULL,'
    'phone_no varchar(11),'
    'email varchar(50) NOT NULL,'
    'profile_pic varchar(256),'
    'b_date date NOT NULL,'
    'friends_list int,'
    'PRIMARY KEY(profile_id),'
    'UNIQUE(email) );')


create_post_query = ('CREATE TABLE IF NOT EXISTS POST('
    'post_id int NOT NULL,'
    'time_stamp timestamp,'
    'poster_id int NOT NULL,'
    'likes_list int,'
    'PRIMARY KEY(post_id) );')


create_comment_query = ('CREATE TABLE IF NOT EXISTS COMMENT('
    'comment_id int NOT NULL,'
    'time_stamp timestamp NOT NULL,'
    'comm_text varchar(256) NOT NULL,'
    'commentor_ID int NOT NULL,'
    'likes_list int,'
    'PRIMARY KEY(comment_id) );')


create_like_query = ('CREATE TABLE IF NOT EXISTS `LIKE`('
    'like_id int NOT NULL,'
    'time_stamp timestamp NOT NULL,'
    'liker_id int NOT NULL,'
    'PRIMARY KEY(like_id) );')


create_message_query = ('CREATE TABLE IF NOT EXISTS MESSAGE('
    'sender_id int NOT NULL,'
    'receiver_id int NOT NULL,'
    'time_stamp timestamp NOT NULL,'
    'message_text varchar(256) NOT NULL,'
    'likes_list int,'
    'PRIMARY KEY(sender_id,receiver_id,time_stamp) );')


create_page_query = ('CREATE TABLE IF NOT EXISTS PAGE ('
    'page_id int NOT NULL,'
    'page_name varchar(128) NOT NULL,'
    'admin int NOT NULL,'
    'page_image varchar(256),'
    'num_views int,'
    'category varchar(64),'
    'description varchar(256),'
    'member_list int,'
    'PRIMARY KEY (page_id),'
    'FOREIGN KEY (admin) REFERENCES PROFILE(profile_id) );')


