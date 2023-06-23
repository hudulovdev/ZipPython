import zipfile

def create_zip_file(directory_path, zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Iterate over all files and subdirectories in the given directory
        for root, _, files in os.walk(directory_path):
            for file in files:
                # Create the full file path by joining the root path and the file name
                file_path = os.path.join(root, file)
                # Add the file to the zip file with its relative path
                zipf.write(file_path, os.path.relpath(file_path, directory_path))

# Example usage
directory_path = input("Enter file path: ")
zip_file_path = input("Enter Zip file save path: ")
create_zip_file(directory_path, zip_file_path)
