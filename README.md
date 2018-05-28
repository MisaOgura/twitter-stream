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

### 2. Launch Zookeeper and Kafka

### 3. Create a topic

### 4. Run the stream

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
