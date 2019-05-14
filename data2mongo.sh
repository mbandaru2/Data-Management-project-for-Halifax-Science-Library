#!/bin/bash
printf "Please enter the mysql username : "
read -s mysql_username

mysql -u $mysql_username -p < "./SQL query/new_tables.sql"
printf "\n Tables inserted successfully \n"


filename="./Json/Article.json"
python cleanJson.py

printf "\nJson created\n-\n"

#Connect and Import JSON file to mongo
printf "\nConnect to mongo\n-\n"
printf "\nsuccessfully connected to mongo\n-\n"

library = "$1"
user = "$2"
pass = "$3"
coll = "Article"

#mongoimport -d "$library" -u "$user" -p "$pass" -c "$coll" --file "./$filename"
mongoimport -d "project" -c "$coll" --file "./$filename" --jsonArray

printf "\nJson successfully imported to Mongo\n-\n"

echo "bye"
