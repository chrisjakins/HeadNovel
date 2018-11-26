# write all queries here

create_profile_query = ('CREATE TABLE IF NOT EXISTS profile ('
    'f_name varchar(20) NOT NULL,'
    'l_name varchar(20) NOT NULL,'
    'u_name varchar(20) NOT NULL,'
    'password varchar(20) NOT NULL,'
    'profile_id int NOT NULL,'
    'created_date datetime NOT NULL,'
    'phone_no varchar(11),'
    'email varchar(50) NOT NULL,'
    'b_date date NOT NULL,'
    'PRIMARY KEY(profile_id),'
    'UNIQUE(email, u_name) );')


create_post_query = ('CREATE TABLE IF NOT EXISTS POST('
    'post_id int NOT NULL,'
    'text varchar(400) NOT NULL,'
    'time_stamp datetime,'
    'poster_id int NOT NULL,'
    'likes_list int,'
    'PRIMARY KEY(post_id) );')


create_comment_query = ('CREATE TABLE IF NOT EXISTS COMMENT('
    'comment_id int NOT NULL,'
    'time_stamp datetime NOT NULL,'
    'comm_text varchar(256) NOT NULL,'
    'commentor_ID int NOT NULL,'
    'likes_list int,'
    'PRIMARY KEY(comment_id) );')


create_like_query = ('CREATE TABLE IF NOT EXISTS `LIKE`('
    'like_id int NOT NULL,'
    'time_stamp datetime NOT NULL,'
    'liker_id int NOT NULL,'
    'PRIMARY KEY(like_id) );')


create_message_query = ('CREATE TABLE IF NOT EXISTS MESSAGE('
    'sender_id int NOT NULL,'
    'receiver_id int NOT NULL,'
    'time_stamp datetime NOT NULL,'
    'message_text varchar(256) NOT NULL,'
    'likes_list int,'
    'PRIMARY KEY(sender_id,receiver_id,time_stamp) );')


create_page_query = ('CREATE TABLE IF NOT EXISTS PAGE ('
    'page_id int NOT NULL,'
    'page_name varchar(128) NOT NULL,'
    'admin int NOT NULL,'
    'num_views int,'
    'category varchar(64),'
    'description varchar(256),'
    'PRIMARY KEY (page_id),'
    'FOREIGN KEY (admin) REFERENCES PROFILE(profile_id) );')


