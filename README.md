# Smart Image Renamer

## Problem Statement

Managing large numbers of images manually is time-consuming and inefficient. Users often face issues like inconsistent naming, duplicate files, and poor organization.

## Project Description

Smart Image Renamer is a Python-based command-line tool designed to efficiently rename and organize image files in bulk. The tool allows users to rename images with custom formats, avoid duplicates, and optionally move files to a new folder.

## Objective

The main objectives of this project are:

* Automate the process of renaming multiple image files
* Prevent duplicate file creation
* Provide user control over naming format and order
* Ensure safe and efficient file handling

## Features

* Batch image renaming
* Supports multiple formats (.png, .jpg, .jpeg, .webp)
* Custom naming styles (img1, img_1, img-1)
* Reverse order option
* Duplicate name protection
* Rename in same folder or move to a new folder
* Progress tracking (e.g., Renaming: 3/20)
* Error handling for file access and permissions
* User confirmation before renaming

## Technologies Used

* Python
* OS Module (file handling)
* Exception Handling

## Project Structure

```
ImageRenamer/
│── Img-Rename-and-Sorting.py
│── README.md
```

## How to Run

1. Install Python (if not installed)
2. Download or clone this repository
3. Open terminal in the project folder
4. Run the program:

```
python main.py
```

## Working Flow

1. Select rename option
2. Enter folder path
3. Choose rename in same folder or new folder
4. Enter base name
5. Select naming format
6. Confirm warning
7. Choose reverse option
8. Program renames images and shows progress

## Example

Before:

```
IMG_1234.jpg
random.png
photo.png
```

After:

```
img1.jpg
img2.png
img3.png
```

## Advantages

* Saves time and effort
* Prevents duplicate files
* Easy to use
* Flexible naming options

## Limitations

* Command-line interface only
* Supports limited image formats
* No undo feature

## Future Improvements

* GUI version
* Drag and drop support
* Undo/backup feature
* More file format support

## Author

Smart Image Renamer Project by Mohit Jagudi   
