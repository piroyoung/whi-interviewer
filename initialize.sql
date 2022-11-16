create user [smc-jp-whi-interviewer] from external provider;
alter role db_datareader add member [smc-jp-whi-interviewer];
alter role db_datawriter add member [smc-jp-whi-interviewer];
