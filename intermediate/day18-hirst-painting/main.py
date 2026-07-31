# import colorgram

# rgb_colors = []
# colors = colorgram.extract('./intermediate/day18-hirst-painting/dot_painting.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new_color = (r, g , b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# Import turtle module and random module 
import turtle as tt
import random 

#color list from the image.png
color_list = [(231, 233, 237), (212, 160, 77), (50, 88, 132), (149, 82, 37), (129, 177, 205), (164, 54, 80), (228, 204, 108), (133, 32, 46), (175, 148, 33), (44, 57, 106), (129, 182, 138), (34, 44, 71), (198, 94, 85), (70, 36, 29), (81, 119, 182), (76, 29, 45), (184, 145, 180), (193, 104, 110), (72, 147, 166), (83, 147, 89), (81, 73, 41), (43, 72, 79), (158, 200, 221), (82, 139, 88), (121, 38, 37), (217, 176, 186), (176, 189, 213)]

# Configure the canvas settings and move the turtle to the starting corner
tt.speed(5)
tt.colormode(255)
tt.penup()
tt.setposition(-250, -250)

# Loop through 10 rows to build the vertical height of the grid
for row in range(10):
    # Loop through 10 columns to draw individual dots horizontally
    for column in range(10):
        current_color = random.choice(color_list)
        tt.dot(20, current_color)
        tt.forward(50)

    # Snap the turtle back to the left and move up one row (typewriter effect) ⌨️
    tt.setx(-250)
    tt.sety(tt.ycor() + 50)

# Keep screen open until a mouse click
tt.Screen().exitonclick()