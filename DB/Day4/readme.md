create table users (
    user_id serial primary key,
    username varchar(100) not null,
    email varchar(100) not null,
    password text not null,
    created_at timestamp 

)


insert into users set (username, email, password) set ('jegan', 'j@j.com', 'password')

Alter table users ADD COLUMN phone varchar(15);
Alter table users ADD COLUMN is_active BOOLEAN NOT NULL;

Alter table users ADD COLUMN age INT check(age > =18);

Alter table user ADD constraint uniq_email_id unique
