import os
from colorama import init, Fore, Back, Style

trash_dir = "C:\\$Recycle.Bin"
deleted_files = []

if os.path.isdir(trash_dir):
    for root, dirs, files in os.walk(trash_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                deleted_files.append(file_path)
            except Exception:
                pass

print(Fore.LIGHTGREEN_EX + "! " + Fore.RESET + Fore.LIGHTWHITE_EX + "The following files were removed from the recycle bin:" + Fore.RESET)
for file_path in deleted_files:
    print(Fore.RED + "! " + Fore.LIGHTBLACK_EX + file_path + Fore.RESET)

print(Fore.LIGHTGREEN_EX + "! " + Fore.RESET + Fore.LIGHTWHITE_EX + f"{len(deleted_files)} files were deleted from the recycling bin.")

