import pycdlib
import os

def create_rock_ridge_iso(iso_file_path, source_dir):
    # Initialize the ISO image with Rock Ridge extensions
    iso_image = pycdlib.PyCdlib()
    iso_image.new(interchange_level=1, joliet=True, rock_ridge='1.12')

    # Add files and directories from the source directory to the ISO image
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            iso_image.add_file(file_path, file_path.replace(source_dir, ''), joliet_path=file_path.replace(source_dir, ''), rr_name=file)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            iso_image.add_directory(dir_path.replace(source_dir, ''), joliet_path=dir_path.replace(source_dir, ''))

    # Write the ISO image to the specified file path
    iso_image.write(iso_file_path)

    # Close the ISO image
    iso_image.close()

if __name__ == '__main__':
    # Path to the source directory containing files to be added to the ISO image
    source_dir = 'files'
    
    # Path to the output Rock Ridge ISO file
    iso_file_path = 'iso/output.iso'
    
    create_rock_ridge_iso(iso_file_path, source_dir)

