create user [smc-jp-whi-interviewer] from external provider;
alter role db_datareader add member [smc-jp-whi-interviewer];
alter role db_datawriter add member [smc-jp-whi-interviewer];

create user [smc-jp-whi-interviewer-dev] from external provider;
alter role db_datareader add member [smc-jp-whi-interviewer-dev];
alter role db_datawriter add member [smc-jp-whi-interviewer-dev];

select *
from Users;

select *
from Messages;
