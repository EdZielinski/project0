# **Chatterbox**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This project is a single-page online messaging service, using Python (3.7), Jinja2, Flask 'socketio,' HTML5, JavaScript(ES6 standards), Bootstrap (version 4), open source icons
(ionicons.com), popper.js and Cascading Style Shees (CSS3).

# **Functionality, Key components and Design**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This one page application consists of the application.py, index.html, script.js and style.css files.  The application is event driven. Event listeners in the script.js file define the changes to the index.html page. The event drivers below explain the functionality of this application and point out key components. The design choices for this application center on Bootstrap 4's grid, cards, and utilities components.

**Event One - document.addEventlListener(;DOMContentLoaded',()=>{}**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;User visits web application for the first time. The index.html triggers the listening function in the script.js file.  It listens for the Document Object Model (DOM) content to load, and once loaded will trigger 'Event One.'  This event checks the following components to render the proper view for the user:

* Check the local storage to assure that no user 'name' is present
* Check if there is at least one 'channel'

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If the above two components are false then the default index.html view displays the Welcome screen as shown below. The form shown below is within the bootstrap grid container with id = "nameForm"

![IMAGE](images/imageOne_WelcomePage.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note:  Should the user click submit here and not enter a name, the bootstrap model relies on popper.js to pop up a message stating, 'this is a required field.'  Bootstrap 4 depends on JavaScript which uses popper.js.
See https://getbootstrap.com/docs/4.1/getting-started/javascript/

**Event Two=document.querySelector('#nameForm').addEventListener('submit',(event)=>{}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;User types a name in the 'Welcome' screen (#nameForm) and clicks the submit button. The #inputName is stored in local Storage and the functio switchToChannels() is called.  The submit button default event from HTML is prevented from running by using the event.preventDefault() function.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The switchToChannels() function switches the view to channels by changing the following attributes in the HTML document:

* The nameHeading class is changed to 'Hi'+ localStorage.getItem("name)
* The heading class is changed to 'Select channel'
* The id=nameForm view is set to not visible by adding the d-none utility in bootstrap. See reference at bootstrap about utilities https://getbootstrap.com/docs/4.0/migration/#utilities
* The chatrooms class is set to visible by removing the d-none utility in bootstrap
* The channelFormRow is set to visible by removing the d-none utility in bootstrap

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The current_view is now 'channels.' Note that jinja2 displays all channels, and if no channels are stored, then 'general' is the default value as defined in the application.py file. As channels grow in number, bootstraps responsiveness keeps moving the channels down the page.

![IMAGE](images/imageTwo_switchToChannels.png)