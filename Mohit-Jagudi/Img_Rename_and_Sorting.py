import os
def get_images(folder):
    image_extensions = ('.png', '.jpg', '.jpeg', '.webp')
    try:
        files = os.listdir(folder)
    except Exception:
        print("Cannot access folder!")
        return []
    return [f for f in files if f.lower().endswith(image_extensions)]
def make_unique_name(folder, name):
    base, ext = os.path.splitext(name)
    counter = 1
    new_name = name

    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{base}_{counter}{ext}"
        counter += 1

    return new_name

def rename_images(folder_path, target_folder):
    try:
        images = get_images(folder_path)

        if not images:
            print("No images found!")
            return

        images.sort()

        # Base name
        base_name = input("\nEnter base name (e.g. img): ").strip()
        if not base_name:
            print("Invalid base name!")
            return

        # Format
        format_type = input("Choose format:\n1. img1\n2. img_1\n3. img-1\nEnter choice: ")

        # WARNING
        print("\nWARNING:")
        print("Files will be renamed/moved permanently.")
        confirm = input("Do you want to continue? (y/n): ").lower()
        if confirm != 'y':
            print("Operation cancelled.")
            return

        # Reverse option
        rev = input("\nReverse order? (y/n): ").lower()
        if rev == 'y':
            images.reverse()

        total = len(images)

        for i, file in enumerate(images, start=1):
            try:
                old_path = os.path.join(folder_path, file)
                ext = os.path.splitext(file)[1]

                if format_type == '1':
                    new_name = f"{base_name}{i}{ext}"
                elif format_type == '2':
                    new_name = f"{base_name}_{i}{ext}"
                elif format_type == '3':
                    new_name = f"{base_name}-{i}{ext}"
                else:
                    new_name = f"{base_name}{i}{ext}"

                new_name = make_unique_name(target_folder, new_name)
                new_path = os.path.join(target_folder, new_name)

                # Skip if same path (extra safety)
                if os.path.abspath(old_path) == os.path.abspath(new_path):
                    continue

                os.rename(old_path, new_path)

                print(f"Renaming: {i}/{total}")

            except PermissionError:
                print(f"Permission denied: {file}")
            except Exception as e:
                print(f"Error processing file {file}: {e}")

        print("\nDone!")
        print("Saved at:", target_folder)

    except Exception as e:
        print("Error:", e)
  
