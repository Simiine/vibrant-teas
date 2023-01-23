# Validation
## HTML
- Testing was carried out using Jigsaw - https://validator.w3.org/ 
- All pages passed except for the Product Management Page and the Shopping Bag.
- Product Management Page: The error said there was a duplicate ID image coming from the Django form, so I wasn't able to remove it.
![HTML Error](readme-docs/testing/html-error.png)

- The Shopping bag had an error of duplicate ID. The main reason for this duplicate ID was because the include file for the quantty form has to appear twice in the DOM because it has a mobile view and larger screen view. 
![Shopping bag Error](readme-docs/testing/shopping-bag-error.png)

## CSS
- Testing was carried out using Validator - https://validator.w3.org/nu/
- No errors were found when passing through the validator.
![CSS](readme-docs/testing/css-validator.png)

## PEP8
- I used the PEP8 validator on my Gitpod Workspace. All pages were cleared. 

# Manual Testing
To ensure cross-compatibility, I tested the website across numerous devices and web browsers. The site was tested across different iPhones, a Samsung, an iPad, a Mac laptop, and a Lenovo laptop. The site was also tested across Google Chrome and Safari. For responsiveness, I used the developer tool for screen adjustments, so I could see how the site would look on different screen sizes as I made the required adjustments for it to be completely responsive.


| Feature        | Expected           | Testing  | Result | 
| ------------- |-------------| -----|  -----|
| Logo | Link to Home page | Click the logo | Navigates to home page | 
| Navigation bar | All products links to products page | Click All Products | Redirected to page with all products | 
|  | Teas opens drop down to subcategories | Click Teas | Dropdown appears for tea subcategories | 
|  | Herbal tea links to page with herbal teas | Click Herbal Tea | Redirected to page with herbal teas  | 
|  | Green tea links to page with herbal teas | Click Green Tea | Redirected to page with green teas  | 
|  | Black tea links to page with herbal teas | Click Black Tea | Redirected to page with black teas  | 
|  | Accessories opens drop down to subcategories | Click Accesssories | Dropdown appears for accessories subcategories | 
|  | Tea strainers links to page with tea strainers | Click Tea Strainers | Redirected to page with tea strainers  | 
|  | Teaware links to page with teaware | Click Teaware | Redirected to page with teaware  | 
|  | Producers links to page list of producers | Click Producers | Redirected to page with list of producers  | 
|  | Contact links to page with contact form | Click Contact | Redirected to page with contact form  | 
|  | Products searched in the search bar are displayed on a product page | Search Green Tea | Redirected to product page with only green teas   | 
|  | Logged out: Account icon link opens drop down menu with links to login and register  | Click Account Icon | Dropdown appears for login or register  | 
|  | Logged In as user: Account icon link opens drop down menu with links to profile and logout  | Click Account Icon | Dropdown appears for profile or logout  | 
|  | Logged In as superuser: Account icon link opens drop down menu with links to product management, profile and logout  | Click Account Icon | Dropdown appears for product management profile and logout  | 
|  | Login links to login page | Click Login | Redirected to login page  | 
|  | Logout links to logout page | Click Logout | Redirected to logout page  | 
|  | Register links to signup page | Click Register | Redirected to signup page  | 
|  | Profile links to profile page | Click Profile | Redirected to profile page  | 
|  | Product management links to product management page | Click Product Management | Redirected to product management page  | 
| Footer | Newsletter signup | Enter emaill address and click subscribe | Emaill address submitted and message appeared saying "Thank you for subscribing!" | 
|  | Links to social media open on a new page | Click each social media icon  | All social media links opened on a new tab | 
|  | Product links open page with products | Click on each product | All product links redirected to selected product page | 
|  | Producers link opens producers page | Click producers | Redirected to page of all producers | 
|  | Contact links to contact form page | Click contact | Redirected to contact form page | 
|  | Privacy policy link opens privacy policay on new tab | Click privacy policy | Redirected to a new tab with privacy policy | 
| Home Page | All Products button links to products page | Click all products | Redirected to page with all products | 
| Home Page | Herbal tea button links to herbal tea page | Click herbal tea | Redirected to page with herbal teas | 
| Home Page | Tea strainers button links to tea strainer page | Click tea strainer | Redirected to page with tea strainers | 
| Registration Page | Fill in signup form and create an account | Input details in signup form | Received email verification to finalise signup process  | 
|  | Verify email address and complete signup process | Click link in email verification | Redirected to site and clicked a button to confirm emaill address | 
| Login Page | Log into account | Enter login details | Succesfully signed into account | 
|  | Reset password to account | Click password reset on login page | Redirected to password reset page to input email and reset password. Received email link to new password, enter new details and password reset | 
| Profile Page | Update delivery information | Input new delivery information and click update information |  | 
|  | Update personal information |  |  | 
|  | View order history |  |  | 

