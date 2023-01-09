# Table of Contents
- [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [UX](#ux)
    - [User Stories](#user-stories)
    - [Strategy](#strategy)
    - [Scope](#scope)
  - [Typography](#typography)
  - [Color](#color)
  - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Wireframes](#wireframes)
    - [Mobile](#mobile)
    - [Desktop](#desktop)
  - [Database Schema](#database-schema)
  - [Features](#features)
    - [Existing Features (Photo Links)](#existing-features-photo-links)
      - [Navbar](#navbar)
      - [Homepage](#homepage)
      - [Footer](#footer)
      - [Pay form Page](#pay-form-page)
      - [Register as a User](#register-as-a-user)
      - [Product Page](#product-page)
      - [404 Page](#404-page)
    - [Future Features](#future-features)
      - [Model of payment based on subscriptions](#model-of-payment-based-on-subscriptions)
      - [Chat window](#chat-window)
      - [Wishlist](#wishlist)
  - [SEO](#seo)
  - [Social Media](#social-media)
  - [Email Marketing](#email-marketing)
  - [Testing](#testing)
    - [Testing User Stories from User Experience (UX) Section](#testing-user-stories-from-user-experience-ux-section)
      - [robots.txt](#robotstxt)
      - [sitemap.xml](#sitemapxml)
      - [Functionality Testing](#functionality-testing)
  - [Deployment](#deployment)
      - [Deploy to Heroku](#deploy-to-heroku)
  - [Credits](#credits)
      - [Media](#media)
      - [Code](#code)
      - [Programming Languages](#programming-languages)
      - [Payments](#payments)
      - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
      - [Acknowledgements](#acknowledgements)

**[LIVE DEMO - https://the-last-chapter.herokuapp.com
*


## Introduction
The Last Chapter is an book retailer best known for selling books, stationery, cards, gifts. Unfornutely I cannot finish this project on time so my first submision is of a incomplete project that im still working on . The whole project is based on Code Institute Boutique Ado with the intent of adding my own apps and features making it an online bookstore and office supplies. 
My second attempt to finish the project for the deadline is a semi failure too as I didnt have enough time to complete a 404 page a facebook page and another few bits and pieces 

## UX

  ### User Stories

  User story format/steps has been taken from Boutique Ado and imported from Repository ecommerce2 (a test for my project) and more issues have been resolved manually during the project.
  
  -Account Creation</a>

- VIEWING AND NAVIGATION
  - As a shopper, I want to view items in my bag to be purchased so I can identify the total cost of my purchase and all items I will receive.</a>
  - As a shopper, I want to view orders and confirmation after checkout so I can verify that I haven't made any mistakes.</a>
  
- REGISTRATION AND USER ACCOUNTS
  - As a user, I want easily register for an account so I can have personal account information.</a>
  - As a user, I want to easily recover my password in case I forgot it so I can recover access to my account.</a>
  - Log In / Log Out  As a user,   I want to easily log in or log out so I can access my personal account details.</a>
  - As a shopper, I can change my account user details(name) so I can pay with another card without problems.</a>
  - >As a shopper, I can delete my account and details if I don't want to use the website or if my details to not kept in the database.</a>
  - As a Shopper, I can receive an email of confirmation when I am resetting my password so that I know that my new password is active and has been changed successfully.</a>
  - As a user, I want to have a personalized user profile so I can view my personal order history and order confirmations and save my payment information.</a>
  - As a shopper, I want to receive an email confirmation after checking out so I can keep the confirmation of what I've purchase for my records.</a>
    
- SORTING AND SEARCHING
  - As a shopper, I can choose the category that I want to see and the group of products I am interested <a>
  - As a shopper, I want to sort the list of available products so I can easily categorically sort products.</a>
  
- PURCHAING AND CHECKOUT
  - As a shopper, I want to adjust the number of individual items in my bag so I can easily make changes to my purchase before checking out.</a>
  - As a shopper, I can delete items from my basket so that I can buy only the items that I need.</a>
  - As a shopper I can press the delete button so that I can have the final price after I had deleted an item in my cart/basket.</a>
  
- ADMIN AND STORE MANAGEMENT
  - As a site owner, I want to add a product so I can add new items to my store.</a>
  - As a store owner, I want to edit/update a product so I can change product prices, descriptions, images, and other product criteria.</a>
  - As a shop owner, I want to delete a product so I can remove items that is no longer for sale.</a>
   
  
  ### Strategy

  - This is a website where users can find old books and office supplies : 
  - Users that are passionate readers :
   ### Scope
   - The website provides for the user an easy navigation , photos,content,filter and prices with regards the books.

## Typography


## Color


 ## Structure
 ### Skeleton

   ### Wireframes 
  - Wireframes created with Balsamiq
  

   ### Mobile



   ### Desktop



   </details>

## Database Schema



## Features

  
   ### Existing Features (Photo Links)

   #### Navbar

   
  
   #### Homepage

   

   #### Footer
   


   #### Pay form Page
   


   #### Register as a User
  


   #### Product Page
 

   #### 404 Page
   Due to time restrections I wouldnt be able to add a 404 page in time for my submmision , I will add one after


   ### Future Features 

   #### Model of payment based on subscriptions

   - 

   #### Chat window

   - 

   #### Wishlist
  
   - 

  ## SEO


  ## Social Media
 

  ## Email Marketing 
  

  ## Testing

  The project was manually tested by following the steps :
  - Code was run trough the validator resulting no issues
  - Deploying the project from gitpod workspace trough Heroku
  - The site was also tested on I-Pad , I-Phone and Laptop.
  
  ### Testing User Stories from User Experience (UX) Section

  - All user stories in the list above has been tested and confirmed after implementation.
   
  #### robots.txt  
   -  
  #### sitemap.xml  
   -  
  
  #### Functionality Testing

  * Lighthouse

    

  * HTML

    

  * CSS

   


  * PEP8 
  <

  </details>


  ## Deployment

  Local Deployment

   I used Gitpod to write the code for my project, with regular commits to document the creation process. For this project, I deployed it to Heroku and used "git push Heroku master" to ensure that my GitHub pushes were also pushed to Heroku.

      Create an .env that contains these variables :
      SECRET_KEY=*******
      DEVELOPMENT=True
      ENVIRON=DEVELOPMENT
      STRIPE_PKEY=*******
      STRIPE_SKEY=*******

  #### Deploy to Heroku

    To deploy this page to Heroku from its GitHub repository, the following steps were taken:

    Start by installing everything in the requirements.txt file.
    You should have the corect requirements.txt and Procfile before moving on with the deployment.
    Log in to Heroku apps
    On Heroku page go to dashboard then to the "New" menu and choose "Create new app"
    Create a unique name for your app , select your region and click "Create app".
    Now the new app's dashboard is opened. Click on the resources tab.
    Add the Heroku Postgres Add-on.
    Go to the settings tab and reveal the Config Vars and add :
    ALLOWED_HOSTS=https://heroku-url
    CLOUDINARY_URL=cloudinary://cloudinary-url
    DATABASE_URL=postgres://database_url
    DEVELOPMENT=False (DEBUG)
    ENVIRON=PRODUCTION
    EMAIL_HOST=smtp.server
    EMAIL_PORT=587
    EMAIL_HOST_USER=****
    EMAIL_HOST_PASS=****
    EMAIL_FROM=email@from
    SECRET_KEY=****
    STRIPE_PKEY=****
    STRIPE_SKEY=****
    STRIPE_ENDPOINT_SECRET=****
    Click on "Deploy" and select your deploy method and repository.
    Click "Connect" on selected repository
    Click "Deploy Branch" in the manual deploy section. -> Heroku will now deploy the App.
    Development Environment

  ## Credits

  #### Media

   - All images for the book  have been taken from  http://www.amazon.com
   - Cover image for the site has been taken from  https://www.centracare.com
   - All description content for the books has been taken from https://books.google.ie/books/about/

  #### Code 

   - Through this project, I relied heavily on tutorials and Bootstrap examples.

   - Code Institute Boutique Ado and Very Academy on Youtube

   - I found this bookstore walkthrough to be brilliant. I found it extremely helpful for making Django sites more dynamic. As a result of this tutorial, I learned how to make AJAX calls. I also learned a lot about database design and setting up a Stripe webhook.

   - [Codegrepper](https://www.codegrepper.com/code-examples/python/jinja+get+current+url+django) as a general resource.

   - [W3School](https://www.w3schools.com/) as a general resource.

  #### Programming Languages 

  - Python
  - HTML
  - CSS
  - JavaScript
  

  #### Payments

  - Payment functionality was implemented using the Stripe system. The system was set up using the Boutique Ado project and Stripe documentation.

  - For testing the payment system, the following dummy details can be used: Card number: 4242 4242 4242 4242 Expiry: 04/24 CVC: 242

  - No auth: 4242424242424242

  - Auth: 4000002500003155

  - Error: 4000000000009995

  
  #### Frameworks, Libraries & Programs Used

  - [Balsamiq](https://balsamiq.cloud/) - Was used to create the wireframes
  - [Bootstrap](https://getbootstrap.com/) - Was used to contribute to responsiveness and styling of the site
  - [TinyJPG](https://tinyjpg.com/) - Was used to compress images before uploading
  - [GitHub](https://github.com/) - Holds the repository of my project, GitHub connects to GitPod and Heroku
  - [GitPod](https://gitpod.io/) - Connected to GitHub, GitPod hosted the coding space,
   allowing the project to be built and then committed to the GitHub repository.
  - [Heroku](https://heroku.com/) - Connected to the GitHub repository, Heroku is a cloud application platform used 
   to deploy this project so the backend language can be utilised/tested.
  - [Django](https://www.djangoproject.com/) - This framework was used to build the foundations of this project
  - [Gunicorn](https://gunicorn.org/) - Gunicorn is a pure-Python HTTP server for WSGI applications.
  - [Cloudinary](https://cloudinary.com/) - Used to store images online for the recipe posts.
   a list of ingredients and method steps.
  - [GoogleFonts](https://fonts.google.com/) - Provide fonts for the website.
  - [FontAwesome](https://fontawesome.com/) - Was used for icons.
  - [AmIResponsive](https://ui.dev/amiresponsive) - To check if the site is responsive on different screen sizes.
  - [W3CMarkupValidator](https://jigsaw.w3.org/) - Was used to validate HTML.
  - [Colors](https://color-hex.org/) - To make color palette

 
  #### Acknowledgements

 