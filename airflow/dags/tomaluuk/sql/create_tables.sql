CREATE TABLE IF NOT EXISTS population.electoral_district
(
    electoral_district_number integer NOT NULL,
    name_fi character varying(255),
    name_se character varying(255),
    PRIMARY KEY (electoral_district_number)
);

CREATE TABLE IF NOT EXISTS population.region
(
    region_number integer NOT NULL,
    name_fi character varying(255),
    name_se character varying(255),
    PRIMARY KEY ("number")
);

CREATE TABLE IF NOT EXISTS population.municipality
(
    municipality_number integer NOT NULL,
    electoral_district_number integer NOT NULL,
    region_number integer NOT NULL,
    name_fi character varying(255),
    name_se character varying(255),
    type character varying(255),
    primary_language character varying(255),
    PRIMARY KEY (municipality_number)
    FOREIGN KEY (electoral_district_number)
        REFERENCES population.electoral_district(electoral_district_number)
    FOREIGN KEY (region_number)
        REFERENCES population.region(region_number)
);


CREATE TABLE IF NOT EXISTS population.birth_name_stats
(
    birth_name_stats_id integer NOT NULL,
    municipality_number integer NOT NULL,
    gender boolean,
    first_name character varying(255),
    amount integer,
    PRIMARY KEY (birth_name_stats_id),
    FOREIGN KEY (municipality_number)
        REFERENCES population.municipality(municipality_number)
);