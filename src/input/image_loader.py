import cv2

class ImageLoader:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        self.load_images()

    def load_images(self):
        import os
        images = []
        for filename in os.listdir(self.folder_path):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                img = cv2.imread(os.path.join(self.folder_path, filename))
                if img is not None:
                    images.append(img)
        return images

if __name__ == "__main__":
    loader = ImageLoader("path/to/your/image/folder")
    print(f"Loaded {len(images)} images.")