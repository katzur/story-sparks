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
7. [Content and Credits](<#content-and-credits>)
8. [Testing](<#testing>)
    * [Stripe Testing Guidance](#stripe-testing-guidance)
9. [Deployment](<#deployment>)
10. [Acknowledgments](<#acknowledgments>)


# Introduction
Story Sparks Co. is a B2C e-commerce store. 
The site is targeted towards users who are interested in purchasing candles for themselves or looking for funny gifts for others. Labels on the products contain witty descriptions reflecting 21st century lifestyle of young adults (aka Millennials).

Users can browse and purchase a variety of candles in two sizes, as well as check the special offers and search the candles based on the scent type. They can view the Shipping and Return information, Policies, information about the Story Sparks Co. Team. They can as well contact the Team through the contact form and add their emails for subscription purposes (supported by Mailchimp). 

The payment system for the Story Sparks Co. store uses Stripe. Please note that this website is created for educational purposes. Do NOT enter any personal credit/debit card details when using the site. For more info how to test the site, please refer to [Stripe Testing Guidance](#stripe-testing-guidance).

Story Sparks Co. is the final project of the Code Institute diploma in Full Stack Development with e-commerce applications.
## Demo
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/amiresponsive.png" />


# UX
## Strategy
### The Issue
When browsing in the Internet to find more about the candle industry, I noticed that the market is covered in mass-production, low quality candles with generic scents. Big brands have the monopoly and sell their products in every
online store with home decor. But the consumers are looking for variety, affordable prices and quality in their candles, as well as something that would stand out. The trend of supporting local, small companies and artists is growing stronger and more creative companies should show their craft mastery on the market to give big brands solid competition.

### The Vision
Story Sparks Co. was created as a response to the current retail needs described above. The vision behind creating this store was focused on delivering a User an option to purchase something extraordinary, not currently seen on the
candle market. No matter if the User is looking to purchase a candle to treat themselves, or a unique gift, that will bring a smile on loved one's face - Story Sparks delivers. Those are intelligent, funny candles that reflect and 
comment our current lifestyle. The scents offered are unique and present a strong opposition to what big brands produce commonly. Uniqueness is Story Spark's strength and might be an inspiration for other small brands that are looking
for their way to start operating on the online market.

Store is easy and clear to navigate, based on the principle of "mobile first approach", which gives the freedom of using it on any type of device due to its full responsiveness. The aim was to provide all the main, necessary features expected for an e-commerce store.

### Target Audience
Consumers that appreciate high-quality, handmade candles with unique scents and labels. Story Sparks Co. ensures to use only natural ingredients and supports zero-waste movement, as the jars and tins can be re-used for other purposes. 
No plastic, no worries. Story Sparks Co. labels contain witty comments on our 21st century lifestyle, hence the target audience will be mainly young adults (aka Millennials), who can identify themselves with words written on the candles. Other Users in different age groups will find Story Sparks Co. attractive as well, since it's a great place to purchase candles as a gift for the loved ones, who might be in a young adults age group. By implementing modern design, intuitive navigation and simple images Story Sparks Co. is aspiring to be a store suitable for all the age groups.

### Personas
Ana, 32, single. Works in IT sector, since COVID fully remotely. Over the last 3 years she discovered many new small brands online that are a great alternative to environmental exploiting corporations and deliver their products to her doorstep. She noticed she can make a difference as a knowledgeable, conscious consumer, who cares about the planet condition. Since the COVID she spends more money online, and likes funny, jokey items that brighten her apartment.

Barbara and Andrew, 58 and 60, married couple. They're parents of two daughters in their late 20s. When looking for Christmas gifts, they use Google to browse for some unique items for their girls. They don't like to spend too much time on combining items, hence pre-selected bundle sets are an ideal choice for them. As all the other consumers they love special offers giving them a chance to save some money. They find candles a good gift idea for their loved ones, when in need to purchase something fast. They understand that support shown to local small companies is important to keep the community together. They gladly purchase products from small sellers and stores due to the great quality and dedicated personal service.

Olivia, 17, high school student, vegan. Spends a lot of time in the social media. When going through her friend's stories on Instagram, a lot of adds are displayed promoting various products. Influencers she's following also post a videos with the product reviews and unboxing events. That's how she noticed Story Sparks Co. and their candles. As a student, Olivia has a small budget and looks for affordable items. She noticed that Story Sparks Co. offers bundles and tin candles, which don't cost much and can be reused after. As a person who cares about the environment and animal rights, she prefers the brands that support organizations like PETA. She considers herself as an conscious and mindful young consumer.

## Marketing Stategy
A set of various marketing strategies was implemented for Story Sparks Co. SEO, Social Media Marketing with elements of Content Marketing, Email Marketing - all to ensure Story Sparks success in the Internet by creating visible and trusty online presence.
Strong brand equals more customers, involved digital community and steady income. More about that in the [Marketing Strategy Implementation](#marketing-strategy-implementation) section.

## Scope
### User Expectations
1. As a User I want the store to be responsive on all device types.
2. As a User I want the store to be accessible and easy to navigate.
3. As a User I want the store to process my data securely.

### User Stories

**Viewing and Navigation**

1. As a Site User I can view a list of products so that I can easily select some to purchase.
2. As a Site User I can view individual product details so that I can identify the name, price, description, ingredients and product image.
3. As a Site User I can easily view the total of my purchases at any time so that I can avoid spending too much and have a good overview of the current total.

**Registration and User Accounts**

4. As a Site User I can easily register an account so that I can have a personal account and be able to view my profile information: saved address details and past order history.
5. As a Site User I can easily log in an account so that I can access my personal account information.
6. As a Site User I can easily log out of my account so that I can ensure no one else can see my personal account information and order history.
7. As a Site User I can easily recover my password in case I forget it so that I can recover access to my account.
8. As a Site User I can receive an email confirmation after registering so that I can verify that my account registration was successful.
9. As a Site User I can have a personalized user profile so that I can view my personal order history and order confirmations, as well as save my payment information.

**Sorting and Searching**

10. As a Site User I can sort the list of available products so that I can easily identify the price of the products (ascending / descending) and view the products in the alphabetical order (ascending / descending).
11. As a Site User I can sort a specific category of products so that I can find the products by price or name (ascending/ descending) for that specific category.
12. As a Site User I can sort a specific product based on their scent so that I can view the price and product name (ascending/ descending) for that selected scent category.
13. As a Site User I can search for the product by name, description or ingredients so that I can find a specific product that I'd like to purchase.
14. As a Site User I can easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available.

**Purchasing and Checkout**

15. As a Site User I can easily select the quantity of a product when purchasing it so that I can ensure I don't accidentally select the wrong product or quantity.
16. As a Site User I can view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive.
17. As a Site User I can adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before the checkout.
18. As a Site User I can easily enter my payment information so that I can checkout quickly and with no issues.
19. As a Site User I can ensure that my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
20. As a Site User I can view an order confirmation after the checkout so that I can verify that I haven't made any mistakes.
21. As a Site User I can receive an email confirmation after checking out so that I can keep the confirmation on what I've purchased for my own records.

**Store Official Data - GDPR**

22. As a Site User I can view the terms & conditions so that I can understand better terms & conditions of using the store.
23. As a Site User I can view the privacy policy settings so that I can understand better store's privacy policy and how they use my data.

**Social Media and Marketing**

24. As a Site User I can subscribe to a newsletter so that I can get all the latest offers and information regarding the store and products, as well as special deals.
25. As a Site User I can see the store's social media accounts links so that I can easily access store's social media pages and profiles to view the information, posts etc.
26. As a Site User I can view the logos and links for any external resources so that I can identify the organizations and movements the store works with to identify the store's mission and profile.
27. As a Site User I can view the testimonials of other media accounts (magazines, radio, TV), who tested the Story Spark's products so that I can see what are their opinions about the company and its products.
28. As a Site User I can quickly identify special offers so that I can take advantage of special savings on products I'd like to purchase.

**Additional Information and Contact**

29. As a Site User I can view the About Us section so that I can learn more about the Story Sparks Co. owners and employees.
30. As a Site User I can view the shipment and returns Q&A section so that I can get more information about the shipping time, return options and international deliveries.
31. As a Site User I can use the contact form so that I can communicate directly with the store to send them a query/ questions regarding the product/store.

### User (Owner) Stories
**Product**

1. As a Site Admin I can add a product so that I can add new items to my store.
2. As a Site Admin I can edit/update a product so that I can change product price, image, description, name, ingredients.
3. As a Site Admin I can delete a product so that I can remove items that are no longer available.

**Creators**

4. As a Site Admin I can add a new creator to About Us section so that I can add new people, who work for Story Sparks Co.
5. As a Site Admin I can edit/update a creator to About Us section so that I can change the information and photos of people, who work for Story Sparks Co.
6. As a Site Admin I can delete a creator from About Us section so that I can remove people, who no longer work for Story Sparks Co.

**Newsletter**

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
* Purple - subpages accessible only for the Admins

<details><summary>View the User Journey Diagram</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/user-journey.png">
</details>

Story Sparks Co. was developed utilizing Django. 
As a result the page functionality was split into separate applications. For this project I created 7 apps for clear functionality split:
* bag - functionality for basket view, where the user can verify product added to the bag
* checkout - functionality for checkout procedure, where the user processes with the payment and adds the delivery details
* contact - functionality for contact form and Shipping & Returns Q&A page
* creators - functionality for About Us section listing all current Story Sparks members, as well as give the Admin an option to add, edit and delete them. 
* home - functionality for main homepage - navbars, search bar, access to the basket and account options, as well as testimonials, social media, subscription field and Privacy Policy and Terms & Conditions.
* products - functionality for the products to be listed and searched - based on the categories and scents.
* profiles - functionality for the profile management - login in/out, registration, profile page with delivery details, order history and product management for the Admins.

## Skeleton
The store website was designed to provide the User with an expected product - easy to navigate, with search bar on the top, clear navigation, easy to identify sections and helpful icons. 
The header and footer on each page repeats, colors are consistent across the all subpages. Amount of information is not excessive - helping the Users to intuitively find what they're looking for. 
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
I decided to stay mostly with default fonts that came with Bootstrap CSS styling. Two fonts I especially liked to continuously use within this project to provide satisfying design:

* Segoe UI - well known, easy to read, fits the page overall style. Used for the page name and login/ registration pages.
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

Based on the Iterative Development idea - while working on this project, I added new functional capabilities and modified existing features as needed over time. Different parts of the project were developed at various times and were integrated based on their successful completion. Increments were build based on their functionality need to not spend efforts on building features not necessary for the project. Subsequent iterations were implemented based on the Users feedback and tests.

MoSCoW prioritization was taken under consideration while creating this project - some of the User Stories were critical (like CRUD functionality, processing orders) compared to other User Stories rather considerable (contact form, Shipments & Returns Q&A, About Us). Those with smaller impact were left for the later phase of page development, while other - vital ones - were guaranteed to be delivered on time. Timeboxing and prioritization were crucial for this project and can be reflected by viewing Iteration process (Todo > In Progress > Done) and labels assigned to each User Story (Must Have, Could Have and Won't Have).

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
* Search bar in the centre on large screens (desktop). Reduced to a loop icon on smaller screens (tablet, mobile) due to space economy.
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
* Information about the number of available products.
* List of the products containing: image, colourful background, name, price.
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
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/product-management.png">
</details>

Product Management page is available to superusers only.
* When logged in as a superuser, "Product Management" is available from "My Account" icon on the top right side.
* Product Management page displays a form, where superuser can add the products to the store.
* The same form is used, when a superuser wants to update a product.

<details> <summary> Shipping And Returns Q&A </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/Q%26A.png">
</details>

Q&A page, where users can learn more about the Shipping and Returns procedures.
* The page has a form of accordion - to view the answer to the question regarding Shipping and Returns - User needs to click on the question, which will reveal the answer.
* Important page, as it displays all the information that customer might be looking for in case of receiving a faulty item or wanting to return the goods.

<details> <summary> About Us </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/aboutus.png">
</details>

About Us page displays the details about the Story Sparks creators - their photos, names, job title and additional information.
* Each creator has a short description field explaining their role in Story Sparks Co. 
* Page brings the User and creators closer - makes the purchase more personal, as the User knows who stands behind the brand.
* When logged in as a superuser - additional buttons are available: "Add new creator", "Update creator" and "Delete creator".
* "Add new creator" takes the superuser to a new page containing a form, which allows to add new members of Story Sparks Co. to the About Us page.

<details> <summary> Contact Form </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/contact-form.png">
</details>

Contact page allows the User to communicate with the Story Sparks Co. Team.
* Page contains a form, where the user can choose the category: Submit a request or Ask a question and add their details.
* Once the contact form is sent - the User receives a success message in the top right corner informing about successful submission.
* In case of any error while sending the form - the user receives an error notification in the top right corner.

## Future Features
* Newsletter Management Panel for the superusers - send a newsletter based on the subscriptions email collection in the database.
* Add more social media accounts.
* Improve the pages design, add more eye-catching homepage elements.
* Add the option for the user to save their name details, not only delivery information.
* Add to the Wishlist option, which will save those items in the User's Profile.
* Add the rating for the products.
* Add more product categories - like accessories, wax melts, tealight sets.
* Add a blog.
* Email to be sent to the customer once contact form is sent.

# Marketing Strategy Implementation
A set of various marketing strategies was implemented for Story Sparks Co. SEO, Social Media Marketing with elements of Content Marketing, Email Marketing - all to ensure Story Sparks success in the Internet by creating visible and trusty online presence. Strong brand equals more customers, involved digital community and steady income.

## Branding
Consistent branding helps with dragging customer's attention and keeps the customers engagement on the high level, as they recognize the social media feed and can associate it with the store.
Story Sparks Co. is aiming to keep it modern, funky and high quality to meet the needs of the Target Audience. 
Strong branding helps to build the trust among customers, who are then more likely to make a purchase or recommend it to their close ones or other people through the social media posts.

## SEO
Customers will most likely find Story Sparks Co. when using Google or other search engine. SEO is very important element to ensure that the page is visible, when search engines are in use:
* I made sure that the content of the page, product descriptions, About Us section, Shipping and Returns Q&A are full of valuable information based on the keywords.
* I ensure that HTML elements boosting CEO are in place: useful alt descriptions for the img elements, meta keywords content in the head element, strong elements and headings.
* I added robots.txt file to allow search engine to crawl the site and allow it to be ranked in search results. 
* I added sitemap.xml to help with crawling the site faster and fetch all relevant content. 
* The site has testimonials on the homepage, Privacy Policy and Terms & Conditions pages to boost the customer's trust and improve search engine rankings.

## Keywords
Keywords have been a consistent thread through all evolutions of search engines. I made sure that Story Sparks page is enriched with helpful informational content, which will allow Google to see it as worthy of a higher search ranking.
I was aiming to find keywords that are high enough volume, but low enough competition to work for the Story Sparks.
I used the [Wordtracker](https://www.wordtracker.com/) to check how much competition is there for my chosen keywords, as the page suggests also other related keywords.
<details> <summary> Wordtracker results </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/wordtracker.png">
</details>

* funny candles
* scented candles
* funny saying candles
* gift ideas for millennials
* candles for him
* candles for her
* funny gift candles
* joke candles
* fragrance oils candle
* natural candles
* organic candles
* best natural candles
* vegan candles

## Newsletter
One of the ways to implement Email Marketing is to use a Newsletter to share deals and information with the customers, who willingly sign up for it. 
This helps the store to communicate directly with potential customers and, convince and encourage them to buy the products (coupons, deals, sales, promo codes).
Anyone visiting the store (no need to be logged in User) can sign up to the newsletter by entering their email address and clicking the "Subscribe" button on in the footer section. 
Newsletter for Story Sparks Co. was created by using the [Mailchimp](https://mailchimp.com/). 

## Social media
Social Media Marketing is a great way to become recognizable for the potential customers within the various social media platforms. It helps with targeting the selected audience, as different social media platforms are attractive to different age groups. Additionally it adds extra links for search engines, building the site's authenticity. 
For this project I created a [Facebook page](https://www.facebook.com/storysparksco) that matches the store in its design.

<details> <summary> Story Sparks Co. Facebook Page </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/facebook.png">
</details>

# Technologies Used
## Languages and Frameworks
* HTML
* CSS
* JavaScript
* Python
* Django - Python Framework used to create the project.
* Bootstrap - CSS framework used for designing the project.

## Other Technologies
* DevTools - help fix problem areas and identify the errors.
* Heroku - project deployment.
* ElephantSQL - database used through Heroku.
* Amazon AWS S3 - store static and media files.
* GitHub, Gitpod - storing code and deploying the site, building and editing the code.
* Notepad++ - help with writing some additional code, experiments and changes.
* Balsamiq - wireframes creation.
* Diagram.net - user journey website diagram creation
* DrawSQL - database models schema creation
* Stripe - supporting store's payments
* TempMail - used for testing purposes

# Content and Credits
* Code Institute's Boutique Ado walkthrough project - base for the project and its functionality.
* Django Testing from Code Institute ['Hello Django' Walkthrough project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/5666926980b74689b37a0d5da3cec510/)
* Color pallete creator and contrast checker were from on [Coolors](https://coolors.co/)
* The collages were created on [VistaCreate](https://create.vista.com/home/)
* [Pinterest](https://www.pinterest.com/) - web design ideas. Color palette idea based on [this pin](https://pl.pinterest.com/pin/598767712973280418/)
* [Printful](https://www.printful.com/custom-candles#create) and [Cortado.ie](https://www.contrado.ie/estore/design/) - creating product visualisations
* [Pexels](https://www.pexels.com/) - images used for Story Sparks Co. About Us:
    * [Image 1](https://www.pexels.com/photo/a-woman-smiling-at-the-camera-8271815/)
    * [Image 2](https://www.pexels.com/photo/smiling-woman-with-burning-candle-at-home-5761126/)
    * [Image 3](https://www.pexels.com/photo/woman-using-a-dropper-7234550/)
    * [Image 4](https://www.pexels.com/photo/a-woman-working-from-home-7005399/)
* [Code Lab](https://www.tutorialrepublic.com/codelab.php?topic=bootstrap&file=testimonial-carousel-with-quote-icon) - Bootstrap Testimonials section
* [CSS Scan](https://getcssscan.com/css-box-shadow-examples) - CSS box-shadow examples to use
* Code Pen - [navigation hover effects]((https://codepen.io/maheshambure21/pen/QwXaRw)) and [rounded side border radius for the order history](https://codepen.io/joeashworth/pen/PXvRzb)
* [The Brandsmen](https://thebrandsmen.com/css-image-hover-effects/) - image hover effects
* Inspiration from the other beautiful CI students projects: [Fresh Nest](https://fresh-nest.herokuapp.com/), [The Chocolate Factory](https://the-chocolate-factory.herokuapp.com/), [Dry Drops](https://dry-drops.herokuapp.com/), [Heiwa Gallery](https://heiwa-gallery.herokuapp.com/) Thank you all!

# Testing
Due to the size of the testing section, I created additional testing page.
Please go to [TESTING.md](TESTING.md) for information on testing and validation.

## Stripe Testing Guidance
When testing site's payments, please use the following from [Stripe's testing documentation](https://stripe.com/docs/testing#cards):

* Stripe test card number, such as 4242 4242 4242 4242.
* Future expiry date, such as 04/24.
* Any three-digit CVC, such as 242.


# Deployment
## Forking The GitHub Repository
To use this code and make changes without affecting the original code you can do what is called 'Forking the repository'. 
By forking this repository you are given a copy of the code at that moment in time that you can use freely. 
To fork this repository you need to follow the following few steps:

1. Create an account or log into your existing GitHub account.
2. Navigate to the [Repository](https://github.com/katzur/story-sparks), you are wanting to fork.
3. In the upper-right of the repository, click the 'Fork' button.
4. A copy of the Repository will now be available within your repositories.

You will now have a copy of the code available to clone and work on without affecting the original code.

## Cloning the Project.
To make a local clone of the project follow these steps:

1. Log into your GitHub account.
2. Navigate to the [Repository](https://github.com/katzur/story-sparks).
3. In the upper section of the repository click the drop-down option: 'Code'.
4. Ensure HTTPS is selected and click the clipboard on the right of the URL to copy it.
5. Open a new workspace in GitPod.
6. Open GitBash. In the bash terminal type 'git clone [copy url here from step 4]'
7. Press enter - the IDE will clone and download the repo.
8. GitBash will clone the repository into this directory.
9. Optionally type: 'python3 manage.py runserver' to host the website locally - it won't run the python file, only allow you see how it looks.
10. To use the required libraries: type in the console: pip3 install -r requirements.txt.
11. To create a web-app from the repo, follow the instructions in "Heroku App Deployment".

## GitHub Desktop App
1. Log in to your GitHub account or create an account.
2. Navigate to the [Repository](https://github.com/katzur/story-sparks).
3. Select the 'Code' button above the file list on the right had side.
4. Select 'Open with GitHub Desktop'
5. Install GitHub Desktop Application.
6. The repo will be copied locally onto your machine.
7. If you want to create a web-app from the repo please follow the instructions in "Heroku App Deployment"

## Download and extract the zip directly from GitHub
1. Log in to your GitHub account
2. Navigate to the [Repository](https://github.com/katzur/story-sparks)
3. Select the 'Code' button above the file list on the right had side
4. Select 'Download Zip'
5. Once you have the Zip downloaded, open it with your preferred file decompression software
6. You can then drag and drop the files from the folder into your chosen IDE or view/edit them on your local machine
7. In the console, run: pip install -r requirements.txt
8. If you want to create a web-app from the repo please follow the instructions in "Project Deployment"

## Deployment - Heroku
To deploy this page to Heroku from its GitHub repository, follow these steps:
### <ins>Create the Heroku App</ins>
- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next, select your region.
- Click on the Create App button.

### <ins>Create a database wth ElephantSQL</ins>
- Log in to [ElephantSQL.com](https://www.elephantsql.com/) to access your dashboard
- If you don't have an ElephantSQL.com account yet, the [steps to create one are here](https://code-institute-students.github.io/deployment-docs/02-elephantsql/elephantsql-01-sign-up).
- Click “Create New Instance”
- Set up your plan: Name, Tiny Turtle (Free) plan, You can leave the Tags field blank
- Select “Select Region” -Select a data center near you
- Click “Review”
- Check your details are correct and then click “Create instance”
- Return to the ElephantSQL dashboard and click on the database instance name for this project
- In the URL section, clicking the copy icon will copy the database URL to your clipboard


### <ins>Attach the ElephantSQL database to Heroku</ins>
- Open the Settings tab in Heroku app, then reveal Config Vars
- Add the config var DATABASE_URL, and for the value, copy in your database url from ElephantSQL. Do not add quotation marks around your database url string.
- Go back to your IDE and install 2 more requirements: `pip3 install dj_database_url==0.5.0 psycopg2`
- Update your requirements.txt file with the newly installed packages by typing: `pip3 freeze --local > requirements.txt`
- In your settings.py file, import dj_database_url underneath the import for os: 
    - `import os`
    - `import dj_database_url`
- Scroll to the DATABASES section and update it to the following:
```
 # DATABASES = {
 #     'default': {
 #         'ENGINE': 'django.db.backends.sqlite3',
 #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #     }
 # }
     
 DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
```
- DO NOT commit this file with your database string in the code, this is temporary so that we can connect to the new database and make migrations.
- In the terminal, run the showmigrations command to confirm you are connected to the external database: `python3 manage.py showmigrations`
- Migrate your database models to your new database: `python3 manage.py migrate`
- Load in the fixtures. Please note the order is very important here. We need to load categories first: `python3 manage.py loaddata categories`
- Then products, as the products require a category to be set: `python3 manage.py loaddata products`
- Create a superuser for your new database: `python3 manage.py createsuperuser`
- Create an if statement in settings.py to run the ElephantSQL database when using the app on heroku or sqlite if not

```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
```
- Create requirements.txt file by typing `pip3 freeze --local > requirements.txt`
- Create a file named "Procfile" in the main directory and add the following: `web: gunicorn project-name.wsgi:application`
- Add Heroku to the ALLOWED_HOSTS list in settings.py in the format ['app_name.heroku.com', 'localhost']
- Push these changes to Github.

### Update Heroku Config Vars
Add the following Config Vars in Heroku:

|     Variable name     |                           Value/where to find value                           |
|:---------------------:|:-----------------------------------------------------------------------------:|
| AWS_ACCESS_KEY_ID     | AWS CSV file(instructions below)                                               |
| AWS_SECRET_ACCESS_KEY | AWS CSV file(instructions below)                                               |
| DATABASE_URL          | ElephantSQL generated (as per step above)                                        |
| EMAIL_HOST_PASS       | Password from email client                                                    |
| EMAIL_HOST_USER       | Site's email address                                                          |
| SECRET_KEY            | Random key generated as above                                                 |
| STRIPE_PUBLIC_KEY     | Stripe Dashboard > Developers tab > API Keys > Publishable key                |
| STRIPE_SECRET_KEY     | Stripe Dashboard > Developers tab > API Keys > Secret key                     |
| STRIPE_WH_SECRET      | Stripe Dashboard > Developers tab > Webhooks > site endpoint > Signing secret |
| USE_AWS               | True (when AWS set up - instructions below)                                   |

### Deploy
- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.

The site is now live and operational.


## AWS Set Up
### AWS S3 Bucket
- Create an AWS account.
- From the 'Services' tab on the AWS Management Console, search 'S3' and select it.
- Click 'Create a new bucket', give it a name(match your Heroku app name if possible), and choose the region closest to you.
- Under 'Object Ownership' select 'ACLs enabled' and leave the Object Ownership as Bucket owner preferred.
- Uncheck block all public access and acknowledge that the bucket will be public.
- Click 'Create bucket'.
- Open the created bucket, go to the 'Properties' tab. Scroll to the bottom and under 'Static website hosting' click 'edit' and change the Static website hosting option to 'enabled'. Copy the default values for the index and error documents and click 'save changes'.
- Open the 'Permissions' tab, locate the CORS configuration section and add the following code:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- In the 'Bucket Policy' section and select 'Policy Generator'.
- Choose 'S3 Bucket Policy' from the type dropdown.
- In 'Step 2: Add Statements', add the following settings:
    - Effect: Allow
    - Principal: *
    - Actions: GetObject
    - ARN: Bucket ARN (copy from S3 Bucket page)
- Click 'Add Statement'.
- Click 'Generate Policy'.
- Copy the policy from the popup that appears
- Paste the generated policy into the Permissions > Bucket Policy area.
- Add '/*' at the end of the 'Resource' key, and save.
- Go to the 'Access Control List' section click edit and enable List for Everyone (public access) and accept the warning box.


### IAM
- From the 'Services' menu, search IAM and select it.
- Once on the IAM page, click 'User Groups' from the side bar, then click 'Create group'. Choose a name and click 'Create'.
- Go to 'Policies', click 'Create New Policy'. Go to the 'JSON' tab and click 'Import Managed Policy'. 
- Search 'S3' and select 'AmazonS3FullAccess'. Click 'Import'.
- Get the bucket ARN from 'S3 Permissions' as per above.
- Delete the '*' from the 'Resource' key and add the following code into the area:

```
"Resource": [
    "YOUR-ARN-NO-HERE",
    "YOUR-ARN-NO-HERE/*"
]
```

- Click 'Next Tags' > 'Next Review' and then provide a name and description and click 'Create Policy'.
- Click'User Groups' and open the created group. Go to the 'Permissions' tab and click 'Add Permissions' and then 'Attach Policies'.
- Search for the policy you created and click 'Add Permissions'.
- You need to create a user to put in the group. Select users from the sidebar and click 'Add user'.
- Give your user a user name, check 'Programmatic Access'.
- Click 'Next' and select the group you created.
- Keep clicking 'Next' until you reach the 'Create user' button and click that.
- Download the CSV file which contains the AWS_SECRET_ACCESS_KEY and your AWS_ACCESS_KEY_ID needed in the Heroku variables as per above list and also in your env.py.


### Connecting S3 to Django 
- Go back to your IDE and install 2 more requirements:
    - `pip3 install boto3`
    - `pip3 install django-storages` 
- Update your requirements.txt file by typing `pip3 freeze --local > requirements.txt` and add storages to your installed apps.
- Create an if statement in settings.py 

```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
```
- Then add the line 

    - `AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'` to tell django where our static files will be coming from in production.


- Create a file called custom storages and import both our settings from django.con as well as the s3boto3 storage class from django storages. 
- Create the following classes:

```
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

- In settings.py add the following inside the if statement:

```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

- and then add the following at the top of the if statement:
```
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

- Go to S3, go to your bucket and click 'Create folder'. Name the folder 'media' and click 'Save'.
- Inside the folder, click 'Upload', 'Add files', and then select all the images that you are using for your site.
- Then under 'Permissions' select the option 'Grant public-read access' and click upload.
- Your static files and media files should be automatically linked from django to your S3 bucket.



# Acknowledgments 
* Huge thank you to my Code Institute fellow students from cohort msletb-nov-2021 and our amazing facilitator Kasia Bogucka.
* Thank you to my mentor Chris Quinn for his precious suggestions and support during this year with Code Institute.
* Thanks to my fiancé Dino for ongoing support and reassurance that stepping into the coding world was the best idea.
* Last but not least thanks to Code Institute's Tutor Support and Student Care Teams for their help, when really needed.


