# GAMER Ø
#### Video Demo: https://youtu.be/BQ0VhuiBtzs
#### Description: Gamer Ø is a web application that allows users to explore a database of video games and check their specific completion stats.

Let's start with the helpers.py file. In it, I applied only the login_required function, which serves to assist the functions in app.py, ensuring that certain actions only occur if the user is logged in. Games.db is my SQL database containing the games and users tables. In app.py, I import essential tools such as Flask, SQL, and werkzeug.security. An important point is the after_request function, which configures headers to prevent the browser from caching pages. This is vital for security, as it prevents someone from being able to go back and view sensitive information just by clicking the browser's 'back' button after logging out.

Regarding account security, I used generate_password_hash and check_password_hash. Instead of saving the user's actual password in the database, which would be dangerous, the system saves an encrypted version (hash). This way, even if the database were accessed, the original passwords would be protected. Regarding the design, index.html was challenging; I used Bootstrap to create a dark theme that matches the gamer aesthetic. In the index, I used Flexbox to align items exactly as planned and the SQL LIKE command to make searching more flexible, allowing games to be found even without typing the full name. To work on the HTML with Bootstrap, the index was one of the most tiring parts because I didn't know much about this library's commands; on the other hand, logout was the easiest.

The busca.html displays results with game covers, gameplay hours, and difficulty. I faced the technical challenge of linking each image to its respective ID. I solved this by creating an img folder where the photos are numbered in sequence with the database IDs, using a Jinja loop to automate the display. Finally, apology.html provides clear visual feedback through a Bootstrap alert box when login errors or empty fields occur.

Project Structure

app.py: The main controller of the Flask application. It manages routes, user authentication logic, and communication with the SQL database to process game searches.

helpers.py: Contains utility functions, specifically the login_required decorator, which protects sensitive site routes, ensuring that only authenticated users can access the search features.

games.db: The SQLite database that stores game information (within the games table) and user credentials with hashed passwords (within the users table).

static/img/: A crucial directory that stores game covers in JPG format. Each file is named according to the game's ID in the database to facilitate automation.

templates/layout.html: The base skeleton of the site. It defines the common structure, such as the navigation bar (navbar) and footer, using Jinja2 blocks to insert content from other pages.

templates/index.html: The project's home page where the search bar is located. It uses Bootstrap and Flexbox for a modern and responsive look.

templates/busca.html: Where the search results are displayed. This file organizes the data returned by SQL into a sleek, dark table showing detailed gameplay statistics.

templates/login.html & register.html: User entry and registration forms, styled with Bootstrap Card components to maintain visual consistency and security.

templates/apology.html: A dedicated error page that displays user-friendly messages when something goes wrong, such as an incorrect password or empty fields.

