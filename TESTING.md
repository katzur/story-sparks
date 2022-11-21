# Story Sparks Co. Testing

[Return to the README](README.md)

# Testing Table of Contents:

1. [User Story Testing](#user-story-testing)
2. [Validator Testing](#validator-testing)
    * [HTML](#html)
    * [CSS](#css)
    * [JSHINT](#jshint)
    * [Python Validation - Pycodestyle](#python-validation---pycodestyle)
    * [Lighthouse](#lighthouse)
3. [Device Testing](#device-testing)
4. [Browser Testing](#browser-testing)
5. [Manual Testing](#manual-testing)
6. [Fixed Bugs](#fixed-bugs)


# User Story Testing

<details><summary>As a Site User I can view a list of products so that I can easily select some to purchase.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/products.png">
</details>
List of products is visible for the User, when clicking on "All Candle Types"

As a Site User I can view individual product details so that I can identify the name, price, description, ingredients and product image.
<details><summary>As a Site User I can view individual product details so that I can identify the name, price, description, ingredients and product image.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/product-details.png">
</details>
Individual products are visible, when selecting a product from the all products list. All informations are included in the product detail view: name, price, description, ingredients and product image.

<details><summary>As a Site User I can easily view the total of my purchases at any time so that I can avoid spending too much and have a good overview of the current total.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/bag.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/cart-total.png">
</details>
Total of the purchases can be viewed under the cart icon or once clicked on it on the Shopping Bag page.

<details><summary>As a Site User I can easily register an account so that I can have a personal account and be able to view my profile information: saved address details and past order history.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/signup.png">
</details>
Any User can register an account. Once clicked on the "My Account" button an option to Register appears. User can fill out the form to proceed with the account registration process.

<details><summary>As a Site User I can easily log in an account so that I can access my personal account information.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/login.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/my-profile.png">
</details>
Users, who registered the accounts have an option to log into the page. Once logged in they can view their details and order history by accessing "MY Account" > "My Profile".

<details><summary>As a Site User I can easily log out of my account so that I can ensure no one else can see my personal account information and order history.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/signout.png">
</details>
User, who is already logged in, has an option to logout once selected "My Account" > "Logout". User is then prompted to a new page, where the action confirmation is expected to proceed.

<details><summary>As a Site User I can easily recover my password in case I forget it so that I can recover access to my account.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/forgot-password.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/password-reset.png">
</details>
Whenever the User forgets the password, the page allows to recover access to the account by resetting the password option. Email with further intructions is sent to the User and a new password can be established.

<details><summary>As a Site User I can receive an email confirmation after registering so that I can verify that my account registration was successful.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/verify-email.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/verify-email2.png">
</details>
Once the registration form is completed, the User is directed to a new page with the information to check the email address provided. A new toast message displays on the right side informing, that the confirmation email was sent to provided address. For testing purposes I used TempMail address, which confirms that the email was received from storysparksco@gmail.com asking to confirm the address.

<details><summary>As a Site User I can have a personalized user profile so that I can view my personal order history and order confirmations, as well as save my payment information.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/my-profile.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/order-history.png">
</details>
When the User is logged in, they can view their delivery details and order history by accessing "MY Account" > "My Profile". They have the option to update their personal information. Once cliked on the order number - they can view the confirmation of the past orders with all the details as well.

<details><summary>As a Site User I can sort the list of available products so that I can easily identify the price of the products (ascending / descending) and view the products in the alphabetical order (ascending / descending).</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/sort.png">
</details>
Customers can sort the products using the sorting tool, when accessing all products, selected category, selected scent or running a search. The available options are shown in the dropdown list: sort by price (ascending / descending) and alphabetically (ascending / descending).

<details><summary>As a Site User I can sort a specific category of products so that I can find the products by price or name (ascending/ descending) for that specific category.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/sort.png">
</details>
Customers can sort the products using the sorting tool, when accessing selected category. The available options are shown in the dropdown list: sort by price (ascending / descending) and alphabetically (ascending / descending).

<details><summary>As a Site User I can sort a specific category of products so that I can find the products by price or name (ascending/ descending) for that specific category.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/sort.png">
</details>
Customers can sort the products using the sorting tool, when accessing selected scent. The available options are shown in the dropdown list: sort by price (ascending / descending) and alphabetically (ascending / descending).

<details><summary>As a Site User I can search for the product by name, description or ingredients so that I can find a specific product that I'd like to purchase.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/search.png">
</details>
Customers can search for specific products. Search displays the matching results based on the name, description or ingredients of the products fitting the query.

<details><summary>As a Site User I can easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/search.png">
</details>
Once the search is done the customers can see the number of results matching their query. Based on that they can quickly see if the results are meeting their expectation and if the product they looked for is available within the available products list returning in the search operation.

<details><summary>As a Site User I can easily select the quantity of a product when purchasing it so that I can ensure I don't accidentally select the wrong product or quantity.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/product-details.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/bag.png">
</details>
The quantity of the product can be increased or decreased by the User in the Product Detail page, or in the Shopping bag page.

<details><summary>As a Site User I can view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/bag.png">
</details>
Customer can access their Shopping Bag page by clicking on the cart icon on the top right corner of every page. It'll open a complete list of the products added to the bag, as well as the cost of products, cost of shipping (if applicable), and grand total cost.

<details><summary>As a Site User I can adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before the checkout.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/bag.png">
</details>
The quantity of the product can be increased or decreased by the User in the Shopping bag page. Customer can adjust the quantity by selecting the right number (+/- icons) and clicking update. They can also delete the products by clicking "Delete", to remove unwanted items.

<details><summary>As a Site User I can easily enter my payment information so that I can checkout quickly and with no issues.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/checkout.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/card-invalid.png">
</details>
In the Checkout view the User can add all necessary payment information (bottom left side, under the delivery details). Card number and its type (e.g. Visa, Mastercard etc.), expiry date and CSV code are verified by Stripe. If any of the information for the payment is not correct - customer will see a red notification under the card details and will be asked to enter the details once more.

<details><summary>As a Site User I can ensure that my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/checkout.png">
</details>
Story Sparks Co. uses Stripe elements UI, which provides secure online payments. Page has integrated webhooks - in case there are any issues/ errors during the checkout - the order can be still processed based on entered details. Personal information is safe due to the login/ logout option, which allows the User to finish their session at any time.

<details><summary>As a Site User I can view an order confirmation after the checkout so that I can verify that I haven't made any mistakes.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/order-confirmation.png">
</details>
After completing the checkout procedure customers are brought to a new page, where the order confirmation displays with all the order details. Additionally a success message appears in the top right corner with the order number as well. That information can be additionally view within "My Account" > "My Profile" order history.

<details><summary>As a Site User I can receive an email confirmation after checking out so that I can keep the confirmation on what I've purchased for my own records.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/email-order-confirmation.png">
</details>
Besides the order history within "My Profile" and order confirmation page - customers are also receiving emails confirming their purchase for their own record.

<details><summary>As a Site User I can view the terms & conditions so that I can understand better terms & conditions of using the store.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/termsconditions.png">
</details>
In the footer section on every page, there's a link to the Terms & Conditions section for User's acknowledgement.

<details><summary>As a Site User I can view the privacy policy settings so that I can understand better store's privacy policy and how they use my data.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/privacypolicy.png">
</details>
In the footer section on every page, there's a link to the Privacy Policy section for User's acknowledgement.

<details><summary>As a Site User I can subscribe to a newsletter so that I can get all the latest offers and information regarding the store and products, as well as special deals.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/newsletter.png">
</details>
In the footer section on every page, there's a section for the Newsletter, where the User can subscribe by clicking "Subscribe" to receive all the information and deals from Story Sparks Co. The newsletter is supported by Mailchimp.

<details><summary>As a Site User I can see the store's social media accounts links so that I can easily access store's social media pages and profiles to view the information, posts etc.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/footer.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/home3.png">
</details>
Social media links are accessible on every page in the footer section on the top left side. Additionally there's information about the Instagram profile account in the banner on the homepage.
Customer can click on the social media icon to be moved to that specific page in a new window. For the purposes of this project a Facebook page was created to meet the Web marketing objectives.

<details><summary>As a Site User I can view the logos and links for any external resources so that I can identify the organizations and movements the store works with to identify the store's mission and profile.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/footer.png">
</details>
Logos of the organizations and movements Story Sparks Co. collaborates with are displayed on every page in the footer section on the right side. Once clicked on the logo, the User is moved to the specific page of that organization/ movement in a new window.

<details><summary>As a Site User I can view the testimonials of other media accounts (magazines, radio, TV), who tested the Story Spark's products so that I can see what are their opinions about the company and its products.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/home2.png">
</details>
"What Others Are Saying" section on the homepage was created for the media testimonials in approachable carrousel style form. 

<details><summary>As a Site User I can quickly identify special offers so that I can take advantage of special savings on products I'd like to purchase.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/home2.png">
</details>
Special Offers section is available through one of the tiles on the homepage, as well as through the navbar on the top under "All Candle Types" as one of the available categories.

<details><summary>As a Site User I can view the About Us section so that I can learn more about the Story Sparks Co. owners and employees.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/aboutus.png">
</details>
Users can access About Us page from the navbar on the top in the About & Contact section, as well as from the footer on every page (middle pane links). Additionally there's a paragraph on the homepage with a link that allows the User to be redirected to that page as well.

<details><summary>As a Site User I can view the shipment and returns Q&A section so that I can get more information about the shipping time, return options and international deliveries.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/Q%26A.png">
</details>
Additional page was created to answer User's questions regarding shipments and returns. It was created in approachable accordeon style - User can click on the question and a new section appears underneath with the answer.

<details><summary>As a Site User I can use the contact form so that I can communicate directly with the store to send them a query/ questions regarding the product/store.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/contact-form.png">
</details>
Contact form was created for the Users to be able to send messages to the Story Spark's Team directly. Page can be accessed from the navar About & Contact, as well as from the footer section on every page (middle pane links). Customer can fill the details in the contact form, select a type of the query and click "Submit". Based on the outcome of the operation - a small message appears on the right side informing about the success/ failure of this operation.

<details><summary>As a Site Admin I can add a product so that I can add new items to my store.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/product-management.png">
</details>
Superuser can add the product through the Product Management page. It can be accessed from "My Account" icon on the top right. It opens a form, where the superuser can add all the product details, image and add product by clicking on "Add Product" button.

<details><summary>As a Site Admin I can edit/update a product so that I can change product price, image, description, name, ingredients.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/product-details.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/products.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/edit-product.png">
</details>
A superuser can edit/ update products. Available icons to perform those operations are available within the all products view or product details page. Once clied on "Edit" a new page opens for the Product Management with information on the top that the superuser is editing the product. All product details will autopopulate based on the information saved in the database.

<details><summary>As a Site Admin I can delete a product so that I can remove items that are no longer available.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/product-details.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/products.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/edit-product.png">
</details>
A superuser can delete products. Available icons to perform those operations are available within the all products view or product details page. Once clied on "Delete" product is removed from the database.

<details><summary>As a Site Admin I can add a new creator to About Us section so that I can add new people, who work for Story Sparks Co.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/aboutus.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/add-creator.png">
</details>
Superusers can add new team members of Story Sparks Co. to About Us section. Once logged in as superuser in the About Us a new button appears "Add new creator". Once clicked a new window appears, where the details can be provided to the form: name, job, description and image. Once saved - a new information appears within the About Us, which can be accessible for the Users from the About & Contact section in the navbar.

<details><summary>As a Site Admin I can edit/update a creator to About Us section so that I can change the information and photos of people, who work for Story Sparks Co.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/aboutus.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/update-creator.png">
</details>
Superusers can edit/ update exisiting team members of Story Sparks Co. in About Us section. Once logged in as superuser in the About Us a new button appears "Update creator". Once clicked a new window appears, where the details are autopopulated based on the exisiting information in the database: name, job, description and image. Once new information is added, it can be saved by clicking "Update creator" - updated information will appear within the About Us, which can be accessible for the Users from the About & Contact section in the navbar.

<details><summary>As a Site Admin I can delete a creator from About Us section so that I can remove people, who no longer work for Story Sparks Co.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/aboutus.png">
</details>
Superusers can delete exisiting team members of Story Sparks Co. in About Us section. Once logged in as superuser in the About Us a new button appears "Delete creator". Once clicked - the exisiting entry will be deleted and new updated version of About Us will be available for the users.

# Validator Testing
## HTML
All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). See results in the table below.