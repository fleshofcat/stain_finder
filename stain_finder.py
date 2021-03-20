import os
import json
from pprint import pprint
import cv2


def get_files_from_dir(images_dir):
    for path, _, files in os.walk(images_dir):
        return [os.path.join(path, file) for file in files]


def get_spots(image_filename):
    img = cv2.imread(image_filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh,
                                   cv2.RETR_TREE,
                                   cv2.CHAIN_APPROX_NONE)
    frames = []
    for contour in contours:
        x1, y1, w, h = cv2.boundingRect(contour)
        x2, y2 = x1 + w, y1 + h
        frame = (x1, y1), (x2, y2)
        frames += [frame]

    return frames


def get_stains_coordinates_for_all_files_in_dir(dir):
    coordinates_for_images = []
    for image_file in get_files_from_dir(dir):
        coordinates_for_images += [{
            'image_file': image_file,
            'coordinates': get_spots(image_file)
        }]

    return coordinates_for_images


if __name__ == '__main__':

    images_coordinates = get_stains_coordinates_for_all_files_in_dir('images')

    with open('out.txt', 'w') as f:
        json.dump(images_coordinates, f, indent=4, ensure_ascii=False)

    pprint(images_coordinates)
