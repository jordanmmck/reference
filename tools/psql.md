# PSQL

```psql
CREATE DATABASE riskshark;
CREATE USER riskshark_user WITH PASSWORD 'riskshark_password';
ALTER ROLE riskshark_user SET client_encoding TO 'utf8';
ALTER ROLE riskshark_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE riskshark_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE riskshark TO riskshark_user;
```

```psql
SELECT * FROM data_exchange;
SELECT name FROM data_company;
DELETE FROM data_company WHERE symbol<>'AE';
select count(*) from data_company;
```

```psql
delete from data_filingsection;
```