import os
import shutil
import datetime

def prune_dir(days, path, item='file'):
    '''
    This function prunes a directory by removing files and/or folders that haven't been modified
    within a defined number of days.

    Inputs:
    days {int or float}: number of days back to keep
    path {str}: directory path to prune
    item {str}: item to prune. input value of (file, folder, all)
    '''
    assert item in ('file', 'folder', 'all'), "item value should be one of ('file', 'folder', 'all')"
    assert type(days) in (int, float), f'expected days type int or float, but {type(days)} was provided'

    # get the current time
    now = datetime.datetime.now()

    # set the time delta
    threshold = datetime.timedelta(days)

    # loop through the directory
    for file_name in os.listdir(path):
        # get the path
        file_path = os.path.join(path, file_name)

        # check if the file has been modified within the time threshold
        if now - datetime.datetime.fromtimestamp(os.path.getmtime(file_path)) > threshold:

            # Check the file case
            if item in ('file', 'all'):
                if os.path.isfile(file_path):          
                    # delete the file
                    os.remove(file_path)

            # Check the folder case
            if item in ('folder', 'all'):
                if os.path.isdir(file_path):
                    # delete old folder
                    shutil.rmtree(file_path)