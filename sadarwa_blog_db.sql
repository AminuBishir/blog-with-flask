# Converted with pg2mysql-1.9
# Converted on Tue, 17 Dec 2019 13:13:07 -0500
# Lightbox Technologies Inc. http://www.lightbox.ca

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone="+00:00";

CREATE TABLE blog (
    subject text NOT NULL,
    content text NOT NULL,
    created timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
    last_modified timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
    author text NOT NULL,
    p_id int(11) NOT NULL,
    img_src varchar(100)
) 

CREATE TABLE comment (
    p_id int(11),
    commentor text NOT NULL,
    comment text NOT NULL,
    created timestamp DEFAULT CURRENT_TIMESTAMP,
    id int(11) NOT NULL
) 

CREATE TABLE likes (
    p_id int(11),
    liker text,
    id int(11) NOT NULL
) 

CREATE TABLE users (
    email text NOT NULL,
    f_name text NOT NULL,
    s_name text NOT NULL,
    password text NOT NULL,
    created timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
    role varchar(50)
) 

ALTER TABLE blog
    ADD CONSTRAINT blog_pkey PRIMARY KEY (p_id);
ALTER TABLE comment
    ADD CONSTRAINT comment_pkey PRIMARY KEY (id);
ALTER TABLE likes
    ADD CONSTRAINT likes_pkey PRIMARY KEY (id);
ALTER TABLE users
    ADD CONSTRAINT users_pkey PRIMARY KEY (email);
