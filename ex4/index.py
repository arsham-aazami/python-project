from turtle import Turtle, Screen
from bishop import Bishop
from knight import Knight

with open("datas.txt") as datas:
	english_alphabet = datas.readlines()


position_dic = {
	"a": -195,
	"b": -135,
	"c": -75,
	"d": -15,
	"e": 45,
	"f": 105,
	"g": 165,
	"h": 225,
	1: -210,
	2: -150,
	3: -90,
	4: -30,
	5: 30,
	6: 90,
	7: 150,
	8: 210,
}

horizontal_list = ["A", "B", "C", "D", "E", "F", "G", "H", "a", "b", "c", "d", "e", "f", "g", "h"]
vertical_list = [1, 2, 3, 4, 5, 6, 7, 8]

# Getting knight datas
knight_horizontal_input = input("Please enter horizontal position of the knight (a,b,c,d,e,f,g,h): ").lower()
knight_vertical_input = int(input("Please enter vertical position of the knight (1,2,3,4,5,6,7,8): "))

# Getting bishop datas
bishop_horizontal_input = input("Please enter horizontal position of the bishop (a,b,c,d,e,f,g,h): ").lower()
bishop_vertical_input = int(input("Please enter vertical position of the bishop (1,2,3,4,5,6,7,8): "))


def validation(bead_name, bead_horizontal_input, bead_vertical_input):
	if bead_horizontal_input in english_alphabet:
		if len(bead_horizontal_input) != 1:
			print("Horizontal input is not a letter")
		if bead_horizontal_input not in horizontal_list:
			print("Horizontal input is not a proper letter")

	if int(bead_vertical_input) < 0:
		print("Vertical input is not a number")
	else:
		if bead_vertical_input not in vertical_list:
			print(f"Vertical input for {bead_name} is not a proper number")


validation("Knight", knight_horizontal_input, knight_vertical_input)
validation("Bishop", bishop_horizontal_input, bishop_vertical_input)

screen = Screen()

text_for_knight = Turtle()
text_for_knight.color("red")
text_for_knight.penup()
text_for_knight.hideturtle()
text_for_knight.goto(-210, 300)
text_for_knight.write("Knight", font=("lalezar", 15, "normal"))

text_for_bishop = Turtle()
text_for_bishop.color("blue")
text_for_bishop.penup()
text_for_bishop.hideturtle()
text_for_bishop.goto(-110, 300)
text_for_bishop.write("Bishop", font=("lalezar", 15, "normal"))

screen.bgpic("download (1).png")
knight_x_pos = position_dic[knight_horizontal_input]
knight_y_pos = position_dic[knight_vertical_input]

bishop_x_pos = position_dic[bishop_horizontal_input]
bishop_y_pos = position_dic[bishop_vertical_input]

knight = Knight(horizontal=knight_x_pos, vertical=knight_y_pos)
bishop = Bishop(horizontal=bishop_x_pos, vertical=bishop_y_pos)

knight.kill_bishop(bishop.pos)
bishop.kill_knight(knight.pos)

screen.mainloop()
