import os
import re
directory = r'DIRECTORY'

def renameInvalid(directory):    
    queue = []
    for f in os.scandir(directory):        
        new_name = f.path.replace(" ", "_")
        if f.is_dir():
            os.rename(f.path, new_name)
            queue.append(new_name)
        else:
            os.rename(f.path, new_name)
    while queue:
        renameInvalid(queue.pop())

renameInvalid(directory)

