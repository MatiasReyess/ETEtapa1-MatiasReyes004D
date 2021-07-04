# ETEtapa1-MatiasReyes004D

url: http://127.0.0.1:8000


http://127.0.0.1:8000/admin
Usuario: admin
Contraseña : zawarudo


--Para las migraciones y usuarios en sql usese este codigo para que funcione correctamente esto en sqlDeveloper 18c
alter session set "_ORACLE_SCRIPT"=true;
create user examen##PT1 identified by 1234 default tablespace users temporary tablespace temp;
grant connect, resource, create view to examen##PT1;
alter user examen##PT1 quota unlimited on users;
commit;

