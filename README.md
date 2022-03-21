# Database Containerization
---
#### Data Engineering Tools: 
- Docker to create images of the following:
  - MySQL (relational database)
  - MongoDB (document-oriented database)
  - Redis (key-value database)
  - Cassandra (distributed scalable database)
  - Firebase (serverless cloud database)
- Perform CRUD (CREATE, READ, UPDATE, and DELETE) operations

#### Overview:
- Create Containers for 
  - MySQL
  ```
  docker run -p 3300:3306 --name final_assignment -e MYSQL_ROOT_PASSWORD=MyNewPass -d mysql', 'mysql'
  ```
  - MongoDB
  ```
  docker run -p 27017:27017 --name some_mongo -d mongo', 'mongo'
  ```
  - Redis
  ```
  docker run -p 6379:6379 --name final_assignment_part3 -d redis', 'redis'
  ```
  - Cassandra
  ```
  docker run -p 9042:9042 --name cassandra -d cassandra', 'cassandra'
  ```
##### Part 2:
- In VS Code, navigate to Part 2 of the folder, which contains the starter file for this part of the assignment. Run the command to initialize the driver. 
- Open the `create.py` file and modify it to create a database with your choice of title. This database should contain at least three entries.
- In a Terminal window, run the correct commands to insert your data in the database you created so that you can visualize your data correctly in the Terminal window.
##### Part 3:
- In VS Code, navigate to Part 3 of the folder containing the starter file for this part of the assignment.
- Open the write.py file from the folder. 
  - Use the Redis method, mset, to create a dictionary, r, with keys equal to “Milk” and “Bread” and corresponding values equal to “Lactose” and “Gluten”. 
- Run the write.py file in your Terminal window to show that your syntax does not contain any errors. 
- Open the read.py file from the folder you downloaded. Use the Redis method, get, to read all values in r.
- Run the read.py file in your Terminal window to show that your code prints the dictionary values correctly.
##### Part 4:
- In your browser, navigate to [Firebase](https://firebase.google.com/) and create a new project called “Assignment-Module12”. 
- In Firebase, obtain permissions to write from Python to your database. Download your own private key and copy it into the serviceAccountKey.json file in VS Code. 
- Create an empty Realtime database for your project in Firebase.
- Open the fire.py file in VS Code. Update the databaseURL field with the URL you copied.
- Edit the fire.py file to update the two entries in your database.
- In a Terminal window, run the correct command to write to your database in Firebase.
