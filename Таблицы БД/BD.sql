--
-- PostgreSQL database cluster dump
--

-- Started on 2024-03-01 00:19:49 MSK

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:LONvLuh1Muds9mijTivsKA==$QkFBxZz78xLRYt7MdGHVqCTtMp1iUwvhvvlDvBNp/Wo=:HEhi4iNWOBngUWWr4M9lLKNImKNHCKTKAcni4k4qWD0=';

--
-- User Configurations
--








--
-- Databases
--

--
-- Database "template1" dump
--

\connect template1

--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Ubuntu 16.2-1.pgdg22.04+1)
-- Dumped by pg_dump version 16.2 (Ubuntu 16.2-1.pgdg22.04+1)

-- Started on 2024-03-01 00:19:49 MSK

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

-- Completed on 2024-03-01 00:19:49 MSK

--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

\connect postgres

--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Ubuntu 16.2-1.pgdg22.04+1)
-- Dumped by pg_dump version 16.2 (Ubuntu 16.2-1.pgdg22.04+1)

-- Started on 2024-03-01 00:19:49 MSK

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16388)
-- Name: Applications; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Applications" (
    id integer NOT NULL,
    "Name" character varying NOT NULL,
    "Korpus" integer NOT NULL,
    "Room" integer NOT NULL,
    "WorkRabotnika" character varying NOT NULL,
    "Opisanie" character varying NOT NULL,
    "NameMasters" character varying NOT NULL,
    "Status" character varying NOT NULL
);


ALTER TABLE public."Applications" OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16416)
-- Name: Masters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Masters" (
    number_tg numeric NOT NULL,
    "Name" character varying NOT NULL,
    "Korpus" integer NOT NULL,
    "Work" character varying NOT NULL
);


ALTER TABLE public."Masters" OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16404)
-- Name: Room; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Room" (
    "Korpus" integer NOT NULL,
    "Room" integer NOT NULL
);


ALTER TABLE public."Room" OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16423)
-- Name: Students; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Students" (
    number_tg numeric NOT NULL,
    name integer NOT NULL,
    korpus integer NOT NULL,
    room integer NOT NULL
);


ALTER TABLE public."Students" OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16397)
-- Name: Students_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Students_info" (
    id integer NOT NULL,
    "Name" character varying NOT NULL,
    "Group" character varying NOT NULL
);


ALTER TABLE public."Students_info" OWNER TO postgres;

--
-- TOC entry 3398 (class 0 OID 16388)
-- Dependencies: 215
-- Data for Name: Applications; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Applications" (id, "Name", "Korpus", "Room", "WorkRabotnika", "Opisanie", "NameMasters", "Status") FROM stdin;
\.


--
-- TOC entry 3401 (class 0 OID 16416)
-- Dependencies: 218
-- Data for Name: Masters; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Masters" (number_tg, "Name", "Korpus", "Work") FROM stdin;
\.


--
-- TOC entry 3400 (class 0 OID 16404)
-- Dependencies: 217
-- Data for Name: Room; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Room" ("Korpus", "Room") FROM stdin;
\.


--
-- TOC entry 3402 (class 0 OID 16423)
-- Dependencies: 219
-- Data for Name: Students; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Students" (number_tg, name, korpus, room) FROM stdin;
\.


--
-- TOC entry 3399 (class 0 OID 16397)
-- Dependencies: 216
-- Data for Name: Students_info; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Students_info" (id, "Name", "Group") FROM stdin;
\.


--
-- TOC entry 3248 (class 2606 OID 16422)
-- Name: Masters Masters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Masters"
    ADD CONSTRAINT "Masters_pkey" PRIMARY KEY (number_tg);


--
-- TOC entry 3238 (class 2606 OID 16460)
-- Name: Applications NameStud; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Applications"
    ADD CONSTRAINT "NameStud" UNIQUE ("Name");


--
-- TOC entry 3244 (class 2606 OID 16408)
-- Name: Room Room_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Room"
    ADD CONSTRAINT "Room_pkey" PRIMARY KEY ("Korpus");


--
-- TOC entry 3242 (class 2606 OID 16403)
-- Name: Students_info Students_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Students_info"
    ADD CONSTRAINT "Students_pkey" PRIMARY KEY (id);


--
-- TOC entry 3250 (class 2606 OID 16429)
-- Name: Students Students_pkey1; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Students"
    ADD CONSTRAINT "Students_pkey1" PRIMARY KEY (number_tg);


--
-- TOC entry 3240 (class 2606 OID 16392)
-- Name: Applications gthfg_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Applications"
    ADD CONSTRAINT gthfg_pkey PRIMARY KEY (id);


--
-- TOC entry 3246 (class 2606 OID 16446)
-- Name: Room lf; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Room"
    ADD CONSTRAINT lf UNIQUE ("Room");


--
-- TOC entry 3252 (class 2606 OID 16435)
-- Name: Students korpus; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Students"
    ADD CONSTRAINT korpus FOREIGN KEY (korpus) REFERENCES public."Room"("Korpus") ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- TOC entry 3251 (class 2606 OID 16452)
-- Name: Masters korpus; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Masters"
    ADD CONSTRAINT korpus FOREIGN KEY ("Korpus") REFERENCES public."Room"("Korpus") ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- TOC entry 3253 (class 2606 OID 16440)
-- Name: Students name; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Students"
    ADD CONSTRAINT name FOREIGN KEY (name) REFERENCES public."Students_info"(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- TOC entry 3254 (class 2606 OID 16447)
-- Name: Students room; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Students"
    ADD CONSTRAINT room FOREIGN KEY (room) REFERENCES public."Room"("Room") ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


-- Completed on 2024-03-01 00:19:49 MSK

--
-- PostgreSQL database dump complete
--

-- Completed on 2024-03-01 00:19:49 MSK

--
-- PostgreSQL database cluster dump complete
--

