import cairo
import math

# Set up the canvas dimensions
WIDTH, HEIGHT = 600, 500
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)
context.set_source_rgb(1,1,1)

# Draw the house body
context.set_line_width(2)
context.move_to(100,200)#a
context.line_to(500,200)#b
context.line_to(500,280)#c
context.line_to(450,280)#d
context.line_to(450,440)#e
context.line_to(150,440)#f
context.line_to(150,280)#g
context.line_to(100,280)#h
context.close_path()
#context.rectangle(150, 200, 300, 150)  # (x, y, width, height)
context.stroke()

# Draw the dome
context.arc(300, 200, 100, math.pi, 2 * math.pi)  # (center_x, center_y, radius, start_angle, end_angle)
context.stroke()

# Draw windows (two square windows)
context.set_line_width(2)
# Left window
context.rectangle(190, 300, 60, 60)
context.move_to(190 + 30, 300)  # Vertical line
context.line_to(190 + 30, 360)
context.move_to(190, 300 + 30)  # Horizontal line
context.line_to(250, 300 + 30)
context.stroke()

# Right window
context.rectangle(350, 300, 60, 60)
context.move_to(350 + 30, 300)  # Vertical line
context.line_to(350 + 30, 360)
context.move_to(350, 300 + 30)  # Horizontal line
context.line_to(410, 300 + 30)
context.stroke()

# Draw the door
context.rectangle(270, 300, 60, 140)
context.stroke()

# Add door knob
context.arc(320, 370, 5, 0, 2 * math.pi)  # (center_x, center_y, radius, start_angle, end_angle)
context.fill()

# Draw the crescent moon
context.set_line_width(2)
context.arc(450, 100, 40, 0, 2 * math.pi)  # Full circle
context.stroke()

# Inner circle to create crescent effect
context.arc(465, 85, 40, 0, 2 * math.pi)
context.set_source_rgb(1, 1, 1)  # White color to mask part of the circle
context.fill()

# Save the image
surface.write_to_png("house.png")
print("Image saved as house.png")
