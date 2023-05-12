# amusementpark

## Description:
This project is a culmination of a semester-long class project from the CS-GY6083 
Principles of Database Systems course taught by Professor Amit Patel at New York University. 
It provides a practical implementation of database concepts and principles learned throughout 
the course. As part of this project, a team of three students went through the entire process 
of analyzing business requirements, designing the database systems, and fully implementing it 
into a usable web application. Through this project, the team gained valuable experience in teamwork, 
communication, project management, and technical skills. This repository contains the complete source code 
of the web application, which can be used as a reference or a starting point for future database system projects.

## Django apps included:
* DBFinalProject: this is where all the main config files are at, such as database connections and apps in Django app
* home: it has all the main pages of the web app, handles tempaltes, views, signin/singout, register logics
* visitor: oen to one field to the django user module, it has all the related templates for membership and group, has the visitor model for the database and subtypes for group and member.
* cart: cart has the model for the invoice table, showing all current user's purchase in the UI and have a button for check out
* parking: parking has all the logic and views for parking, including adding a spot and delete all spot. 
* payment: has payment logic, with card form asking for user input
* stores: has dynamic URLs for stores, can be clicked on and choose variety of items and add them to card
* tickets: user can purchase a ticket for the current day, or for the future days, also can delete all tickets that are added to shopping cart
* attractions: has a table of attractions that shows the list of rides etc.
* shows: has a list of shows and can be added to the cart

## Other folders and files
  * models.py: has the whole django design models from django inpectdb command
  * requirements.txt: has all the dependencies needed for running the project
  * /static: has the stylesheet, some image and a base template for all the html templates used

## Run it locally?
  * Git clone the repository to your local machine
  * Open the code on an IDE/text editor, in the terminal (project root level), getting all dependencies type
    > pip install requirements.txt
  * To spin up the server, type
    > python manage.py runserver
  * Then click on the link showing in the terminal to check out the web app locally on your machine

## Future optimizations and acknowledgement
While the project has the most fundamental functionalities, there is still room for improvement in terms of performance. 
As of now, the team has designed the database, implemented the workflow, and added CRUD operations. 
However, further enhancements are needed to optimize the performance metrics. 
To achieve this, the focus can be shifted to improving the code efficiency and implementing additional middleware, such as Redis caching.


