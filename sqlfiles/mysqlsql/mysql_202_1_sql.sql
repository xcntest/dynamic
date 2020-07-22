select * from wangzq_100lie limit 1000;
select * from wangzq_100lie;
insert into wangzq_100lie select * from wangzq_100lie limit 1000;
select col_120_varchar,col_114_varchar2,col_116_varchar,col_119_varchar2,col_117_number,col_119_varchar2,col_1_varchar
from wangzq_100lie limit 1000;
select col_120_varchar,col_114_varchar2,col_116_varchar,col_119_varchar2,col_117_number,col_119_varchar2,col_1_varchar
from wangzq_100lie where col_2_number > 1;
select col_120_varchar,col_114_varchar2,col_116_varchar,col_119_varchar2,col_117_number,col_119_varchar2,col_1_varchar
from wangzq_100lie where col_2_number > 1
and col_100_varchar is not NULL;
select * from `中文表`;
select * from DataMask_table_mySQl;
select * from mysql_column_longest_MASK;
select * from mysql_column_longest_Mask_NULL;
select * from mysql_column_longest_zerofill_com1;
select * from mysql_column_longest_zerofill_com4;
select * from wangzq_100lie limit 1000;
select col_120_varchar,col_114_varchar2,col_116_varchar,col_119_varchar2,col_117_number,col_119_varchar2,col_1_varchar
from wangzq_100lie limit 1000;
select col_120_varchar,col_114_varchar2,col_116_varchar,col_119_varchar2,col_117_number,col_119_varchar2,col_1_varchar
from wangzq_100lie where col_2_number > 1;
select col_120_varchar,col_114_varchar2,col_116_varchar,col_119_varchar2,col_117_number,col_119_varchar2,col_1_varchar
from wangzq_100lie where col_2_number > 1
and col_100_varchar is not NULL;
select col_120_varchar,col_114_varchar2,col_116_varchar,col_119_varchar2,col_117_number,col_119_varchar2,col_1_varchar
from wangzq_100lie where col_2_number > 1
and col_100_varchar is not NULL order by col_120_varchar;
select col_120_varchar,col_114_varchar2,col_116_varchar,col_119_varchar2,col_117_number,col_119_varchar2,col_1_varchar
from wangzq_100lie where col_2_number > 1
and col_100_varchar is not NULL GROUP BY col_116_varchar order by col_120_varchar;
select col_120_varchar,col_114_varchar2,col_116_varchar,col_119_varchar2,col_117_number,col_119_varchar2,col_1_varchar
from (select * from wangzq_100lie) a
where col_2_number > 1
and col_100_varchar is not NULL GROUP BY col_116_varchar order by col_120_varchar;

select 
col_120_varchar,col_114_varchar2,col_116_varchar,col_119_varchar2,col_117_number,col_119_varchar2,col_1_varchar
from (select * from wangzq_100lie
where col_2_number > 1
and col_100_varchar is not NULL 
GROUP BY col_116_varchar 
order by col_120_varchar
) a
where col_2_number > 1
and col_100_varchar is not NULL 
GROUP BY col_116_varchar 
order by col_120_varchar;

select 
aaa.col_120_varchar,aaa.col_114_varchar2,aaa.col_116_varchar,aaa.col_119_varchar2,aaa.col_117_number,col_119_varchar2,col_1_varchar
from (select * from wangzq_100lie
where col_2_number > 1
and col_100_varchar is not NULL 
GROUP BY col_116_varchar 
order by col_120_varchar
) aaa
where col_2_number > 1
and col_100_varchar is not NULL 
GROUP BY col_116_varchar 
order by col_120_varchar;

select 
aaa.col_120_varchar,aaa.col_114_varchar2,aaa.col_116_varchar,aaa.col_119_varchar2,aaa.col_117_number,col_119_varchar2,col_1_varchar
from (select * from wangzq_100lie bbb
where col_2_number > 1
and col_100_varchar is not NULL 
GROUP BY col_116_varchar 
order by col_120_varchar
) aaa
where col_2_number > 1
and col_100_varchar is not NULL 
GROUP BY col_116_varchar 
order by col_120_varchar;
select distinct col_120_varchar,sum(col_114_varchar2),avg(col_116_varchar),col_119_varchar2,AVG(col_117_number),col_119_varchar2,col_1_varchar
from wangzq_100lie limit 1000;
select col_120_varchar,col_114_varchar2,max(col_116_varchar),col_119_varchar2,count(col_117_number),col_119_varchar2,col_1_varchar
from wangzq_100lie limit 1000;
select col_120_varchar,col_114_varchar2,min(col_116_varchar),col_119_varchar2,min(col_117_number),col_119_varchar2,col_1_varchar
from wangzq_100lie limit 1000;
select col_120_varchar,col_114_varchar2,max(col_116_varchar),col_119_varchar2,max(col_117_number),col_119_varchar2,col_1_varchar
from wangzq_100lie limit 1000;
select col_120_varchar,col_114_varchar2,max(col_116_varchar),col_119_varchar2,max(col_117_number),col_119_varchar2,col_1_varchar
from wangzq_100lie
where col_117_number BETWEEN -10 and 9999;
select col_120_varchar,col_114_varchar2,col_116_varchar,col_119_varchar2,col_117_number,col_119_varchar2,col_1_varchar
from wangzq_100lie
where col_110_varchar is not NULL
GROUP BY col_120_varchar
HAVING col_117_number > -1;
select * from `中文表`;
select * from DataMask_table_mySQl;
select * from mysql_column_longest_MASK;
select * from mysql_column_longest_Mask_NULL;
select * from mysql_column_longest_zerofill_com1;
select * from mysql_column_longest_zerofill_com4;