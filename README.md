# The Big Review

<image src="assets/readme/primary-image.png" width="700px"></image>

The Big Review is a movie review website which uses the TMDB API to get movie data. Users can carry out the following actions on the site:
1. Create an account and login
2. Read reviews
3. Create/add their own movie reviews
4. Edit their reviews
5. Delete their reviews
6. Like/unlike other peoples reviews

This project has been developed as my 4th Portfolio Project for my Diploma in Full Stack Software Development with Code Institute. 

The project can be viewed here:

## Table of Contents
1. [User Experience](#user-experience-ux)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Colour Scheme](#colour-scheme)
2. [Planning](#planning)
    - [Methodology](#methodology)
    - [Models](#models)
    - [Wireframes](#wireframes)
3. [Features](#features)
    - [General](#general)
    - [Home Page](#home-page)
    - [Search Results Page](#search-results-page)
    - [Movie Detail Page](#movie-detail-page)
    - [Add Review Page](#add-review-page)
    - [Edit Review Page](#edit-review-page)
    - [Delete Review Page](#delete-review-page)
    - [Register Page](#register-page)
    - [Login Page](#login-page)
    - [Logout Page](#logout-page)
4. [Technololgies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programmes](#frameworks-libraries-and-programmes)
5. [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Code Validation](#code-validation)
    - [Automated Tests](#automated_tests)
    - [Feature Testing](#feature-testing)
    - [Bugs](#bugs)
6. [Deployment](#deployment)
7. [Credit](#credit)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
8. [Acknowledgements](#acknowledgements)

## User Experience (UX)
### Project Goals
- Build a modern movie review website using movie data from the TMDB API.
- Ensure the website is fully responsive. 
- Implement full CRUD functionality so users can interact with the website and modify data.
- Build an intuative website that provides users with feedback when as they interact with the various features.
- Implement authentification layers to key pages so the site is robust. 

### User Stories
1. As a site user I can search movies by name/keyword so that I can find a specific movie.
2. As a site user I can click on a movie so that I can see information about the movie.
3. As a site user I can register an account so that I can leave reviews and like reviews.
4. As a site user I can login so that I can leave new reviews and edit reviews.
5. As a site user I can read reviews so that I can see what people think of the movie.
6. As a site user I can create a new review so that I can be involved in the community.
7. As a site user I can edit my reviews so that my reviews are accurate and up-to-date.
8. As a site user I can delete a review so that I can only show reviews that I want.
9. As a site user I can like or unlike reviews so that I can show my support for their opinion.

### Future User Stories (to be implemented in the next iteration):
10. As a site user I can view a paginated list of movie results so that I can easily select a movie to view.
11. As a site user I can see a list of new movies so that I can discover new movies to watch.
12. As a site user I can see a list of the top 10 rated movies so that I can discover good movies to watch.
13. As a site user I can create and update my public profile so that I can share my interest and track my activity.
14. As a site user I can filter search results by genre so that I can narrow down my search.

### Colour Scheme
The website was designed to look clean and modern. As darkmode rises in popularity among web users, a dark background colour was chosen for the website to align with this trend. 

The following colours are used in the project: 
- Black (#000000): Background color
- Night (#111111): Reviews background color
- Aquamarine (#1AE6AF): Logo, buttons, links, icons, h1 headings.
- White (#FFFFFF): Body text and headings.

## Planning
### Methodology
The project was planned and implemented following agile methdology principles. Github Projects was used to manage and document this process.

The GitHub project can be viewed here: [The Big Review User Stories](https://github.com/users/orlagh-sweeney/projects/4)

EPICS were defined using GitHub milestones and each User Story was assigned to one of the following milestones:
- Core Functionality: API set up to display movie content for users.
- Account Management: User login and authentification.
- CRUD Functionality: Creating, Reading, Updating and Deleting reviews/likes.
- Secondary Features: Features that add value but are not essential.  

User Stories contained a list of Acceptance Criteria and Tasks to support the development of the project.
Following MoSCoW Priortisation principles, each User Story was assigned a tag from one of the following:
- Must Have
- Should Have
- Could Have
- Won't Have

### Models
The project uses two models, Review and ReviewLikes. It also uses the Django allauth User model.
1. The Review model stores movie review data:
    - author is a foreign key connecting to the User model.
2. The ReviewLikes model stores data about likes on a review:
    - review is a foreign key connecting to the Review model.
    - voter is a foreign key connecting to the User model.

The below entity relationship diagram was created using [dbdigram](https://dbdiagram.io/home) and demonstrates the relationship between the models. <br> <image src="assets/readme/erd.png" width="600px"></image>

### Wireframes
- [Balsamiq](https://balsamiq) was used to develop wireframes for mobile and desktop in the planning stage of the website. <br> <image src="assets/readme/wireframe-home-mob.png" width="300px"></image>
    - Home Page: <br> <image src="assets/readme/wireframe-home.png" width="600px"></image> <br> <image src="assets/readme/wireframe-home-mob.png" width="300px"></image>
    - Search Results Page: <br> <image src="assets/readme/wireframe-results.png" width="600px"></image> <br> <image src="assets/readme/wireframe-results-mob.png" width="300px"></image>
    - Movie Detail Page: <br> <image src="assets/readme/wireframe-moviedetail.png" width="600px"></image> <br> <image src="assets/readme/wireframe-moviedetail-mob.png" width="300px"></image>
    - Add Review Page: <br> <image src="assets/readme/wireframe-addreview.png" width="600px"></image> <br> <image src="assets/readme/wireframe-addreview-mob.png" width="300px"></image>
    - Register Page: <br> <image src="assets/readme/wireframe-register.png" width="600px"></image> <br> <image src="assets/readme/wireframe-register-mob.png" width="300px"></image>
    - Login Page: <br> <image src="assets/readme/wireframe-login.png" width="600px"></image> <br> <image src="assets/readme/wireframe-login-mob.png" width="300px"></image>

## Features
### General
- The website incorporates a responsive design so it can be used across multiple device sizes. 
- The website uses a consistent colour scheme across the site. 
- Each page has a responsive navigation bar containing the logo and nav menu. The nav bar turns into a burger menu on mobile devices. <br>
<image src="assets/readme/feature-nav.png" width="600px"></image>
- Each page has a repsonsive footer with social media links. Social media links open in a new browser window.<br>
<image src="assets/readme/feature-footer.png" width="600px"></image>

### Home Page
- Search Bar
    - The home page has a search bar where users can type in query to find a movie. <br><image src="assets/readme/feature-search.png" width="600px"></image>
- Hero Image
    - The home page has a photograph of people in a cinema. The photo is dark to match the website's dark theme. <br><image src="assets/readme/feature-hero.png" width="600px"></image>

### Search Results Page
- Search results are displayd using bootsrap cards which have the following details:
    - Movie title
    - Movie poster
    - View Movie button
- Results are displayed in rows of 3. 
- On mobile devices, 1 result is displayed per row.<br>
<image src="assets/readme/feature-results.png" width="600px"></image>

### Movie Detail Page
- This page displays the following movie data:
    - Movie title (TMDB API data)
    - Movie poster (TMDB API data - a placeholder image is displayed if no poster is found in the API request)
    - Genre (TMDB API data)
    - Summary (TMDB API data)
    - Rating (average rating calculated from ratings left by TheBigReview users) <br><image src="assets/readme/feature-moviedetail.png" width="600px"></image>
- This page displays movie reviews left by TheBigReview users. 
- The 'Leave a review' button allows users to add a review for this movie. 
- Users can like others peoples reviews if they are logged in. 
- Users can access edit and delete buttons for reviews they have left. <br><image src="assets/readme/feature-reviews.png" width="600px"></image>

### Add Review Page
- This page displays a form for users to leave a review. <br><image src="assets/readme/feature-add.png" width="600px"></image>

### Edit Review Page
- This page displays a pre-populated form for users to edit a review. <br><image src="assets/readme/feature-edit.png" width="600px"></image>

### Delete Review Page
- This page displays a form for users to delete a review. <br><image src="assets/readme/feature-delete.png" width="600px"></image>

### Register Page
- This page displays a form for users to create an account on TheBigReview. <br><image src="assets/readme/feature-register.png" width="600px"></image>

### Login Page
- This page displays a form for users to login into their account. <br><image src="assets/readme/feature-login.png" width="600px"></image>

### Logout Page
- This page displays a form for users to logout of their account. <br><image src="assets/readme/feature-logout.png" width="600px"></image>

## Technologies Used
### Languages
- HTML
- CSS
- Javascript
- Python
- [Jinja Templating Langugage](https://jinja.palletsprojects.com/en/3.1.x/)

### Frameworks, Libraries and Programmes
- [Balsamiq](https://balsamiq.com/): this was used to create wireframes in the planning stage of the project. 
- [Font Awesome](https://fontawesome.com/): this was used to add social media icons to footer to enhance user experience. 
- [Fontpair](https://www.fontpair.co/): this was used to find fonts that compliment each other. 
- [Google Fonts](https://fonts.google.com/): this was used to import fonts into the website.
- [Coolers](https://coolors.co/): this was used to create a colour pallete for the website. 
- [Pexels](https://www.pexels.com/): this was used to find the hero image and placeholder image for the project. 
- [Django](https://www.djangoproject.com/): this was the MVC web framework used.
- [Bootstrap 5](https://getbootstrap.com/): this was the CSS framework used to make the site responsive. 
- [Cloudinary](https://cloudinary.com/): this was used to store static and media files.
- [Gitpod](https://www.gitpod.io/): this was used to write, commit and to push the code to Github. 
- [Github](https://github.com/): this was used for version control. 
- [Heroku](https://dashboard.heroku.com/login): this was used to host and deploy the finished project.
- [Heroku Postgres](https://devcenter.heroku.com/articles/heroku-postgresql): this is the SQL database used in production.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/): this was used throughout the project to check responsiveness and debug. 
- [W3C Markup Validator](https://validator.w3.org/): this was used throughout the project to validate HTML code. 
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): this was used throughout the project to validate CSS code. 
- [CI Python Linter](https://pep8ci.herokuapp.com/): this was used to validate python code.
- [pycodestlye](https://pypi.org/project/pycodestyle/): this was used to validate python code.
- [JSHint](https://jshint.com/): this was used to validate Javascript code. 
- [Responsive Design Checker](https://www.responsivedesignchecker.com/): this was used to check responsiveness on various device sizes. 
- [Am I Respsonsive?](https://ui.dev/amiresponsive): this was used to create an image to show how the site looks on different device sizes for this README file. 

## Testing
### Testing User Stories
1. As a site user I can search movies by name/keyword so that I can find a specific movie.
    - The homepage has a search bar where users can type a word to find a movie. 
    - The API processes the request and returns the relevant movie results. 
    - The user is brought to the search results page.
2. As a site user I can click on a movie so that I can see information about the movie.
    - Each movie has a button that brings the user to the movie detail page.
    - The correct movie data loads. 
3. As a site user I can register an account so that I can leave reviews and like reviews.
    - The register page allows the user to create an account.
    - The user must submit a unique username and/or email.
    - They must confirm their password. 
    - Once registered, the user has access to all CRUD functionality.
4. As a site user I can login so that I can leave new reviews and edit reviews.
    - Unauthenticated users can access the login page via the navigation menu. 
    - If an unathenticated user tries to click the 'leave a review' button on the movie_detail page, they are shown a warning that they need to login.
    - The user can use their username/email to login into the website via the login page.
5. As a site user I can read reviews so that I can see what people think of the movie.
    - All site visitors can read existing movie reviews. 
6. As a site user I can create a new review so that I can be involved in the community.
    - If authenticated, the user can access the add_review page via the 'leave a review' button.
    - The user can fill in the movie review form.
    - After submitting they are redirected back to the relevant movie_detail page and shown a notfication that their review has been successful.
7. As a site user I can edit my reviews so that my reviews are accurate and up-to-date.
    - If authenticated and if the user is the review author, an 'edit review' button is visible on their review.
    - The user is brought to the edit_review page which is populated with their review data.
    - The user can update the form to edit the review.
    - After submitting they are redirected back to the relevant movie_detail page and shown a notfication that their review has been updated.
8. As a site user I can delete a review so that I can only show reviews that I want.
    - If authenticated and if the user is the review author, a 'delete review' button is visible on their review.
    - The user is brought to the delete_review page and asked to confirm if they want to delete the review. 
    - After deleting they are redirected back to the relevant movie_detail page and shown a notfication that their review has been deleted.
9. As a site user I can like or unlike reviews so that I can show my support for their opinion.
    - If authenticated, users can click the like button on movie reviews.
    - The number of likes is shown beside the like button.
    - The user can also unlike by clicking the like button again. 

### Code Validation
The following validators were used to test the code:
- [W3C Markup Validator](https://validator.w3.org/): No errors were reported when passing the final HTML code through the validator. 
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): No errors were reported when passing the final CSS code through the validator. <br>
- [JSHint](https://jshint.com/): No errors were reported when passing the final javascript code through the validator. <br>
- [pycodestlye](https://pypi.org/project/pycodestyle/): No errors were reported when passing the final python code through the validator.  <br>

The validators were used throughout the development stage of the website as part of ongoing testing and at the end of the project to complete a final code check. Examples of errors and warnings can be found below which were all resolved: <br>
- Example 1: HTML Errors due to a missing closing div tag on the sign up page: <br> <image src="assets/readme/html-errors-1.png" width="600px"></image>
- Example 2: HTML Errors on a width attribute. Styling added to custom css file to resolve: <br> <image src="assets/readme/html-errors-2.png" width="600px"></image>
- Example 3: Python errors for line length and trailing white spaces: <br> <image src="assets/readme/pycode-errors.png" width="600px"></image>

Unresolved python errors:
- The two API request URLS in the views.py file were flagged as errors but have been left as they are. 

### Automated Tests
Automated tests were written for forms.py, models.py and views.py. Coverage was used to generate a report to see how much code was tested. <br> <image src="assets/readme/coverage-report.png" width="600px"></image>

### Feature Testing
The following manual tests were carried out:
#### General: base.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Logo | When the logo is clicked, the user is brought back to the home page | PASS
Authenticated user | If a site user is logged in, the navigation menu displays Home and Logout nav links | PASS
Unauthenticated user | If a site user is not logged in, the navigation menu displays Home, Register and Login nav links | PASS
Mobile menu | On mobile devices, a burger menu is used to display nav links | PASS
Home nav link | Brings the user to the home page | PASS
Register nav link | Brings the user to the signup page | PASS
Login nav link | Brings the user to the login page | PASS
Logout nav link | Brings the user to the logout page | PASS
Footer links | When clicked, footer links open in a new browser window | PASS

#### Home Page: index.html 
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Search Bar | The user can type in the search bar | PASS
Search Button | When clicked, the user is brought to the search_results page | PASS 

#### Search Results: searchresults.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Results | The API processes the request and displays relevant movie results | PASS
Results display | Results are displayed in rows of 3 | PASS
Results mobile display | Results are displayed in rows of 1 | PASS
Placeholder image | If a movie does not have a poster to display, a placeholder image is displayed | PASS
No results | If the API does not find any movies matching the query, the user is shown a message explaining this | PASS
View Movie Button | Brings the user to the correct movie detail page | PASS
Pagination | The search results are paginated | FAIL

#### Movie Detail: moviedetail.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Movie data | The API processes the request and displays the correct movie data | PASS
Leave a review Button | When clicked, the user is brought to the add_review page | PASS
Movie reviews | The correct movie reviews are retrieved from the database and displayed | PASS
Edit Button visibility | If the user is authenticated and the user is the review author, the edit button is visible | PASS
Edit Button | Brings the user to the edit_review page | PASS
Delete Button visibility | If the user is authenticated and the user is the review author, the delete button is visible | PASS
Delete Button | Brings the user to the delete_review page | PASS
Like Button | If the user is authenticated they can like and unlike a review | PASS
Like count | The total number of likes on a review increases/decreases when a user likes/unlikes a review | PASS

#### Add Review: add_review.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Authenticated user | If the user is logged in, the review form is visible | PASS
Unauthenticated user | If the user is not logged in, a message is displayed telling them that they must be logged in to leave a review | PASS
Review form | The reivew form loads with the correct form fields | PASS
Required fields | If the user does not complete a required field they are shown a message that it needs to be completed | PASS 
Submit Review Button | Adds the review to the database and redirects the user back to the relevant movie detail page | PASS
Success message | The user is shown a message that their review has been submitted | PASS

#### Edit Review: edit_review.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Authenticated user | If the user is logged in AND the user is the review author, the review form is visible | PASS
Unauthenticated user | If the user is not logged in and/or is not the review author, a message is displayed telling them that they do not have permission to view this page | PASS
Pre-populated form fields | The form loads and is pre-populated with the correct data from the database | PASS 
Update Review Button | Updates the review in the database and redirects the user back to the relevant movie detail page | PASS
Success message | The user is shown a message that their review has been submitted | PASS

#### Delete Review: delete_review.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Authenticated user | If the user is logged in AND the user is the review author, the delete form is visible | PASS
Unauthenticated user | If the user is not logged in and/or is not the review author, a message is displayed telling them that they do not have permission to view this page | PASS
Delete form | The delete form loads with the correct form fields | PASS
Delete Review Button | Deletes the review from the database and redirects the user back to the relevant movie detail page | PASS
Success message | The user is shown a message that their review has been submitted | PASS

#### Register: signup.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Register form | The correct form and form fields are displayed | PASS 
Unique username | If the user chooses a username that already exists in the database they are shown a warning | PASS
Short password | If their chosen password is too short/weak they are shown a warning | PASS
Confirm password | The user must confirm their password in order to sign up | PASS 
Sign Up Button | The user is added to the database, logged in and redirected back to the homepage | PASS
Success message | The user is shown a message that they are logged in | PASS

#### Login: login.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Login form | The correct form and form fields are displayed | PASS
Credentials | If the users credentials do not match, the user is shown a warning that they were incorrect | PASS
Sign In Button | The user is logged in and redirected back to the homepage | PASS
Success message | The user is shown a message that they have logged in | PASS

#### Logout: logout.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Logout Form | The correct form and form fields are displayed | PASS
Sign Out Button | The user is signed out and redirected back to the homepage | PASS
Success message | The user is shown a message that they have signed out | PASS

#### Cascade: models
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Deleted User | If a user is deleted their reviews and review likes are also deleted from the database | PASS 

#### Alert Messages
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Boostrap Alert message | Alert messages automtically disappear after 2.5 seconds | PASS 

### Bugs
### Resovled Bugs:
1. Fontawesome and Cloudinary deployment bug:
When setting DEBUG to False to test the functionality of static files hosted on Cloudinary, the application would not deploy on Heroku. The build log error pointed to a problem between Cloudinary and the fontawesome solid assets. Fontawesome was originally setup as a package for this project, by doing it this way Cloudinary stored each fontawesome icon as an asset meaning the Cloudinary static folder had 2700 assets. I attempted to delete the static folder from Cloudinary and set it up again but the folder would not delete and the issue was not resolved. I then uninstalled Fontawesome as a package and instead use the CDN link to access icons. This fixed the issue with being able to deploy the site to Heroku. 

2. URL bug:
The deployed site was unable to render to edit page due to an error in the URL page. The error was in the href on the movie_detail page. 

### Unresolved Bugs:
1. Pagination:
The site intended to paginate movie search results for better display and navigation. The django paginator feature did not work since the data was coming from an API rather than a database model. This issue has been left unresolved and will be addressed in the next iteration of the project.

## Deployment
The program was developed in Gitpod. It was then commited and pushed to GitHub.
The finished project was deployed in Heroku. 
Deployment to Heroku was completed using the following steps: 
1. Open and login to [Heroku](https://id.heroku.com/login).
2. From the dashboard, click 'New', then click 'Create new app' from the dropdown menu. 
3. Enter the App name, choose a region, then click 'Create app'.
4. Navigate to the 'Settings' tab.
5. Within 'Settings', navigate to 'Convig Vars'. Click 'Reveal Config Vars'.
6. Two config vars need to be added using the following 'KEY' and 'VALUE' pairs:
    1. KEY = 'CREDS', VALUE = Copy and paste the entire contents of the creds.json file into this field. Then click 'Add'.
    2. KEY = 'PORT', VALUE = '8000'. Then click 'Add'.
7. Within 'Settings', navigate to 'Buildpack'. 
8. Click 'Add buildpack'. Select 'Python', then click 'Save changes'.
9. Click 'Add buildpack' again. Select 'nodejs', then click 'Save changes'.
    - Ensure that these buildpacks are in the correct order: Python on top and nodejs underneath. 
    - If they are in the wrong order, click and drag to fix this. 
10. Navigate to the 'Deploy' tab. 
11. Within 'Deploy', navigate to 'Deployment method'. 
12. Click on 'GitHub'. Navigate to 'Connect to GitHub' and click 'Connect to GitHub' 
13. Within 'Connect to GitHub', use the search function to find the repository to be deployed. Click 'Connect'.
14. Navigate to either 'Automatic Deploys' or 'Manual Deploys' to choose which method to deploy the application.
15. Click on 'Enable Automatic Deploys' or 'Deploy Branch' respectively, depending on chosen method. 
16. Once the app is finished building, a message saying 'Your app was successfully deployed' will appear.
17. Click 'View' to see the deployed app. 

## Credit
### Content
- Movie specific content was provided by the [TMDB API](https://www.themoviedb.org/). 
- All other content was written by the developer.

### Media
- Movie images were obtained from the [TMDB API](https://www.themoviedb.org/).
- All other images were sourced from [Pexels](https://pixabay.com/):
    - The hero image is friends-at-a-movie-house-8263319 (https://www.pexels.com/photo/friends-at-a-movie-house-8263319/) by cottonbro studio (https://www.pexels.com/@cottonbro/)
    - The placeholder image for movies with movies with no poster path is spotlight-on-a-red-curtain-4722571/(https://www.pexels.com/photo/spotlight-on-a-red-curtain-4722571/) by cottonbro studio (https://www.pexels.com/@cottonbro/);

### Code
- [Stackoverflow](https://stackoverflow.com/) and [W3Schools](https://www.w3schools.com/) were used throughout the development to educate myself and to seek help and clarification features. In particular I used the following sources:
    - How to use groupby in Django: answer by Stackoverflow user [Alvaro](https://stackoverflow.com/a/19102493)
    - How to access a dictonary element using Jinga: answer by [russian_spy](https://stackoverflow.com/a/6285769)
- [TMDB API](https://www.themoviedb.org/) the API documentation was used to set up the API queries for movie search and movie detail.
- [YouTube](https://www.youtube.com/): The following YouTube sources were used: 
    - [DevWithMe](https://www.youtube.com/watch?v=tm9Yps3IkmQ) this YouTube video was watched to learn how to inject the users search query into the API request URL and display the API data in html.
    - [A Design Who Codes](https://www.youtube.com/watch?v=45QSuJaHEss) this YouTube video was watched to learn how to change the colour of the bootsrap mobile menu icon.
- [Code Institute](https://codeinstitute.net/de/):
    - Code Insitute full stack walkthrough projects were referred to when setting up the project. Elements of these projects were used and adapted to suit this project.
- [Bootstrap5](https://getbootstrap.com/) was used to add elements including cards for movies, the navigation bar and the search bar. 
- [Django](https://www.djangoproject.com/) documentation was referred to throughout development. 

## Acknowledgements
- Thank you to my mentor Marcel for his feedback and suggestions at each stage of the project.
- Thank you to Jason, Martin and Joanne from Code Institute Tutor Support for helping me along the way. 
- Thank you to Code Institute for providing me with the tools and skills to complete this project. 