# CSCI S-33a: Project Proposal
## Due: Friday, July 27 at 6pm

#### Your name

Edward Zielinski

#### Your teaching fellow's name

Rodrigo Daboin Sanchez

#### Which language(s) will you use for your project?

English

#### What will (likely) be the title of your project?

Charlie’s Coffee and Sandwich Shop

#### In just a sentence or two, summarize your project. (e.g. "A website that lets you check the weather in different cities.")

A website to provide real-time communication of inventory control for a small food vendor located within the city of Boston’s MBTA subway system.  The website will use the MBTA's API for schedules, arrival predictions, and service alerts because the vendor delivers the inventory on the subway.

#### Where will your project ultimately live? (e.g. within CS50 IDE, Heroku, AWS, some commerical web host...)

Heroku

#### In a paragraph or more, detail your project. What will it do? What features will it have?

**Summary:**
	Charlie has an amazing sandwich shop that serves meals from 5am to 6pm. Charlie must keep his inventory storage and shop rental costs low, so he strategically located six vendor carts around the city of Boston’s subway system.  He has a kitchen and warehouse located at one location.  Each cart can hold only 50 sandwiches and 10 lbs. of coffee.  Sales at each location range from 30 to 100 sandwiches a day and 20 lbs. of coffee per day.

**Problem:**
	Charlie must use the subway system to deliver inventory to the vendor carts located around the city.  The vendor must know whether his inventory will arrive on time; otherwise, they have to close down, or be able to manage the customer expectations of when the sandwich or coffee will arrive.

**Requirements for solution:**
* Create a communication system between the vendor carts and warehouse to monitor inventory.
* It will have a username and login page
* Listing the location of the vendor station
* Python, JavaScript, JSON, and Socket.IO will drive the application.  Heroku will manage the logins and communications.
* Implementation of Bootstrap 4’s mobile responsiveness allows the vendor carts to use their smart phones to communicate.
* The vendor’s have a simple interface that communicates the total number of meals to the warehouse
* When the inventory of coffee or sandwiches falls below a certain level an order is created at the warehouse for both Coffee and Sandwich to bring them back up to the highest inventory level
* The subway system has an API for schedules, arrival predictions, and service alerts.  The use of this API is key to the communication system.  A message displays to the vendor cart about arrival time.  A countdown animation displays on the vendor’s phone to track arrival time.  The countdown clock adjusts depending on the real-time location of the train that contains the inventory.
* The API information is located at https://www.mbta.com/developers/v3-api and will take advantage of at least one of the following:

1. When a vehicle is predicted to be at a stop
2. The predicted schedule for one route
3. The predicted schedule for a whole trip
4. When a vehicle is scheduled to be at a stop
5. The schedule for one route
6. When a route is open
7. Query for the first and last stops on the route.
8. The schedule for a whole trip





<hr>

- In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

#### In a sentence or list, define a GOOD outcome for your project. What WILL you accomplish no matter what?

* Username and login for Vendors
* Messaging system to chat back and forth to trigger an inventory delivery
* Count-down clock for arrival of inventory
* Communication between at least one vendor and the warehouse.  Determining multiple vendors time from warehouse may be difficult

#### In a sentence or list, define a BETTER outcome for your project. What do you THINK you will accomplish in time?

* An automatic alert system tied into the Point of Sale operation at the vendor cart
* A database to control the inventory and ordering at the warehouse to suppliers
* A scaled up version to sell this to other vendors working in different metropolitan subway systems through-out the world, therefore in different languages
* A translator API to effectively communicate to different nationalities throughout a metropolitan area
* An interactive map that will update the location of inventory in a graphical way

The above items in this section are a wish list.  Realistically I believe on these three items will get accomplished in-time:
1.	Username and login for Vendors
2.	Messaging system to chat back and forth to trigger an inventory delivery
3.	Count-down clock for arrival of inventory


#### In a sentence or list, define a BEST outcome for your project. What do you HOPE you will accomplish in time?

* Username and login for Vendors
* Messaging system to chat back and forth to trigger an inventory delivery
* Count-down clock for arrival of inventory
* Determine multiple routes and times from warehouse to different vendor locations.  Realistically, it may be difficult to determine routes for varying locations.


#### In a paragraph or more, outline your next steps. What new skills do you need to acquire? What topics will you need to research?

* Study the API information located at https://www.mbta.com/developers/v3-api and assess feasibility of reaching goal
