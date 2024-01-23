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


INSERT role VALUES(1, 'Admin');
INSERT role VALUES(2, 'User');
INSERT INTO user VALUES('joshuang321', 'password123!', 1, 1);
INSERT INTO user VALUES('joshuang_user321', 'password123!', 2, 1);
INSERT INTO user VALUES('inactive_user', 'password', 1, 0)