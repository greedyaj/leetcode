select Name, Marks
from Student s
where s.Marks % 2 == 0
order by Name ASC

select c.CITY_NAME, SUM(r.REVENUE)
from CITIES c, REVENUE r
where c.CITY_CODE = r.CITY_CODE