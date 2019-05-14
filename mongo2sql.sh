#!/bin/bash

#Connect and export JSON file to CSV
printf "\nConnect to mongo\n-\n"

mongoexport --host "localhost" --db "project" --collection "Article" --type="csv" --out "./Json/Article.csv" --fields article_id,article_name,pg_no,year_published,volume_id,magazine_name,fname,lname

printf "\nSuccessfully converted a project collection to csv file\n-\n"

printf "Please enter the mysql username : "
read -s mysql_username

mysql -u $mysql_username -p -h 127.0.0.1 --local-infile project

set global local_infile="ON"

use project

load data local infile "./Json/Article.csv" into table master fields terminated by ',' linesterminated by '\n' IGNORE 1 LINES;

printf "\n master fields inserted successfully \n"
