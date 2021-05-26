# What 2 Watch BackEnd

## Table of Contents
- [Contributors](#Contributors)
- [Requirements](#Requirements)
- [Summary](#Summary)
- [Routes](#Routes)
- [Schema](#Schema)

## Contributors
- Hope McGee | [LinkedIn](linkedin.com/in/hope-mcgee/) | other socials
- Trevor Robinson | [LinkedIn](https://www.linkedin.com/in/trevor-robinson-0bb251207/) | other socials
- Garrett Cottrell | [LinkedIn](https://www.linkedin.com/in/garrett-cottrell-52850834/) | other socials

## Requirements
- Python 3.9.4
- Django 3.2.3
- Django REST Framework 3.12.4

## Summary
This app is designed to work as the backend for an app that is able to tell a user what movies are on the streaming service(s) that they own, as well as being able to provide tailored recommendations for the user. This app is hosted on [Heroku](https://what-2-watch-be.herokuapp.com/) and uses [CircleCI](https://app.circleci.com/pipelines/github/What-2-Watch/what-2-watch-be) for continuous integration.

This app uses data from [The Movie DataBase API V3](https://api.themoviedb.org/3) | [Documentation](https://developers.themoviedb.org)

This app is tested using Django-Pytest.

## Routes:
Main path:
```
'https://what-2-watch-be.herokuapp.com/'
```

### Users:

```
  /v1/users/:

    get:
      - Fetches all users and reports their information. Doesn't require a body or any parameters.

    post:
      - Creates a user with the given information. Requires a JSON request body with the following information:
        - email (string)
        - first_name (string)
        - last_name (string)
        - password (string)
        - region (string)
        - language (string)

  /v1/users/{id}/:

    get:
      - Fetches the specified user's information. Doesn't require a body or parameters because the user ID is passed in the URI.

    put:
      - Replaces the specified user's information. Requires a JSON body with the following information:
        - email (string)
        - first_name (string)
        - last_name (string)
        - password (string)
        - region (string)
        - language (string)

    patch:
      - Replaces the specified user's information. requires a JSON body with any of the following information:
        - email (string)
        - first_name (string)
        - last_name (string)
        - password (string)
        - region (string)
        - language (string)

    delete:
      - Deletes the specified user. Doesn't require a body or any params.
  ```
  
### Login

  ```
  /v1/rest-auth/login/
    
    post:
      - Authenticates a user's login credentials. Requires a JSON body with the following fields:
        - email (string)
        - password (string)
      - If given credientials are valid, returns a unique user token. Otherwise, returns an error.
      
  /v1/rest-auth/user/
  
    get:
      -Returns a user's details if a valid user token is present. If no token is present, returns an error.
  ```

### Subscriptions

  ```
  /v1/subscriptions/:

    post:
      - Creates a subscription for a user. Requires the user's id be passed in along with other fields for its creation, in a JSON body. Requires:
        - user (integer) - this is the ID of the user to connect this subscription to
        - api_provider_id (integer) - this is the ID that The Movie DB API uses for a Watch Provider.
        - name (string) - this is the name of the service (i.e. Netflix, Hulu)

  /v1/subscriptions/{id}/:

    get:
      - Displays the information for a specified Subscription object.

    put:
      - Updates all fields of a Subscription object. Requires these fields in a JSON body:
        - user (integer) - this is the ID of the user to connect this subscription to
        - api_provider_id (integer) - this is the ID that The Movie DB API uses for a Watch Provider.
        - name (string) - this is the name of the service (i.e. Netflix, Hulu)

    patch:
      - Updates specified fields of a Subscription object. Requires any of these fields in a JSON body:
        - user (integer) - this is the ID of the user to connect this subscription to
        - api_provider_id (integer) - this is the ID that The Movie DB API uses for a Watch Provider.
        - name (string) - this is the name of the service (i.e. Netflix, Hulu)

    delete:
      - Deletes a Subscription object. This is particularly useful for when a user reports that they are no longer subscribed to a service. Doesn't require any params or a body.
  ```

### Watchlists

  ```
  /v1/watchlists/:

    get:
      - Fetches all Watchlists. Doesn't require a body or any params.

    post:
      - Creates a Watchlist object for a user. Requires the user's ID. Requires a JSON body. Fields:
        - user (integer) - the user's ID
        - api_movie_id (integer) - the ID of the mmovie that TMDB API uses
        - title (string) - the title of the movie

  /v1/watchlists/{id}/:

    get:
      - Fetches a Watchlist object from its ID. Doesn't require a JSON body or any params.

    put:
      - Updates all fields a Watchlist object. Requires a JSON body. Fields:
        - user (integer) - the user's ID
        - api_movie_id (integer) - the ID of the movie that TMDB API uses
        - title (string) - the title of the movie

    patch:
      - Updates the specified fields on a Watchlist object. Requires a JSON body. Fields:
        - user (integer) - the user's ID
        - api_movie_id (integer) - the ID of the movie that TMDB API uses
        - title (string) - the title of the movie

    delete:
      - Deletes a Watchlist object. Doesn't require any params or a JSON body.
  ```

### Thumbs

  ```
  /v1/thumbs/:

    get:
      - Get all Thumbs objects. Doesn't require any parameters or a body.

    post:
      - Creates a Thumb object. Requires a user ID. Requires a JSON body. Fields:
        - user (integer) - the ID of the user to create a Thumb object for
        - title (string) - the title of the movie
        - api_movie_id (integer) - the ID that TMDB API uses to refer to the movie
        - up (boolean) - True for thumbs up, False for thumbs down.
        - api_actor_id (integer) - the ID that TMDB API uses to refer to the movie's first listed actor
        - api_director_id (integer) - the ID that TMDB API uses to refer to the movie's first listed director
        - api_genre_id (integer) - the ID that TMDB API uses to refer to the movie's first listed genre
        - api_similar_id (integer) - the ID that TMDB API uses to refer to the movie's ??????

  /v1/thumbs/{id}/:

    get:
      - Fetches a Thumb object and shows its information. Doesn't require a body or any params.

    put:
      - Updates all fields for a Thumb object. Requires the following fields in a JSON body:
        - user (integer) - the ID of the user that the Thumb object is related to
        - title (string) - the title of the movie
        - api_movie_id (integer) - the ID that TMDB API uses to refer to the movie
        - up (boolean) - True for thumbs up, False for thumbs down.
        - api_actor_id (integer) - the ID that TMDB API uses to refer to the movie's first listed actor
        - api_director_id (integer) - the ID that TMDB API uses to refer to the movie's first listed director
        - api_genre_id (integer) - the ID that TMDB API uses to refer to the movie's first listed genre
        - api_similar_id (integer) - the ID that TMDB API uses to refer to the movie's ??????

    patch:
      - Updates the specified fields for a Thumb object. Requires a JSON body with any of the following fields:
        - user (integer) - the ID of the user that the Thumb object is related to
        - title (string) - the title of the movie
        - api_movie_id (integer) - the ID that TMDB API uses to refer to the movie
        - up (boolean) - True for thumbs up, False for thumbs down.
        - api_actor_id (integer) - the ID that TMDB API uses to refer to the movie's first listed actor
        - api_director_id (integer) - the ID that TMDB API uses to refer to the movie's first listed director
        - api_genre_id (integer) - the ID that TMDB API uses to refer to the movie's first listed genre
        - api_similar_id (integer) - the ID that TMDB API uses to refer to the movie's ??????

    delete:
      - Deletes the Thumb object. Useful for when a user retracts their votes on a movie entirely. Doesn't require a body or any params.
  ```
### Recommendations

```
  /v1/movies?user={id}/:
    
    get:
      - fetches recommended movies for a user based on our data and TMDB's. Requires a "user" query param that is the user's ID in order to provide personalized recommendations. Without a "user" param, the returned data will be based on popular movies (according to TMDB).
      - This endpoint doesn't refer to a table, and as such, does not have CRUD functionality.
```
## Schema

### User:
A table to manage users. This is a custom table that's actually named CustomUser.

Fields:
| Name | Type | Description |
| :---: | :---: | :---: |
| id | Integer | Primary Key set automatically by Django. |
| first_name | String | The user's first name. |
| last_name | String | The user's last name. |
| email | String | The user's email address. |
| region | String | The code to signify the user's region (ex: 'US'). |
| language | String | The code to signify the user's language (ex: 'EN'). |

Relationships:
* Watchlist (Many)
* Thumb (Many)
* Subscription (Many)

### Subscription:
A table to manage a user's subscription status to various streaming services.

Fields:
| Name | Type | Description |
| :---: | :---: | :---: |
| id | Integer | Primary Key set automatically by Django. |
| user | Integer | The related user's ID. |
| api_provider_id | Integer | The ID that The Movie Database API uses to refer to the streaming service. |
| name | String | The name of the streaming service. |

Relationships:
* User(CustomUser) (Owner)

### Watchlist:
A table to manage information on the movies that the user has marked to watch later.

Fields:
| Name | Type | Description |
| :---: | :---: | :---: |
| id | Integer | Primary Key set automatically by Django. |
| user | Integer | The related user's ID. |
| api_movie_id | Integer | The ID that The Movie Database API uses to refer to the movie. |
| title | String | The title of the movie. |

Relationships:
* User(CustomUser) (Owner)

### Thumbs:
A table to manage movies that a user has given their opinion on.

Fields:
| Name | Type | Description |
| :---: | :---: | :---: |
| id | Integer | Primary Key set automatically by Django. |
| title | String | The title of the movie. |
| up | Boolean | States whether the user liked or disliked the movie. |
| api_movie_id | Integer | The ID that The Movie Database API uses to refer to the movie. |
| api_director_id | Integer | The ID that The Movie Database API uses to refer to the movie's first listed director. |
| api_actor_id | Integer | The ID that The Movie Database API uses to refer to the movie's first listed actor. |
| api_genre_id | Integer | The ID that The Movie Database API uses to refer to the movie's first listed genre. |
| api_similar_id | Integer | The ID that The Movie Database API uses to refer to the first movie returned in a 'similar movies' call. |

Relationships:
* User(CustomUser) (Owner)
