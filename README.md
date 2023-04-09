# Slice of Spice #

The Live link can be found here - https://8000-huddy2022-sliceofspice-724f0pui3mj.ws-eu93.gitpod.io/

Slice of Spice website offers a restaurant booking system for the Sice of Spice resturant and provides the user with navigation such as home/about us, menu, gallery, contact, and a user authentification for sign in/log in (and when loged in a signout and a reservations page for that user is displayed in the navigation). The site is targetted for any user to explore the restaurant and understand if its somewhere they would like to go an eat. If so they have the opporutnity to book a table with this restaurant but only if they sign up to become a member (which allows the super user to have details of the customer but also allows the user to have their own reservations page for any of their own bookings).

![Responsive Mockup]()

## Tools ##

- Django
- Bootstrap - 5.3
- Cloudinary
- Allauth and its user model
- Django-The message Framework
- Django - Q object
- Python import timezone
- timedelta class

## Base ##

This is the hub for all my templates in the slice of spice website. In the head of the base.html has all the required documents for the meta tags, font awesome, bootstrap CSS, google fonts used and the link to my static folder. In the body is the navigation, a success alert and the footer which links on to all pages of the website apart from the admin area.

- __Navigation__

  - When you are not loged in there are eight navigation tabs and the slice of spice header which also acts as a link to the home index page.
  - Home, menu, book a table, contact, gallery, sign up, sign in, admin user.
  - When loged in there are nine navigation tabs.
  - Home, menu, book a table, contact, gallery, welcome user (doesnt link to any page), reservations, logout, admin user.
  - The navigation i used a bootstrap template and styled it slightly different to suit the website.
  - It's desgined to make it easy for the user to navigate throughout the website.
  - I incorporated the sign in and sign up so that users have there own access to any of their bookings but also allows the super user to have identification of anyone booking a table.
  - The admin user tab was to allow easy access for the super user to log in and out of the website to control and bookings, cancellations, tables and customers.

![Navigation not signed in]()

![Navigation signed in]()

- __Alert__

  - The success alert is useful to help the user understand if they were successful or unsuccessful on a certain task.
  - Wether they signed in / signed up.
  - If they have successfully booked a table.
  - If that table is already booked for a specific date or time.
  - If they have succesfully sent a cancellation request to the super user.
  - To warn the user if they have already sent a canellation request for that booking.

![Success alert]()

- __Footer__

  - The footer has three compartments to it, about, contact and follow us.
  - About - is another useful navigation tool for the user but only for the home page, menu page and book a table page.
  - Contact - is for the user to contact the website if they have any quieries (the contact tab on navigation links to this footer contact section).
  - Follow us - Allows the user to follow us on social media sites such as facebook and instagram. 

![Footer]()

## Home ##

- The index.html is the home page for the slice of spice website with two main compartments the home image and the about us section.

- __home image__

   - Main image for the website which is an image of the restuarant and a table to give the impression of your about to sit down at a restuarnt. 

![Home image]()

- __About us__

   - In this section there is an about us description and another image.
   - The about us description i used an upper and a lower heading for better asthetics and a short paragraph about how it all began.
   - The image compliments the the about us section so it doesnt look to boring.

![About us]()

## Menu ##

- The menu is a page that offers the user to browse through the resturants food and drinks options and their prices.
- Top center is the heading and a sub heading.
- To the left (desktop size) is the food menu.
- Centre (desktop size) is the image of fire to give the impression its a spicy restuarant.
- To the right (desktop size) is the drinks menu.
- When in mobile size each column stacks on top of each other.

![Menu]()

## Book a table ##

- The book a table page has two parts the main image and the reservations form

- __image__

   - The main image is a menu to give the impression you are about to order

![Book a table image]()

- __Reservation form__

    - I used a bootstrap form to help me template .
    - In the form there are seven inputs which include, name, email, phone, date, time, select a table and message.
    - Each input is required apart from message as this helps the user understand they need to fill the whole form to book a table and the super user gets all the information needed from the customer.
    - The name field needs to be at least three characters long or will come up with an alert.
    - The email address needs to be valid otherwise an alert comes up
    - The phone number needs to be an integer and at least 11 digits long
    - The date field allows the user to select a date, with the format of dd/mm/yyyy
    - The time field allows the user to select a time, with the format of hour/minutes - the user can only select times between 12pm and 10pm and its only every 15 minutes, otherwise an alert comes up to tell the user to select between or on specific times.
    - select a table - allows the user to select from a list of ten tables four of which have a capacity of 2 and the rest have a capacity of 4 - this is a required field also. A for loop is used to loop through the tables model and show all ten tables that was created by the super user.
    - Lastly there is a message box if the user wishs to send a message to the restaurant but this is not a required field.
    - The submit button is only visable is the user is authenticated/loged in otherwise the alert is shown at the bottom (i used an if statement for this)

