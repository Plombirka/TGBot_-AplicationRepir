PGDMP  )                     |            postgres    16.0    16.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    5    postgres    DATABASE     |   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE postgres;
                postgres    false            �           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    4850            �            1259    17513    stud    TABLE     �   CREATE TABLE public.stud (
    id character varying NOT NULL,
    fio character varying,
    frame character varying,
    room character varying
);
    DROP TABLE public.stud;
       public         heap    postgres    false            �          0    17513    stud 
   TABLE DATA           4   COPY public.stud (id, fio, frame, room) FROM stdin;
    public          postgres    false    216          \           2606    17519    stud stud_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY public.stud
    ADD CONSTRAINT stud_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.stud DROP CONSTRAINT stud_pkey;
       public            postgres    false    216            �   �   x�}�=�0Fg�9R��i8bb�3BE�����TZ5gx�N�3Y�����`\�L�,ǅ��mt�Z�o"��J`�v/^+��E4<��a*\r2�u��s�#�Tr��y �p�4u�;f��JwU�a�p�     