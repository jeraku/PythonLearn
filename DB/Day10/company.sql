--
-- PostgreSQL database dump
--

\restrict aqn0q2AN1WsSu8ZXRDb6NskoLA3xrhRrXlWr73PqHXNlewzVvCXQMFuTnnFBsvH

-- Dumped from database version 17.7 (Ubuntu 17.7-3.pgdg22.04+1)
-- Dumped by pg_dump version 17.7 (Ubuntu 17.7-3.pgdg22.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: departments; Type: TABLE DATA; Schema: public; Owner: syedjaferk
--

COPY public.departments (dept_id, dept_name) FROM stdin;
1	Engineering
2	HR
3	Sales
\.


--
-- Data for Name: employees; Type: TABLE DATA; Schema: public; Owner: syedjaferk
--

COPY public.employees (emp_id, emp_name, salary, dept_id) FROM stdin;
1	Alice	80000	1
2	Bob	60000	1
3	Charlie	50000	2
4	David	70000	3
5	Eva	90000	1
\.


--
-- Data for Name: projects; Type: TABLE DATA; Schema: public; Owner: syedjaferk
--

COPY public.projects (project_id, project_name, budget, dept_id) FROM stdin;
1	Project A	100000	1
2	Project B	50000	2
3	Project C	75000	3
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: syedjaferk
--

COPY public.users (id, name, email, age, salary, is_active, role, metadata, created_at) FROM stdin;
\.


--
-- Name: departments_dept_id_seq; Type: SEQUENCE SET; Schema: public; Owner: syedjaferk
--

SELECT pg_catalog.setval('public.departments_dept_id_seq', 3, true);


--
-- Name: employees_emp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: syedjaferk
--

SELECT pg_catalog.setval('public.employees_emp_id_seq', 5, true);


--
-- Name: projects_project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: syedjaferk
--

SELECT pg_catalog.setval('public.projects_project_id_seq', 3, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: syedjaferk
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

\unrestrict aqn0q2AN1WsSu8ZXRDb6NskoLA3xrhRrXlWr73PqHXNlewzVvCXQMFuTnnFBsvH

