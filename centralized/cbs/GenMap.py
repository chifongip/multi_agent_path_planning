import cv2 as cv 
import random

class Generator:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.obstacles = []
        self.agent = []

    def GenMap(self, img_source):
        img = cv.imread(img_source)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        _, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

        self.row, self.col = thresh.shape

        for i in range(self.row):
            for j in range(self.col):
                if thresh[i][j] == 0:
                    self.obstacles.append(tuple([i, j]))

        return [self.row, self.col], self.obstacles

    def Grid(self, grid):
        self.row, self.col = grid.shape
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] == 1:
                    self.obstacles.append(tuple([i, j]))
        
        return [self.row, self.col], self.obstacles

    def GenAgent(self, n):
        idx = 0
        while idx < n:
            sx = random.randint(0, self.col - 1)
            sy = random.randint(0, self.row - 1)
            gx = random.randint(0, self.col - 1)
            gy = random.randint(0, self.row - 1)
            if (sx, sy) != (gx, gy) and (sx, sy) not in self.obstacles and (gx, gy) not in self.obstacles:
                self.agent.append({'name': 'agent' + str(idx), 'start': [sx, sy], 'goal': [gx, gy]})
                idx += 1
        
        return self.agent
