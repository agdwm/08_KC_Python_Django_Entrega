# Wordplease:
"Wordplease" is a blogging platform in which any user can register to create a personal blog.

## Development setup

1. Install Python 3.5+
2. Install requirements** using: `pip install -r requirements.txt`
3. Enter the `src` folder with `cd src`
4. Create database & apply migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`   
6. Run development server with `python manage.py runserver`

** ***NOTES*** :

This application uses the following extra dependencies:  

- django-embed-video: [https://github.com/jazzband/django-embed-video](https://github.com/jazzband/django-embed-video)
- django-rest-framework: [http://www.django-rest-framework.org/](http://www.django-rest-framework.org/)
- django-filter: [https://github.com/carltongibson/django-filter/tree/master](https://github.com/carltongibson/django-filter/tree/master)

Every time we install a new dependency, we must update the field ***"requirements.txt"***:

`pip freeze > requirements.txt`


## Website related paths

The following paths are available on this site:  

[/](/): The home path shows the latest posts created by the registered users (sorted by release date in descending order).

[admin/](admin/): This path provides a superuser access to the Administration Panel through an authentication form.

[singup/](singup/): It allows any user to register on the platform and register a blog associated with their account.

[login/](login/): It allows a user to logging into the website using basic authentication (username and password)

[logout/](logout/): It allows a user to logout.

[blogs/](blogs/): It shows a list of all the blogs registered on the website.

[blogs/\<str\:author\>/](blogs/\<str\:author\>/): It shows a list of all the posts created by one author on the website.

[blogs/\<str\:author\>/\<int:pk\>](blogs/\<str\:author\>/\<int:pk\>): It shows the detail of a post belonging to one user (author).

[new-post/](new-post/): It allows an authenticated user to create a new post associated with their blog.

## API usage and related paths:

***NOTE***: Some of the following endpoints require the user to be authenticated. To do this, we only need to register as a new user on the platform (in case we have not previously registered), in the way explained in point number 2. After that, you have use those endpoints sending your requests with a *Basic Authentication* ("username" and "password"). 

### * USERS API:

### 1. List of users:
It retrieves a list of all of the users registered on the platform.

HTTP Method: **GET**

Requirements: This endpoint can only be used by an administrator.

URL: [http://localhost:8000/api/1.0/users/](http://localhost:8000/api/1.0/users/)


### 2. Register a user:
It register a new user on the platform.

HTTP Method: **POST**

Requirements: Any user can use this endpoint.

URL: [http://localhost:8000/api/1.0/users/](http://localhost:8000/api/1.0/users/)

Request Body: *(The following fields are required)*

```
{
	"first_name": "john",
	"last_name": "doe",
	"username": "johndoe",
	"email": "johndoe@mail.com",
	"password": "supersegura",
	"blog_title": "John Doe's blog"
}	
```

### 3. Retrieve the detail of a user:

It retrieves the detail of a user registered on the platform.  

HTTP Method: **GET**

Requirements: This endpoint can only be used by the user himself or an administrator.

URL: [http://localhost:8000/api/1.0/users/\<int:pk\>](http://localhost:8000/api/1.0/users/\<int:pk\>)

** `<int:pk>`: It is the Primary Key of that user.

Example:

[http://localhost:8000/api/1.0/users/1>](http://localhost:8000/api/1.0/users/1>)


### 4. Update the data of a user:

It updates the data of a user registered on the platform.

HTTP Method: **PUT**

Requirements: This endpoint can only be used by the user himself or an administrator.

URL: [http://localhost:8000/api/1.0/users/\<int:pk\>](http://localhost:8000/api/1.0/users/\<int:pk\>)

** `<int:pk>`: It is the Primary Key of that user.

Request Body: *(The following fields are required)*

```
{
	"first_name": "john",
	"last_name": "doe",
	"username": "johndoe",
	"email": "johndoe@mail.com",
	"password": "supersegura",
	"blog_title": "John Doe's blog title"
}
```

### 5. Delete a user:

It deletes a user registered on the platform.

HTTP Method: **DELETE**

Requirements: This endpoint can only be used by the user himself or an administrator.

URL: [http://localhost:8000/api/1.0/users/\<int:pk\>](http://localhost:8000/api/1.0/users/\<int:pk\>)

** `<int:pk>`: It is the Primary Key of that user.


### * BLOGS API:
### 1. List of blogs:

It retrieves a list of all the blogs registered by the differents user on the platform.

HTTP Method: **GET**

Requirements: Any user can use this endpoint.

URL: [http://localhost:8000/api/1.0/blogs/](http://localhost:8000/api/1.0/blogs/)

*NOTE:*  This endpoint allows us to search blogs by their username and order them by their title. To this end, the following query params are allowed:  

- search
- ordering

Examples:

* It finds a blog whose author matches the username entered.  
[http://localhost:8000/api/1.0/blogs/?search=\<username\>](http://localhost:8000/api/1.0/blogs/?search=\<username\>)
* It sorts all the blogs alphabetically by their title.  
[http://localhost:8000/api/1.0/blogs/?ordering=blog_title](http://localhost:8000/api/1.0/blogs/?ordering=blog_title)


### * POSTS API:
### 1. List of posts:

It retrieves a list of all the posts belonging to a registered user's blog.

HTTP Method: **GET**

Requirements: Any user can use this endpoint. However, if a user is not authenticated or is authenticated but is not an administrator or the owner of that blog, they will not be able to see those posts that have a future release date. In other words, only the owner of the blog or an administrator will be able to see the posts that are still in draft status.

URL: [http://localhost:8000/api/1.0/blogs/\<username\>/](http://localhost:8000/api/1.0/blogs/\<username\>)

*NOTE:*  This endpoint allows us to search and filter among the posts of blog by their 'title' or 'intro' and order them by their title or release date. To this end, the following query strings are allowed:  
- search  
- ordering

Examples:

* It ***finds*** all the posts whose title or intro contains the searched text.  
[http://localhost:8000/api/1.0/blogs/\<username\>/?search=\<searched_text\>](http://localhost:8000/api/1.0/blogs/\<username\>/?search=\<searched_text\>)
 
* It ***sorts*** all the posts alphabetically, either according to the title or by release date.  
[http://localhost:8000/api/1.0/blogs/\<username\>/?ordering=post_title](http://localhost:8000/api/1.0/blogs/jonhdoe/?ordering=post_title>)  
[http://localhost:8000/api/1.0/blogs/\<username\>/?ordering=release_date](http://localhost:8000/api/1.0/blogs/jonhdoe/?ordering=release_date>) 

* It ***filter*** all the posts whose title or intro matches the searched text.  
[http://localhost:8000/api/1.0/blogs/\<username\>/?post\_title=\<searched_text\>](http://localhost:8000/api/1.0/blogs/jonhdoe/?post\_title=\<searched_text\>)  
[http://localhost:8000/api/1.0/blogs/\<username\>/?intro=\<searched_text\>](http://localhost:8000/api/1.0/blogs/jonhdoe/?intro=\<searched_text\>)

### 2. Create a new post:

It creates a new post in a registered user's blog.

HTTP Method: **POST**

Requirements: Only authenticated users will be able to use this endpoint. Once the article is created, it will automatically be associated with the blog of the  authenticated user, previously mentioned.

URL: [http://localhost:8000/api/1.0/blogs/\<username\>/](http://localhost:8000/api/1.0/blogs/\<username\>/)

Request Body:

**Optional Fields:** *'video', 'image'*

*NOTE:*  A post may have an image or a video associated with it, or neither of them, but not both at the same time. Therefore, two possible resquests exist.

```
{
    "post_title": "This is the title of this post(up to 150 characteres)",
    "intro": "This is the introduction text of this post (up to 400 characters)",
    "content": "This is the content of this blog",
    "image": "https://loremflickr.com/960/540/tech",
    "release_date": "2019-02-06T18:28:37+01:00",
    "category": [2, 4]
}

