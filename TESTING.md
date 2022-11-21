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



