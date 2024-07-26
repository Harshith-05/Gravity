import cv2
import random
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def parse_labels_from_file(file_path):
    labels = []
    with open(file_path, 'r') as file:
        for line in file:
            label_parts = line.strip().split()
            if len(label_parts) == 5:
                class_id, x, y, w, h = map(float, label_parts)
                labels.append((int(class_id), x, y, w, h))
    return labels


def yolo_to_pixels(image_width, image_height, box):
    x, y, w, h = box
    xmin = int((x - w / 2) * image_width)
    xmax = int((x + w / 2) * image_width)
    ymin = int((y - h / 2) * image_height)
    ymax = int((y + h / 2) * image_height)
    return xmin, ymin, xmax, ymax


def display_image_with_labels(image_path, labels):
    # Load the image
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_height, image_width, _ = image.shape

    # Create figure and axes
    fig, ax = plt.subplots(1)
    ax.imshow(image_rgb)

    # Add bounding boxes and labels
    for label in labels:
        class_id, x, y, w, h = label

        # Convert YOLO coordinates to pixel values
        xmin, ymin, xmax, ymax = yolo_to_pixels(image_width, image_height, (x, y, w, h))

        # Create a rectangle patch
        rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, linewidth=1, edgecolor='b', facecolor='none')

        # Add the rectangle patch to the axes
        ax.add_patch(rect)

        # Add label text above the bounding box
        ax.text(xmin, ymin - 10, f'Crater {class_id}', fontsize=10, color='r')

    # Set plot title
    plt.title('Image with Labels')

    # Show the plot
    plt.axis('off')
    plt.show()


def main():
    img_path = r"C:\Users\harsh\OneDrive\Desktop\craters\images"  # Update with your image directory
    labels_path = r"C:\Users\harsh\OneDrive\Desktop\craters\labels"  # Update with your labels directory

    for _ in range(5):  # Display 5 random images
        random_img = random.choice(os.listdir(img_path))
        final_path_img = os.path.join(img_path, random_img)

        labels_file_path = os.path.join(labels_path, random_img.rsplit('.', 1)[0] + '.txt')
        labels = parse_labels_from_file(labels_file_path)

        # Display the image with labels
        display_image_with_labels(final_path_img, labels)


if __name__ == "__main__":
    main()



