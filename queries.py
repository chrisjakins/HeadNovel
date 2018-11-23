# write all queries here

create_profile_query = ('CREATE TABLE profile ('
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
    'PRIMARY KEY(profile_id) );')
