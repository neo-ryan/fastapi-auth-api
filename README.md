# User Authentication API
Simple and straight to the point api for user authentication, it register users, hashes passwords,
generates and validates access and refresh tokens.

## Tech
- FastAPI framework
- JWT for token generation and validation
- bcrypt for hashing and checking passwords

## Features
- User registration
- Authentication system based on tokens

## How to use
To clone it you should run: 
`git clone https://github.com/neo-ryan/fastapi-auth-api.git`
on your terminal.

Install all the requirements by using:
`pip install -r requirements.txt`
in the root folder, remember to do this on a virtual environment, you shouldn't be deliberately installing
libraries without virtual environments.

### Environment Variables

Create a `.env` file in the root folder with the following variables:

```env
KEY=your_secret_key_here
ALGORITHM=HS256
```

To generate a secure key you can run the following command in your terminal:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
### Start the server
Running the server: `fastapi dev main.py` 

By default, the url will be http://127.0.0.1:8000/ and the docs url http://127.0.0.1:8000/docs#/.

Now to test the endpoints, you can either use curl or the url, but i do recommend going to the 
/docs# page that FastAPI provides, it makes the job quite easier, although the /auth/users/me endpoint
needs curl to be tested.

## Endpoints
- POST /auth/register - Registers an user in the database/json, after the username, email and password are provided,
  the password will be hashed and the user data will be saved with a hash replacing the password for security.
- POST /auth/login - Receives the user's email and password, it will then find the user by the email and validate the
  hash, after validated, it will return a temporary access token to the user, while creating a refresh token that
  can be used to extend the access.
- GET /auth/users/me - Receives an access token, searches for the user data and returns it to the user.
- POST /auth/refresh - Receives a refresh token and validates it, if it's valid and not expired, another access
  token will be generated and returned to the user.
- POST /auth/logout - Receives a refresh token and removes it from the tokens database, effectively forcing the user
  to log in after expiration.

# How the authentication works
It is based on jwt token generation and validation, it generates digitally signed tokens that shall be included in 
subsequent requests to verify the user.

After successfully logging in, the user will receive a temporary access token and a refresh token that can be used
to extend the access for a while by adding more 30 minutes, the refresh token lasts for way more than the access,
it is safely kept in the tokens database (json file as a mock database) and is removed while logging out (/auth/logout).
