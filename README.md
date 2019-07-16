# city-explorer-python

# game-of-greed
**Author**: Raven W. Robertson
**Version**: 1.0.0 (increment the patch/fix version number up if you make more commits past your first submission)

## Overview


## Getting Started
I'll be writing this code in python in a pipenv shell. 

## Architecture
I built this application using python3. I installed python dotenv and requests for my dependancies in this project. and 

## API
have a .env file containgin API keys from dark sky and from google geo code. 

## Change Log
10:00pm - features all working but a little buggy. Can't get dict to hold onto infor for longer that one roll of dice? Check with JB ot James tomorrow  7/8/19
11:44pm - worked out most bugs. Trying to build a tally score function to over write user input for score. I built a test for the function. I'm able to get the user input into the function and stored in a dictionary, but the actual tally isn't working and I just need to sleep. 7/9/19
11:55pm - able to get scoring function to pass all tests. Also have a function built to bring in alternate score from a text file. Still working out bugs, really need to refactor. Still need to add classes. 7/11/19
1240am - build up a class for default and alternate rules. I tried to replace scores directly in my function with attributes from the class object, but I received the error, "'Rules' object is not subscriptable". I was, however able to replace the values in my dictionary to a reference of the class and it is still functioning. 
-->