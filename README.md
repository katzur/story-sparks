<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/Logo.png" width="150" height="150" />

# **Story Sparks Co.** - Django e-commerce candle store.

### [Click here to view the page](https://story-sparks.herokuapp.com/)
### [Click here to view the repository](https://github.com/katzur/story-sparks)


# Table of Contents:

1. [Introduction](#introduction)
	* [Demo](<#demo>)
2. [UX](#ux)
	* [Strategy](#strategy)
    * [Marketing Strategy](#marketing-strategy)
    * [Scope](#scope)
        * [User Stories](<#user-stories>)
        * [Priority chart](<#priority-chart>)
    * [Structure](#structure)
        * [Database Models Diagram](<#database-models-diagram>)
        * [User Journey Diagram](<#user-journey-diagram>)
    * [Skeleton](#skeleton)
        * [Wireframes](<#wireframes>)
    * [Surface](#surface)
3. [Agile](#agile)
    * [Kanban Board](#kanban-board)
    * [Epics](#epics)
4. [Features](<#features>)
	* [Existing Features](<#existing-features>)
	* [Future Features](<#future-features>)
5.  [Marketing Strategy Implementation](#marketing-strategy-implementation)
    * [Branding](#branding)
    * [SEO](#seo)
    * [Keywords](#keywords)
    * [Newsletter](#newsletter)
    * [Social media](#social-media)
6. [Technologies Used](<#technologies-used>)
7. [Testing](<#testing>)
    * [Stripe Testing Guidance](#stripe-testing-guidance)
8. [Deployment](<#deployment>)
9. [Credits](<#credits>)


# Introduction
Story Sparks Co. is a B2C e-commerce store. 
The site is targeted towards users who are interested in purchasing candles for themselves or looking for funny gifts for others. Labels on the products contain witty descriptions reflecting 21st cenyury lifestyle of young adults (aka Millennials).

Users can browse and purchase a variety of candles in two sizes, as well as check the special offers and search the candles based on the scent type. They can view the Shipping and Return information, Policies, information about the Story Sparks Co. Team. They can as well contact the Team trhough the contact form and add their emails for subscription purposes (supported by Mailchimp). 

The payment system for the Story Sparks Co. store uses Stripe. Please note that this website is created for educational purposes. Do NOT enter any personal credit/debit card details when using the site. For more info how to test the site, please refer to [Stripe Testing Guidance](#stripe-testing-guidance).

Story Sparks Co. is the final project of the Code Institute diploma in Fullstack Development with e-commerce applications.

# UX
## Strategy
### The Issue
When browsing in the Internet to find more about the candle industry, I noticed that the market is covered in mass-production, low quality candles with generic scents. Big brands have the monopol and sell their products in every
online store with home decor. But the consumers are looking for variety, affordable prices and quality in their candles, as well as someting that would stand out. The trend of supporting local, small companies and artists is growing stronger and more creative companies should show their craft mastery on the market to give big brands solid competition.

### The Vision
Story Sparks Co. was created as a response to the current retail needs described above. The vision behind creating this store was focused on delivering a User an option to purchase something extraordinary, not currently seen on the
candle market. No matter if the User is looking to purchase a candle to treat themselves, or a unique gift, that will bring a smile on loved one's face - Story Sparks delivers. Those are inteligent, funny candles that reflect and 
comment our current lifestyle. The scents offered are unique and present a strong opposition to what big brands produce commonly. Uniqueness is Story Spark's strenght and might be an inspiration for other small brands that are looking
for their way to start operating on the online market.

Store is easy and clear to navigate, based on the principle of "mobile first approach", which gives the freedom of using it on any type of device due to its full responsiveness. The aim was to provide all the main, necessary features expected for an e-commerce store.

### Target Audience
Consumers that appreciate high-quality, handmade candles with unique scents and labels. Story Sparks Co. ensures to use only natural ingredients and supports zero-waste movement, as the jars and tins can be re-used for other purposes. 
No plastic, no worries. Story Sparks Co. labels contain witty comments on our 21st century lifestyle, hence the target audience will be mainly young adults (aka Millenialls), who can identify themselves with words written on the candles. Other Users in different age groups will find Story Sparks Co. attractive as well, since it's a great place to purchase candles as a gift for the loved ones, who might be in a young adults age group. By implementing modern design, intuitive navigation and simple images Story Sparks Co. is aspiring to be a store suitable for all the age groups.

### Personas
Ana, 32, single. Works in IT sector, since COVID fully remotely. Over the last 3 years she discovered many new small brands online that are a great alternative to environmental exploiting corporations and deliver their products to her doorstep. She noticed she can make a difference as a knowledgeable, conscious consumer, who cares about the planet condition. Since the COVID she spends more money online, and likes funny, jokey items that brighten her apartment.

Monica and Chandler, 58 and 60, married couple. They're parents of two daughters in their late 20s. When looking for Christmas gifts, they use Google to browse for some unique items for their girls. They don't like to spend too much time on wrapping and boxing items, hence pre-packed sets are an ideal choice for them. As all other consumers they love special offers, and find candles a good side gift for their loved ones. They understand that support shown to local small companies is important to keep the community together. They gladly purchase products from small sellers and stores due to the great quality and dedicated personal service.

## Marketing Stategy
A set of various marketing strategies was implemented for Story Sparks Co. SEO, Social Media Marketing with elements of Content Marketing, Email Marketing - all to ensure Story Sparks success in the Internet by creating visible and trusty online presence.
Strong brand equals more customers, involved digital community and steady income. More about that in the [Marketing Strategy Implementation](#marketing-strategy-implementation) section.

## Scope
### User Expectations
1. As a User I want the store to be responsive on all device types.
2. As a User I want the store to be accessible and easy to navigate.
3. As a User I want the store to process my data securely.

### User Stories
1. As a Site User I can view a list of products so that I can easily select some to purchase.
2. As a Site User I can view individual product details so that I can identify the name, price, description, ingredients and product image.
3. As a Site User I can easily view the total of my purchases at any time so that I can avoid spending too much and have a good overview of the current total.
4. As a Site User I can easily register an account so that I can have a personal account and be able to view my profile information: saved address details and past order history.
5. As a Site User I can easily log in an account so that I can access my personal account information,
6. As a Site User I can easily log out of my account so that I can ensure no one else can see my personal account information and order history.
7. As a Site User I can easily recover my password in case I forget it so that I can recover access to my account.
8. As a Site User I can receive an email confirmation after registering so that I can verify that my account registration was successful.
9. As a Site User I can have a personalized user profile so that I can view my personal order history and order confirmations, as well as save my payment information.
10. As a Site User I can sort the list of available products so that I can easily identify the price of the products (ascending / descending) and view the products in the alphabetical order (ascending / descending).
11. As a Site User I can sort a specific category of products so that I can find the products by price or name (ascending/ descending) for that specific category.
12. As a Site User I can sort a specific product based on their scent so that I can view the price and product name (ascending/ descending) for that selected scent category.
13. As a Site User I can search for the product by name, description or ingredients so that I can find a specific product that I'd like to purchase.
14. As a Site User I can easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available.
15. As a Site User I can easily select the quantity of a product when purchasing it so that I can ensure I don't accidentally select the wrong product or quantity.
16. As a Site User I can view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive.
17. As a Site User I can adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before the checkout.
18. As a Site User I can easily enter my payment information so that I can checkout quickly and with no issues.
19. As a Site User I can ensure that my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
20. As a Site User I can view an order confirmation after the checkout so that I can verify that I haven't made any mistakes.
21. As a Site User I can receive an email confirmation after checking out so that I can keep the confirmation on what I've purchased for my own records.
22. As a Site User I can view the terms & conditions so that I can understand better terms & conditions of using the store.
23. As a Site User I can view the privacy policy settings so that I can understand better store's privacy policy and how they use my data.
24. As a Site User I can subscribe to a newsletter so that I can get all the latest offers and information regarding the store and products, as well as special deals.
25. As a Site User I can see the store's social media accounts links so that I can easily access store's social media pages and profiles to view the information, posts etc.
26. As a Site User I can view the logos and links for any external resources so that I can identify the organizations and movements the store works with to identify the store's mission and profile.
27. As a Site User I can view the testimonials of other media accounts (magazines, radio, TV), who tested the Story Spark's products so that I can see what are their opinions about the company and its products.
28. As a Site User I can quickly identify special offers so that I can take advantage of special savings on products I'd like to purchase.
29. As a Site User I can view the About Us section so that I can learn more about the Story Sparks Co. owners and employees.
30. As a Site User I can view the shipment and returns Q&A section so that I can get more information about the shipping time, return options and international deliveries.
31. As a Site User I can use the contact form so that I can communicate directly with the store to send them a query/ questions regarding the product/store.

### User (Owner) Stories
1. As a Site Admin I can add a product so that I can add new items to my store.
2. As a Site Admin I can edit/update a product so that I can change product price, image, description, name, ingredients.
3. As a Site Admin I can delete a product so that I can remove items that are no longer available.
4. As a Site Admin I can add a new creator to About Us section so that I can add new people, who work for Story Sparks Co.
5. As a Site Admin I can edit/update a creator to About Us section so that I can change the information and photos of people, who work for Story Sparks Co.
6. As a Site Admin I can delete a creator from About Us section so that I can remove people, who no longer work for Story Sparks Co.
7. As a Site Admin I want to send newsletters to our mailing list so that I can share information about the new products and upcoming deals.

Here's a table of the features based on the User Stories ordered by their importance and urgency to complete.
Possible importance of the User Stories: MUST HAVE, COULD HAVE, WON'T HAVE. It is reflected in the [Kanban Board's Labels](https://github.com/users/katzur/projects/6/views/1) for the project.
MUST HAVE User Stories were implemented first, while COULD HAVE were or implemented/or left in the process as pending for the future store releases.
WON'T HAVE were left behind for this release of the store, but they possibly can be implemented in the future releases, if the time and capacity allows.

Story no. | Feature | Importance
:---: | --- | :---: |
1 | Responsiveness | MUST HAVE
2 | Accessibility | MUST HAVE
3 | Data Security | MUST HAVE
4 | Homepage | MUST HAVE
5 | Customer Profile | MUST HAVE
6 | Products view | MUST HAVE
7 | Product categories | MUST HAVE
8 | Product scents | MUST HAVE
9 | Search | MUST HAVE
10 | Add products | MUST HAVE
11 | Delete products | MUST HAVE
12 | Edit qty | MUST HAVE
13 | Payment form | MUST HAVE
14 | Payment processing | MUST HAVE
15 | Toasts | MUST HAVE
16 | ADMIN: Add products | MUST HAVE
17 | ADMIN: Edit products | MUST HAVE
18 | ADMIN: Delete products | MUST HAVE
19 | Bag review | MUST HAVE
20 | Checkout review | MUST HAVE
21 | Contact form | MUST HAVE
22 | ADMIN: Add creators | MUST HAVE
23 | ADMIN: Edit creators | MUST HAVE
24 | ADMIN: Delete creators | MUST HAVE
25 | Sign Up | MUST HAVE
26 | Log In | MUST HAVE
27 | Log Out | MUST HAVE
28 | Privacy Policy, Terms and Conditions | MUST HAVE
29 | External resources | COULD HAVE
30 | Subscription box | COULD HAVE
31 | Testimonials | COULD HAVE
32 | Autofill saved data at checkout | COULD HAVE
33 | Social media links | COULD HAVE
34 | About Us | COULD HAVE
35 | Shipment & Returns Q&A | COULD HAVE
36 | ADMIN: Send newsletters | WON'T HAVE

### Priority Chart
<details><summary>Priority chart implementation</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/chart.jpg">
</details>

## Structure
### Database Models Diagram
To create a database models diagram I used great and intuitive online tool [DrawSQL](https://drawsql.app/).
<details><summary>View the Database Models Diagram</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/models+diagram.jpg">
</details>

### User Journey Diagram
To create a user journey diagram I used known and reliable online tool [Diagrams.net](hhttps://www.diagrams.net/).

Color legend:
* Blue - parent pages containing subpages
* Grey - all other subpages and additional features (Search, Footer)
* Green - subpages requiring User to be logged in
* Purple - subpages accessable only for the Admins

<details><summary>View the User Journey Diagram</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/user-journey.png">
</details>

Story Sparks Co. was developed usiutalizing Django. 
As a result the page functionality was split into separate applications. For this project I created 7 apps for clear functionality split:
* bag - functionality for basket view, where the user can verify product added to the bag
* checkout - functionality for checkout procedure, where the user processes with the payment and adds the delivery details
* contact - functionality for contact form and Shipping & Returns Q&A page
* creators - functionality for About Us section listing all current Story Sparks members, as well as give the Admin an option to add, edit and delete them. 
* home - functionality for main homepage - navbars, search bar, access to the basket and account options, as well as testimonials, social media, subscription field and Provacy Policy and Terms & Conditions.
* products - functionality for the products to be listed and searched - based on the categories and scents.
* profiles - functionality for the profile management - login in/out, registration, profile page with delivery details, order history and product management for the Admins.

## Skeleton
The store website was designed to provide the User with an expected product - easy to navigate, with search bar on the top, clear navigation, easy to identify sections and helpful icons. 
The header and footer on each page repeats, colors are consistent across the all subpages. Amount of information is not excesive - helping the Users to intuitively find what they're looking for. 
Wireframes for main pages for all screen sizes (desktop, tablet and mobile) were created in [Balsamiq](https://www.balsamiq.com/), as shown below.

### Wireframes
<details> <summary> Home page</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/wireframe-home.png">
</details>
<details> <summary> Shopping Bag</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/wireframe-bag.png">
</details>
<details> <summary> Checkout</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/wireframe-checkout.png">
</details>
<details> <summary> Products</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/wireframe-products.png">
</details>
<details> <summary> My Profile</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/wireframe-profile.png">
</details>

## Surface
The aim was to design a store, that would look modern and warm, but comply with Users experience of using online e-commerce stores.
### Colors
The colors used within all the pages are shown below and were inspired by some of the [Pinterest](https://www.pinterest.com/) ideas for modern web design. They are complimented by simple and readable product images, buttons and toast messages. I wanted to achieve consistent website look that would reflect store's character. Colors and layout of the elements were intentionally picked to keep the modern, simple design. Colors compliment each other well and keep great page contrast, which makes it more user-friendly and accessible. Confirmed on [Coolors](https://coolors.co/):

<details> <summary> Color Palette</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/color-palette.png">
</details>
<details> <summary> Contrast Checker</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/contrast-checker1.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/contrast-checker2.png">
</details>

### Typography
I decided to stay mostly with default fonts that came with Bootstrap CSS styling. Two fonts I especially liked to continuously use within this project to provide satisfiying design:

* Segoe UI - well known, easy to read, fits the page overal style. Used for the page name and login/ registration pages.
* Roboto - sans-serif font - clean and easy to read.

### Images
* All icons used for Story Sparks Co. come from [FontAwesome](https://fontawesome.com/)
* All images used for Story Sparks Co. About Us come from [Pexels](https://www.pexels.com/)
* Product images were created by me. For product visualisation I used [Printful](https://www.printful.com/custom-candles#create) and [Cortado.ie](https://www.contrado.ie/estore/design/)

# Agile
## Kanban Board
Story Sparks Co. e-commerce store project was based on the Agile Methodology. I used Agile Kanban Board Framework and implemented it in the site's creation process. 
* It can be viewed [here](https://github.com/users/katzur/projects/6)
It was divided into three sections for clear tasks distribution and visual progress:
* Todo
* In Progress
* Done

<details><summary>Kanban Board look for the project</summary><img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/kanban-board.png"></details>

Based on the Iterative Development idea - while working on this project, I added new functional capabilities and modified existing features as needed over time. Different parts of the project were developed at various times and were integrated based on their successful completion. Increments were build based on their functionality need to not spend efforts on building features not neccessary for the project. Subsequent iterations were implemented based on the Users feedback and tests.

MoSCoW prioritization was taken under consideration while creating this project - some of the User Stories were critical (like CRUD functionality, processing orders) compared to other User Stories rather considerable (contact form, Shipments & Returns Q&A, About Us). Those with smaller impact were left for the later phase of page development, while other - vital ones - were guaranteed to be delivered on time. Timeboxing and prioritization were crutial for this project and can be reflected by viewing Iteration process (Todo > In Progress > Done) and labels assigned to each User Story (Must Have, Could Have and Won't Have).

## Epics
Story Sparks Co. project was broken into smaller Epics and were reflected in the creation process by starting new apps. Groups of User Stories were added to the Kanban Board based on those firstly established Epics. 

Epics (Ideas):
* Purchasing (Shopping Bag) and Checkout
* Contact and Searchability - Contact Form, Subscription Form, Social Media
* Information about the shop and handling - Information about creators in About Us and Shipping and Returns Q&A
* User Notifications (emails, toasts)
* Page Visibility (Search, Sort, Order History, My Profile)
* Viewing and Navigation - Products, Product Details
* CRUD - Management for the User and Admin
* Registration and User Accounts (Sign-in, Sign-up, Log out, Password Reset)

# Features
Story Sparks Co. was designed as a functional e-commerce store and features were selected based on the Kanban Board and MoSCoW prioritization (applied labels to User Stories). 
During the process of the page creation I was able to decide what needs to be implemented, and what set of features can be potentially added in the future.

## Existing Features
<details> <summary> Header </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/header.png">
</details>

Header is a static element visible on every page. It contains:
* Free delivery banner, to let the Users know that they can get free shipping if they place an order over €50.
* Logo visible on large screens (desktop) on the top left. It's removed on smaller screens (tablet, mobile) to reduce the navbar size.
* Search bar in the center on large screens (desktop). Reduced to a loop icon on smaller screens (tablet, mobile) due to space economy.
* My Account button with dropdown menu that provides links for "Register" and "Login", allowing users to either register for a new account, or login with an existing one. 
Once logged in, the links update to "My Profile" and "Logout". If logged in as a superuser, there is also a "Product Management" link available here.
* Cart button - transfers the User to Bag view page. 
* Navigation contains "All Candle Types", "Scents", "About & Contact" links, helping users to navigate to the needed parts of the store. On smaller screens (tablet, mobile) replaced with Hamburger Icon.

<details> <summary> Footer </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/footer.png">
</details>

Footer color compliments the free delivery banner for page's consistency. It contains:
* "Let's keep in touch!" section with social media icons, that open social media pages in a new window.
* Newsletter sign up field. Connected to [Mailchimp](https://mailchimp.com/). User can add their email address to subscribe to the latest offers emails.
* Middle section with useful links - All Products, About Us, Contact, Shipping and Returns, Privacy Policy, Terms & Conditions.
* Organisation logos and links - BDIH, Peta, Nature.org and Zero Waste Movement.
* Copyright section and disclaimer about educational purpose of the page.

<details> <summary> Home page </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/home1.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/home2.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/home3.png">
</details>

Main page that allows the User to easily navigate through available options:
* Hero section: Hero image with funny candle collage and a small description with the button to the store.
* 3 tiles with the featured links to: store, scents and special offers.
* Testimonial carrousel section with comments from media sources about Story Sparks Co.
* Section with a tins collage, small text section and a button to About Us page.
* Banner above the footer with Instagram account name information and direct link to the social media.

<details> <summary> Products </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/products.png">
</details>

Products page displays the list of all products added to the store:
* Sort field - allows to sort the available products by name (A-Z and Z-A) and price (lowest/ highest first)
* Information about the number of avilable products.
* List of the products containing: image, colorful background, name, price.
* List can be filtered by Scent in the navbar on the top.
* User can also perform a search on the products by name, description and ingredients.
* When logged in as a superuser, additional buttons appear: "Edit" and "Delete". These give the superuser quick access to CRUD functionality.


<details> <summary> Product Details </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/product-details.png">
</details>

Product Details page provides further information about the selected product:
* Larger image of the product on the left side.
* On the right side information about: item name, price, description, ingredients. 
* When logged in as a superuser, additional buttons appear: "Edit" and "Delete". These give the superuser quick access to CRUD functionality.
* Quantity selector (minimum of 1 and a maximum of 99).
* Buttons on the bottom: Add to bag and Keep shopping.

<details> <summary> Shopping Bag </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/bag.png">
</details>

Full-page view of User's current shopping bag:
* Column headings with color matching the free delivery banner and the footer for color consistency across the page: Product info, Price, Qty, Subtotal.
* Products list: image, name, price per 1 item, quantity selector and buttons: Update and Delete, subtotal.
* Information in the right bottom corner: Bag total, delivery cost, total cost.
* If the items total is lower than €50 - information how much User needs to spend to get the free delivery.
* Buttons on the bottom: Keep Shopping and Secure Checkout.

<details> <summary> Checkout </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/checkout.png">
</details>

Checkout contains a delivery information form and order details:
* On the left side delivery information form needs to be filled with necessary information.
* Customer has an option to save the details for the future purchases and store delivery information within My Profile page.
* Card details displayed on the bottom and verified by Stripe.
* On the right side Order details section - displays the same information as the Shopping bag.
* Buttons on the bottom: Adjust bag (back to the Shopping bag in need of adjustment) or Complete order - based on provided details.

<details> <summary> Purchase Confirmation </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/confirmation.png">
</details>

After successful checkout User will see the Purchase Confirmation page:
* A success toast message will display in the right top corner informing the user about successfully finished transaction and the order number.
* Thank you page for the User for placing their order. Information on the top about a confirmation email being sent via email to the specified email address.
* Confirmation page displays all of the order details (without the payment details), date and time, order number.
* Button visible on the bottom: Now let's check the other products, which brings the User to the All products page.
* Information displayed on this page, can be viewed by the user under My Profile > Order History.

<details> <summary> Error Pages: 500 and 404 </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/404error.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/500error.png">
</details>

Project has custom error pages for 404 and 500 errors.
* 404 error - Page not found - very common error. Added a custom error page to keep it user-friendly. It has a "Return to the homepage" button that takes the User to the main page back.
* 500 error - Server error. Added a custom error page to keep it user-friendly. It has a "Return to the homepage" button that takes the User to the main page back.

<details> <summary> My Profile and Order History </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/my-profile.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/order-history.png">
</details>

When the User is logged in, they can access "My Profile" section from "My Account" icon on the top right side.
* Left side of the page shows the saved information about delivery details, that can be edited at any time.
* The user will receive a success message when the profile is updated.
* Saved delivery information is used to autofill the Checkout form.
* Right side of the profile page displays the order history.
* Clicking on the order number will show the full order details and a toast message informing it's a past order information, as per screenshot provided.

<details> <summary> Product Management </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/confirmation.png">
</details>

Product Management page is available to superusers only.
* When logged in as a superuser, "Product Management" is available from "My Account" icon on the top right side.
* Product Management page displays a form, where superuser can add the products to the store.
* The same form is used, when a superuser wants to update a product.

<details> <summary> Shipping And Returns Q&A </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/Q%26A.png">
</details>

Q&A page, where users can learn more about the Shipping and Returns procedures.
* The page has a form of accordeon - to view the answer to the question regarding Shipping and Returns - User needs to click on the question, which will reveal the answer.
* Important page, as it displays all the ionformation that customer might be looking for in case of receiving a faulty item or wanting to return the goods.

<details> <summary> About Us </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/aboutus.png">
</details>

About Us page displays the details about the Story Sparks creators - their photos, names, job title and additional information.
* Each creator has a short description field explaining their role in Story Sparks Co. 
* Page brings the User and creators closer - makes the purchase more personal, as the User knows who stands behind the brand.
* When logged in as a superuser - additional buttons are availabe: "Add new creator", "Update creator" and "Delete creator".
* "Add new creator" takes the superuser to a new page containing a form, which allows to add new members of Story Sparks Co. to the About Us page.

<details> <summary> Contact Form </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/contact-form.png">
</details>

Contact pagre allows the User to communicate with the Story Sparks Co. Team.
* Page contains a form, where the user can choose the category: Submit a request or Ask a question and add their details.
* Once the contact form is sent - the User receives a success message in the top right corner informing about successful submission.
* In case of any error while sending the form - the user receives an error notification in the top right corner.

## Future Features
* Newsletter Management Panel for the superusers - send a newsletter based on the subscriptions email base.
* Add more social media accounts.
* Improve the pages design, add more eye-catching homepage elements.
* Add the option for the user to save their name details, not only delivery information.
* Add to the Wishlist option, which will save those items in the User's Profile.
* Add the rating for the products.
* Add more product categories - like accessories, wax melts, tealight sets.
* Add a blog.
