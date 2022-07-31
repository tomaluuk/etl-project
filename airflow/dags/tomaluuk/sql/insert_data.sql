delete from population.electoral_district;
delete from population.region;
delete from population.municipality; 
delete from population.municipality_birth_stats; 


insert into population.electoral_district
select distinct
  electoral_district_number,
  electoral_district_name_fi,
  electoral_district_name_se
from sources.municipality_listing
where electoral_district_number is not null;


insert into population.region
select distinct
  region_number,
  region_name_fi,
  region_name_se
from sources.municipality_listing
where region_number is not null;


insert into population.municipality 
select distinct
	municipality_number,
	electoral_district_number,
	region_number,
	municipality_name_fi as name_fi,
	municipality_name_se as name_se,
	municipality_type as type,
	primary_language
from sources.municipality_listing
where municipality_number is not null;


insert into population.municipality_birth_stats
with stats as (
select
	MD5(birth_municipality_number::text || year_of_birth::text || first_name::text) as id,
	birth_municipality_number as municipality_number,
	year_of_birth,
	first_name,
	gender::int::boolean,
	amount
from sources.most_popular_first_names_by_municipality
)
select *
from stats
where id is not null;