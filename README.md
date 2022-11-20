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
    * [Epics](#epics)
    * [Kanban Board](#kanban-board)
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

