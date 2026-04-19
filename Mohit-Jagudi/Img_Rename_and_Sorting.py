import os
def get_images(folder):
    image_extensions = ('.png', '.jpg', '.jpeg', '.webp')
    try:
        files = os.listdir(folder)
    except Exception:
        print("Cannot access folder!")
        return []
    return [f for f in files if f.lower().endswith(image_extensions)]
  
