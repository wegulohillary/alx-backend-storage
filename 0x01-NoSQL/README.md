
Curriculum <br>
**Short Specializations** <br>

# 0x01. NoSQL advanced

`Back-end` `NoSQL` `MongoDB`

## Resources

**Read or watch:**

* [NoSQL Databases Explained](https://www.riak.com/resources/nosql-databases/)
* [What is NoSQL ?](https://www.youtube.com/watch?v=qUV2j3XBRHc)
* [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xl85Zog8)
* [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
* [Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
* [Introduction to MongoDB and Python](https://www.realpython.com/introduction-to-mongodb-and-python/)
* [mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
* [The mongo Shell](https://www.mongodb.com/docs/)

## Requirement

### MongoDB Command File

* All files interpreted/compiled on Ubuntu 18.04 LTS using `mongoDB` (version 4.2)
* All files must end with a new line
* First line of all files must be commented: `// my comment`
* Mandatory `README.md` file
* File length tested using `wc`

### Python Scripts

* Files intrepreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7) and `PyMongo` (Version 3.10
* Files must end with a new line
* The first line of files should be exactly `#!/usr/bin/env python3`
* Code should use the `pycodestyle` style (Version 2.5.*)
* All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
* Code should not execute when imported (by using `if __name__ == "__main__"`:)
* Mandatory `README.md` file
* Length of files tested using `wc`

## More Info

### Install MongoDB 4.2 in Ubuntu 18.04

[Official installation guide](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/) <br>

```
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-get add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$ sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d2518g4568g52485h02458f014526g
OpenSSL version: OpenSSL 1.1.1 11 sep 2018
allocator: tcmalloc
modules: none
build environment:
      distmod: ubuntu1804
      distarch: x86_64
      target_arch: x86_64
$
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'
```

Potiential issue if documents creation doesn't work or this error: `Data directory /data/db not found., terminating <br>
([source](https://www.bryantson.com/fixing-data-db-not-found-error-in-macos-x-when-starting-mongodb-d7b82abb2479) and [source](https://stackoverflow.com/questions/37702957/mongodb-data-db-not-found)) <br>

```
$ sudo mkdir -p /data/db
```

Or if `/etc/init.d/mongod` is missing, please find here an example file: <br>

<details>
  <summary>Click to expand/hide file contents</summary>

</details>

### Use "container-on-demand" to run MongoDB

* Ask for container `Ubuntu 18.04 - MongoDB`
* Connect via SSH
* Or via the Web Terminal
* In the container, start MongoDB before playing with it:

```
$ service mongod start
* Starting database mongod
$
$ cat 0-list_databases | mongo
Mongo shell version v4.2.8
Connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("70518564-6doofg-48e1-a9a25-053254fgh556") }
MongoDB server version: 4.2.8
admin	0.000GB
config	0.000GB
local	0.000GB
bye
$
```

## Finally...
# NoSQL

The learning objectives of this project are:

- What NoSQL means
- What is difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## 0. List all databases
Write a script that lists all databases in MongoDB.

## 1. Create a database 
Write a script that creates or uses the database `my_db`:

## 2. Insert document
Write a script that inserts a document in the collection `school`:

- The document must have one attribute `name` with value “Holberton school”
- The database name will be passed as option of `mongo` command

## 3. All documents
Write a script that lists all documents in the collection `school`:

- The database name will be passed as option of `mongo` command

## 4. All matches
Write a script that lists all documents with `name="Holberton school"` in the collection `school`:

- The database name will be passed as option of `mongo` command

## 5. Count
Write a script that displays the number of documents in the collection `school`:

- The database name will be passed as option of `mongo` command

## 6. Update
Write a script that adds a new attribute to a document in the collection `school`:

- The script should update only document with `name="Holberton school"` (all of them)
- The update should add the attribute `address` with the value `“972 Mission street”`
- The database name will be passed as option of `mongo` command

## 7. Delete by match 
Write a script that deletes all documents with `name="Holberton school"` in the collection `school`:

- The database name will be passed as option of `mongo` command

## 8. List all documents in Python
Write a Python function that lists all documents in a collection:

- Prototype: `def list_all(mongo_collection):`
- Return an empty list if no document in the collection
- `mongo_collection` will be the `pymongo` collection object

## 9. Insert a document in Python
Write a Python function that inserts a new document in a collection based on kwargs:

- Prototype: `def insert_school(mongo_collection, **kwargs):`
- `mongo_collection` will be the `pymongo` collection object
- Returns the new `_id`

## 10. Change school topics
Write a Python function that changes all topics of a school document based on the name:

- Prototype: `def update_topics(mongo_collection, name, topics):`
- `mongo_collection` will be the `pymongo` collection object
- `name` (string) will be the school name to update
- `topics` (list of strings) will be the list of topics approached in the school

## 11. Where can I learn Python?
Write a Python function that returns the list of school having a specific topic:

- Prototype: `def schools_by_topic(mongo_collection, topic):`
- `mongo_collection` will be the `pymongo` collection object
- `topic` (string) will be topic searched

## 12. Log stats
Write a Python script that provides some stats about Nginx logs stored in MongoDB:

- Database: `logs`
- Collection: `nginx`
- Display (same as the example):
  - first line: `x logs` where x is the number o f documents in this collection
  - second line: `Methods:`
  - 5 lines with the number of documents with the `method = ["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order (see example below - warning: it’s a tabulation before each line)
  - one line with the number of documents with:
    - `method=GET`
    - `path=/status`

You can use this dump as data sample: [dump.zip](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-webstack/411/dump.zip)

## 13. Regex filter
Write a script that lists all documents with `name` starting by `Holberton` in the collection `school`:

- The database name will be passed as option of `mongo` command

## 14. Top students
Write a Python function that returns all students sorted by average score:

- Prototype: `def top_students(mongo_collection):`
- `mongo_collection` will be the `pymongo` collection object
- The top must be ordered
- The average score must be part of each item returns with key = `averageScore`

## 15. Log stats - new version
Improve [12-log_stats.py](./12-log_stats.py) by adding the top 10 of the most present IPs in the collection `nginx` of the database `logs`