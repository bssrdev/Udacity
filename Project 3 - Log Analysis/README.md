# Logs Analysis Project
In this project we are giving a summary from logs by sql database queries.

### Softwares used:
- Python3
- Vagrant
- VirtualBox

### Commands

Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`

To load the data, use the command `psql -d news -f newsdata.sql` to connect a database and run the necessary SQL statements.

The database includes three tables:
- Authors table
- Articles table
- Log table

To execute the program, run `python3 newsdata.py` from the command line.

## Views used
#### statustotal
````sql
CREATE VIEW statustotal AS
SELECT time ::date,
       status
FROM log;
````
#### statusfailed
````sql
CREATE VIEW statusfailed AS
SELECT time,
       count(*) AS num
FROM statustotal
WHERE status = '404 NOT FOUND'
GROUP BY time;
````
#### statusall
````sql
CREATE VIEW statusall
SELECT time,
       count(*) AS num
FROM statustotal
WHERE status = '404 NOT FOUND'
  OR status = '200 OK'
GROUP BY time;
````
#### percentagecount
````sql
CREATE VIEW percentagecount AS
SELECT statusall.time,
       statusall.num AS numall,
       statusfailed.num AS numfailed,
       statusfailed.num::double precision/statusall.num::double precision * 100 AS percentagefailed
FROM statusall,
     statusfailed
WHERE statusall.time = statusfailed.time;
````