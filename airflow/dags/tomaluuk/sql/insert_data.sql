delete from population.electoral_district;
delete from population.region;
delete from population.municipality;
 

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
