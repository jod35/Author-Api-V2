# Author API V2
This is a second version of the AuthorApi I created. It has some added functionality like JSON serialization and deserialization with Marshmallow.

## Built With
- Flask
- Flask Marshmallow
- MySQL
## The API Endpoints
 ENDPOINT  |METHOD | FUNCTION|
 ----------|-------|---------|
 /authors/ | GET   |Get all authors|
 /authors/ | POST  |Create an author|
 /author/id| GET   | Get an author with an id|
 /author/id| PUT   | Update an author with an id|
 /author/id| DELETE   | Delete an author with an id|




## To get running
1. Clone the project
`git clone https://github.com/jod35/AuthorAPI-V2`

2. Install project Dependencies
` pip3 install -r requirements.txt `

3. To run the API,
- Create the database ` apidb ` (With MySQL of course)
- Edit ` user ` and ` passwd ` to your MySQL database user and password.
- Enter the command in your termainal ` export FLASK_APP=wsgi.py`
- Enter the command in your terminal ` flask shell ` to access the app in the Flask interactive console. 
- And then run ` db.create_all() ` to set the database up
- Finally run the appliaction with ` flask run `

## Author
[Ssali Jonathan (Jod35)](https://github.com/jod35)
