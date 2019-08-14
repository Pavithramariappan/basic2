-SELECT * FROM demo;
--create table consultation11(pid int(10),fees int(1000),health varchar(10),consult_date date);
--insert into consultation11 VALUES(576,1000,'fever',date());
--select pid,fees,health,consult_date from consultation11;
--select date()
create table sample1(available_time char(4) check (available_time in ('mor','noon','eve')));
--insert into sample VALUES('mor');
--insert into sample values('noon');
--insert into sample values('eve');
--select * from sample;


