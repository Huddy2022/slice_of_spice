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

## Base.html ##

This is the hub for all my templates in the slice of spice website. In the head of the base.html has all the required documents for the meta tags, font awesome, bootstrap CSS, google fonts used and the link to my static folder. In the body is the navigation, a success alert and the footer which links on to all pages of the website apart from the admin area.

- __Navigation__

  - When you are not loged in there are eight navigation tabs and the slice of spice header which also acts as a link to the home index page.
  - Home, menu, book a table, contact, gallery, sign up, sign in, admin user
  - When loged in there are nine navigation tabs.
  - Home, menu, book a table, contact, gallery, welcome user (doesnt link to any page), reservations, logout, admin user.
  - The navigation i used a bootstrap template and styled it slightly different to suit the website.
  - It's desgined to make it easy for the user to navigate throughout the website
  - I incorporated the sign in and sign up so that users have there own access to any of their bookings but also allows the super user to have identification of anyone booking a table
  - The admin user tab was to allow easy access for the super user to log in and out of the website to control and bookings, cancellations, tables and customers.

![Navigation not signed in]()

![Navigation signed in]()