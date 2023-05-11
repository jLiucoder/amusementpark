# amusementpark

* Django apps included:
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


  
* Other folders and files
  * models.py: has the whole django design models from inpectdb command 
  * requirements.txt: has all the dependencies needed for running the project
  * /static: has the stylesheet, some image and a base template for all the html templates used