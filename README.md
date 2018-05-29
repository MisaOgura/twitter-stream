# Twitter Stream with Kafka

## Introdunction

A project for Gender Paygap Data Hack!

## Instructions

### 1. Create a virtual environment & install dependencies

```sh
# Move to the project directory.
$ cd twitter-stream

# virtualenv helps you manage isolated Python environments.
$ (sudo) pip install virtualenv

# Check the version to make sure virtual env is installed correctly.
$ virtualenv --version

# Create a virtual environment.
# This creates a directory venv/ where all the dependencies will be installed.
$ virtualenv venv

# Activate the virtual environment just created.
$ source venv/bin/activate

# Install dependencies under the virtual environment.
$ pip install -r requirements.txt

# When you are done working with this project.
$ deactivate
```

### 2. Obtain credentials from Twitter Developer

You need API tokens from Twitter in order to use the Streaming API.

- Follow steps described in the Twitter Developer API docs: [Access Tokens](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html)

- When you create a new app, you are asked to fill in Name, Description and Website for your application. You can use a placeholder for the website (e.g. `http://placeholder.com`).

- You can see your credentials under the `Keys and Access Tokens` tab of your application.

- Create `.env` file in the root of the project, and add following 4 lines, replacing the values with your own credentials. This file is ignored in `/.gitognore`, as it _should not_ be checked in for security purposes.

```sh
CONSUMER_KEY="PASTE YOUR COMSUMER KEY"
CONSUMER_SECRET="PASTE YOUR CONSUMER SECRET"
ACCESS_TOKEN="PASTE YOUR ACCESS TOKEN"
ACCESS_TOKEN_SECRET="PASTE YOUR ACCESS TOKEN SECRET"
```

### 3. Launch Zookeeper and Kafka

### 4. Create a topic

### 5. Run the stream

## Other tips

### Modifying the tweet filter

```python
### twitter_stream.py

# Filter with one word - provide a string
stream.filter(track='paygap', async=True)

# Filter with multiple words - provide a list
stream.filter(track=['gender', 'paygap'], async=True)

```

## Authour

Misa Ogura