random_insert_queries = [
    "INSERT INTO profile "
    "VALUES ('Chris', 'Jakins', 'chrisjakins',"
    "'password',0,'2014-10-23 15:21:07','8175551000',"
    "'chris@email.com','1994-04-22')",

    "INSERT INTO profile "
    "VALUES ('Luis', 'Gonzalez', 'luisgonzalez',"
    "'password',1,'2014-10-24 15:21:07','8175551001',"
    "'luis@email.com','1997-06-13')",

    "INSERT INTO profile "
    "VALUES ('Ray', 'Robinson', 'rayrobinson',"
    "'password',2,'2014-10-13 15:21:07','8175551002',"
    "'ray@email.com','1980-03-23')",

    "INSERT INTO profile "
    "VALUES ('Marsha', 'McDonald', 'doubleM',"
    "'dogsandcats',3,'2015-10-23 15:22:07','8176543210',"
    "'doublem@email.com','1990-07-01')",

    "INSERT INTO profile "
    "VALUES ('Spongebob', 'Squarepants', 'da_sponge',"
    "'iluvpatrick',4,'2014-10-23 17:21:07','1234567890',"
    "'da.sponge@email.com','1994-01-21')",

    "INSERT INTO profile "
    "VALUES ('Patrick', 'Star', 'big_n_pink',"
    "'iluvspongebob',5,'2012-08-23 08:21:07','9876543456',"
    "'big.n.pink@email.com','1994-01-21')",

    "INSERT INTO profile "
    "VALUES ('Robert', 'Downey Jr.', 'ironman',"
    "'thicc',6,'2017-10-23 15:10:07','5554446666',"
    "'ironman@email.com','1975-10-05')",

    "INSERT INTO profile "
    "VALUES ('Gordan', 'Ramsay', 'raw_salmon',"
    "'food',7,'2013-12-25 15:21:07','1112223333',"
    "'raw.salmon@email.com','1970-10-10')",

    "INSERT INTO profile "
    "VALUES ('Ali', 'Sharifara', 'alisharifara',"
    "'databases',8,'2010-10-23 15:10:07','2223334444',"
    "'alisharifara@email.com','1985-10-25')",

    "INSERT INTO profile "
    "VALUES ('Dr.', 'Zhivago', 'thedoc',"
    "'medicalschool',9,'2016-08-10 15:21:07','3334445555',"
    "'thedoc@email.com','2000-04-25')",

    "INSERT INTO profile "
    "VALUES ('Snoop', 'Dog', 'snoopdog',"
    "'maryjane',10,'2014-04-20 16:20:00','8174201420',"
    "'snoopdog@email.com','1994-04-20')",

    "INSERT INTO profile "
    "VALUES ('Sun', 'Tzu', 'suntzu',"
    "'artofwar',11,'1980-01-23 15:21:07','1110008889',"
    "'suntzu@email.com','1900-09-18')",

    "INSERT INTO profile "
    "VALUES ('Bruce', 'Wayne', 'darkknight',"
    "'batsrcool',12,'2014-02-10 12:01:59','8435552049',"
    "'darkknight@email.com','1969-06-20')",

    "INSERT INTO profile "
    "VALUES ('Tom', 'Brady', 'patsqb',"
    "'football',13,'2014-10-23 15:21:07','6549873214',"
    "'patsqb@email.com','1977-11-30')",

    "INSERT INTO profile "
    "VALUES ('Charlie', 'Kelly', 'greenman',"
    "'eagles',14,'2013-10-10 20:21:07','4567891234',"
    "'greenman@email.com','1980-02-05')",

    "INSERT INTO profile "
    "VALUES ('Dennis', 'Reynolds', 'goldengod',"
    "'secret',15,'2017-12-10 02:50:07','8175675678',"
    "'goldengod@email.com','1982-10-21')",

    "INSERT INTO profile "
    "VALUES ('Deandra', 'Reynolds', 'richnfamous',"
    "'notsecret',16,'2017-12-11 02:51:07','8178678567',"
    "'richnfamous@email.com','1982-10-21')",

    "INSERT INTO profile "
    "VALUES ('Ronald', 'MacDonald', 'lotsofmuscle',"
    "'bodyguard',17,'2018-12-23 18:21:07','8904563847',"
    "'lotsofmuscle@email.com','1983-01-15')",

    "INSERT INTO profile "
    "VALUES ('Frank', 'Reynolds', 'rumham',"
    "'rumham',18,'2018-03-23 15:21:07','8178178176',"
    "'rumham@email.com','1955-07-08')",

    "INSERT INTO profile "
    "VALUES ('Morihei', 'Ushiba', 'artofpeace',"
    "'aikido',19,'1999-04-19 19:19:19','8171919199',"
    "'artofpeace@email.com','1919-04-19')",

    "INSERT INTO page "
    "VALUES (0,'CSE3320 Database Group', 0,"
    "0,'Professional','The group for the databases project')",

    "INSERT INTO page "
    "VALUES (1,'Cookie Club', 15,"
    "0,'Organization','A club that loves to make cookies!')",
    
    "INSERT INTO page "
    "VALUES (2,'Book Club', 3,"
    "0,'Personal','Reading group every Sunday :)')",
    
    "INSERT INTO page "
    "VALUES (3,'Chess Club', 8,"
    "0,'Organization','Learn to play chess.')",
    
    "INSERT INTO page "
    "VALUES (4,'Programming Club', 9,"
    "0,'Organization','For all programmers, old and new!')",
    
    "INSERT INTO page "
    "VALUES (5,'Anime Club', 12,"
    "0,'Personal','Who is best girl? Come hang out and discuss!')",
    
    "INSERT INTO page "
    "VALUES (6,'Linux Admins', 15,"
    "0,'Personal','sudo rm')",
    
    "INSERT INTO page "
    "VALUES (7,'Extreme Parkour Group', 19,"
    "0,'Social','Let us go jump and stuff!')",
    
    "INSERT INTO page "
    "VALUES (8,'Board Game Club', 1,"
    "0,'Social','Like board games? This is the group for you!')",
    
    "INSERT INTO page "
    "VALUES (9,'Computer Network Security Club', 7,"
    "0,'Organization','TCP or UDP? Come network!')",

    "INSERT INTO post "
    "VALUES (0, 'Meeting today at 5pm', '2017-08-10 10:10:10',5, NULL)"
]
