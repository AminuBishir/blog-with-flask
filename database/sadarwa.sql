--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.18
-- Dumped by pg_dump version 9.5.18

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: blog; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.blog (
    subject text NOT NULL,
    content text NOT NULL,
    created timestamp with time zone DEFAULT now() NOT NULL,
    last_modified timestamp with time zone DEFAULT now() NOT NULL,
    author text NOT NULL,
    p_id integer NOT NULL,
    img_src character varying(100)
);


ALTER TABLE public.blog OWNER TO vagrant;

--
-- Name: blog_p_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.blog_p_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blog_p_id_seq OWNER TO vagrant;

--
-- Name: blog_p_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.blog_p_id_seq OWNED BY public.blog.p_id;


--
-- Name: comment; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.comment (
    p_id integer,
    commentor text NOT NULL,
    comment text NOT NULL,
    created timestamp with time zone DEFAULT now(),
    id integer NOT NULL
);


ALTER TABLE public.comment OWNER TO vagrant;

--
-- Name: comment_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.comment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.comment_id_seq OWNER TO vagrant;

--
-- Name: comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.comment_id_seq OWNED BY public.comment.id;


--
-- Name: likes; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.likes (
    p_id integer,
    liker text,
    id integer NOT NULL
);


ALTER TABLE public.likes OWNER TO vagrant;

--
-- Name: likes_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.likes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.likes_id_seq OWNER TO vagrant;

--
-- Name: likes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.likes_id_seq OWNED BY public.likes.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.users (
    email text NOT NULL,
    f_name text NOT NULL,
    s_name text NOT NULL,
    password text NOT NULL,
    created timestamp with time zone DEFAULT now() NOT NULL,
    role character varying(50)
);


ALTER TABLE public.users OWNER TO vagrant;

--
-- Name: p_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.blog ALTER COLUMN p_id SET DEFAULT nextval('public.blog_p_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.comment ALTER COLUMN id SET DEFAULT nextval('public.comment_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.likes ALTER COLUMN id SET DEFAULT nextval('public.likes_id_seq'::regclass);


--
-- Data for Name: blog; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.blog (subject, content, created, last_modified, author, p_id, img_src) FROM stdin;
Greetings	Hi there!\r<br>This is greeting from Sadarwa.	2019-08-20 20:22:48.618843+00	2019-08-20 20:22:48.6199+00	aminubishir@gmail.com	4	\N
Hola	Hola there!\r<br>I dey try tins out!	2019-09-04 05:45:57.217017+00	2019-09-04 05:45:57.217797+00	aminubishir@gmail.com	6	\N
Morning Greating	Hi!\r<br>Good morning and welcome to my Blog post.	2019-09-04 05:46:38.465178+00	2019-09-04 05:46:38.465502+00	aminubishir@gmail.com	7	\N
Barka da Zuwa	Salam!\r<br>Barkanku da zuwa wannan shafi namu mai albarka.	2019-09-04 05:47:56.323962+00	2019-09-04 05:47:56.324324+00	aminubishir@gmail.com	8	\N
Hello	Sannunku dai!\r\nPost with Image	2019-09-06 00:46:13.563014+00	2019-09-06 00:46:13.563387+00	aminubishir@gmail.com	9	\N
Posting	Hi there	2019-09-06 00:47:56.399424+00	2019-09-06 00:47:56.399846+00	aminubishir@gmail.com	10	\N
Testing Image	I'm just trying to save image!	2019-09-06 00:50:43.177534+00	2019-09-06 00:50:43.178013+00	aminubishir@gmail.com	11	\N
Posting with Image	This post is made with an image!	2019-09-09 21:26:09.939314+00	2019-09-09 21:26:09.939957+00	aminubishir@gmail.com	12	/vagrant/sadarwa-blog/firts_Web_Server.png
Another img post	Another Post made with picture	2019-09-09 21:31:19.267143+00	2019-09-09 21:31:19.26751+00	aminubishir@gmail.com	13	/vagrant/sadarwa-blog/templates/image/temple.png
TEsting	Just another Img post	2019-09-09 21:34:43.717047+00	2019-09-09 21:34:43.717435+00	aminubishir@gmail.com	14	image/petro.png
With Img	Hi there!\r\nThis is just another test post!	2019-09-09 21:39:16.427426+00	2019-09-09 21:39:16.427899+00	aminubishir@gmail.com	15	/vagrant/sadarwa-blog/image/petro.png
Testing Image src	Posing with Image	2019-09-09 21:45:40.186687+00	2019-09-09 21:45:40.1871+00	aminubishir@gmail.com	16	/vagrant/sadarwa-blog/static/image/Utta.jpg
Image Post	Posting with Image. Please bear with us.	2019-09-09 21:47:57.421047+00	2019-09-09 21:47:57.421592+00	aminubishir@gmail.com	17	/static/image/Snapshot_-_1.png
Photo News	Hello there!\r\nPosting with image works now!\r\nCheer!\r\nAnd this line is part of the updated post :)	2019-09-09 21:55:30.315695+00	2019-09-09 21:55:30.316223+00	aminubishir@gmail.com	18	/static/image/petro.png
\.


