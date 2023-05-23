# Slice of Spice #

The Live link can be found here - https://8000-huddy2022-sliceofspice-724f0pui3mj.ws-eu97.gitpod.io/home

Slice of Spice website offers a restaurant booking system for the Slice of Spice restaurant and provides the user with navigation such as home/about us, menu, gallery, contact, and a user authentication for sign in/log in (and when logged in a sign out and a reservations page for that user is displayed in the navigation). The site is targeted for any user to explore the restaurant and understand if its somewhere they would like to go an eat. If so they have the opportunity to book a table with this restaurant but only if they sign up to become a member (which allows the super user to have details of the customer but also allows the user to have their own reservations page which they can browse and check which bookings they have, plus if a user's wishes to they can either cancel or edit one of their current reservations.).

![Responsive Mockup](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/Responsive.png)

## Tools ##

- Django
- Bootstrap - 5.3
- Cloudinary
- Allauth and its user model
- Django-The message Framework
- Django - Q object
- Python import timezone
- datetime and timedelta class

## Base ##

This is the hub for all my templates in the slice of spice website. In the head of the base.html has all the required documents for the meta tags, font awesome, bootstrap CSS, google fonts used and the link to my static folder. In the body is the navigation, a success alert and the footer which links on to all pages of the website apart from the admin area.

- __Navigation__

  - When you are not logged in there are eight navigation tabs and the slice of spice header which also acts as a link to the home index page.
  - Home, menu, book a table, contact, gallery, sign up, sign in, admin user.
  - When logged in there are nine navigation tabs.
  - Home, menu, book a table, contact, gallery, welcome user (doesn’t link to any page, but references the user), reservations, logout, admin user.
  - The navigation I used a bootstrap template and styled it slightly different to suit the website.
  - It's designed to make it easy for the user to navigate throughout the website.
  - I incorporated the sign in and sign up so that users have their own access to any of their bookings but also allows the super user to have identification of anyone booking a table.
  - The admin user tab was to allow easy access for the super user to log in and out of the website to control any bookings, cancellations, tables and customers.

![Navigation not signed in](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/Navigation_not_signed_in.png)

![Navigation signed in](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/Navigation_signed_in.png)

- __Alert__

  - The success alert is useful to help the user understand if they were successful or unsuccessful on a certain task.
  - Whether they signed in / signed up.
  - If they have successfully booked a table.
  - If that table is already booked for a specific date or time.
  - If they have successfully cancelled a booking.
  - If they have successfully edited one of their bookings.

![Success alert](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/success_alert.png)

- __Footer__

  - The footer has three compartments to it, about, contact and follow us.
  - About - is another useful navigation tool for the user but only for the home page, menu page and book a table page.
  - Contact - is for the user to contact the website if they have any queries (the contact tab on navigation links to this footer contact section).
  - Follow us - Allows the user to follow us on social media sites such as Facebook and Instagram. 

![Footer](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/footer.png)

## Home ##

- The index.html is the home page for the slice of spice website with two main compartments the home image and the about us section.

- __home image__

   - Main image for the website which is an image of the restaurant and a table to give the impression of your about to sit down at a restaurant. 

![Home image](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/home_image.png)

- __About us__

   - In this section there is an about us description and another image.
   - The about us description I used an upper and a lower heading for better aesthetics and a short paragraph about how it all began.
   - The image compliments the about us section so it doesn’t look to boring.

![About us](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/about_us.png)

## Menu ##

- The menu is a page that offers the user to browse through the restaurants food and drinks options and their prices.
- Top centre is the heading and a sub heading.
- To the left (desktop size) is the food menu.
- Centre (desktop size) is the image of fire to give the impression it’s a spicy restaurant.
- To the right (desktop size) is the drinks menu.
- When in mobile size each column stacks on top of each other.

![Menu](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/menu.png)

## Book a table ##

- The book a table page has two parts the main image and the reservations form

- __image__

   - The main image is a menu to give the impression you are about to order

![Book a table image](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/book_a_table_image.png)

- __Reservation form__

    - I used a bootstrap form to help me template .
    - In the form there are seven inputs which include, name, email, phone, date, time, select a table and message.
    - Each input is required apart from message as this helps the user understand they need to fill the whole form to book a table and the super user gets all the information needed from the customer.
    - The name field needs to be at least three characters long or will come up with an alert.
    - The email address needs to be valid otherwise an alert comes up
    - The phone number needs to be an integer and at least 11 digits long
    - The date field allows the user to select a date, with the format of dd/mm/yyyy.
    - The time field allows the user to select a time, with the format of hour/minutes - the user can only select times between 12pm and 10pm and it’s only every 15 minutes, otherwise an alert comes up to tell the user to select between or on specific times.
    - select a table - allows the user to select from a list of ten tables four of which have a capacity of 2 and the rest have a capacity of 4 - this is a required field also. A for loop is used to loop through the tables model and show all ten tables that was created by the super user.
    - Lastly there is a message box if the user wishes to send a message to the restaurant but this is not a required field.
    - The submit button is only visible is the user is authenticated/logged in otherwise the alert is shown at the bottom (I used an if statement for this)

![Reservation form when signed in](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/Reservation_form_when_signed_in.png)

  - __Functionality__

      - The user can only book a table when have signed in otherwise the submit button is disabled.
      - All alerts come up on the input fields if the user hasn’t correctly filled out the form
      - Once a user selects the book a table tab on navigation this function creates all tables to be available (so that they are shown on the form)
      - The reservations view functions gets all the data from the form using the post method in an if statement
          - It first checks if the date is valid and not in the past, otherwise an alert comes up to the user saying it must be a valid date in the future.
          - Afterwards is creates / updates a customer record using the Customer model
          - Then it checks if there is a current reservation for that specific date, time and table. If there is then an alert comes up to let the user know, so we don’t get any double bookings.
          - Once checked and all fine a reservation is made and saved with all the data for the table Id, customer, table, date and time. Then a success message is shown to the user as it sends the user back to home page.
      - There is another function relating to this form which is the delete_expired_bookings function, where if a user selects to go on this page or the reservations page it will check this function first and will automatically delete any out of date bookings on the system.

![Alert when double booking](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/alert_double_booking.png)

- __Message/alert__

- At the bottom of the form there is a message and potentially an alert
- The message is for the user to know if there is more than four guests coming they would need to contact the restaurant so the restaurant can organise the tables accordingly.
- The alert is shown to remind the user that they need to either sign up or log in to book a table at the restaurant and there are two buttons which link to either the sign up or log in pages for easy access for the user.

![Message / alert when not signed in](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/Message_alert_when_not_signed_in.png)

## Contact ##

- The contact navigation tab is linked to the contact details shown on the footer, so whenever a user selects this tab it will take them to the bottom of any page showing the contact details for the restaurant.

## Gallery ##

- The gallery page shows the user multiple images of the restaurant, customers and staff to give the overall impression of the slice of spice.

![Gallery](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/gallery.png)

## Sign up / Login ##

- The sign up and login in tabs have been created using Django’s Allauth 
- I have styled both the sign up, log in and sign out pages to link to the base.html and the style used with this restaurant website.
- Authorisation is needed to book a table in this restaurant - which helps the manager/super user to manage all bookings, cancellations, customers and tables.
- Once signed in there is a welcome alert message but also a nice Welcome {user} tab in the navigation which makes it more personal for the user when logged in.
- Also, when signed in any user will have a reservations tab in the navigation, so they can see what bookings if any they have.
- I have put ACCOUNT_EMAIL_VERIFICATION = 'none' so that login and registration should work without errors regardless of whether you use an email address to sign in/up. Instead we can get the email of a user when they book a table.

![Sign up](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/sign_up.png)

![Login](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/sign_in.png)

![Sign out](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/sign_out.png)

## Reservations ##

- I created a reservations tab in the navigation to allow users to see any of their bookings but also to cancel/edit any of their own bookings.
 
  - __Reservations__
      - This tab only shows when a user is logged in using the booked_table function in the views.
      - On this page it shows the users table number, date booked and time booked
      - There’s a cancel booking button for each of the bookings booked which redirects you to the cancel_booking page.
      - There's also an edit booking button for each of the bookings booked which redirects you to the edit_booking page.
      - If you don’t have any bookings yet there will be a message of this page saying that to you.

![Reservations](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/reservations.png)

  - __Cancel booking__
      
      - This cancel booking page is linked to the reservations page and can only be accessed when a user selects the cancel booking button for one of their bookings.
      - On this page I have created a card that displays a header, a sub text, a cancel booking button and a cancel button(if the user changes their mind).
      - Once a user selects the cancel booking button the cancel_booking function in my views retrieves the specific booking id and using the post method will delete that specific booking and redirect you back to the home page with a success message is then shown to the user saying your cancellation has been successful.
      - Alternatively, if the user changes their mind and cancels the request with the cancel button it will redirect the user back to the reservations page.

![Cancel booking](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/cancel_booking.png)

  - __Edit booking__
      
      - This edit booking page is linked to the reservations page and can only be accessed when a user selects the edit booking button for one of their bookings.
      - On this page I have re created a very similar form to that of the book_a_table.html, with a new header.
      - However, if a user creates a new booking it will update the original booking that was linked to reservation page using its specific ID, through the edit_booking function.
      - Once the user submits the new booking it will redirect the user back to the home page with a success message saying Congratulations you have edited your booking!.
      - In the function I have put the current booking_id as excluded as some users might get paranoid about changing a booking and might just want to re book for the same date/time/table, rather than feel they might have lost it after clicking the edit booking button.
      - Alternatively, if the user changes their mind and cancels the request with the cancel button it will redirect the user back to the reservations page.

![Edit booking](https://github.com/Huddy2022/slice_of_spice/blob/main/assets/images/edit_booking.png)

## Admin user ##

- As I have created a super user to basically be the manager of this website/restaurant, I thought it would be easier to have an accessibility to the administration by having a admin user link in the navigation. It only allows staff members to log in on this particular area.

   - __Models__

      - I created three models for this website, customer, booking and table.
        
        - __Customer__
           
           - This model stores the user, email and phone.
           - The user has a one to one relationship and uses the Django’s built in user model.

        - __Booking__
          
           - This model stores the customer, table, booking date and booking time.
           - The customer has a foreign key relating to the Customer model.
           - The table has a foreign key relating to the Table model.
           - I used a class meta to create a unique together of all the tuples of table, booking_date and booking_time.
           - An admin user can edit any booking or delete

        - __Table__

           - This model stores the table number, capacity of the table and the tables availability.
           - The capacity has a for loop which allows positive integers to be stored in the database with choices of values between 1-4.

## Testing ##

- __Testing__

| Tested | Functionality | Result | Responsiveness | 
|:------------:|:---------------:|:---------:|:----------:|
| Slice of spice heading | Renders index home page | yes renders home page when clicked | works well on tablet and mobile |
| Home nav | Renders index home page | yes renders home page when clicked | works well on tablet and mobile |
| Menu nav | Renders menu page | yes renders menu page when clicked | works well on tablet and mobile |
| Book a table nav | Renders book a table page | yes renders book a table page when clicked | works well on tablet and mobile |
| Contact Nav | Redirects to contact in footer | yes redirects to contact area in footer when clicked | works well on tablet and mobile |
| Gallery nav | Renders gallery page | yes renders gallery page when clicked | works well on tablet and mobile |
| Sign up nav | Renders sign up page | yes renders sign up page when clicked | works well on tablet and mobile |
| log in nav | Renders login page | yes renders login page when clicked | works well on tablet and mobile |
| Admin user nav | Renders Django admin page | yes renders Django’s admin page when clicked | works well on tablet and mobile |
| Welcome {user} nav | Doesn’t link to anywhere | yes doesn’t render any page or error when logged in and clicked | works well on tablet and mobile |
| Reservations nav | Renders reservations page | yes renders reservations page when logged in and clicked | works well on tablet and mobile fits relatively well but user needs to slide left and right to see edit booking button and nav bar |
| Cancel booking page | Renders cancel booking page | yes renders cancel booking page when user clicks cancel booking button | works well on tablet and mobile |
| Edit booking page | Renders edit booking page | yes renders edit booking page when user clicks edit booking button | works well on tablet and mobile |
| Logout nav | Renders logout page | yes renders logout page when logged in and clicked | works well on tablet and mobile |
| Past booking | Checks specific date/time is in the past | yes alert comes up if user tries to book a table for a past date/time | works well on tablet and mobile |
| Double booking | Checks specific date/time/table is already booked| yes alert comes up if user tries to book the same table for same date/time | works well on tablet and mobile |
| Successful booking | Allows user to book a table | yes once signed in and no double booking or past date a successful alert comes up for user | works well on tablet and mobile |
| Not logged in booking | Doesn’t allow user to book a table | yes if not signed in submit button is disabled | works well on tablet and mobile |
| Booking reservation | Shows users table number, date and time of reservation | yes on reservation page, table number, date and time booked are showing | works well on tablet and mobile |
| Cancel booking successful | Allow user to cancel a specific booking | yes buttons work to allow a user to cancel a specific booking | works well on tablet and mobile |
| Delete expired bookings | Deletes any out of date booking | yes deletes any out of date booking | n/a |

- I created two tests in the booking app
- test_models.py to test all three of the models were working correctly
- test_views.py to test all the functions in my views.py were working correctly
- I changed the database back to SQLite and ran the tests and I can confirm all tests ran ok

## Validator Testing ##

- __HTML__

   - I originally had four errors when I put it through the validator.
   - I can confirm now, no errors were returned when passing through the official w3c validator.

- __CSS__

   - I can confirm no errors were returned when passing through the official w3c validator.

- __Python__
   
   - I used the CI Python Linter to check my code and I can confirm all clear and no errors were found.

- __Accessibility__

   - I confirmed the colours and fonts are easy to read and I tested the colours I have chosen through the web aim contrast checker.
   - I used the lighthouse in dev tools to test my web page on a desktop and mobile devices.

## Bugs ##

- Initially I tried an approach similar to the I think I therefore blog and the hello Django projects for my models but found they were not the right fit for the booking system
- I tried multiple different models but as I was trying different methods I have multiple problems, especially if I migrated various times. I had to reset the database most times to rectify this.
- Main bugs I had with the models was trying get them to connect properly using the right foreign keys and if they were a one to one field etc.
- rendering the cancel booking view I initially had errors with but I found a way to return the booking_id as an integer to get around the error and rendered properly.
- My reservations functions I struggled with quite a bit and had various different errors coming up through the process.
  - Firstly get method didn’t always return what was needed and I needed to update my models accordingly to get the right return.
  - It took me while to understand I needed to create/update a user - I made it work when I linked this up to the Customer model
  - Double booking was difficult and I got multiple errors when I tried to understand if I could take out the booked table on the form or not. Eventually settled for an alert and filtered through the Booking models objects to check if a booking for a specific table number, date and time had already been done. I did have to update the Booking model to include a meta class to create the unique together. Then used a nested if statement in the reservations to check for previous reservations and then alerted the user.
  - The booking wasn’t always being created in the models and I had to create and save a reservation each time it was being posted
  - When I created all ten tables with the super user in the tables model, I had a bug where once a table had been booked it was taken out of the reservation form. I created an available is always true to stop this from happening. 
  - The hardest part of this function was working with dates and times and I took me a while to understand which to use but I added from django.utils import timezone
from datetime import timedelta, datetime to make everything work in this function.
- I wanted a user to be logged in to book a table and see any of their previous reservations - I got past the initial bugs by adding a @login_required decorator.
  - I also used a try and except to get the users booking details - I struggled at first but amended the models to add a related_name to associate them with.
- The cancel booking function was similar to the reservations, where I had to find the users booking and then in the if statement save the cancellation before passing it to the cancellation model. The booking I used get_object_or_404 to retrieve the booking object or if not there raise and error.
- The delete expired bookings is difficult to work with the timezone now - I had to filter through to get all the bookings and I had to use a Q class to be more complex by adding the dates and times together to make sure it’s out of date.
- To get the delete_expired_bookings to work I had to add the function in two other functions otherwise it would get called.
- Re visiting the code I had an error with the UX navigation broken link when deployed which was a result of using the wrong URL for the admin page. I have corrected this now and created a new url path that will allow any user to click on the admin link without it breaking.
- Another bug was I didn't use CRUD properly, where the user can create, read any booking but only had the option to cancel a booking or put a message to the super user if they wished to edit/cancel a booking. Now I have removed the cancellation model as was unnecessary and changed the function for the cancel booking, so a user can cancel their own booking without an approval from the super user. Also, I have created an edit booking where the user can if they wish edit one of their own bookings by creating a new reservation which will overwrite the old one. These two amendments should allow for a complete CRUD.

## Un fixed bugs ##

- I'm not sure if this is an un fixed bug but regarding the delete_expired_bookings function it does delete any expired bookings from the database when the date and time has passed. However as we have had daylight savings recently its saying my server is 1 hour ahead so the booking won’t be deleted until an hour later than my time. I didn’t want to change the settings.py timezone as I felt might jeopardise the whole websites functions.

## Commented code left in ##

- I know you need to take out commented code you’re not using but there are two I left in as per the reasons below.
- I left in the code for the database SQLite as I needed this when I did my testing on the test_models.py and the test_views.py. I thought this might be needed later on.
- I also left in the password validation commented out code, as in the think I therefore blog it was also left in.

## Deployment ##

- created a Heroku app - sliceofspice.
- created a new instance from elephantSQL.
- I created an env.py file to hide to the secret key, database URL and the Cloudinary URL.
- Linked the env.py file to my settings.py.
- In the settings of the Heroku app I added the database_url, cloudinary_url, secret_keyand PORT 8000.
- For deployment I set debug to False.
- Removed the DISABLE_COLLECTSTATIC 1
- Deployed branch to main in Heroku 

The live link can be found here - https://8000-huddy2022-sliceofspice-724f0pui3mj.ws-eu97.gitpod.io/home

## Credits ##

### Content ###

- This website gave me a rough understanding of how I wanted to template my website and the drinks for my menu https://www.theslanteddoor.co.uk/
- This website helped me with my menu as in the food https://www.godine.co.uk/dalyan-nottingham/menu
- The icons used were taken from font awesome https://fontawesome.com.
- The think before I blog project helped me with my initial models but mainly with the Allauth authentication.
- The hello Django project helped me with my test_views and my test_models.
- These two websites gave me a good understanding of types of models to use, the type of views to create and the basic form to use https://github.com/anujsaxena9127/restaurant / https://github.com/NDevox/django_restaurant_manager.
- This video helped me with my models https://www.youtube.com/watch?v=TuXFAl8aMvc
- This website also helped me understand the type of models and views to use https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78.
