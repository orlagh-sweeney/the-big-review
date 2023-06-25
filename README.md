# The Big Review
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

4. [Technololgies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programmes](#frameworks-libraries-and-programmes)
5. [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Code Validation](#code-validation)
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
### User Stories
1. As a site user I can search movies by name/keyword so that I can find a specific movie.
2. As a site user I can view a paginated list of movie results so that I can easily select a movie to view.
3. As a site user I can click on a movie so that I can see information about the movie.
4. As a site user I can register an account so that I can leave reviews and like reviews.
5. As a site user I can login so that I can leave new reviews and edit reviews.
6. As a site user I can read reviews so that I can see what people think of the movie.
7. As a site user I can create a new review so that I can be involved in the community.
8. As a site user I can edit my reviews so that my reviews are accurate and up-to-date.
9. As a site user I can delete a review so that I can only show reviews that I want.
10. As a site user I can like or unlike reviews so that I can show my support for their opinion.
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

### Wireframes
- [Balsamiq](https://balsamiq) was used to develop wireframes for mobile and desktop in the planning stage of the website. 

## Features


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
- [Google Fonts](https://fonts.google.com/): this was used to import fonts into the style.css file.
- [Coolers](https://coolors.co/): this was used to create a colour pallete for the website. 
- [Pexels](https://www.pexels.com/): this was used to find the hero image and placeholder image for the project. 
- [Django](https://www.djangoproject.com/): this was the web framework used.
- [Boostrap 5](https://getbootstrap.com/): this was the CSS framework used to make the site responsive. 
- [Cloudinary](https://cloudinary.com/): this was used to store static and media files.
- [Gitpod](https://www.gitpod.io/): this was used to write, commit and to push the code to Github. 
- [Github](https://github.com/): this was used for version control. 
- [Heroku](https://dashboard.heroku.com/login): this was used to host and deploy the finished project.
- [Heroku Postgres](https://devcenter.heroku.com/articles/heroku-postgresql): this is the SQL database used in production.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/): this was used throughout the project to check responsiveness and debug. 
- [W3C Markup Validator](https://validator.w3.org/): this was used throughout the project to validate HTML code. 
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): this was used throughout the project to validate CSS code. 
- [Responsive Design Checker](https://www.responsivedesignchecker.com/): this was used to check responsiveness on various device sizes. 
- [Am I Respsonsive?](https://ui.dev/amiresponsive): this was used to create an image to show how the site looks on different device sizes for this README file. 


## Testing
### Testing User Stories
1. As a site user I can search movies by name/keyword so that I can find a specific movie.
    - The homepage has a search bar where users can type a word to find a movie. 
    - The API processes the request and returns the relevant movie results. 
    - The user is brought to the search results page.
2. As a site user I can view a paginated list of movie results so that I can easily select a movie to view.

3. As a site user I can click on a movie so that I can see information about the movie.
    - Each movie has a button that brings the user to the movie detail page.
    - The correct movie data loads. 
4. As a site user I can register an account so that I can leave reviews and like reviews.
    - The register page allows the user to create an account.
    - The user must submit a unique username and/or email.
    - They must confirm their password. 
    - Once registered, the user has access to all CRUD functionality.
5. As a site user I can login so that I can leave new reviews and edit reviews.
    - Unauthenticated users can access the login page via the navigation menu. 
    - If an unathenticated user tries to click the 'leave a review' button on the movie_detail page, they are shown a warning that they need to login.
    - The user can use their username/email to login into the website via the login page.
6. As a site user I can read reviews so that I can see what people think of the movie.
    - All site visitors can read existing movie reviews. 
7. As a site user I can create a new review so that I can be involved in the community.
    - If authenticated, the user can access the add_review page via the 'leave a review' button.
    - The user can fill in the movie review form.
    - After submitting they are redirected back to the relevant movie_detail page and shown a notfication that their review has been successful.
8. As a site user I can edit my reviews so that my reviews are accurate and up-to-date.
    - If authenticated and if the user is the review author, an 'edit review' button is visible on their review.
    - The user is brought to the edit_review page which is populated with their review data.
    - The user can update the form to edit the review.
    - After submitting they are redirected back to the relevant movie_detail page and shown a notfication that their review has been updated.
9. As a site user I can delete a review so that I can only show reviews that I want.
    - If authenticated and if the user is the review author, a 'delete review' button is visible on their review.
    - The user is brought to the delete_review page and asked to confirm if they want to delete the review. 
    - After deleting they are redirected back to the relevant movie_detail page and shown a notfication that their review has been deleted.
10. As a site user I can like or unlike reviews so that I can show my support for their opinion.
    - If authenticated, users can click the like button on movie reviews.
    - The number of likes is shown beside the like button.
    - The user can also unlike by clicking the like button again. 
11. As a site user I can see a list of new movies so that I can discover new movies to watch.
12. As a site user I can see a list of the top 10 rated movies so that I can discover good movies to watch.
13. As a site user I can create and update my public profile so that I can share my interest and track my activity.
14. As a site user I can filter search results by genre so that I can narrow down my search

### Code Validation
### Feature Testing
The following manual tests were carried out:
#### General: base.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |

#### Home Page: index.html 
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |

#### Search Results: searchresults.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |

#### Movie Detail: moviedetail.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |

#### Add Review: add_review.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |

#### Edit Review: edit_review.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |

#### Login: login.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |

#### Logout: logout.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |

#### Register: signup.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |

### Bugs

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
- [Bootsrap5](https://getbootstrap.com/) was used to add elements including cards for movies, the navigation bar and the search bar. 
- [Django](https://www.djangoproject.com/) documentation was referred to throughout development. 
- [Code Institute](https://codeinstitute.net/de/):
    - Code Insitute full stack walkthrough projects were referred to when setting up the project. Elements of these projects were used and adapted to suit this project.
- [TMDB API](https://www.themoviedb.org/) the API documentation was used to set up the API queries for movie search and movie detail.
- [DevWithMe](https://www.youtube.com/watch?v=tm9Yps3IkmQ) this YouTube video was watched to learn how to inject the users search query into the API request URL and display the API data in html.

## Acknowledgements
- Thank you to my mentor Marcel for his feedback and suggestions at each stage of the project.
- Thank you to Jason and Martin from Code Institute Tutor Support for helping me along the way. 
- Thank you to Code Institute for providing me with the tools and skills to complete this project. 