| Products Page |  |  |  | 

| Product Details |  |  |  | 

| Product Reviews |  |  |  | 
|  | Add review |  |  | 
|  | Edit review |  |  | 
|  | Delete review |  |  | 

| Add Product |  |  |  | 

| Edit Product |  |  |  | 

| Delete Product |  |  |  | 

| Shopping Bag |  |  |  | 
|  | Add product to bag |  |  | 
|  | Update products in bag |  |  | 
|  | Delete products from bag |  |  | 

| Secure Checkout | View |  |  | 

| User Profile |  |  |  | 











| Navbar links | Clicking All Products takes user to All Products page | Click All Products | Redirected to All Products page | Pass |
|  | Clicking category takes user to the specific category page | Click each category in turn | Redirected to specific category page | Pass |
|   | Click Bag takes user to Bag page | Click Bag | Redirected to Bag page | Pass |
|   | Clicking Blog takes user to the Blog homepage | Click Blog | Redirected to Blog Page | Pass |
|   | Searching using Search Bar displays the product in the products page | Type wool in search bar | Redirected to Products page with all wool shown | Pass |
| Footer | Redirect to Facebook in new tab | Click Facebook icon | Facebook page opened in new tab | Pass |
|  | Redirect to Instagram in new tab | Click Instagram icon | Instagram page opened in new tab | Pass |
|  | Redirect to GitHub in new tab | Click GitHub icon | My GitHub profile page opened in new tab | Pass |
|  | Redirect to Pinterest in new tab | Click Pinterest icon | Pinterest page opened in new tab | Pass |
|  | Clicking T&Cs takes user to the Terms and Conditions page | Click T&Cs | Terms and conditions page opened | Pass |
|  | Clicking Privacy Policy takes user to the Terms and Conditions page | Click Privacy Policy | Privacy Policy page opened | Pass |

## Navigation Links
## Footer Links
## Register
## Login
## Logout
## Profile page
## Products page
## Bag
## Checkout

# Performance
## Desktop
## Mobile

# Bugs
## Solved Bugs
1. Problem: Programming Error when trying to access Heroku deployed link 
    - Cause: Site will only be connected to Elephant SQL satabase id DATABASE_URL is in env.py
    - Solution: Add DATABASE_URL value to env.py and run migrations for any outstanding 

2. Problem: NoReverseMatch when trying to add a review
    - Cause: Reviews URL not registered in base urls
    - Solution: Registered it in the base urls 

3. Problem: Testimonials App not appearing on the home page
    - Cause: The testiominals model wasn't added to the the home app view so home app wasn't aware of testimonials app
    - Solution: Testimonials was added to home app view

4. Problem: Delete confirmation modal, deleting a different product
    - Cause: The ID of the delete modal element was the same for every product
    - Solution: Create a dynamic ID, so each modal will have a different ID and be unique. Done using the products ID as the modal ID 

5. Problem: Reviews not submitting with star input
    - Cause: Radio buttons not being selected when clicked on as input is nested in li so when user selects the li, the radio isn't getting selected. 
    - Solution: Remove ratings field on the form in forms.py to grab the value in view that user choses from frontend. After, add rating request in the views Then use JS code to add checked property to the selected stars input to trigger it's value for the backend to pick up. 

## Outstanding Bugs
1. Problem: Confirmation Email not coming through
    - Cause: Network Error. Gmail servers down
    - Solution: 