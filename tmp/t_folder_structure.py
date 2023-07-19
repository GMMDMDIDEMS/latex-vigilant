# import os
# import shutil
# import tempfile
# import pytest

# # Import the get_tex_files function from your code
# from main import get_tex_files

# def create_temporary_folder_structure():
#     """
#     Create a temporary folder structure with random files.
#     The structure will look like this:
#     temp_dir/
#     ├── file1.tex
#     ├── folder1/
#     │   ├── file2.tex
#     │   ├── folder2/
#     │   │   └── file3.txt
#     │   └── folder3/
#     └── folder4/
#         └── file4.tex
#     """
#     temp_dir = tempfile.mkdtemp()
    
#     # Create files
#     file1 = os.path.join(temp_dir, "file1.tex")
#     open(file1, 'a').close()

#     file2 = os.path.join(temp_dir, "folder1", "file2.tex")
#     open(file2, 'a').close()

#     file3 = os.path.join(temp_dir, "folder1", "folder2", "file3.txt")
#     open(file3, 'a').close()

#     file4 = os.path.join(temp_dir, "folder1", "folder3", "file4.tex")
#     open(file4, 'a').close()

#     return temp_dir

# def test_get_tex_files():
#     # Create a temporary folder structure
#     temp_dir = create_temporary_folder_structure()
    
#     # Call the function to get the ".tex" files
#     tex_files = get_tex_files(temp_dir)
    
#     # Define the expected file paths
#     expected_files = [
#         os.path.join(temp_dir, "file1.tex"),
#         os.path.join(temp_dir, "folder1", "file2.tex"),
#         os.path.join(temp_dir, "folder1", "folder3", "file4.tex")
#     ]
    
#     # Compare the expected files with the files returned by the function
#     assert sorted(tex_files) == sorted(expected_files)
    
#     # Clean up the temporary folder structure
#     shutil.rmtree(temp_dir)
