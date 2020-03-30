# Github Project Opener
## Overview
Simple script written for opening existing project on github page. 

Instead of opening browser and manually going into github and specified repository - use this script! 

## How to run
1. Download or clone repository
2. In settings.py change github_username
3. In open.bat change open.py to full path to open.py script (eg. "C:/Users/Test/Documents/github-project-opener/open.py")
4. Add new environment variable with name of your chose and path to the open.bat script
5. Run script using environment variable  
```
%your_variable_name% optional_project_name
```

if you pass optional_project_name - script will open that project on github,  
if you dont - script will take current directory and one above and concatenate them into project name, and try to open that on github 


### Scenario 1
- You're currently in the directory given below:
> C:/Users/Test/Python/HelloWorld
- when you open cmd here and type 
```
%env_variable_name%
```
- script will take Python and HelloWorld and concatenate it into
> https://github.com/github_user/python-HelloWorld
- and then will open it in system's default browser

### Scenario 2
- You're currently in the directory given below:
> C:/Users/Test/Python/HelloWorld
- when you open cmd here and type
```
%env_variable_name% MyTestProjectOnGithub
```
- script will open following url in your default browser
> https://github.com/github_user/MyTestProjectOnGithub