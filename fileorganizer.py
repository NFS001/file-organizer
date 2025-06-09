import os
import shutil

def organize_by_type(folder_path):
    move_counter = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            target_dir = os.path.join(folder_path, ext + "_files")
            
            if not os.path.exists(target_dir):
                os.mkdir(target_dir)
            shutil.move(file_path, os.path.join(target_dir, filename))
            print(f"Moved: {filename} -> {target_dir}")
            move_counter += 1
    if move_counter == 0:
        print("No files to Organize")

if __name__ == "__main__":
    folder_path = input("Enter the full path of the folder to organize: ").strip()
    
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        organize_by_type(folder_path)
    else:
        print("Invalid folder path. Please try again")