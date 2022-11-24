# Story Sparks Co. Testing

[Return to the README](README.md)

# Testing Table of Contents:

1. [User Story Testing](#user-story-testing)
2. [Validator Testing](#validator-testing)
    * [HTML](#html)
    * [CSS](#css)
    * [JSHint](#jshint)
    * [Python Validation](#python-validation)
    * [Lighthouse](#lighthouse)
3. [Device Testing](#device-testing)
4. [Browser Testing](#browser-testing)
5. [Manual Testing](#manual-testing)
6. [Fixed Bugs](#fixed-bugs)
7. [Unfixed Bugs](#unfixed-bugs)
8. [Responsiveness Testing](#responsiveness-testing)


# User Story Testing

<details><summary>As a Site User I can view a list of products so that I can easily select some to purchase.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/products.png">
</details>
List of products is visible for the User, when clicking on "All Candle Types"

As a Site User I can view individual product details so that I can identify the name, price, description, ingredients and product image.
<details><summary>As a Site User I can view individual product details so that I can identify the name, price, description, ingredients and product image.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/product-details.png">
</details>
Individual products are visible, when selecting a product from the all products list. All information is included in the product detail view: name, price, description, ingredients and product image.

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
Whenever the User forgets the password, the page allows to recover access to the account by resetting the password option. Email with further instruction is sent to the User and a new password can be established.

<details><summary>As a Site User I can receive an email confirmation after registering so that I can verify that my account registration was successful.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/verify-email.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/verify-email2.png">
</details>
Once the registration form is completed, the User is directed to a new page with the information to check the email address provided. A new toast message displays on the right side informing, that the confirmation email was sent to provided address. For testing purposes I used TempMail address, which confirms that the email was received from storysparksco@gmail.com asking to confirm the address.

<details><summary>As a Site User I can have a personalized user profile so that I can view my personal order history and order confirmations, as well as save my payment information.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/my-profile.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/order-history.png">
</details>
When the User is logged in, they can view their delivery details and order history by accessing "MY Account" > "My Profile". They have the option to update their personal information. Once clicked on the order number - they can view the confirmation of the past orders with all the details as well.

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
Additional page was created to answer User's questions regarding shipments and returns. It was created in approachable accordion style - User can click on the question and a new section appears underneath with the answer.

<details><summary>As a Site User I can use the contact form so that I can communicate directly with the store to send them a query/ questions regarding the product/store.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/contact-form.png">
</details>
Contact form was created for the Users to be able to send messages to the Story Spark's Team directly. Page can be accessed from the navbar About & Contact, as well as from the footer section on every page (middle pane links). Customer can fill the details in the contact form, select a type of the query and click "Submit". Based on the outcome of the operation - a small message appears on the right side informing about the success/ failure of this operation.

<details><summary>As a Site Admin I can add a product so that I can add new items to my store.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/product-management.png">
</details>
Superuser can add the product through the Product Management page. It can be accessed from "My Account" icon on the top right. It opens a form, where the superuser can add all the product details, image and add product by clicking on "Add Product" button.

<details><summary>As a Site Admin I can edit/update a product so that I can change product price, image, description, name, ingredients.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/product-details.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/products.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/edit-product.png">
</details>
A superuser can edit/ update products. Available icons to perform those operations are available within the all products view or product details page. Once clicked on "Edit" a new page opens for the Product Management with information on the top that the superuser is editing the product. All product details will autopopulate based on the information saved in the database.

<details><summary>As a Site Admin I can delete a product so that I can remove items that are no longer available.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/product-details.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/products.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/edit-product.png">
</details>
A superuser can delete products. Available icons to perform those operations are available within the all products view or product details page. Once clicked on "Delete" product is removed from the database.

<details><summary>As a Site Admin I can add a new creator to About Us section so that I can add new people, who work for Story Sparks Co.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/aboutus.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/add-creator.png">
</details>
Superusers can add new team members of Story Sparks Co. to About Us section. Once logged in as superuser in the About Us a new button appears "Add new creator". Once clicked a new window appears, where the details can be provided to the form: name, job, description and image. Once saved - a new information appears within the About Us, which can be accessible for the Users from the About & Contact section in the navbar.

<details><summary>As a Site Admin I can edit/update a creator to About Us section so that I can change the information and photos of people, who work for Story Sparks Co.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/aboutus.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/update-creator.png">
</details>
Superusers can edit/ update existing team members of Story Sparks Co. in About Us section. Once logged in as superuser in the About Us a new button appears "Update creator". Once clicked a new window appears, where the details are autopopulated based on the existing information in the database: name, job, description and image. Once new information is added, it can be saved by clicking "Update creator" - updated information will appear within the About Us, which can be accessible for the Users from the About & Contact section in the navbar.

<details><summary>As a Site Admin I can delete a creator from About Us section so that I can remove people, who no longer work for Story Sparks Co.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/aboutus.png">
</details>
Superusers can delete existing team members of Story Sparks Co. in About Us section. Once logged in as superuser in the About Us a new button appears "Delete creator". Once clicked - the existing entry will be deleted and new updated version of About Us will be available for the users.

# Validator Testing
## HTML
All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). See results in the table below:

| Page                           | Result     | 
|--------------------------------|------------|
| Home                           | No Errors  |
| All Products                   | No Errors  |
| Product Detail                 | Note       |
| Search Result                  | No Errors  |
| Add Product                    | N/A        |
| Edit Product                   | N/A        |
| Confirm Delete Product         | N/A        |
| Bag                            | No Errors  |
| Checkout                       | No Errors  |
| Checkout Success               | No Errors  |
| Profile                        | N/A        |
| Order History                  | N/A        |
| Product Management             | N/A        |
| Contact                        | No Errors  |
| Sign In                        | No Errors  |
| Sign Up                        | No Errors  |
| Log Out                        | No Errors  |
| Password Reset                 | No Errors  |
| 404.html                       | N/A        |
| 500.html                       | N/A        |
| About Us                       | No Errors  |
| Add Creator                    | N/A        |
| Edit Creator                   | N/A        |
| Confirm Delete Creator         | N/A        |
| Returns & Shipping             | No Errors  |

NOTE: Product Details - error related to additional  
````
</p> 
````
element.

Based on the code for Product Details - no issues were seen in line 35. Please compare the validation with the actual code:

<details><summary>Error displayed for the Product Details page within the Validator</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/html-error1.png">
</details>

<details><summary>Checking within the source code, where the issue was found by the Validator.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/html-error2.png">
</details>

<details><summary>Comparing it with the actual code - issue pointed by the Validator not found.</summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/html-error3.png">
</details>

## CSS
No errors were found when passing CSS direct input through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
<details> <summary> Check the result of the test for base.css, checkout.css, profile.css </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/css-validation.png">
</details>

## JSHint
All Javascript was passed through [JSHint](https://jshint.com/) with no issues.

<details> <summary> Base </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/base.html_js.png">
</details>

<details> <summary> Products </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/products.html_js.png">
</details>

<details> <summary> Profile </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/profile_js.png">
</details>

<details> <summary> Checkout </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/checkout_js.png">
</details>

<details> <summary> Bag </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/base.html_js.png">
</details>

<details> <summary> Product Quantity </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/quantity_js.png">
</details>

## Python Validation
For the Python testing I used PEP8 and [flake8](https://pypi.org/project/flake8/) to check for any syntax errors.
The errors found (please refer to the screenshot below) can be ignored, as they are automatically generated files (such as migrations).
Formatting errors for settings.py were ignored to not disrupt the settings functionality for AUTH_PASSWORD_VALIDATORS. 
Imported but unused for empty test files, models and admin files were ignored as well, as they don't disrupt the functionality and are irrelevant.
<details> <summary> flake8 </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/flake1.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/flake2.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/flake3.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/flake4.png">
</details>


## Lighthouse
Lighthouse validation was performed for all the pages to verify their performance. Based on the Lighthouse suggestions I fixed some of the issues regarding missing labels for the Search button element and issue with 'Background and foreground colours do not have a sufficient contrast ratio' for the Checkout page regarding the muted-text class not being readable enough on the beige background.
Scores are listed below for the pages:

<details> <summary> About Us </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/lighthouse-about-us.png">
</details>

<details> <summary> All Products </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/lighthouse-all-products.png">
</details>

<details> <summary> Checkout </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/lighthouse-checkout.png">
</details>

<details> <summary> Contact </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/lighthouse-contact.png">
</details>

<details> <summary> Homepage </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/lighthouse-homepage.png">
</details>

<details> <summary> My Profile </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/lighthouse-my-profile.png">
</details>

<details> <summary> Product Details </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/lighthouse-product-details.png">
</details>

<details> <summary> Product Management </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/lighthouse-product-management.png">
</details>

<details> <summary> Shipping & Returns </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/lighthouse-shipping.png">
</details>

<details> <summary> Shopping Bag </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/lighthouse-shopping-bag.png">
</details>


# Device Testing
The store pages were viewed and tested on a variety of devices such as Desktop, Large Desktop, Laptop 13", iPhone 13mini, iPhoneX and iPad to ensure responsiveness on different screen sizes. 
The page performed as expected. The responsive design was also checked using Chrome Developer Tools across multiple devices. Additionally it was tested through [Am I Responsive?](https://ui.dev/amiresponsive) to provide a demo.
<details> <summary> Am I Responsive Demo </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/amiresponsive.png">
</details>


# Browser Testing
The page was tested using Chrome, Firefox, Safari and Edge browsers without any issues.

# Manual Testing
## Site Navigation
| Element                          | Action                        | Expected Result                                              | Pass?     |
|----------------------------------|-------------------------------|--------------------------------------------------------------|-----------|
| **Header**                       |                               |                                                              |           |
| Site Name (logo area)            | Click                         | Redirect to home                                             | &check;   |
| Search Box Function              | Enter Text and Click Search   | Search in the product's name, description and ingredients    | &check;   |
| My Account Dropdown              | Click                         | Open profile dropdown                                        | &check;   |
| Sign Up Link                     | Click                         | Redirect to Sign Up page (for not logged in users)           | &check;   |
| Login Link                       | Click                         | Redirect to login page (for not logged in users)             | &check;   |
| Product Management               | Click                         | Opens add new product page                                   | &check;   |
| My Profile                       | Click                         | Opens new page to manage user account and view the history   | &check;   |
| Logout                           | Click                         | Log out from their account - redirect to check out page      | &check;   |
| Cart                             | Click                         | Redirects to the Shopping Bag Page and displays total cost   | &check;   |
| **Navbar**                       |                               |                                                              |           |
| All Candle Types                 | Click                         | Opens dropdown with categories                               | &check;   |
| All Products                     | Click                         | Redirect all products page                                   | &check;   |
| Jars                             | Click                         | Redirects to page filtered to jar category                   | &check;   |
| Tins                             | Click                         | Redirects to page filtered to tin category                   | &check;   |
| Special Offers                   | Click                         | Redirects to page filtered to special offers category        | &check;   |
| Scents                           | Click                         | Opens dropdown with available scent types                    | &check;   |
| Sweet and fruity                 | Click                         | Redirects to page filtered to sweet and fruity scents        | &check;   |
| Warm and deep                    | Click                         | Redirects to page filtered to warm and deep scents           | &check;   |
| Floral                           | Click                         | Redirects to page filtered to floral scents                  | &check;   |
| Fresh                            | Click                         | Redirects to page filtered to fresh scents                   | &check;   |
| Autumn Spices                    | Click                         | Redirects to page filtered to autumn spices scents           | &check;   |
| About & Contact                  | Click                         | Opens dropdown with About Us, Contact and Shipping Q&A       | &check;   |
| About Us                         | Click                         | Opens page with creators information                         | &check;   |
| Contact                          | Click                         | Opens page with comntact form                                | &check;   |
| Shipping and Returns             | Click                         | Opens page with shipping and returns q&a                     | &check;   |
| **Mobile Top Header**            |                               |                                                              |           |
| Search Icon Button               | Click                         | Open up search box                                           | &check;   |
| Search Box Function              | Enter Text and Click Search   | Search both the product's name, description and ingredients  | &check;   |
| My Account Dropdown              | Click                         | Open profile dropdown                                        | &check;   |
| Sign Up Link                     | Click                         | Redirect to Sign Up page (for not logged in users)           | &check;   |
| Login Link                       | Click                         | Redirect to login page (for not logged in users)             | &check;   |
| Product Management               | Click                         | Opens add new product page                                   | &check;   |
| My Profile                       | Click                         | Opens new page to manage user account and view the history   | &check;   |
| Logout                           | Click                         | Log out from their account - redirect to check out page      | &check;   |
| Cart                             | Click                         | Redirects to the Shopping Bag Page and displays total cost   | &check;   | 
| Hamburger Menu                   | Responsive                    | Display when screen size reduces to medium size              | &check;   | 
| Home Link                        | Click                         | Redirect to home                                             | &check;   | 
| **Footer**                       |                               |                                                              |           |
| Social Media Icon Links          | Click                         | Open correct location in new tab                             | &check;   | 
| Newsletter Email field           | Insert incorrect/empty format | On submit: form won't submit                                 | &check;   | 
| Newsletter Email field           | Insert incorrect/empty format | Error message displays                                       | &check;   | 
| Subscribe Button                 | Click                         | Form submit                                                  | &check;   | 
| Subscribe Button                 | Click                         | Message appears saying Thank You for subscribing!            | &check;   | 
| All Products Link                | Click                         | Open All Products Page                                       | &check;   |
| About Us Link                    | Click                         | Open About Us Page                                           | &check;   |
| Contact Link                     | Click                         | Open Contact Page                                            | &check;   |
| Shipping and Returns Link        | Click                         | Open Shipping and Returns Page                               | &check;   |
| Privacy Policy Link              | Click                         | Open Privacy Policy Page in new tab                          | &check;   |
| Terms & Conditions Links         | Click                         | Open Terms & Conditions in new tab                           | &check;   |

## Allauth Pages 

| Element                         | Action                                    | Expected Result                              | Pass?     |
|---------------------------------|-------------------------------------------|----------------------------------------------|-----------|
| **Sign Up**                     |                                           |                                              |           |
| Sign in link                    | Click                                     | Redirect to sign in page                     | &check;   |
| Email field                     | Insert incorrect format                   | On submit: form won't submit                 | &check;   |
| Email field                     | Insert incorrect format                   | Error message displays                       | &check;   |
| Email field                     | Insert correct format                     | On submit: form submit                       | &check;   |
| Email field                     | Leave empty                               | On submit: form won't submit                 | &check;   |
| Email field                     | Insert duplicate email                    | On submit: form won't submit                 | &check;   |
| Email field                     | Insert duplicate email                    | Error message displays                       | &check;   |
| Email Confirmation field        | Insert different email                    | On submit: form won't submit                 | &check;   |
| Email Confirmation field        | Insert different email                    | Error message displays                       | &check;   |
| Username field                  | Leave empty/incorrect format              | On submit: form won't submit                 | &check;   |
| Username field                  | Leave empty/incorrect format              | Error message displays                       | &check;   |
| Username field                  | Insert correct format                     | On submit: form submit                       | &check;   |
| Username field                  | Insert duplicate username                 | On submit: form won't submit                 | &check;   |
| Username field                  | Insert duplicate username                 | Error message displays                       | &check;   |
| Password field                  | Insert incorrect format/length            | On submit: form won't submit                 | &check;   |
| Password field                  | Insert incorrect format/length            | Error message displays                       | &check;   |
| Password field                  | Passwords don't match                     | On submit: form won't submit                 | &check;   |
| Password field                  | Passwords don't match                     | Error message displays                       | &check;   |
| Password field                  | Insert correct format + passwords match   | On submit: form submit                       | &check;   |
| Sign Up button(form valid)      | Click                                     | Form submit                                  | &check;   |
| Sign Up button(form valid)      | Click                                     | Redirect to Verify Email Address page        | &check;   |
| Sign Up button(form valid)      | Click                                     | Alert message confirming email sent appears  | &check;   |
| Confirmation Email Confirm Link | Click                                     | Open Confirm Email Address Page              | &check;   |
| Confirm Button                  | Click                                     | Success message confirming new user appears  | &check;   |
| Confirm Button                  | Click                                     | Redirect to sign in page                     | &check;   |
|                                 |                                           |                                              |           |
| **Log in**                      |                                           |                                              |           |
| Sign up link                    | Click                                     | Redirect to sign up page                     | &check;   |
| Username field                  | Leave empty                               | On submit: form won't submit                 | &check;   |
| Username field                  | Leave empty                               | Error message displays                       | &check;   |
| Username field                  | Insert wrong username                     | On submit: form won't submit                 | &check;   |
| Username field                  | Insert wrong username                     | Error message displays                       | &check;   |
| Password field                  | Leave empty                               | On submit: form won't submit                 | &check;   |
| Password field                  | Leave empty                               | Error message displays                       | &check;   |
| Password field                  | Insert wrong password                     | On submit: form won't submit                 | &check;   |
| Password field                  | Insert wrong password                     | Error message displays                       | &check;   |
| Login button(form valid)        | Click                                     | Form submit                                  | &check;   |
| Login button(form valid)        | Click                                     | Redirect to home page                        | &check;   |
| Login button(form valid)        | Click                                     | Success message confirming login appears     | &check;   |
| Forgot Password Link            | Click                                     | Redirect to Password Reset page              | &check;   |
| Email field                     | Leave empty/incorrect format              | On submit: form submit                       | &check;   |
| Reset My Password Button        | Click                                     | Confirmation message that email sent         | &check;   |
| Password Reset Email Link       | Click                                     | Open Change Password Page                    | &check;   |
| Change Password Button          | Click                                     | Success message confirming Password Changed  | &check;   |
|                                 |                                           |                                              |           |
| **Sign Out**                    |                                           |                                              |           |
| Sign Out  button                | Click                                     | Redirect to homepage                         | &check;   |
| Sign Out  button                | Click                                     | Success message confirming Sign Out  appears | &check;   |


## All Products

| Element                         | Action  | Expected Result                                                                                | Pass?     |
|---------------------------------|---------|------------------------------------------------------------------------------------------------|-----------|
| Sort By  Dropdown               | Click   | Open 'sort by' options                                                                         | &check;   |
| Sort By  Options                | Click   | Re-order products correctly (alphabetically or by price)                                       | &check;   |
| Product Name                    | Display | Displays correct name of products on page                                                      | &check;   |
| Product Price                   | Display | Displays product price                                                                         | &check;   |
| Product Details                 | Click   | Redirect to product detail page                                                                | &check;   |
| If Searched Product             | Display | Only display products with search term in the product's name, description or ingredients       | &check;   |
| If Searched Product             | Display | Display number of products found for searched product                                          | &check;   |
| **Superuser logged in**         |         |                                                                                                |           |
| Edit product link               | Click   | Redirect to edit product page                                                                  | &check;   |
| Delete product link             | Click   | Delete the product                                                                             | &check;   |

## Product Detail

| Element                  | Action                    | Expected Result                                                                              | Pass?     |
|--------------------------|---------------------------|----------------------------------------------------------------------------------------------|-----------|
| Product Content          | Display                   | Display correct product image, name, price, product details and ingredients                  | &check;   |
| Qty control buttons      | Click                     | Increase/decrease quantity                                                                   | &check;   |
| Qty control buttons      | Click                     | Minus button disabled if quantity is 1                                                       | &check;   |
| Qty control buttons      | Click                     | Plus button disabled if quantity is 99                                                       | &check;   |
| Qty control buttons      | Manually Input  <1 or >99 | If quantity >99 or <1 manually entered, error message appears when Add to Bag button clicked | &check;   |
| Keep Shopping button     | Click                     | Redirect to home decor page                                                                  | &check;   |
| Add to bag button        | Click                     | Add item to bag                                                                              | &check;   |
| Add to bag button        | Click                     | Toast Success appears                                                                        | &check;   |
| Add to bag button        | Click                     | Product and quantity visible in toast success                                                | &check;   |
| **Superuser logged in**  |                           |                                                                                              |           |
| Edit product link        | Click                     | Redirect to edit product page                                                                | &check;   |
| Delete product link      | Click                     | Delete the product                                                                           | &check;   |

## Product Management 

| Element                         | Action                | Expected Result                                                                                                            | Pass?     |
|---------------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------|-----------|
| **Add Product**                 |                       |                                                                                                                            |           |
| Add Product                     | Access                | If a user tries to add a product (by changing the url) without being signed in they are redirected to the login page       | &check;   |
| Add Product                     | Access                | If a user tries to add a product (by changing the url) without being superuser they are redirected to a custom 403 page    | &check;   |
| Form Text Input (if required)   | Leave blank           | On Submit: Warning appears, form won't submit                                                                              | &check;   |
| Form Text Input (if required)   | Just input whitespace | On Submit: Form won't submit                                                                                               | &check;   |
| Form image select button        | Click                 | Open device storage                                                                                                        | &check;   |
| Form image select button        | Display               | Chosen image name displayed once selected                                                                                  | &check;   |
| Form image select button        | Display               | Default image is used if no image is selected                                                                              | &check;   |
| Cancel button                   | Click                 | Redirect to All Products page                                                                                              | &check;   |
| Add Product button (form valid) | Click                 | Form submit                                                                                                                | &check;   |
| Add Product button (form valid) | Click                 | Redirect to Product detail page for new product with all information displaying correctly                                  | &check;   |
| Add Product button (form valid) | Click                 | Success message appears informing the superuser that the product has been added                                            | &check;   |
|                                 |                       |                                                                                                                            |           |
|                                 |                       |                                                                                                                            |           |
| **Edit Product**                |                       |                                                                                                                            |           |
| Edit Product                    | Access                | If a user tries to add a product (by changing the url) without being signed in they are redirected to the login page       | &check;   |
| Edit Product                    | Access                | If a user tries to add a product (by changing the url) without being superuser they are redirected to a custom 403 page    | &check;   |
| Edit Product Form               | Display               | Form has all the fields filled out with the original content                                                               | &check;   |
| Edit Product Form               | Image Field           | Thumbnail of original image is shown                                                                                       | &check;   |
| Form Text Input (if required)   | Leave blank           | On Submit: Warning appears, form won't submit                                                                              | &check;   |
| Form Text Input (if required)   | Just input whitespace | On Submit: Form won't submit                                                                                               | &check;   |
| Cancel button                   | Click                 | Redirect to All Products page                                                                                              | &check;   |
| Submit button(form valid)       | Click                 | Form submit                                                                                                                | &check;   |
| Edit Product button(form valid) | Click                 | Redirect to Product detail page for new product with all information displaying correctly                                  | &check;   |
| Edit Product button(form valid) | Click                 | Success message appears informing the superuser that the product has been updated                                          | &check;   |
|                                 |                       |                                                                                                                            |           |
| **Confirm Delete Product**      |                       |                                                                                                                            |           |
| Delete Product                  | Access                | If a user tries to Delete a product (by changing the url) without being signed in they are redirected to the login page    | &check;   |
| Delete Product                  | Access                | If a user tries to Delete a product (by changing the url) without being superuser they are redirected to a custom 403 page | &check;   |
| Confirm Delete -  cancel button | Click                 | Redirect to All Products page                                                                                              | &check;   |
| Confirm Delete -  delete button | Click                 | Delete product                                                                                                             | &check;   |
| Confirm Delete -  delete button | Click                 | Success message appears confirming product deleted successfully                                                            | &check;   |   


## Bag

| Element                                                       | Action              | Expected Result                                        | Pass?     |
|---------------------------------------------------------------|---------------------|--------------------------------------------------------|-----------|
| **No Items in the Bag**                                       |                     |                                                        |           |
| Keep Shopping button                                          | Click               | Redirect to home decor page                            | &check;   |  
| **Items in the Bag**                                          |                     |                                                        |           |
| Qty control buttons                                           | Click               | Increase/decrease quantity                             | &check;   |  
| Qty control buttons                                           | Click               | Minus button disabled if quantity is 1                 | &check;   |  
| Qty control buttons                                           | Click               | Plus button disabled if quantity is 99                 | &check;   |  
| Qty control buttons                                           | Manually Input  >99 | Error message appears when refresh button is clicked   | &check;   |  
| Qty control buttons                                           | Manually Input  <1  | Shopping bag is emptied when refresh button is clicked | &check;   |  
| Refresh Icon button                                           | Click               | Update bag item quantity                               | &check;   |  
| Refresh Icon button                                           | Refresh Icon button | Updated confirmation toast appears                     | &check;   |  
| Bin Icon button                                               | Click               | Remove item from bag                                   | &check;   |  
| Bin Icon button                                               | Click               | Removed confirmation toast appears                     | &check;   |  
| Line item subtotal / Bag total / Delivery cost / Grand Total  | Calculate           | All numbers are calculated correctly                   | &check;   |  
| Continue shopping button                                      | Click               | Redirect to products page                              | &check;   |  
| Secure Checkout button                                        | Click               | Redirect to checkout page                              | &check;   |  

## Checkout

| Element                             | Action                          | Expected Result                                                     | Pass?     |
|-------------------------------------|---------------------------------|---------------------------------------------------------------------|-----------|
| Checkout Page                       | Direct URL input (empty bag)    | Redirect to products page                                           | &check;   | 
| Checkout Page                       | Direct URL input (empty bag)    | Empty bag toast appears                                             | &check;   | 
| Form fields(if user logged in)      | On load                         | Fields populated with user default info (if previously saved)       | &check;   | 
| Text Input(if required)             | Leave blank                     | On submit:form won't submit                                         | &check;   | 
| Text Input(if required)             | Leave blank                     | Error message on invalid field(s)                                   | &check;   | 
| Text Input(if required)             | Just whitespace                 | On submit:form won't submit                                         | &check;   | 
| Text Input(if required)             | Just whitespace                 | Error message on invalid field(s)                                   | &check;   | 
| Text Input(if required)             | Fill in correctly               | On submit: form submits                                             | &check;   | 
| Phone number Input                  | Leave blank                     | On submit:form won't submit                                         | &check;   | 
| Phone number Input                  | Leave blank                     | Error message on field                                              | &check;   | 
| Phone number Input                  | Just whitespace                 | On submit:form won't submit                                         | &check;   | 
| Phone number Input                  | Just whitespace                 | Error message on field                                              | &check;   | 
| Phone number Input                  | Use non numeric characters      | On submit:form won't submit                                         | &check;   | 
| Phone number Input                  | Use non numeric characters      | Error message on field                                              | &check;   | 
| Email Input                         | Leave blank                     | On submit:form won't submit                                         | &check;   | 
| Email Input                         | Leave blank                     | Error message on field                                              | &check;   | 
| Email Input                         | Just whitespace                 | On submit:form won't submit                                         | &check;   | 
| Email Input                         | Just whitespace                 | Error message on field                                              | &check;   | 
| Email Input                         | Fill in correctly               | On submit: form submits                                             | &check;   | 
| Save to profile checkbox            | On load(user logged in)         | Shown                                                               | &check;   | 
| Save to profile checkbox            | On load(user not logged in)     | Not shown                                                           | &check;   | 
| Save to profile checkbox            | Checked                         | On submit: Delivery information saved to user profile               | &check;   | 
| Save to profile checkbox            | Unchecked                       | On submit: Delivery information not saved to user profile           | &check;   | 
| Payment card input                  | Input invalid card number       | Error message on field                                              | &check;   | 
| Payment card input                  | Input invalid date              | Error message on field                                              | &check;   | 
| Adjust Bag button                   | Click                           | Redirect to bag page                                                | &check;   | 
| Complete Order button(form invalid) | Click                           | Form won't submit                                                   | &check;   | 
| Complete Order button(form invalid) | Click                           | Error message on invalid fields                                     | &check;   | 
| Complete Order button(form valid)   | Payment succeeds                | Loading screen reappears                                            | &check;   | 
| Complete Order button(form valid)   | Payment succeeds                | Form submits                                                        | &check;   | 
| Complete Order button(form valid)   | Payment succeeds                | Redirect to order confirmation page                                 | &check;   | 
| Complete Order button(form valid)   | (if user logged in)             | Order saved to user profile                                         | &check;   | 
| Complete Order button(form valid)   | Payment failed                  | Loading animation appears                                           | &check;   | 
| Complete Order button(form valid)   | Payment failed                  | Form won't submit                                                   | &check;   | 
| Complete Order button(form valid)   | Payment failed                  | Error message at bottom of form                                     | &check;   | 
| Complete Order button(form valid)   | Click                           | Success message appears confirming order successfully processed     | &check;   | 
| Complete Order button(form valid)   | Payment Requires authentication | Authentication box appears                                          | &check;   | 
| Fail Authentication button          | Click                           | Authentication box closes                                           | &check;   | 
| Fail Authentication button          | Click                           | User directed back to form                                          | &check;   | 
| Fail Authentication button          | Click                           | Error message at bottom of form                                     | &check;   | 
| Complete Authentication button      | Click                           | Loading screen reappears                                            | &check;   | 
| Complete Authentication button      | Click                           | Form submits                                                        | &check;   | 
| Complete Authentication button      | Click                           | Redirect to order confirmation page                                 | &check;   | 
| Complete Order button(form valid)   | Click                           | Success message appears confirming order successfully processed     | &check;   | 
| Complete Order button(form valid)   | Click                           | User receives an order confirmation email with correct information  | &check;   | 
| **Checkout Success Page**           |                                 |                                                                     |           |
| Order Confirmation                  | Display                         | Display Correct Order Details                                       | &check;   | 
| Keep Shopping! button               | Click                           | Redirect to products page                                           | &check;   | 

## My Profile

| Element                | Action            | Expected Result                                                                                                                | Pass?     |
|------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------|
| Open My Profile Page   | Access            | If a user tries to access the profile page (by changing the url) without being signed in they are redirected to the login page | &check;   |
| Form fields            | On load           | Fields populated with user default info (if previously saved)                                                                  | &check;   |
| All input fields       | Leave blank       | On submit: form submits                                                                                                        | &check;   |
| All input fields       | Just whitespace   | On submit: form submits                                                                                                        | &check;   |
| All input fields       | Fill in correctly | On submit: form submits                                                                                                        | &check;   |
| Update button          | Click             | Form submits                                                                                                                   | &check;   |
| Update button          | Click             | Success message appears confirming profile successfully updated                                                                | &check;   |
| Order history number   | Click             | Redirect to previous order confirmation page for that order                                                                    | &check;   |
| **Order History**      |                   |                                                                                                                                |           |
| Information Display    | Display           | All previous order information displays correctly                                                                              | &check;   |
| Toast                  | On load           | Previous order info toast appears                                                                                              | &check;   |
| Back to Profile button | Click             | Redirect to profile page                                                                                                       | &check;   |

## Contact

| Element                       | Action                | Expected Result                                                                     | Pass?     |
|-------------------------------|-----------------------|-------------------------------------------------------------------------------------|-----------|
| Form Text Input (if required) | Leave blank           | On Submit: Warning appears, form won't submit                                       | &check;   |
| Form Text Input (if required) | Just input whitespace | On Submit: Warning appears Form won't submit                                        | &check;   |
| Email Input                   | Incorrect Format      | On Submit: Warning appears, form won't submit                                       | &check;   |
| Inquiry Type Dropdown         | Click                 | Display all Inquiry Types to choose from                                            | &check;   |
| Cancel button                 | Click                 | Redirect to Home page                                                               | &check;   |
| Submit button(form valid)     | Click                 | Form submit                                                                         | &check;   |
| Submit button(form valid)     | Click                 | Redirect to home Page                                                               | &check;   |
| Submit button(form valid)     | Click                 | Success message appears informing the superuser that the enquiry has been submitted | &check;   |
| Submit button(form valid)     | Click                 | User receives confirmation email about their enquiry                                | &check;   |

## About Us

| Element                  | Action                    | Expected Result                                                                              | Pass?     |
|--------------------------|---------------------------|----------------------------------------------------------------------------------------------|-----------|
| Creators Content         | Display                   | Display correct creators info: image, name, job, details                                     | &check;   |
| Image hover              | Hover                     | Change from B&W to color                                                                     | &check;   |
| **Superuser logged in**  |                           |                                                                                              |           |
| Edit creator button      | Click                     | Redirect to edit creator page                                                                | &check;   |
| Delete creator button    | Click                     | Delete the creator                                                                           | &check;   |
| Add new creator button   | Click                     | Redirect to add new creator page form                                                        | &check;   |

## Creator Management 

| Element                         | Action                | Expected Result                                                                                                            | Pass?     |
|---------------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------|-----------|
| **Add Creator**                 |                       |                                                                                                                            |           |
| Add Creator Form                | Display               | Form has all the fields ready to populate: name, job, description, image                                                   | &check;   |
| Form Text Input (if required)   | Leave blank           | On Submit: Warning appears, form won't submit                                                                              | &check;   |
| Form Text Input (if required)   | Just input whitespace | On Submit: Form won't submit                                                                                               | &check;   |
| Form image select button        | Click                 | Open device storage                                                                                                        | &check;   |
| Form image select button        | Display               | Chosen image name displayed once selected                                                                                  | &check;   |
| Form image select button        | Display               | Default image is used if no image is selected                                                                              | &check;   |
| Cancel button                   | Click                 | Redirect to About Us page                                                                                                  | &check;   |
| Add Creator (form valid)        | Click                 | Form submit                                                                                                                | &check;   |
| Add Creator (form valid)        | Click                 | Redirect to About Us page for new creator with all information displaying correctly                                        | &check;   |
| Add Creator button (form valid) | Click                 | Success message appears informing the superuser that the creator has been added                                            | &check;   |
|                                 |                       |                                                                                                                            |           |
|                                 |                       |                                                                                                                            |           |
| **Edit Creator**                |                       |                                                                                                                            |           |
| Edit Creator Form               | Display               | Form has all the fields filled out with the original content                                                               | &check;   |
| Edit Creator Form               | Image Field           | Thumbnail of original image is shown                                                                                       | &check;   |
| Form Text Input (if required)   | Leave blank           | On Submit: Warning appears, form won't submit                                                                              | &check;   |
| Form Text Input (if required)   | Just input whitespace | On Submit: Form won't submit                                                                                               | &check;   |
| Cancel button                   | Click                 | Redirect to About Us page                                                                                                  | &check;   |
| Submit button(form valid)       | Click                 | Form submit                                                                                                                | &check;   |
| Edit Creator button(form valid) | Click                 | Redirect to About Us page for new creator with all information displaying correctly                                        | &check;   |
| Edit Creator button(form valid) | Click                 | Success message appears informing the superuser that the creator has been updated                                          | &check;   |
|                                 |                       |                                                                                                                            |           |
| **Delete Creator**              |                       |                                                                                                                            |           |
| Confirm Delete -  cancel button | Click                 | Redirect to About Us page                                                                                                  | &check;   |
| Confirm Delete -  delete button | Click                 | Delete creator                                                                                                             | &check;   |
| Confirm Delete -  delete button | Click                 | Success message appears confirming creator was deleted successfully                                                        | &check;   |   

# Fixed bugs

**1. Search for categories and scents**

Discovered that links in main-nav.html are case sensitive and must match exactly admin panel (e.g. Warm, not warm), otherwise it won't render the request and result will come back empty once selecting a specific category.
<details> <summary> Issue screenshots </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/issue1.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/issue1a.png">
</details>

**2. Adjust_bag and remove_from_bag views in bag views.py**

Forgot to add 
````
product = get_object_or_404(Product, pk=item_id)
````
to adjust_bag and remove_from_bag views in bag views.py
As a result when clicking on update or remove buttons in the bag - no changes were made and error 500 was written to the console. After adding the line on the top of the view functionality started to work as expected.
<details> <summary> Issue screenshots </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/issue2.png">
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/issue2a.png">
</details>


**3. When running a local server 8000 media and static load as expected, but on deployed Heroku page there's an issue with missing images and css.**

Cause of the issue - missing media processor in the settings.py:
````
django.template.context_processors.media
````

**4. Success toast**

Every time a success message appeared (for adding a creator, submitting contact form etc.) and if the user had items in their shopping bag, 
the success message would display the bag contents under the toast notification. Shopping bag content was unwanted element to display.
Issue resolution - adding extra context into Django views using:
````
'get_context_data'
````
or set it up as
````
'on_profile_page': True
````
Thanks to that it was possible to add context to display only the toast message without bag content information for chosen views like add Creator, send a contact form.

**5. Sending emails - smtp**

When attempting to send emails to the users, who are trying to sign up or purchasing products - no real emails were sent. 
The cause of this issue was that in settings.py DEBUG = 'DEVELOPMENT' instead of 'False'. Additionally in Heroku Config Vars DEVELOPMENT was set up to TRUE.
After changing DEBUG = False and deleting DEVELOPMENT config var from Heroku settings for the app - all emails are now sent as expected.

**6. ElephantSQL Database issue - apps not recognized. Error 500**

After the initial migration to ElephantSQL two new apps were created: contact and creators. Whenever trying to send a contact form or access About Us section - error 500 was seen on the deployed site.
Locally, while running the project using port 8000 all worked as expected.
The issue behind it was that env.py file was missing on the project level, containing information:
````
import os

os.environ['DATABASE_URL'] = <url of the ElephantSQL database>
````

as well as settings.py was missing configuration for it:
````
if os.path.isfile("env.py"):
    import env
````
After applying those changes and performing migration:
````
python3 manage.py makemigrations
python3 manage.py migrate
````
all started working as expected.

**7. Sending emails as [example.com]**

When sending emails to the customers (with confirmation links, order details etc.) emails had "example.com" in the email title as per screenshot below.

<details> <summary> Issue screenshot </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/example-issue.png">
</details>

After further research it turned out that this information is based on the SITE_ID value declaired in settings.py. In the Django admin panel under the Sites section example.com was the only site declared.
There were two solutions to this issue:
* edit example.com to any other domain name and display name
* add a new site with different set of information regarding domain and display name. Then SITE_ID would need th be switched accordingly, e.g. SITE_ID = 2.

<details> <summary> Resolved screenshot </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/example-solution.png">
</details>

# Unfixed bugs

**1. Carrousel with testimonials on the homepage changes its height when switching between the views**

Problem is purely based on the size of the comments inside - there are 2 comments displayed on the same view - if one is bigger than the other on the next page - the hight will slightly drop/ increase while switching between the views.

**2. Footer alignment on certain pages**

Footer on certain pages tends to move up, leaving extra space on the bottom, even though code wise everything seems to be set up correctly.

**3. When login in/ logging out the dropdowns are opening, but not able to click on the available links**

It requires a page refresh, then all works as expected. Not sure about the root cause of this issue as it appears to happen for the Heroku deployment only.

# Responsiveness Test
<details> <summary> Home </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/home-responsive.png">
</details>

<details> <summary> Bag </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/bag-responsive.png">
</details>

<details> <summary> Contact </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/contact-responsive.png">
</details>

<details> <summary> Products All </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/products-responsive.png">
</details>

<details> <summary> Product Details </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/details-responsive.png">
</details>

<details> <summary> Checkout </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/checkout-responsive.png">
</details>

<details> <summary> Product Management </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/productmanagement-responsive.png">
</details>

<details> <summary> My Profile </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/profile-responsive.png">
</details>

<details> <summary> Shipping and Returns </summary>
<img src="https://story-sparks.s3.eu-west-1.amazonaws.com/media/shipping-responsive.png">
</details>