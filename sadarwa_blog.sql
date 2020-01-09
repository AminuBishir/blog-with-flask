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
Morning Greating	Hi!\r<br>Good morning and welcome to my Blog post.	2019-09-04 05:46:38.465178+00	2019-09-04 05:46:38.465502+00	aminubishir@gmail.com	7	\N
Barka da Zuwa	Salam!\r<br>Barkanku da zuwa wannan shafi namu mai albarka.	2019-09-04 05:47:56.323962+00	2019-09-04 05:47:56.324324+00	aminubishir@gmail.com	8	\N
Posting with Image	This post is made with an image!	2019-09-09 21:26:09.939314+00	2019-09-09 21:26:09.939957+00	aminubishir@gmail.com	12	/vagrant/sadarwa-blog/firts_Web_Server.png
Another img post	Another Post made with picture	2019-09-09 21:31:19.267143+00	2019-09-09 21:31:19.26751+00	aminubishir@gmail.com	13	/vagrant/sadarwa-blog/templates/image/temple.png
TEsting	Just another Img post	2019-09-09 21:34:43.717047+00	2019-09-09 21:34:43.717435+00	aminubishir@gmail.com	14	image/petro.png
With Img	Hi there!\r\nThis is just another test post!	2019-09-09 21:39:16.427426+00	2019-09-09 21:39:16.427899+00	aminubishir@gmail.com	15	/vagrant/sadarwa-blog/image/petro.png
Testing Image src	Posing with Image	2019-09-09 21:45:40.186687+00	2019-09-09 21:45:40.1871+00	aminubishir@gmail.com	16	/vagrant/sadarwa-blog/static/image/Utta.jpg
Image Post	Posting with Image. Please bear with us.	2019-09-09 21:47:57.421047+00	2019-09-09 21:47:57.421592+00	aminubishir@gmail.com	17	/static/image/Snapshot_-_1.png
Photo News	Hello there!\r\nPosting with image works now!\r\nCheer!\r\nAnd this line is part of the updated post :)	2019-09-09 21:55:30.315695+00	2019-09-09 21:55:30.316223+00	aminubishir@gmail.com	18	/static/image/petro.png
PHP Security!	Hello There!\r\nOur today's topic has to do with PHP Security and the latest vulnerabilities uncovered in the age long web programming language.	2019-12-14 14:38:14.404265+00	2019-12-14 14:38:14.404602+00	aminubishir@gmail.com	21	/static/image/cover_photo.png
Want Validate Your Form data? Make It Automatic With WTForms	From Software Development point of view, Form Validation is a task that involved applying some rules that the data, inserted via the form, are expected to conform with. This is very important step as it helps the developer in making sure that only the accepted type of data, which is also in the acceptable format, are allowed to pass unto the next step for further processing.\r\n\r\nForm can be validated from the client-side or from the server-side. In this tutorial, I will be using wtforms, a python library, and a flask, a simple and light weight web app framework, to generate, display and also validate the form from the server-side.\r\n\r\n\r\n \r\nBy default, python installation comes with a flask framework. But in case if yours didn’t, run the command below to install it:\r\n\r\n$ pip install flask\r\nRun the command below to install the wtforms library:\r\n\r\n$ pip install wtforms\r\nAfter successfully installing the two modules above, we are now ready to dive into the wonderful world of form auto generation and auto validation!\r\n\r\nTo generate a form, using wtforms, one needs to follow these simple steps:\r\n\r\nImport the required fields and the Form module\r\nCreate the Form model\r\nDisplay the form (in the hmtl) and/or validate the data submitted via the form\r\nImporting the Form class & the Fields\r\n\r\nForm is the class we need to inherit in our models:  from wtforms import Form\r\n\r\nAll the fields/controls that we need to use in our form are already defined in the wtforms library. All we need to do is to import them and then put them into use (in our model). We also need to import validators, which is also a wtforms module  used in applying validation rules to our form.\r\n\r\n\r\n \r\nFor instance, if we want to use text fields , password field and checkbox, the general import, including the Form class, will look like:\r\n\r\nfrom wtforms import Form, StringField, PasswordField, BooleanField, validators\r\nNote: StringField is for text field, PasswordField is for text field with hidden password characters, BooleanField is for checkbox. To know more about the other available fields, click here\r\n\r\nCreating the Form model\r\n\r\nThe form model is a class, which we need to create, which contains the definition of the form we want to use. This class also has to extend the Form module that we imported. A simple model for a login form, that uses the fields we imported above, can look like the following:\r\n\r\n  class LoginForm(Form):\r\n      username = StringField('Username',[validators.required(), validators.Length(min=3)])\r\n      password = PasswordField('Password',[validators.required(),validators.Length(min=3)])\r\n      remember_me = BooleanField('Remember Me') \r\nIn the above form model, called LoginForm, we defined three fields (username, password and remember_me) which are the names we will be using to access the form controls in the html and in our server-side code. Each of the fields above is initialized with its label (such as Remember Me for the remember_me  field and the validation rules).\r\n\r\nDisplaying the form\r\n\r\nBefore we can display our form in the html, we need to create the object of the form model and then pass it in the function that render our template. Below is the route that displays our login page (or grabs data from our form based on type of request):\r\n\r\n #the '/' below indicates that this is default/index page\r\n @app.route('/',methods=['GET','POST'])\r\n def home_page():\r\n      #create object of our LoginForm\r\n      login_form = LoginForm()\r\n      \r\n      #check if our request is of GET type, then display form\r\n      if request.method == 'GET':\r\n            return render_template('home.html',login_form=login_form)\r\n            \r\n      else:\r\n      #our request is of POST type which mean data is being submitted via the form\r\n      \r\n      #validate the login grab our data here and do something with it\r\n      if login_form.validate() #check if the data conform to the rules\r\n            username = login_form.username.data\r\n            userpass = login_form.password.data\r\n            stay_logged = login_form.remember_me.data #boolean yes or no\r\n            \r\n            #now that we have the data we can do what we like with it\r\n      else: #if validation failed\r\n      #some form's rules are violated, you can acess the errors in the template through login_form.errors \r\n In our html, we need to display the form by accessing the form object that is passed through the render_template function. Below is how the html will look like:\r\n\r\n     <form class="form">    \r\n   {{login_form.username(class="form-control mb-3 mt-5",placeholder="Username",style="width:250px")}} \r\n\r\n    {{login_form.password(class="form-control mb-3",placeholder="Password", style="width:250px")}}   \r\n\r\n   {{login_form.remember_me(class="form-control")}}<p >Remember me</p>     <button type="submit" class="btn btn-primary">Login</button>     </form>\r\n (if you don’t know about generating html using template, like jinja2, click here for short intro)\r\n\r\nAs you can see above, you can apply css classes and other attributes to the form elements.\r\n\r\n\r\n \r\nThis is my little intro to using wtform for generating and validating form inputs. If you are curious about how you can apply form generation and validation in your project, feel free to clone/download this my github repo which is a small blog website in which I made use of wtform in generating and validating my form elements and data (especially the login, signup, new and edit blog forms). If you have any difficulty understanding some parts of this tutorial feel  free to comment and/or connect with me as I’m always ready to help and be helped.  \r\n\r\nCheers!	2019-12-15 09:18:59.566181+00	2019-12-15 09:18:59.566708+00	aminubishir@gmail.com	22	/static/image/login_form.png
Greetings	Hi there!\r\n<br>This is greeting from Sadarwa. I Salute you all!	2019-08-20 20:22:48.618843+00	2019-08-20 20:22:48.6199+00	aminubishir@gmail.com	4	\N
Hello	Sannunku dai!\r\nPost with Image. And this is a great post!	2019-09-06 00:46:13.563014+00	2019-09-06 00:46:13.563387+00	aminubishir@gmail.com	9	\N
Let’s Talk About Nigeria, How Secured is Our Internet?	Keeping information secured and protecting the integrity of data over the internet is now becoming a huge and complex task, due to the increasing number of threats to the information security. Security over the internet is now becoming a top priority for any government or privately owned establishments that are serious about their businesses as well as protecting the integrity of their data (or data belonging to their clients). It is thus very worrisome to see that up to now, in Nigeria, both the government and the private establishments are not giving information security (most especially those available on the internet) the necessary attention that it deserves, thus turning Nigerian cyber-space into a hot cakes for hackers that either want to try their hacking expertise (experiment) or steal some information.\r\n\r\nDoes The Government Care?\r\nEven though the Nigerian government has a cyber-security laws that clearly state the punishments awaiting those that take part, in anyway, in cyber-security breach, it seems that the government is oblivious of the fact that it also has the responsibility of taking control measures that will enhance the security of the Nigerian cyber-space, so that breaching the cyber-security would not be as ‘easy’ as it seems to be now. The government’s failure to take this responsibility is what makes the Nigerian cyber-space so vulnerable to the extent that hacking a government owned websites is now becoming a common thing that we hear about every now and then, despite the huge maintenance costs being budgeted to manage the websites.\r\n\r\nHacking Incidences\r\nIt should not be forgotten that hacking a Nigerian government owned websites, which was publicly known, started as far back as 2012 when a website belonging to an agency of the Federal Ministry of Health was hacked and taken down by some hackers identified to be of foreign origin. The website (nphc.gov.ng), for National Primary Health Care, was hacked and taken down for a period of more than two weeks! But to the amusement of the press, after contacting the ministry about the incidence, the ministry said that they were not aware of the incidence!\r\n\r\nIn 2013 also, the website belonging to the Federal Government (nigeria.gov.ng) was hacked and taken down by the Nigerian members of the world renowned hacktivits’ group called Anonymous. The website was hacked, as mentioned by the hackers, due the Anti-gay law that the then government was about to pass. The hackers warned the then president that, if he succeeded in passing the bill into law, they’ll make a startling revelations of documents exposing the massive corruption that characterized his government. It was after this hacking incidence that the government took the bull by the horn by passing 14 years jail term to anybody found taking part same-sex marriage or homosexuality.\r\n\r\n\r\n \r\nEarlier before hacking the nigeria.gov.ng, the national assembly was hacked in an attempt by the hackers to influence the passing of the Anti-gay law bill. It’s after this attack that the hackers made available, to the public, a huge database containing personal information of about 1101 persons both Nigerians and foreigners that have some relationship with the National Assembly.\r\n\r\nAfter the above incidences, it seems that the government did not learn anything, because the hackers keep taking down the government owned websites one after the other unabated. In 2016, a website belonging to the court of appeal (courtofappeal.gov.ng) was also hacked and taken down by another notorious hackers’ group. In 2017 also, a website belonging to the Nigerian law school (lawschool.gov.ng) was hacked as information were leaked to the public.\r\n\r\nMore recent of the hacking incidences were those of the SMEDAN websites and, again, National Assembly website. The website belonging to the Small and Medium Enterprises Commission (smedan.gov.ng) was hacked some few months back (in 2018) by a hacker who identifies himself (as written on the homepage) as Ismael Chriki. The website took time before it was recovered. The latest happening is the hacking of the website belonging to the second arm of Nigerian government -National Assembly (nass.gov.ng). The hacker who identified himself as Mr.OneJack, bearing an {InfoSec} logo, leaked a lot of documents and files belonging to the website. Up to the time of writing this article, the website is still in the control of the hacker(s).\r\n\r\n\r\n \r\nGovernment owned websites are not the only target by the hackers, they also, for often, target Nigerian banks stealing credit cards information and account details. More recent was incidence of one Medical doctor turned hacker, who was arrested by the Lagos state police command. He was alleged to have been hacking the Nigerian banks and stealing money. He said, while paraded to the press, that “the Nigerian banks are very very easy to hack….” Nigerian banks lose a lot of money to the activities of hackers within and outside of Nigeria.\r\n\r\nThe government needs to understand that, having cyber-security laws is not enough to checkmate the activities of hackers, but also living up to its responsibility of providing measures that will strengthen the security of Nigerian cyber-space. These measures include, but no limited to, applying the international standard for information/internet security and mandating all its ministries, agencies, arms as well as the private sector to abide by the standards, making sure that the jobs of handling the cyber-security are given to a competent and qualified hands as opposed to the current practice of who-knows-you-and-who-do-you-know that favors the mediocre over the merit.\r\n\r\n\r\n \r\nDo you like this article? Never miss my future articles, subscribe to mail list and let them meet at the comfort of your mailbox. 🙂	2019-12-17 07:48:20.761792+00	2019-12-17 07:48:20.762379+00	aminubishir@gmail.com	23	/static/image/CyberSecurity.jpg
Testing Image	I'm just trying to save image!\r\nBut this doesn't show Image	2019-09-06 00:50:43.177534+00	2019-09-06 00:50:43.178013+00	aminubishir@gmail.com	11	\N
\.


