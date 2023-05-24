# CG NETWORK

## Installation from requirements:
`pip install -r requirement.txt`

## Run server:
`python manage.py runserver`

## Run livereload:
`python manage.py livereload`

## Migrations:
`python manage.py makemigrations` > create migrations files
`python manage.py migrate` > apply migrations in db

## Load json fixtures in db:
`python manage.py loaddata .\CgNetwork\fixtures\user_data.json`


## Postgres commands:
`CREATE DATABASE nom_db;
DROP DATABASE nom_db;
CREATE TABLE nom_table (colonne1 type, colonne2 type, ...);
ALTER TABLE nom_table ADD COLUMN nom_colonne type;
ALTER TABLE nom_table DROP COLUMN nom_colonne;
INSERT INTO nom_table (colonne1, colonne2, ...) VALUES (valeur1, valeur2, ...);
UPDATE nom_table SET colonne1 = valeur1, colonne2 = valeur2, ... WHERE condition;
DELETE FROM nom_table WHERE condition;
SELECT colonne1, colonne2, ... FROM nom_table WHERE condition;
CREATE USER nom_utilisateur WITH PASSWORD 'mot_de_passe';
ALTER USER nom_utilisateur WITH PASSWORD 'mot_de_passe';
GRANT droit1, droit2, ... ON nom_table TO nom_utilisateur;
REVOKE droit1, droit2, ... ON nom_table FROM nom_utilisateur;
DROP USER nom_utilisateur;`

## Cheat sheet:
`\dt : affiche la liste de toutes les tables de la base de données actuelle.
\c <database> : se connecter a la db
\du : list users
\dt+ : affiche la liste de toutes les tables de la base de données actuelle, avec des informations supplémentaires telles que le propriétaire de la table, la taille de la table, etc.
\z nom_table; : voir les privileges user lies a une table. 
\q : quitte la console PostgreSQL.`

 
## Postgres security setup:
`SECURITY settings in POSTGRES
alter role cguser set client_encoding to 'utf8';
alter role cguser set default_transaction_isolation to 'read committed';
grant all privileges on database cg_network to cguser;`


## SQL DB_SETUP USER
`CREATE USER cguser WITH ENCRYPTED PASSWORD '0203';
ALTER ROLE cguser SET client_encoding TO 'utf8';
ALTER ROLE cguser SET edfault_transaction_isolation TO 'read committed';
GRANT ALL PRIVILEGES ON DATABASE cg_network TO cguser;
GRANT ALL PRIVILEGES ON SCHEMA public TO cguser;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO cguser;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO cguser;`
