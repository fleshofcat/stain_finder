import os

import cv2


def get_files_from_dir(images_dir):
    for _, _, files in os.walk(images_dir):
        return [os.path.join(images_dir, file) for file in files]


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


if __name__ == '__main__':

    files = get_files_from_dir('images')
    spotses = [get_spots(file) for file in files]

    to_write = [spots[] for spots in spotses]

    with open('out.txt', 'a') as f:
        f.writelines(spotses)


    print(spotses)
