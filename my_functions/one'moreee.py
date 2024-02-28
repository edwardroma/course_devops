
# # This is to compare and overwrite 2 files
#
# import os.path
# import shutil
#
# #
# def file_compare(file1, file2):
#     time_file1 = os.path.getmtime(file1)
#     time_file2 = os.path.getmtime(file2)
#     if time_file1 < time_file2:
#         print(file1, "was updated earlier than", file2)
#         file_to_keep = file2
#         file_to_overwrite = file1
#     elif time_file1 > time_file2:
#         print(file1, "was updated later than", file2)
#         file_to_keep = file1
#         file_to_overwrite = file2
#     shutil.copyfile(file_to_keep, file_to_overwrite)
#     print("file to stay is: ", file_to_keep)
#     return file_to_keep
#
# file_compare("file1.py", "file2.py")
#
#
