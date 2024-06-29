import cv2
import matplotlib.pyplot as plt




GRID_X = 15
GRID_Y = 12
GRID_SIZE = (GRID_X, GRID_Y)

map_01_filepath = r"Game Boy Advance - Fire Emblem The Sacred Stones - Chapter 01.png"
valani_01_filepath = r"Game Boy Advance - Fire Emblem The Sacred Stones - Tower of Valni I.png"

# Load the image
img = cv2.imread(map_01_filepath)


def show_grid():
    x_cell = GRID_SIZE[0]
    y_cell = GRID_SIZE[1]

    # Calculate the size of each grid cell
    height, width, _ = img.shape
    grid_height = height // y_cell
    grid_width = width // x_cell

    # Draw the grid lines
    for i in range(1, x_cell):
        cv2.line(img, (i * grid_width, 0), (i * grid_width, height), (0, 0, 255), 1)

    for i in range(1, y_cell):
        cv2.line(img, (0, i * grid_height), (width, i * grid_height), (0, 0, 255), 1)

    # Display the image with grid lines
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Image with Grid Lines")
    plt.axis('off')
    plt.show()


if img is not None:
    # Display the image
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis('off')
    plt.show()
else:
    print(f"Image not found at {map_01_filepath}")

show_grid()

