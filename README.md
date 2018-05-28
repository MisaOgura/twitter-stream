# Twitter Stream with Kafka
---

## Introdunction

A project for Gender Paygap Data Hack

## Instructions

### 1. Create a virtual environment & install dependencies

```sh
# Move to the project directory
$ cd twitter-stream

# virtualenv helps you manage isolated Python environments
$ (sudo) pip install virtualenv

# Check the version to make sure virtual env is installed correctly
$ virtualenv --version

# Create a virtual environment
# This creates a directory venv/ where all the dependencies will be installed
$ virtualenv venv

# Activate the virtual environment just created
$ source venv/bin/activate

# Install dependencies under the virtual environment
$ pip install -r requirements.txt

# When you are done working with this project:
$ deactivate
```

### 2. Obtain credentials from Twitter API

- Follow steps here: [How to get API Keys and Tokens for Twitter](https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/)
- create `.env` file (this is ignored in `/.gitognore` for security purposes)

```sh
ACCESS_TOKEN="PASTE YOUR ACCESS TOKEN"
ACCESS_TOKEN_SECRET="PASTE YOUR ACCESS TOKEN SECRET"
CONSUMER_KEY="PASTE YOUR COMSUMER KEY"
CONSUMER_SECRET="PASTE YOUR CONSUMER SECRET"
```

### 3. Launch Zookeeper and Kafka

### 4. Create a topic

### 5. Run the stream

## Tips

### Modifying the tweet filter

```python
# For one word filter - provide a string
stream.filter(track='paygap', async=True)

# For multiple words - provide a list
stream.filter(track=['gender', 'paygap'], async=True)

```

## Authour

Misa Ogura
