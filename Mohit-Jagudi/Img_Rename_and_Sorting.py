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
  def main():
    while True:
        print("\n===== IMAGE RENAMER TOOL =====")
        print("1. Rename Images")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            folder_path = input("Enter folder path: ").strip().strip('"')

            if not os.path.exists(folder_path):
                print("Invalid path!")
                continue

            print("\n1. Rename in same folder")
            print("2. Create new folder")

            sub_choice = input("Enter choice: ")

            if sub_choice == '1':
                rename_images(folder_path, folder_path)

            elif sub_choice == '2':
                print("\n1. Auto create folder")
                print("2. Custom location")

                new_choice = input("Enter choice: ")

                if new_choice == '1':
                    new_folder = os.path.join(folder_path, "Renamed_Images")
                    os.makedirs(new_folder, exist_ok=True)

                elif new_choice == '2':
                    drive = input("\nEnter drive (C:/ D:/ E:/ etc): ").strip()
                    folder_name = input("Enter new folder name: ")

                    new_folder = os.path.join(drive, folder_name)

                    # Check invalid drive/location
                    if not os.path.exists(os.path.dirname(new_folder)):
                        print("Invalid drive/location!")
                        continue

                    os.makedirs(new_folder, exist_ok=True)

                else:
                    print("Invalid choice")
                    continue

                rename_images(folder_path, new_folder)

            else:
                print("Invalid choice")

        elif choice == '2':
            print("Exiting...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
