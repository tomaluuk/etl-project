delete from population.electoral_district;

insert into population.electoral_district
select distinct
  electoral_district_number,
  electoral_district_name_fi,
  electoral_district_name_se
from sources.municipality_listing
where electoral_district_number is not null;

