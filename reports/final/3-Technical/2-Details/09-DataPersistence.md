### Data Persistence {#sec-3-2-9-1}

There are many different ways to achieve data persistence in a system, each with their own 
advantages. The data is to be stored on the system hub, which is located on the Raspberry Pi. As 
previously mentioned, the ability to preserve relationships in the data being stored is critical to 
the success of our system. This functionallity, along the hardware constraints of the Raspberry Pi, 
were the driving factors in deciding which data persistence option was best suited for this project.
The options that were considered were flat files, a server based Structured Query Language (SQL), 
NoSQL, and SQLite.

The main advantage to using flat files is that they are quick to set up, and do not take much 
processing power. However, a flat file has no concept of relations between the information being 
stored. The level of complexity in the data that is being stored makes being able to represent 
relationships in the data paramount.  

SQL is a common solution for storing relational data, and has many different concrete 
implementations. Two examples of such implementations are PostgreSQL and MySQL. A common feature of
SQL implementations is that they are server based databases. This requires that a separate process 
is running to support a dedicated server for the database. All requests to the database require a 
connection to this database server. As mentioned above, the database is being run on a Raspberry Pi,
meaning there are a limited amount of computational resources available. 

NoSQL is an alternative option to server based SQL. General advantages of NoSQL are that it can be
fast, flexible, and has the ability to scale. This has made it a popular choice for situations where
there is big data movement or response time is critical. However, the less rigid nature of NoSQL can 
present a higher level of complexity, which complicates the database design. The benifits of a NoSQL
database are not relevant to this project, and the added complexity makes NoSQL unnecessary and 
undesirable in this situation. This leads to the last option, which is SQLite.

SQLite is a file-based database, which does not require a separate process to run a database server.
SQLite instead allows the system to write to a file directly, while still maintaining the relational
structure offered by SQL. This is the ideal choice for our system, as it fulfills the need for 
relational data without overburdening the constraints set by our limited hardware.

