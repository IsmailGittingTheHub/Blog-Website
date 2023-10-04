Blog Website
#### Video Demo:  https://youtu.be/AIiagTcncBs?si=1TAxbt4xM5N6Oliv
#### Description:

In this project I have a created a blog website, where users can write and view blog posts. The website is based on a flask framework, where I have 
imported multiple flask modules and functions to help me create the website. I first created the __init__ python file, where the blueprints, application, and 
SQL databases are imported and created. This is where the flask is also imported and the foundation of project is at. After the blueprints
are created we go to the first blueprint where all the routes are created. This is called views.py, and it has 3 routes. / is for homepage,
/create-post, is a page created for the user where they can make a post and view-post is an extra feature I had added. 

Each route has its own set of criteria and logic to help the website function. The homepage is where all of the previous posts are posted. It goes through the sql 
database and selects all the posts and shows them. You then have the create post page, where the create post html takes in a username and 
text box to include to the post database. The username is just made to show who created the post. Once the html form is completed and the criteria
has been met, it will send the info to the Post table and flash a successful image and redirecting them to the homepage. You then have the view-post 
page, which is an extra feature I had put in. I created some JavaScript in my index.js file which is connected to my homepage, that checks for a click
in the specific section and if it does find a click. It will then give a full screen view of the page by redirecting it to its own page, which the 
/view-post/id<int> page will create for it. 

You then have the auth.py, where the authentication process is made. This is where the code for signing up, logining in, staying logged in, and logging out are created. 
You first have the login code, where the critiera is set on checking if the login info the user had entered in the login.html corresponds with 
the information in the SQL databse for the table user. You then have the sign up page, where the html page has a form with the email, name, password,
and confirmation password to check if the user puts in the correct password. It checks each of the information through a specific criteria, and if it passes
the test, it will be entered into the user table. The user then logs in with just the email and password.

Finally, the layout of the templates is based on a base template called based.html. This is where the bootstrap is put in and defined. You then have 
the navigation bar here too, but layed out, that logged in users only see a specific set of bars and unlogged user sees another set of bars. 
The layout is simple and clean and not too much. The base template also has the flash flask template created, where with a specifc error or success
message that has been sent to it will create a specific flash image. Then finally down below you have the javascript connection. All of this is backed 
up by the sql database and tables created in the models.py. It is where the Post table and User table are defined. A relationship has alos been created
between the two, with a one-to-many relationship, where one user can have many posts.