```
or

```
{
    "post_title": "This is the title of this post(up to 150 characteres)",
    "intro": "This is the introduction text of this post (up to 400 characters)",
    "content": "This is the content of this blog",
    "video": "https://www.youtube.com/watch?v=ShOVEPNW_co",
    "release_date": "2019-02-06T18:28:37+01:00",
    "category": [2, 4]
}
```

### 3. Retrieve the detail of a post:

It retrieves the detail of one post belonging to a registered user's blog.

HTTP Method: **GET**

Requirements: Any user can use this endpoint. However, if a user is not authenticated or is authenticated but is not an administrator or the owner of that blog, they will not be able to see those posts that have a future release date. In other words, only the owner of the blog or an administrator will be able to see the posts that are still in draft status.

URL: [http://localhost:8000/api/1.0/blogs/\<username\>/\<int:pk\>](http://localhost:8000/api/1.0/blogs/\<username\>/\<int:pk\>)


### 4. Update a post:

It updates the data of a post belonging to a registered user's blog.

HTTP Method: **PUT**

Requeriments: Only the owner of the post or an administrador will be able to use this endpoint.

URL: [http://localhost:8000/api/1.0/blogs/\<username\>/\<int:pk\>](http://localhost:8000/api/1.0/blogs/\<username\>/\<int:pk\>)

Request Body:

**Optional Fields:** *'video', 'image'* 

*NOTE:*  A post may have an image or a video associated with it, or neither of them, but not both at the same time. Therefore, two possible resquests exist.

```
{
    "post_title": "Post title updated",
    "intro": "Post introduction text updated",
    "content": "Post content text updated",
    "image": "https://loremflickr.com/960/540/tech",
    "release_date": "2019-02-06T18:28:37+01:00",
    "category": [1, 4]
}
```
or
```
{
    "post_title": "Post title updated",
    "intro": "Post introduction text updated",
    "content": "Post content text updated",
    "video": "https://www.youtube.com/watch?v=ShOVEPNW_co",,
    "release_date": "2019-02-06T18:28:37+01:00",
    "category": [1, 4]
}
```

### 5. Delete a post:

It deletes a post belonging to a registered user's blog.

HTTP Method: **DELETE**

Requeriments: Only the owner of the post or an administrador will be able to use this endpoint.

URL: [http://localhost:8000/api/1.0/blogs/\<username\>/\<int:pk\>](http://localhost:8000/api/1.0/blogs/\<username\>/\<int:pk\>)