# File Organizer

A simple Python script that organizes files in a folder by their file types.

## How to Use

1. Run the script:
   ```bash
   python file_organizer.py
   ```
2. Enter the full folder path you want to organize.
3. The script will:
   - Create folders based on file extensions (e.g., `txt_files`, `jpg_files`).
   - Move files into the appropriate folders.
   - Skip already organized files.
   - Display a message if no new files need to be moved.

## Features

- ✅ Organizes files by extension.
- 📁 Automatically creates folders if they don’t exist.
- 🔁 Skips already organized files.
- 🛑 Displays a message if no new files are found.

## Example

Before running:

```
my_folder/
├── photo.jpg
├── notes.txt
├── code.py
```

After running:

```
my_folder/
├── jpg_files/
│   └── photo.jpg
├── txt_files/
│   └── notes.txt
├── py_files/
    └── code.py
```

## License

This project is open-source and free to use.
