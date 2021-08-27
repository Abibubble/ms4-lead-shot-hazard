# Testing Steps

## Contents

* [Icon Key](#icon-key)
* [Manual Testing](#manual-testing)
    * [Devices and Browsers](#devices-and-browsers)
    * [Testing Technologies](#testing-technologies)
    * [Testing User Stories](#testing-user-stories)
        * [Business Goals](#business-goals)
        * [First Time User Goals](#first-time-user-goals)
        * [Returning User Goals](#returning-user-goals)
        * [Admin Goals](#admin-goals)
* [Links and Navigation](#links-and-navigation)
    * [Navigation Bar](#navigation-bar)
    * [Modals](#modals)
    * [External Links](#external-links)
* [Styling and Layout](#styling-and-layout)
* [User Access](#user-access)
* [Functions](#functions)
    * [Register](#register)
    * [Log In](#log-in)
    * [Log Out](#log-out)
    * [Add Products](#add-products)
    * [Edit Products](#edit-products)
    * [Delete Products](#delete-products)
    * [Search Products](#search-products)
    * [Messages](#messages)
    * [Stripe](#stripe)
    * [Pagination](#pagination)
    * [404](#404)
    * [Validation](#validation)
* [Database](#database)
* [Accessibility](#accessibility)
    * [Tap Targets](#tap-targets)
    * [Color Contrast](#color-contrast)
    * [Visually-Impaired Users](#visually-impaired-users)
    * [Assistive Technologies](#assistive-technologies)
    * [Reading Level](#reading-level)
* [Responsive Design](#responsive-design)
    * [Mobile](#mobile)
    * [Tablet](#tablet)
    * [Computer](#computer)
* [Images](#images)
    * [Desktop and Laptop](#desktop-and-laptop)
    * [Tablet](#tablet)
    * [Mobile](#mobile)

---

## Icon key

&#128272; <-- Superuser only access

&#128100; <-- Logged In Only

&#128683; <-- Logged Out only

[Back to the top](#testing)

---

## Manual Testing
### Devices and Browsers
#### Desktop / Laptop
1. Google Chrome
    * All tested and working correctly.

2. Microsoft Edge
    * All tested and working correctly.

3. Mozilla Firefox
    * All tested and working correctly.

4. Safari
    * All tested and working correctly.

#### Tablet
1. Safari
    * All tested and working correctly.

#### Mobile
1. Google Chrome
    * All tested and working correctly.

2. Safari
    * All tested and working correctly.

3. Samsung Internet
    * All tested and working correctly.

#### Full devices and browsers
* The website was tested on Google Chrome, Mozilla Firefox, Microsoft Edge, Safari and Samsung Internet browsers.
* Testing was not done on Internet Explorer due to it being depreciated in favour of Microsoft Edge.
* The website was viewed on a variety of devices, including:
    * Custom built desktop PC, running Windows 10
    * Acer Aspire V Nitro Laptop, running Windows 10
    * Lenovo B51 IntelCore i7 Laptop, running Ubuntu 16.04 LTS
    * MacBook Air7,2 (13-inch, 2017)
    * MacBook Pro (15-inch, 2017), running macOS Catalina
    * iPad 6,11 5th generation, running iOS 10.3
    * iPhone 7
    * iPhone X
    * iPhone 12
    * OPPO Find X2 Lite
    * OPPO Find X2
    * Samsung Galaxy A70
    * Samsung Galaxy S9
    * Samsung A20
    * xBox One

A large amount of testing was done to ensure that all pages were displayed, and all functionality worked as it should. Friends, family members, and other developers were asked to review the site and documentation to point out any bugs and/or user experience issues that they came across.

[Back to the top](#testing)

---

### Testing technologies
* HTML was validated using [W3C HTML Markup Validator](https://validator.w3.org/).
* CSS was validated using [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/).
* JavaScript was validated using [JSHint](https://jshint.com/).
* Python was validated using [PEP8 Online](http://pep8online.com/) and [Flake8](https://flake8.pycqa.org/en/latest/).
* Accessibility was checked via [WebAim's W.A.V.E](https://wave.webaim.org/), [WebAIM's Contrast Checker](https://webaim.org/resources/contrastchecker/), and [Google Chrome's Lighthouse](https://developers.google.com/web/tools/lighthouse).
* [Toptal Color Blind Filter](https://www.toptal.com/designers/colorfilter/) was used to check that the site was suitable for color blind users, as well as manually testing it with my color blind partner.
* Unit Testing was done using [Django’s testing tools](https://docs.djangoproject.com/en/3.2/topics/testing/).

1. W3C HTML Markup Validator
    * [Homepage](LINK)
    * Unfortunately, as it's not possible to log in using the Validator, it was only possible to test the pages available to a user who isn't logged in.

2. W3C CSS Validator
    * [Homepage](LINK)
    * Unfortunately, as it's not possible to log in using the Validator, it was only possible to test the pages available to a user who isn't logged in.

3. JSHint
    * [JSHint](https://jshint.com/)
    * EXPLANATIONS

![Image of JSHint results](static/docs/img/jshint.png)

4. PEP8 Online
    * [PEP8 Online](http://pep8online.com/)

![Image of PEP8 Online results](static/docs/img/pep8.png)

### Testing User Stories
#### Business Goals
##### Sell merchandise and music.
* This site provides a secure method for the band to earn money from their merchandise sales.

##### Match the design and personality of the band.
* The color scheme has been directly taken from the band's artwork.

##### Offer a website that is easy to navigate and free of confusion.
* Every page has the full navigation bar across the top of the page.
* For long pages, there is a 'Back to top' button to help the user easily get back to the top.

##### Become another source of revenue for the band.
* Currently the band is only able to sell merchandise at gigs, or via their Bandcamp page.
* This site provides a dedicated site to sell all merchandise.
* This can be linked to from all social media platforms, to allow easy online sales.
* This means that the band can be earning money from merchandise sales whilst not actively gigging.

##### Become a platform where fans can follow the future gigs of the band.
* All future gigs will be updated onto the site.
* This will be collated on the 'Gigs' page.


#### First Time Visitor Goals
##### Easily navigate the site.
* Every page has the full navigation bar across the top of the page.
* For long pages, there is a 'Back to top' button to help the user easily get back to the top.

##### Intuitively and easily understand what to do.
* Everything is clearly laid out.
* All buttons describe what they're for in simple terms.
* Icons are used to help convey meaning.

##### Create an account for future purchases.
* The user can navigate to the Register page via the navigation bar, which is visible on every page.
* The registration process is clearly decribed, and all instructions are clear.
* It only requires a username, an email address, a password, and a confirmation of that password to register an account.
* The user then needs to verify their email address to gain full access to their account.

##### Search for a specific product and it's information.
* There is a search bar on the products pages, so the user can search by product name, description
* There is also the option in the navigation bar to search by category.

##### Browse through all merch.
* The user can scroll through all available merch via a link in the navigation bar.

##### Buy products online as a guest.
* Registration to the site is not required to make a purchase.

##### Get visual feedback when an action on the site is completed.
* When any action is completed, a message will appear to inform the user of the action.
* A full list of actions and messages can be found below in [Messages](#messages).

##### Receive a confirmation email with all relevant information.
* Once an order has been paid for successfully, an email will be sent out with order details.

##### Contact the band through the website.
* A contact page is available via the navigation bar.
* Users can fill in the form to send a message to the band.

##### View full product information.
* A user can click on any product to view the full product information.

##### Add or remove items from the shopping bag.
* Products can be added to the shopping bag via any product details page.
* Products can be removed from the shopping bag via the Shopping Bag page.

##### Add multiple items to the shopping bag.
* Multiples of the same item can be added to the shopping bag by updating the quantity field.
* This can be done on the product details page, or on the shopping bag page.

##### Receive an update of the shopping bag when the user performs an action.
* When any action is completed, a message will appear to inform the user of the action.
* This message will include a summary of the user's shopping bag.
* A full list of actions and messages can be found below in [Messages](#messages).

##### Purchase products securely through Stripe.
* How


#### Returning Visitor Goals
##### Log in / out.
* The Log In and Log Out button is visible in the navigation bar.
* The Log In and Log Out process is intuitive and simple to use.
* If the user is logged out, the Log In button will show.
* If the user is logged in, the Log Out button will show.

##### Be confident that the user's password is be stored securely.
* Werkzeug's password hashing methods have been used to store all user's passwords in a secure and safe way.

##### Navigate intuitively, with no need to use the browser's back button.
* The navigation bar is constantly visible across the top of the site.
* This is either the full navigation bar, or the condensed burger icon menu bar on smaller screen sizes.

##### Create, update or delete the user's personal information.
* Once a user has created an account, they can store their name, phone number, email address and address details for faster checkout in the future.

##### See a history of the user's previous purchases.
* All previous purchases of an account are listed on the user's profile under 'Order History'.


#### Admin Goals
##### Be confident that a user can't to brute force their way into the restricted pages.
* The superuser is set through Django, so there can only be one.
* If a logged out user tried to access a restricted page, it directs them to the log in page.
* If a logged in user without access rights tries to access a restricted page, it redirects them to the homepage, and presents them with a message informing them of this.

##### Edit any product.
* Only the superuser can edit an existing product.
* This can be done on any product details page.

##### Delete any product.
* Only the superuser can delete an existing product.
* This can be done on any product details page.

##### Add a new product.
* Only the superuser can add a new product.
* This can be done on the Manage Products page.

##### Create a stock of products to be sold online and keep track of the sales as a superuser.
* How

[Back to the top](#testing)

---

## Links and Navigation
On every device and browser listed above, I tested the following:

### Navigation Bar
#### Logo
* Click the Logo to take the user to the Home page from the Home page.
* Click the Logo to take the user to the Home page from the Product Details page.
* Click the Logo to take the user to the Home page from the Shopping Bag page.
* Click the Logo to take the user to the Home page from the Checkout page.
* Click the Logo to take the user to the Home page from the Order Success page.
* &#128100; Click the Logo to take the user to the Home page from the Profile page.
* &#128272; Click the Logo to take the user to the Home page from the Manage Products page.
* &#128683; Click the Logo to take the user to the Home page from the Log In page.
* &#128683; Click the Logo to take the user to the Home page from the Register page.

#### Home
* Click the Home button to take the user to the Home page from the Home page.
* Click the Home button to take the user to the Home page from the Product Details page.
* Click the Home button to take the user to the Home page from the Shopping Bag page.
* Click the Home button to take the user to the Home page from the Checkout page.
* Click the Home button to take the user to the Home page from the Order Success page.
* &#128100; Click the Home button to take the user to the Home page from the Profile page.
* &#128272; Click the Home button to take the user to the Home page from the Manage Products page.
* &#128683; Click the Home button to take the user to the Home page from the Log In page.
* &#128683; Click the Home button to take the user to the Home page from the Register page.

#### Profile
* &#128100; Click the Profile button to take the user to the Profile page from the Home page.
* &#128100; Click the Profile button to take the user to the Profile page from the Product Details page.
* &#128100; Click the Profile button to take the user to the Profile page from the Shopping Bag page.
* &#128100; Click the Profile button to take the user to the Profile page from the Checkout page.
* &#128100; Click the Profile button to take the user to the Profile page from the Order Success page.
* &#128100; Click the Profile button to take the user to the Profile page from the Profile page.
* &#128272; Click the Profile button to take the user to the Profile page from the Manage Products page.

#### Manage Products
* &#128272; Click the Manage Products button to take the user to the Manage Products page from the Home page.
* &#128272; Click the Manage Products button to take the user to the Manage Products page from the Product Details page.
* &#128272; Click the Manage Products button to take the user to the Manage Products page from the Shopping Bag page.
* &#128272; Click the Manage Products button to take the user to the Manage Products page from the Checkout page.
* &#128272; Click the Manage Products button to take the user to the Manage Products page from the Order Success page.
* &#128272; Click the Manage Products button to take the user to the Manage Products page from the Profile page.
* &#128272; Click the Manage Products button to take the user to the Manage Products page from the Manage Products page.

#### Add / Edit / Delete Product
* &#128272; Click the Add button to take the user to the Add page from the Manage Products page.
* &#128272; Click the Edit button to take the user to the Edit page from the Manage Products page.
* &#128272; Click the Delete button to open the Delete modal from the Manage Products page.

#### Log Out
* &#128100; Click the Log Out button to log the user out and take them to the Log In page from the Home page.
* &#128100; Click the Log Out button to log the user out and take them to the Log In page from the Product Details page.
* &#128100; Click the Log Out button to log the user out and take them to the Log In page from the Shopping Bag page.
* &#128100; Click the Log Out button to log the user out and take them to the Log In page from the Checkout page.
* &#128100; Click the Log Out button to log the user out and take them to the Log In page from the Order Success page.
* &#128100; Click the Log Out button to log the user out and take them to the Log In page from the Profile page.
* &#128272; Click the Log Out button to log the user out and take them to the Log In page from the Manage Products page.

#### Log In
* &#128683; Click the Log In button to take the user to the Log In page from the Home page.
* &#128683; Click the Log In button to take the user to the Log In page from the Log In page.
* &#128683; Click the Log In button to take the user to the Log In page from the Register page.
* &#128683; Click the Log In button to take the user to the Log In page from the Product Details page.
* &#128683; Click the Log In button to take the user to the Log In page from the Shopping Bag page.
* &#128683; Click the Log In button to take the user to the Log In page from the Checkout page.
* &#128683; Click the Log In button to take the user to the Log In page from the Order Success page.

#### Register
* &#128683; Click the Register button to take the user to the Register page from the Home page.
* &#128683; Click the Register button to take the user to the Register page from the Log In page.
* &#128683; Click the Register button to take the user to the Register page from the Register page.
* &#128683; Click the Register button to take the user to the Register page from the Product Details page.
* &#128683; Click the Register button to take the user to the Register page from the Shopping Bag page.
* &#128683; Click the Register button to take the user to the Register page from the Checkout page.
* &#128683; Click the Register button to take the user to the Register page from the Order Success page.

[Back to the top](#testing)

---

## Modals
* &#128272; The Delete modal is visible in front of all other items on the screen, and clearly displays the Cancel and Delete buttons.

[Back to the top](#testing)

---

## External Links
* The Facebook social media icon opens up the Lead Shot Hazard Facebook page in a new tab.
* The Bandcamp social media icon opens up the Lead Shot Hazard Bandcamp page in a new tab.
* The Instagram social media icon opens up the Lead Shot Hazard Instagram page in a new tab.
* The Twitter social media icon opens up the Lead Shot Hazard Twitter page in a new tab.
* The YouTube social media icon opens up the Lead Shot Hazard YouTube page in a new tab.
* The Spotify social media icon opens up the Lead Shot Hazard Spotify page in a new tab.
* The TikTok social media icon opens up the Lead Shot Hazard TikTok page in a new tab.
* The Soundcloud social media icon opens up the Lead Shot Hazard Soundcloud page in a new tab.

[Back to the top](#testing)

---

## Styling and Layout
* Ensure all images load correctly.
* Ensure all grid layouts size correctly on all screen sizes.
* Ensure all modals appear in front of all other content on the screen.

[Back to the top](#testing)

---

## User Access
### Logged Out Users
* &#128683;
* Navigation bar will show Logo, Home, Log In, Register.

### Logged In Users
* &#128100;
* Navigation bar will show Logo, Home, Profile, Log Out.

### Admin Users
* &#128272;
* Navigation bar will show Logo, Home, Profile, Manage Products, Log Out.

[Back to the top](#testing)

---

## Functions
### Register
* &#128683;
* Creates a new user account.
* Confirm password field is checked against password field to ensure no typos are made.
* If the username already exists, it informs the user and clears the form.
* If the passwords don't match, the user is informed via a toast message.

### Log In
* &#128683;
* Logs the user into their existing account.
* Checks their password entry against the hashed password stored in their user in the database.
* If either username or password don't match what's in the database, it returns a message.
* The message doesn't inform them if it was the username or password that was incorrect.
* The user is able to view their password before logging in to check for typos.

### Log Out
* &#128100;
* Logs the user out of the current session user account.
* Removes all session data.

### Homepage
* &#128683;
* All products are displayed on this page.
* There is a search function, as explained below in [Search Products](#search-products).

### Profile
* &#128100;
* Only accessible for logged in users.
* It allows users to view any order that they have made.
* It allows users to edit their personal details.
* There is also a button to allow a user to delete their account.

### Delete Account
* &#128100;
* Only accessible for logged in users.
* Creates a modal to confirm if the user wishes to delete their account.
* Once submitted, it deletes the user from the database, so the user can no longer log in and their address details will be removed.
* The user will be permanently deleted from the database.
* &#128272; This function is not able to delete the superuser.

### Add Products
* &#128272;
* Only accessible for the superuser.
* Provides a form for users to fill in, with placeholder text.
* All input elements have the correct validation on.
* Once submitted, it adds an item into the database, which then populates it onto the site.

### Edit Products
* &#128272;
* Only accessible for the superuser.
* Provides a form for users to fill in, with placeholder text.
* All input elements have the correct validation on.
* The form is pre-filled in with the current item details, for easy editing.
* Once submitted, it edits the item in the database, which then populates those edits onto the site.

### Delete Products
* &#128272;
* Only accessible for the superuser.
* Creates a modal to confirm if the user wishes to delete this item.
* Once submitted, it deletes the item from the database, so the item can no longer be viewed on the site.
* The item will be permanently deleted from the database.

### Search Products
* Accessible by all users.
* Searches through database for what the user has entered into the search box.
* It uses the product name and description to search within.
* It returns all results, or a message if there are no results.
* The reset button then clears the search bar, and returns the page to it's standard state.

### Messages
* If products are added to the database, the phrase '{Item} Successfully Added' should display.
* If products are deleted from the database, the phrase '{Item} Successfully Deleted' should display.
* If products are edited in the database, the phrase '{Item} Successfully Updated' should display.
* If a product is added to the user's shopping bag, the phrase '{Item} successfully added to your bag' should display, with a summary of the user's shopping bag shown.
* If a product is removed from the user's shopping bag, the phrase '{Item} successfully removed from your bag' should display, with a summary of the user's shopping bag shown.
* If a product quantity is updated in the user's shopping bag, the phrase '{Item} quantity successfully updated to {quantity}' should display, with a summary of the user's shopping bag shown.
* If a logged in user without access rights tries to access a restricted page, it redirects them to the homepage, and presents them with a message saying 'You do not have access to this page'.

### Stripe
* To test the webhooks and payment process, I used the following Stripe testing card numbers:
    * No authentication successful payment: 4242 4242 4242 4242
    * Failed payment: 4000 0000 0000 9995
    * Authentication required: 4000 0025 0000 3155
* The no authentication successful card was run, didn't ask for authentication, and successfully paid.
* The failed payment card was run and the card payment failed.
* The authentication required card was run, asked for authentication, and successfully paid.
* After each payment event, a message was shown to the user to explain the action that had just happened.

### Pagination
* Accessible by all users
* If there are more than 10 items visible on the page, it displays only the first 10, and shows pagination information and links under the items to allow easy navigation.
* This also works within the search function.
* The user can click the number buttons to take them to a specific page.
* The user can click the arrow buttons to take them forwards or backwards one page.

### 404
* Accessible by all users
* This page will display if a user has tried to access a page that doesn't exist, or if a user doesn't have access to the page they're trying to reach.
* It accesses whether the user is logged in or not, and if logged in, whether they are a superuser or not, and displays the corresponding navigation bar.
* It states clearly that it's a 404 error, and that the page hasn't been found.
* It directs the user to the navigation bar to continue back to the safety of the site.

### Validation
* Form validation
    * This has been used on every form input on the site to ensure the correct data is added.
    * If incorrect data is added, red warning text appears, to instruct the user of how to fix the error.
* Adding products to the bag
    * Custom validation has been added to ensure that users can't:
        * Add less than one of a product into their bag (such as adding a 0 quantity of a product).
        * Add more than 99 of a product into their bag.
* Password validation
    * When a user is registering for an account, the site ensures no typos happen by prompting the user to enter the password twice, with the site checking to confirm that the passwords match.
* Email validation
    * When a user is registering for an account, the site ensures the correct email address has been entered by sending a verification email to the email address the user has supplied.
    * The account cannot be used until the user has verified that their email address is correct by following the link in the validation email.

[Back to the top](#testing)

---

## Database
* When the superuser adds products to the database, the information should be stored.
* When the superuser edits a product in the database, the information should be populated from the current product data.
* When the superuser edits a product in the database, the information should be stored.
* When the superuser deletes a product from the database, the product should be permanently removed.
* If products are added to the database, the phrase '{Item} Successfully Added' should display.
* If products are deleted from the database, the phrase '{Item} Successfully Deleted' should display.
* If products are edited in the database, the phrase '{Item} Successfully Updated' should display.

[Back to the top](#testing)

---

## Accessibility
### Tap Targets
* All tap targets are a minimum of 40px x 40px, to comply with WCAG Accessibility standards.
* All tap targets have a minimum of an 8px gap between them, to avoid any overlapping tap targets.

### Color Contrast
* All background and foreground colors have a sufficient contrast ratio.
* This site has been checked by a user with deuteranopia color blindness with no issues present.
* [Toptal Color Blind Filter](https://www.toptal.com/designers/colorfilter/) was used to check every accessible page against every type of color blindness, with no issues present. Unfortunately, the checker doesn't support loggin in, so the logged in only pages were not able to be checked this way.
* All color contrasts were checked using [WebAIM's Contrast Checker](https://webaim.org/resources/contrastchecker/), with all large-scale text having a contrast ratio of at least 3:1, and all other text having a contrast ratio of at least 4.5:1.

### Visually-Impaired Users
* All images have meaningful alt text.
* All icons have an aria-label to describe them, unless semantic text is also visible.
* All buttons that need more description for a visually-impaired user have an aria-labelledby attribute attached to them.

### Assistive Technologies
* All actions are keyboard-focusable.
* All interactable elements have hover and focus styling applied to them.

### Reading Level
* All text content on the site has a maximum reading level of age 9, to aid people with cognitive impairments, and people who don't speak English as a first language, among others.
* All text content on this site has been tested against the Automated Readability Index (ARI) on [Readability Formulas](https://readabilityformulas.com/free-readability-formula-tests.php).

[Back to the top](#testing)

---

## Lighthouse
I tested my website using DevTools Lighthouse feature, and got these results:


### Desktop
![Lighthouse desktop first try](static/docs/img/lighthousedesktop.png)


### Mobile
![Lighthouse mobile first try](static/docs/img/lighthousemobile.png)


### Performance:
* 


### Accessibility:
* 


### Best Practices:
* 


### SEO:
* 


## WebPageTest
* [WebPageTest Results](LINK)

[Back to the top](#testing)

---

## Responsive Design
### Mobile
* The Home page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Log In page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Log Out page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Register page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Profile page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Add Merchandise page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Edit Merchandise page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Delete Merchandise modal looks good, is placed in front of all other content, and nothing wraps where it shouldn't or disappears off the edge of the viewport.

* The buttons have well sized text, not so big it takes up too much screen space, and not so small that they're difficult to read.
* All the font sizes aren't too big or too small for the screen size.
* All fonts are easy to read.
* All images are scaled to the screen size, whilst maintaining the correct aspect ratio.

### Tablet
* The Home page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Log In page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Log Out page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Register page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Profile page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Add Merchandise page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Edit Merchandise page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Delete Merchandise modal looks good, is placed in front of all other content, and nothing wraps where it shouldn't or disappears off the edge of the viewport.

* The buttons have well sized text, not so big it takes up too much screen space, and not so small that they're difficult to read.
* All the font sizes aren't too big or too small for the screen size.
* All fonts are easy to read.
* All images are scaled to the screen size, whilst maintaining the correct aspect ratio.

### Computer
* The Home page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Log In page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Log Out page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Register page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Profile page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Add Merchandise page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Edit Merchandise page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Delete Merchandise modal looks good, is placed in front of all other content, and nothing wraps where it shouldn't or disappears off the edge of the viewport.

* The buttons have well sized text, not so big it takes up too much screen space, and not so small that they're difficult to read.
* All the font sizes aren't too big or too small for the screen size.
* All fonts are easy to read.
* All images are scaled to the screen size, whilst maintaining the correct aspect ratio.

[Back to the top](#testing)

---

## Images
### Desktop and Laptop
#### Chrome
![Home page](static/docs/testing/desktop/chrome/home.png)
![Log In page](static/docs/testing/desktop/chrome/log-in.png)
![Register page](static/docs/testing/desktop/chrome/register.png)
![Add Merchandise page](static/docs/testing/desktop/chrome/add-merch.png)
![Edit Merchandise page](static/docs/testing/desktop/chrome/edit-merch.png)

[Back to the top](#testing)

---

#### Edge
![Home page](static/docs/testing/desktop/edge/home.jpeg)
![Log In page](static/docs/testing/desktop/edge/log-in.jpeg)
![Register page](static/docs/testing/desktop/edge/register.jpeg)
![Add Merchandise page](static/docs/testing/desktop/edge/add-merch.jpeg)
![Edit Merchandise page](static/docs/testing/desktop/edge/edit-merch.jpeg)

[Back to the top](#testing)

---

#### Mozilla Firefox
![Home page](static/docs/testing/desktop/moz/home.png)
![Log In page](static/docs/testing/desktop/moz/log-in.png)
![Register page](static/docs/testing/desktop/moz/register.png)
![Add Merchandise page](static/docs/testing/desktop/moz/add-merch.png)
![Edit Merchandise page](static/docs/testing/desktop/moz/edit-merch.png)

[Back to the top](#testing)

---

#### Safari
![Home page](static/docs/testing/desktop/safari/home.png)
![Log In page](static/docs/testing/desktop/safari/log-in.png)
![Register page](static/docs/testing/desktop/safari/register.png)
![Add Merchandise page](static/docs/testing/desktop/safari/add-merch.png)
![Edit Merchandise page](static/docs/testing/desktop/safari/edit-merch.png)

[Back to the top](#testing)

---

### Tablet
#### Safari
![Home page](static/docs/testing/tablet/safari/home.jpg)
![Log In page](static/docs/testing/tablet/safari/log-in.jpg)
![Register page](static/docs/testing/tablet/safari/register.jpg)
![Add Merchandise page](static/docs/testing/tablet/safari/add-merch.jpg)
![Edit Merchandise page](static/docs/testing/tablet/safari/edit-merch.jpg)
![Menu](static/docs/testing/tablet/safari/menu.jpg)

[Back to the top](#testing)

---

### Mobile
#### Chrome
![Home page](static/docs/testing/mobile/chrome/home.jpg)
![Log In page](static/docs/testing/mobile/chrome/log-in.jpg)
![Register page](static/docs/testing/mobile/chrome/register.jpg)
![Add Merchandise page](static/docs/testing/mobile/chrome/add-merch.jpg)
![Edit Merchandise page](static/docs/testing/mobile/chrome/edit-merch.jpg)
![Navigation menu](static/docs/testing/mobile/chrome/menu.jpg)

[Back to the top](#testing)

---

#### Safari
![Home page](static/docs/testing/mobile/safari/home.jpg)
![Log In page](static/docs/testing/mobile/safari/log-in.jpg)
![Register page](static/docs/testing/mobile/safari/register.jpg)
![Add Merchandise page](static/docs/testing/mobile/safari/add-merch.jpg)
![Edit Merchandise page](static/docs/testing/mobile/safari/edit-merch.jpg)
![Navigation menu](static/docs/testing/mobile/safari/menu.jpg)

[Back to the top](#testing)

---

#### Samsung Internet
![Home page](static/docs/testing/mobile/samsung/home.jpg)
![Log In page](static/docs/testing/mobile/samsung/log-in.jpg)
![Register page](static/docs/testing/mobile/samsung/register.jpg)
![Add Merchandise page](static/docs/testing/mobile/samsung/add-merch.jpg)
![Edit Merchandise page](static/docs/testing/mobile/samsung/edit-merch.jpg)
![Navigation menu](static/docs/testing/mobile/samsung/menu.jpg)

[Back to the top](#testing)