import os

folder = input("Enter folder path: ").strip('" ')
target_suffix = input("Enter text to remove (e.g. _x64): ").strip()
extension = input("Enter file extension (e.g. .dll): ").strip()

if not os.path.isdir(folder):
    print("Invalid folder path.")
    exit()

count = 0
for filename in os.listdir(folder):
    if filename.endswith(extension) and target_suffix in filename:
        old_path = os.path.join(folder, filename)
        new_name = filename.replace(target_suffix, "")
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        print(f"{filename}  ->  {new_name}")
        count += 1

if count == 0:
    print("No files renamed.")
else:
    print(f"{count} file(s) renamed.")

input("Done. Press Enter to exit.")