--
-- Name: blog_p_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.blog_p_id_seq', 23, true);


--
-- Data for Name: comment; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.comment (p_id, commentor, comment, created, id) FROM stdin;
8	aminubishir@gmail.com	Sannunku da kokari. Gaskiya wannan post ya matukar burgeni!	2019-09-04 06:05:55.323593+00	6
8	aminubishir@gmail.com	Wannan magana hakane. Allah ya saka	2019-09-04 06:46:20.80515+00	7
8	aminubishir@gmail.com	That's really a great post!	2019-09-04 06:46:58.181503+00	8
8	aminubishir@gmail.com	great Job!	2019-09-04 06:48:19.007079+00	9
4	aminubishir@gmail.com	Thank you sadarwa, we greet you too!	2019-09-04 06:48:45.819275+00	10
18	aminubishir@gmail.com	Nice one. And it's with Image! Wow	2019-09-10 05:56:22.552828+00	15
18	aminubishir@gmail.com	That's very awesome!	2019-09-13 16:18:33.817453+00	16
18	aminubishir@gmail.com	Hello there and good day to you. I really like reading this article and I really love it to the core! Just keep it up as we continue to be with now and always!	2019-09-13 16:46:19.953042+00	17
18	a@b.com	What a great post! Gaskiya I really like it. Keep it up!	2019-09-29 15:39:27.991154+00	19
18	aminubishir@gmail.com	It's really saddening to see how people are hating PHP today unjustifiably!	2019-12-14 14:39:43.932327+00	20
21	aminubishir@gmail.com	It's really saddening to see how people are hating PHP today unjustifiably!	2019-12-14 14:40:25.932353+00	22
22	aminubishir@gmail.com	Great Piece!	2019-12-15 09:51:40.753376+00	23
\.


--
-- Name: comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.comment_id_seq', 23, true);


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

