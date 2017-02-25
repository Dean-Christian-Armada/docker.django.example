# Source: http://stackoverflow.com/questions/23755523/how-to-reset-migrations-in-django-1-7
"""
Run this file from a project root. 
Removes all migration files from all apps in a project for production purposes
""" 
from unipath import Path

this_file = Path(__file__).absolute()
current_dir = this_file.parent
dir_list = current_dir.listdir()

print dir_list

for paths in dir_list:
    migration_folder = paths.child('migrations')
    if migration_folder.exists():
        list_files = migration_folder.listdir()
        for files in list_files:
            split = files.components()
            if split[-1] != Path('__init__.py'):
                files.remove()