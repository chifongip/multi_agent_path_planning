import cv2 as cv 

def GenMap(img_source):
    img = cv.imread(img_source)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

    row, col = thresh.shape
    obstacles = []

    for i in range(row):
        for j in range(col):
            if thresh[i][j] == 0:
                obstacles.append(tuple([i, j]))

    return [row, col], obstacles

