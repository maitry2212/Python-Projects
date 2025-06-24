#Image Slideshow App

from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Image Slideshow Viewer")
root.geometry("800x600")

image_paths = [
    r"C:\Users\MAITRY CHAUHAN\Pictures\IMG-20250107-WA0036.jpg",
    r"C:\Users\MAITRY CHAUHAN\Pictures\Saved Pictures\IMG_20241226_140546.jpg",
    r"C:\Users\MAITRY CHAUHAN\Pictures\Saved Pictures\IMG_20241221_152952.jpg",
    r"C:\Users\MAITRY CHAUHAN\Pictures\Screenshots\21096.jpg",
    r"C:\Users\MAITRY CHAUHAN\Pictures\Screenshots\20464.jpg",
]

# Load images using PIL and convert to Tkinter format
def load_images(paths):
    images = []
    for path in paths:
        try:
            img = Image.open(path)
            img = img.resize((800, 600), Image.Resampling.LANCZOS)  # Updated for Pillow >=10.0.0
            img_tk = ImageTk.PhotoImage(img)
            images.append(img_tk)
        except Exception as e:
            print(f"Failed to load image {path}: {e}")
    return images

# Create Label to show images
label = tk.Label(root)
label.pack()

# Slideshow function
def start_slideshow(images, delay=2000):  # delay in milliseconds
    image_cycle = cycle(images)

    def show_next_image():
        img = next(image_cycle)
        label.config(image=img)
        label.image = img  # Keep a reference to avoid garbage collection
        root.after(delay, show_next_image)

    show_next_image()

# Load and start slideshow
loaded_images = load_images(image_paths)
if loaded_images:
    start_slideshow(loaded_images)
else:
    print("No images loaded.")

root.mainloop()
