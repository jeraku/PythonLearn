--
-- PostgreSQL database dump
--

\restrict ih2MoWHYIeVIDCvMBhyaXMKhNyocfJwYLTRCDBauIb79MIoSupXwffaQhGqMkEn

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
-- Data for Name: appointments; Type: TABLE DATA; Schema: public; Owner: syedjaferk
--

COPY public.appointments (id, patient_id, appointment_date) FROM stdin;
1	1	2025-01-02
2	1	2025-01-10
3	1	2025-01-25
4	2	2025-01-05
5	2	2025-01-20
6	2	2025-02-02
\.


--
-- Data for Name: customers; Type: TABLE DATA; Schema: public; Owner: syedjaferk
--

COPY public.customers (id, customer_name, total_spent) FROM stdin;
1	Arun	5000
2	Bala	7000
3	Chitra	10000
4	Divya	12000
5	Eshan	3000
6	Farah	9000
7	Gokul	20000
8	Hari	15000
\.


--
-- Data for Name: employees; Type: TABLE DATA; Schema: public; Owner: syedjaferk
--

COPY public.employees (emp_id, emp_name, department, salary) FROM stdin;
1	Asha	HR	65000
2	Ravi	HR	64000
3	Meena	HR	64000
4	Karan	IT	80000
5	Priya	IT	78000
6	Suresh	IT	76000
7	Nisha	Finance	70000
8	Rahul	Finance	73000
9	Deepa	Finance	73000
10	Ganesh	Finance	69000
\.


--
-- Data for Name: logins; Type: TABLE DATA; Schema: public; Owner: syedjaferk
--

COPY public.logins (id, user_id, login_date) FROM stdin;
1	U01	2025-01-01
2	U01	2025-01-02
3	U01	2025-01-04
4	U01	2025-01-05
5	U02	2025-01-01
6	U02	2025-01-03
7	U02	2025-01-04
8	U02	2025-01-06
\.


--
-- Data for Name: monthly_sales; Type: TABLE DATA; Schema: public; Owner: syedjaferk
--

COPY public.monthly_sales (id, region, month, sales_amount) FROM stdin;
1	North	2025-01-01	12000
2	North	2025-02-01	15000
3	North	2025-03-01	18000
4	North	2025-04-01	16000
5	South	2025-01-01	10000
6	South	2025-02-01	12000
7	South	2025-03-01	15000
8	South	2025-04-01	17000
\.


--
-- Data for Name: rides; Type: TABLE DATA; Schema: public; Owner: syedjaferk
--

COPY public.rides (id, city, driver_id, total_rides) FROM stdin;
1	Chennai	D01	150
2	Chennai	D02	140
3	Chennai	D03	130
4	Madurai	D11	200
5	Madurai	D12	170
6	Madurai	D13	160
\.


--
-- Data for Name: salesperson; Type: TABLE DATA; Schema: public; Owner: syedjaferk
--

COPY public.salesperson (id, emp_name, total_sales) FROM stdin;
1	Asha	50000
2	Ravi	45000
3	Kumar	40000
4	Nisha	70000
5	Ramesh	55000
6	Divya	60000
7	Suresh	65000
8	Rahul	47000
\.


--
-- Data for Name: stocks; Type: TABLE DATA; Schema: public; Owner: syedjaferk
--

COPY public.stocks (id, company, stock_date, price) FROM stdin;
1	ABC Corp	2025-01-01	100
2	ABC Corp	2025-01-02	110
3	ABC Corp	2025-01-03	105
4	ABC Corp	2025-01-04	115
5	XYZ Ltd	2025-01-01	90
6	XYZ Ltd	2025-01-02	85
7	XYZ Ltd	2025-01-03	88
8	XYZ Ltd	2025-01-04	92
\.


--
-- Data for Name: transactions; Type: TABLE DATA; Schema: public; Owner: syedjaferk
--

COPY public.transactions (txn_id, account_id, txn_date, amount) FROM stdin;
1	1001	2025-01-01	2000
2	1001	2025-01-05	-500
3	1001	2025-01-10	1000
4	1001	2025-01-15	-700
5	1002	2025-01-03	5000
6	1002	2025-01-07	-1000
7	1002	2025-01-14	2000
8	1002	2025-01-20	-1500
\.


--
-- Data for Name: weather; Type: TABLE DATA; Schema: public; Owner: syedjaferk
--

COPY public.weather (id, city, reading_date, temperature) FROM stdin;
1	Chennai	2025-01-01	30
2	Chennai	2025-01-02	32
3	Chennai	2025-01-03	33
4	Chennai	2025-01-04	31
5	Chennai	2025-01-05	29
6	Madurai	2025-01-01	28
7	Madurai	2025-01-02	30
8	Madurai	2025-01-03	31
9	Madurai	2025-01-04	29
\.


--
-- Name: appointments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: syedjaferk
--

SELECT pg_catalog.setval('public.appointments_id_seq', 6, true);


--
-- Name: customers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: syedjaferk
--

SELECT pg_catalog.setval('public.customers_id_seq', 8, true);


--
-- Name: employees_emp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: syedjaferk
--

SELECT pg_catalog.setval('public.employees_emp_id_seq', 10, true);


--
-- Name: logins_id_seq; Type: SEQUENCE SET; Schema: public; Owner: syedjaferk
--

SELECT pg_catalog.setval('public.logins_id_seq', 8, true);


--
-- Name: monthly_sales_id_seq; Type: SEQUENCE SET; Schema: public; Owner: syedjaferk
--

SELECT pg_catalog.setval('public.monthly_sales_id_seq', 8, true);


--
-- Name: rides_id_seq; Type: SEQUENCE SET; Schema: public; Owner: syedjaferk
--

SELECT pg_catalog.setval('public.rides_id_seq', 6, true);


--
-- Name: salesperson_id_seq; Type: SEQUENCE SET; Schema: public; Owner: syedjaferk
--

SELECT pg_catalog.setval('public.salesperson_id_seq', 8, true);


--
-- Name: stocks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: syedjaferk
--

SELECT pg_catalog.setval('public.stocks_id_seq', 8, true);


--
-- Name: transactions_txn_id_seq; Type: SEQUENCE SET; Schema: public; Owner: syedjaferk
--

SELECT pg_catalog.setval('public.transactions_txn_id_seq', 8, true);


--
-- Name: weather_id_seq; Type: SEQUENCE SET; Schema: public; Owner: syedjaferk
--

SELECT pg_catalog.setval('public.weather_id_seq', 9, true);


--
-- PostgreSQL database dump complete
--

\unrestrict ih2MoWHYIeVIDCvMBhyaXMKhNyocfJwYLTRCDBauIb79MIoSupXwffaQhGqMkEn

