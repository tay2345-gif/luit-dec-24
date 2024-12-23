import os
from pprint import pprint  # To print in a more readable format
from datetime import datetime

# Get the current working directory
working_directory = os.getcwd()

# Get the list of files and directories in the working directory
files_and_dirs = os.listdir(working_directory)

# Create a list of dictionaries about the files
file_info_list = []
for item in files_and_dirs:
    item_path = os.path.join(working_directory, item)
    
    # Check if it's a file
    if os.path.isfile(item_path):
        # Get file times
        created_time = os.path.getctime(item_path)
        modified_time = os.path.getmtime(item_path)
        accessed_time = os.path.getatime(item_path)
        
        # Convert timestamps to human-readable format
        created_time = datetime.fromtimestamp(created_time).strftime('%Y-%m-%d %H:%M:%S')
        modified_time = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M:%S')
        accessed_time = datetime.fromtimestamp(accessed_time).strftime('%Y-%m-%d %H:%M:%S')
        
        # Create a dictionary with file information
        file_info = {
            'name': item,
            'size': os.path.getsize(item_path),
            'created': created_time,
            'modified': modified_time,
            'accessed': accessed_time
        }
        file_info_list.append(file_info)

# Print the list of dictionaries in a straight-line format
print("Files in the working directory with their details:")
pprint(file_info_list, width=120)

