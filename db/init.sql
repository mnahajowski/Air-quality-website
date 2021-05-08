SELECT 'CREATE DATABASE air_data'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'air_data')\gexec
GRANT ALL PRIVILEGES ON DATABASE air_data TO docker;

\connect air_data

CREATE TABLE IF NOT EXISTS stations (
    id_station int,
    date date,
    name varchar(255),
    lat double precision,
    lon double precision,
    PRIMARY KEY (id_station, date)
);

CREATE TABLE IF NOT EXISTS pollution (
    id Serial PRIMARY KEY,
    id_station int,

    measurement_date date,
    measurement_time time,
    no2 real,
    o3 real,
    pm25 real,
    so2 real,
    pm10 real,
    co real,
    c6h6 real
);
