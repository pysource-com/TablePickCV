import cv2

class ImageLoder:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        self.images = self.load_images_from_folder()

    def load_images_from_folder(self):
        import os
        images = []
        for filename in os.listdir(self.folder_path):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(self.folder_path, filename)
                img = cv2.imread(img_path)
                if img is not None:
                    images.append(img)
        return images

if __name__ == "__main__":
    loader = ImageLoder(r"C:\Users\pinoloufficio\Desktop\images")
    print(f"Loaded {len(loader.images)} images.")
    for img in loader.images:
        cv2.imshow("img", img)
        cv2.waitKey(0)