--
-- Name: blog_p_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.blog_p_id_seq', 18, true);


--
-- Data for Name: comment; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.comment (p_id, commentor, comment, created, id) FROM stdin;
8	aminubishir@gmail.com	Sannunku da kokari. Gaskiya wannan post ya matukar burgeni!	2019-09-04 06:05:55.323593+00	6
8	aminubishir@gmail.com	Wannan magana hakane. Allah ya saka	2019-09-04 06:46:20.80515+00	7
8	aminubishir@gmail.com	That's really a great post!	2019-09-04 06:46:58.181503+00	8
8	aminubishir@gmail.com	great Job!	2019-09-04 06:48:19.007079+00	9
4	aminubishir@gmail.com	Thank you sadarwa, we greet you too!	2019-09-04 06:48:45.819275+00	10
6	aminubishir@gmail.com	Hola Sadarwa	2019-09-04 06:49:43.958391+00	11
6	aminubishir@gmail.com	Nice one	2019-09-04 07:08:07.625129+00	12
6	aminubishir@gmail.com	Great Job indeed!	2019-09-04 07:08:44.951623+00	13
6	aminubishir@gmail.com	Hi guys! Thanks for this post.	2019-09-04 07:10:30.025003+00	14
18	aminubishir@gmail.com	Nice one. And it's with Image! Wow	2019-09-10 05:56:22.552828+00	15
18	aminubishir@gmail.com	That's very awesome!	2019-09-13 16:18:33.817453+00	16
18	aminubishir@gmail.com	Hello there and good day to you. I really like reading this article and I really love it to the core! Just keep it up as we continue to be with now and always!	2019-09-13 16:46:19.953042+00	17
\.


--
-- Name: comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.comment_id_seq', 18, true);


--
-- Data for Name: likes; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.likes (p_id, liker, id) FROM stdin;
\.


--
-- Name: likes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.likes_id_seq', 1, false);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.users (email, f_name, s_name, password, created, role) FROM stdin;
aminubishir@gmail.com	Aminu	Bishir	qFjTK,9f20d6e4b28d333ff74823b5977f5e833b8442dadd732f1e64f03b8f47a0176f	2019-08-16 11:54:20.768883+00	admin
a@b.com	Aminu	Bishir	qvvMk,6daff2302240c5c6a534db25fd1551a58df8a5a178917a32c22b7b0f5432dc34	2019-09-25 06:59:43.036313+00	user
\.


--
-- Name: blog_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.blog
    ADD CONSTRAINT blog_pkey PRIMARY KEY (p_id);


--
-- Name: comment_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT comment_pkey PRIMARY KEY (id);


--
-- Name: likes_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_pkey PRIMARY KEY (id);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (email);


--
-- Name: comment_commentor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT comment_commentor_fkey FOREIGN KEY (commentor) REFERENCES public.users(email);


--
-- Name: comment_p_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT comment_p_id_fkey FOREIGN KEY (p_id) REFERENCES public.blog(p_id);


--
-- Name: likes_liker_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_liker_fkey FOREIGN KEY (liker) REFERENCES public.users(email);


--
-- Name: likes_p_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_p_id_fkey FOREIGN KEY (p_id) REFERENCES public.blog(p_id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