![Reservation form when signed in]()

  - __Functionality__

      - The user can only book a table when have signed in otherwise the submit button is disabled.
      - All alerts come up on the input fields if the user hasnt correclty filled out the form
      - Once a user selects the book a table tab on navigation this function creates all tables to be available (so that they are shown on the form)
      - The reservations view functions gets all the data from the form using the post method in an if statement
          - It first checks if the date is valid and not in the past, otherwise an alert comes up to the user saying it must be a valid date in the future.
          - Afterwards is creates / updates a customer record using the Customer model
          - Then it checks if there is a current reservation for that specific date, time and table. If there is then an alet comes up to let the user know, so we dont get any double bookings.
          - Once checked and all fine a reservation is made and saved with all the data for the table Id, customer, table, date and time. Then a success message is shown to the user as it sends the user back to home page.
      - There is another function relating to this form which is the delete_expired_bookings function, where if a user selects to go on this page or the reservations page it will check this function first and will automatically delete any out of date bookings on the system.
          

- __Message/alert__

- At the bottom of the form there is a message and potentially an alert
- The message is for the user to know if there is more than four guests coming they would need to contact the restaurant so the restaurant can organise the tables accordingly.
- The alert is shown to remind the user that they need to either sign up or log in to book a table at the restaurant and there are two buttons which link to either the sign up or log in pages for easy access for the user.

![Message / alert when not signed in]()

## Contact ##

- The contact navigation tab is linked to the contact details shown on the footer, so whenever a user selects this tab it will take them to the bottom of any page showing the contact details for the restaurant.

## Gallery ##

- The gallery page shows the user multiple images of the restaurant, customers and staff to give the overall impression of the slice of spice.

![Gallery]()

## Sign up / Login ##

- The sign up and login in tabs have been created using djagnos allauth 
- I have styled both the sign up, log in and sign out pages to link to the base.html and the style used with this resturant website.
- Authorisation is needed to book a table in this restaurant - which helps the manager/super user to manage all bookings, cancellations, customers and tables.
- Once signed in there is a welcome alert message but also a nice Welcome {user} tab in the navigation which makes it more personal for the user when loged in.
- Also, when signed in any user will have a reservations tab in the navigation, so they can see what bookings if any they have.

![Sign up]()

![Log in]()

![Log out]()

## Reservations ##

- I created a reservations tab in the navigation to allow users to see any of their bookings but also to cancel any of their bookings.
 
  - __Reservations__
      - This tab only shows when a user is logged in using the booked_table function in the views.
      - On this page it shows the users table number, date booked and time booked
      - Theres a cancel booking button for each of the bookings booked which redirects you to the cancel_booking page.
      - If you dont have any bookings yet there will be a message of this page saying that to you.
      - If a user has selected to cancel a booking it would be sent to the super user to authorise and until the super user has approved this there will be an awaiting approval message for the user on that selected booking and the cancel booking will be disabled, so the user cannot keep sending cancellations for that booking.

  - __Cancel booking__
      
      - This cancel booking page is linked to the reservations page and can only be accessed when a user selects the cancel booking button for one of their bookings.
      - On this page i have created a card that displays a header, a sub text, a message box for the user to explain why this wish to cancel the booking or if they want to amend anything to their booking and a submit cancellation button. There is also a cancel button if the user changes their mind.
      - Once a user selects the cancel booking button i use the cancel_booking function in my views to retrieve the specific booking id, and using the post method i get the message from the user and create a cancellation using the Cancellation model for the user and message. A success message is then sent to the user when it renders them back to the home page saying your cancellation request has been submitted.
      - I have put in a double safe method on this cancellation if a user who has already submitted a cancellation for this specific booking and somehow gets onto the cancellation page again it will come up with an alert stating to the user they have already submitted a request and its awaiting approval. 
      - Using the cancellation model, once a user has submitted a cancellation request it is sent to the super user to check and has the authority to approve the cancellation, or if a message is received to amend a booking the super user has authority to amend the booking in the booking model and cancel the cancellation request instead.

