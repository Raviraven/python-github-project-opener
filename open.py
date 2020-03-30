import sys
import os
import settings

def open_project():
    project_name = get_project_name()
    if not project_name:
        project_name = 'test none'
        current_directory = os.getcwd().split('\\')
        project_name = '{0}-{1}'.format(current_directory[-2].lower(), current_directory[-1])
    
    url = 'https://github.com/{0}/{1}'.format(str(settings.github_username), project_name)
    

def get_project_name():
    try:
        project_name = str(sys.argv[1])
        return project_name
    except:
        return None


if __name__ == '__main__':
    open_project()
