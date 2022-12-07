from turtle import Turtle


class Bishop(Turtle):

    def __init__(self, horizontal, vertical):
        super().__init__()
        self.shape = self.shape("circle")
        self.color = self.color("blue")
        self.width = self.width = 12
        self.height = self.height = 12
        self.pos = (horizontal, vertical)
        self.penup()
        self.goto(self.pos)

    def kill_knight(self, knight_pos):
        cases1 = []
        cases2 = []
        cases3 = []
        cases4 = []

        for step in range(60, 421, 60):
            case1 = (self.pos[0] + step, self.pos[1] + step)
            cases1.append(case1)
        for step in range(60, 421, 60):
            case2 = (self.pos[0] + step, self.pos[1] - step)
            cases2.append(case2)
        for step in range(60, 421, 60):
            case3 = (self.pos[0] - step, self.pos[1] + step)
            cases3.append(case3)
        for step in range(60, 421, 60):
            case4 = (self.pos[0] - step, self.pos[1] - step)
            cases4.append(case4)
        all_cases = cases1 + cases2 + cases3 + cases4

        if self.pos == knight_pos:
            print("They can't be in the same square")
        if knight_pos in all_cases:
            print("Bishop can attack knight")
