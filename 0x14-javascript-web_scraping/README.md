# 0x14-javascript-web_scraping

## Resources

**Read or watch:**
    - [Working with JSON data](https://intranet.alxswe.com/rltoken/ONv-sSv-FA87Mc5rMZmO6A)
    - [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://intranet.alxswe.com/rltoken/zm0h7FqpQCZZpPZqxxwLxA)
    - [request module](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ)
    - [Modern JS](https://intranet.alxswe.com/rltoken/j2PStAUtVPdXKwrrFxpt0g)

## More Info

### Install Node 10

    $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    $ sudo apt-get install -y nodejs


### Install semi-standard

[Documentation](https://intranet.alxswe.com/rltoken/GXh9DyGGivUB7pdq9Oqmzg)

    $ sudo npm install semistandard --global

### Install `request` module and use it

[Documentation](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ)

    $ sudo npm install request --global
    $ export NODE_PATH=/usr/lib/node_modules

**Notes**: Request module has been deprecated since February 2020- the team is considering alternative to replace this module - however, it's a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

### Tasks

#### 0. Readme

Write a script that reads and prints the content of a file.

- The first argument is the file path
- The content of the file must be read in `utf-8`
- If an error occurred during the reading, print the error object

#### 1. Write me

Write a script that writes a string to a file.

- The first argument is the file path
- The second argument is the string to write
- The content of the file must be written in `utf-8`
- If an error occurred during while writing, print the error object

#### 2. Status code

Write a script that display the status code of a `GET` request.

- The first argument is the URL to request (`GET`)
- The status code must be printed like this: `code: <status code>`
- You must use the module `request`

#### 3. Star wars movie title

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

- The first argument is the movie ID
- You must use the [Star wars API](https://intranet.alxswe.com/rltoken/HwLU2L7tJ4TEjzfTBc7zTA) with the endpoint `https://swapi-api.alx-tools.com/api/films/:id`
- You must use the module `request`

#### 4. Star wars Wedge Antilles

Write a script that prints the number of movies where the character 'Wedge Antilles' is present.

- The first argument is the API URL of the [Star wars API](https://intranet.alxswe.com/rltoken/HwLU2L7tJ4TEjzfTBc7zTA): `https://swapi-api.alx-tools.com/api/films/`
- Wedge Antilles is character ID `18` - your script must use this ID for filtering the result of the API
- You must use the module `request`

#### 5. Loripsum

Write a script that gets the contents of a webpage and stores it in a file.

- The first argument is the URL to request
- The second argument the file path to store the body response
- The file must be `UTF-8` encoded
- You must use the module `request`

#### 6. How many completed?

Write a script that computes the number of tasks completed by user id.

- The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`
- Only print users with completed task
- You must use the module request

