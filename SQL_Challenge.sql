
select UserName, max(individual_streaks) as CONSEC from (
select UserName,  count(*) as individual_streaks from (
select UserName, sum(changed) over (partition by UserName order by date(UserDate)) sum_changed from (
select UserName, UserDate,
  case when lag(date(UserDate)) over (partition by UserName order by UserDate) - date(UserDate) = -1 
    then 0 else 1 end as changed 
from UserTable
)as d) as d2

group by UserName, sum_changed) as d3
group by UserName;