DROP DATABASE DevOps2023Asg1;
CREATE DATABASE DevOps2023Asg1;
USE DevOps2023Asg1;
SHOW DATABASES;

CREATE TABLE role(
    id int NOT NULL,
    name varchar(10) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE user(
    username varchar(32) NOT NULL,
    password varchar(32) NOT NULL,
    role_id int NOT NULL,
    is_active int NOT NULL,
    PRIMARY KEY(username),
    FOREIGN KEY(role_id) REFERENCES role(id)
);

CREATE TABLE capstone(
    pic varchar(100) NOT NULL,
    role_id int NOT NULL,
    nstudent int NOT NULL,
    year int NOT NULL,
    title varchar(100) NOT NULL,
    companyname varchar(100) NOT NULL,
    poc varchar(100) NOT NULL,
    description varchar(300) NOT NULL
);

INSERT INTO role VALUES(0, 'Admin');
INSERT INTO role VALUES(1, 'User');

INSERT INTO user VALUES('joshuang321', 'password123!', 0, 1);
INSERT INTO user VALUES('joshuang_user321', 'password123!', 1, 1);