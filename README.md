# Vibrant Teas
Vibrant Teas is B2C e-commerce website that sells organic teas and tea accessories. The site is aimed at tea lovers who care about the products they consume being organic and where they are being sourced from. The is a full stack site with an authentication mechanism. The site was created using HTML, CSS, JavaScript, Django and Python.
![responsive design picture](readme-docs/)

## Planning

### User Stories
#### Site User
#### Site Admin
#### Site Owner Goals
### Kanban Board
![Kanban Board]()
### Information Architecture
![SQL diagram]()


## UX Design
### Design Choices
#### Typography
#### Colour Palette
![Colour Palette]()

#### Logo
To showcase the theme of the site I designed a logo to show a stack of plates with a plane going around it.
![Logo](static/images/logo.png)

### Wireframes
#### Home Page
![Home wireframe]()
#### Products Page
![Products page wireframe]()
#### Producers
![Producers page wireframe]()
#### Contact
![Contact page wireframe]()
#### Sign Up Page
![Sign Up wireframe]()
#### Log In Page
![Log In wireframe]()

## Features
### Existing Features
#### Navigation
The navigation bar sits at the top of all the pages and has links to the different pages across the site. The navigation bar has a section for you to search products on the page. It links to the product pages through subcategories which drop down. It has a shipping bag symbol to access to bag and profile section which has different options depending on if you are logged in or out and if you are logged in as a superuser or normal customer. If a user is not yet logged in they will be given options to either log in or register. If a user is logged in as a normal customer they will have to option to go to their profile. If the user is logged in as a super user they will have an extra option to access the product management page where they can add a product.

![Nav bar logged in]()

![Nav bar logged out]()

![Nav bar toggle]()

#### Logo
The logo sits to the left of the navbar and showcases a teapot and cup with the name Vibrant Teas underneath it and Organic. 

#### Home Page hero image
On the home page, the hero image is a table with clear glass jars, with different herbal teas in each and filled with water.
![Home page header image]()

#### Home Page Content
The home page has a welcome section just underneath the hero image, giving a brief intro to the website and what type of products are offered. Underneat the welcome section is a row of testimonials from 3 different people to showcase how great the site is and it's products. The goals was to create a very minimal simple homepage just focused on what the site does and people who have purchased from the site. 
![Home page page content]()

#### Footer
The footer links to different social media pages, all the products on the site and useful site links such as the contact page, the producers page, the site map and the privacy policy. It also has contact information such as the country location of the business and a contact email address and phone number. In the footer section is also an email newsletter where customers can sign up to the newsletter.
![Footer]()

#### Products
![Products Products page]()

#### Product Detail
![Products Products page]()

#### Reviews
If a user that is logged in is the owner of a review they can edit or delete the review, changing the star rating and the review text. When they click delete a delete confirmation modal appears where they can either cancel the delete request or continue with the deletion.
![Products Products page]()

#### Producers
![Products Products page]()

#### Contact
![Products Products page]()

#### Profile
![Products Products page]()

#### Bag
![Products Products page]()

#### Product Management
![Products Products page]()

#### Edit/Delete Products
If a superuser is logged in they have the option to delete or edit the products on the site from the all products page or from the products detail page. When the click edit they can edit all the information of the product and change the image. When they click delete a delete confirmation modal appears where they can either cancel the delete request or continue with the deletion.
![Edit Delete Experience]()
![Edit Experience]()
![Delete Experience]()

#### Sign Up Page
The sign-up page was formed using crispy forms. The user can simply input their username, optional email, and password twice to sign up.
![Sign up]()

#### Log In Page
The log-in page was formed using crispy forms. The user can simply input their username and password to log in. 
![Log In page]()

#### Log Out Page
When the user clicks on the log-out page they are directed to a confirmation page
![Log Out page]()

## Testing

Testing can be found in a seperate document called [TESTING.md](TESTING.md) 

To ensure cross-compatibility, I tested the website across numerous devices and web browsers. The site was tested across different iPhones, a Samsung galaxy fold, an iPad, a Mac laptop, and a hp laptop. The site was also tested across Google Chrome, Safari and Edge. For responsiveness, I used the developer tool for screen adjustments, so I could see how the site would look on different screen sizes as I made the required adjustments for it to be completely responsive.

### Bugs
#### URL not linking
I had an issue linking up my URLs. Every time I tried to go to a page I would get an error message saying 'no experience matched the given query'. The issue was because the URL root that only used the argument '<slug:slug>/' was not at the end of the URLs. I fixed this by moving the URL to the bottom of the list which fixed the issue.  

#### Slug not generating
I had an issue with the slug not generating for an experience post when I created one through the site which resulted in an error when I tried to create a post. I was able to fix that by generating a slug automatically from the title when saving a post by adding a slug function to my models.py. This solved the issue.

#### Submit button in add experience not working
The submit button in my add experience stopped working after I fixed the slug issue. The reason for this was that I had the slug blank set to false but also had created a function in my models to autogenerate a slug. I was able to fix this by changing my slug blank to true so that the auto generate function would be able to go through.

