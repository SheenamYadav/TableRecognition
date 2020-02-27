class Table:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.joints = None

    def __str__(self):
        return "(x: %d, (x+w): %d, y: %d, (y+h): %d)" % (self.x, self.x + self.w, self.y, self.y + self.h)
    
    def set_joints(self, joints):
        if self.joints != None:
            return

        self.joints = []
        row_y = joints[0][1]
        row = []
        for i in range(len(joints)):
            if i == len(joints) - 1:
                row.append(joints[i])
                self.joints.append(row)
                break

            row.append(joints[i])
            
            if joints[i + 1][1] != row_y:
                self.joints.append(row)
                row_y = joints[i + 1][1]
                row = []

    def print_joints(self):
        if self.joints == None:
            print("Joint coordinates not found.")
            return

        for row in self.joints:
            print("\t" + str(row))
