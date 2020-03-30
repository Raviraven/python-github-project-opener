import sys
import os
import settings
import webbrowser

def open_project():
    project_name = get_project_name()
    url = 'https://github.com/{0}/{1}'.format(str(settings.github_username), project_name)
    
    '''
    If new is 0, the url is opened in the same browser window if possible. 
    If new is 1, a new browser window is opened if possible. 
    If new is 2, a new browser page ("tab") is opened if possible.
    '''
    webbrowser.open(url, new=2)

def get_project_name():
    try:
        project_name = str(sys.argv[1])
    except:
        project_name = 'test none'
        current_directory = os.getcwd().split('\\')
        project_name = '{0}-{1}'.format(current_directory[-2].lower(), current_directory[-1])
    return project_name
    

if __name__ == '__main__':
    open_project()