### Manual Testing
#### Navigation Links
I tested the navigation links which worked as expected. The navigation bar was visible on every screen. It was responsive as it toggled as I viewed it on smaller screen sizes. The nav buttons brought me to the correct pages. They correctly changed to the expected options when I was logged in giving me the button to add an experience and log out. It also gave the expected options when I was not logged in giving me the options to sign up or log in.

#### Footer Links
I tested the footer links. When I clicked on a social media icon it took me to the social media page, opening up a new tab.

#### Home Page
I tested the home page. In the welcome section of the home page when I clicked on the login link it took me to the log-in page. When I clicked the link to sign up it took me to the sign-up page. 

#### View Experience post
I tested the view experience post. I was able to click on the title of an experience which brought me to the experience detail page. When I wasn't logged in it gave me the correct instructions below the content to sign up or log in to like or comment on the experience. When I was logged in it gave me the box at the bottom of the screen to add a comment and I was able to like the post. When I was underneath a post that I added it gave me additional buttons to edit or delete the post. 

#### Sign up
The sign-up page currently appeared in the nav bar when not logged in. I was able to sign up. The link in the nav bar worked, opening up the sign-up page where I was able to input my username, email(optional) and password and sign up.

#### Log In/log Out
The log-in and log-out appeared in the nav bar correctly. When I was not logged in, the log-out option was in the nav bar and when I was logged out the log-in option appeared in the nav bar. I was able to log in by adding my username and password. When I logged out I was taken to a confirmation page to log out of the site.

#### Like
I tested the like feature and was able to like posts when I was logged in. When I was logged out I was given instructions on the experience details page to log in or signup to like the experience. I was also able to like a post and unlike a post.

#### Comment
I tested the comment feature. The same with the like feature when I was logged in there was a box below the content for me to submit a comment. When I submitted a comment I got an alert saying "your comment is awaiting approval". When I approved the comment through admin, the comment appeared in the experience. When I was not logged in I could see instructions to log-in or sign-up to leave a comment. 

#### Add experience
I tested adding an experience. The option only appeared in the nav bar when I signed in. When I clicked on the option I was able to add a title, upload an image, select the country, add the content, recipe and submit. Once I submitted the experience it appeared on the home page.

#### Edit/Delete Experience
I tested the edit and delete experience feature. The edit and delete feature only appeared when I was logged in and in my own experience. When I clicked on edit I was able to edit the title, image, country, content and recipe and submit. When I clicked on delete I was taken to a confirmation page where it asked me to confirm if I wanted to delete the experience and gave me the option to cancel. When I clicked the delete button it deleted the experience. When I clicked the cancel button it took me back to the experience page. 

### Automated Testing
#### PEP8
- I used the PEP8 validator on my Gitpod Workspace. All pages were cleared. 

#### HTML
- Testing was carried out using Jigsaw - https://validator.w3.org/ 
- All pages passed.

#### CSS
- Testing was carried out using Jigsaw - https://jigsaw.w3.org/css-validator/
- No errors were found when passing through the official (Jigsaw) validator.

![CSS](static/images/css.png)

## Deployment
The live deployment can be found using the following URL - https://events-planner-p3.herokuapp.com/

I deployed this project in Heroku using the following steps:
1. Log In to Heroku
2. From the Heroku dashboard, click on "New" and in the drop-down click "Create new app"
3. Create a unique name for the project, select your region and click "Create app"
4. Navigate to the Resources tab, under add-ons search for Heroku Postgres and.
5. Navigate to the Settings tab
6. Scroll down to config var and click on "Reveal Config Vars"
   - Add Cloudinary url
   - Add Database url
   - Add Secret key
   - Click "Add"
7. Using the code institute template, you must add another config var
   - In the field for KEY enter PORT
   - In the field for VALUE enter 8000
8. Navigate to the Deploy tab at the top of the page
9. Go to deployment method and select "GitHub"
10. Confirm you want to connect to GitHub by clicking "Connect to GitHub"
    - Insert repository name and click "Search"
    - Click "Connect" to link up Heroku app to the GitHub repository code
11. Scroll down and choose a deployment method 
    - In manual deploy click "Deploy Branch"
    - Then click on "Enable Automatic Deploys" 
   - This allows Heroku to rebuild your app every time you push a new change to your code to GitHub

## Technologies Used
* Python
* HTML
* CSS
* Bootstrap 4
* Django
* AWS
* Heroku

## Credits
- I used other people's projects for ideas and inspiration 
  - https://github.com/KarinOldbring/vegan-a-eat
  - https://github.com/dougiemath/photo_sharing_site  

### Media
- Pictures were taken from the open source site Unsplash -  https://unsplash.com/ and Pexels - https://www.pexels.com/

## Support
* Richard Wells Code Institute Mentor.

## Resources

https://mdbootstrap.com/docs/standard/navigation/footer/

https://bbbootstrap.com/snippets/bootstrap-5-user-testimonial-star-ratings-51527336

https://eteakol.com/collections/beyondarie

https://getbootstrap.com/docs/4.0/components/modal/