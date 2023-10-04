import os


def delete_files_below_threshold(directory, size_threshold):
    """
    Deletes files in the specified directory if their size is below the given threshold.

    Parameters:
    - directory (str): The path to the directory to be checked.
    - size_threshold (int): The size threshold in bytes. Files below this size will be deleted.
    """

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            if file_size < size_threshold:
                # os.remove(file_path)
                print("want to remove file = ", file)
                # print(f"Deleted {file_path}")
            else:
                print("dont want to delete file = ", file)


# Usage
delete_files_below_threshold(".", 1000)  # Deletes files below 1KB
