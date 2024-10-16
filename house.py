import cairo
import math

# Set up the canvas dimensions
WIDTH, HEIGHT = 600, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)
context.set_source_rgb(1,1,1)
context.paint()

# Draw the house body
context.set_line_width(1)
context.rectangle(150, 200, 300, 150)  # (x, y, width, height)
context.set_source_rgb(0,0,1)
context.stroke()

# Draw the dome
context.arc(300, 200, 75, math.pi, 2 * math.pi)  # (center_x, center_y, radius, start_angle, end_angle)
context.stroke()

# Draw windows (two square windows)
context.set_line_width(1)
# Left window
context.rectangle(190, 240, 60, 60)
context.move_to(190 + 30, 240)  # Vertical line
context.line_to(190 + 30, 300)
context.move_to(190, 240 + 30)  # Horizontal line
context.line_to(250, 240 + 30)
context.set_source_rgb(0,0,1)
context.stroke()

# Right window
context.rectangle(350, 240, 60, 60)
context.move_to(350 + 30, 240)  # Vertical line
context.line_to(350 + 30, 300)
context.move_to(350, 240 + 30)  # Horizontal line
context.line_to(410, 240 + 30)
context.set_source_rgb(0,0,1)
context.stroke()

# Draw the door
context.rectangle(270, 260, 60, 90)
context.set_source_rgb(0,0,1)
context.stroke()

# Add door knob
context.arc(325, 305, 5, 0, 2 * math.pi)  # (center_x, center_y, radius, start_angle, end_angle)
context.set_source_rgb(0,0,1)
context.fill()

# Draw the crescent moon
context.set_line_width(1)
context.arc_negative(450, 100, 40, 5*math.pi/4, math.pi/4)
context.curve_to(450,125,420,120,422,70)
context.set_source_rgb(0.8,0.8,0)
context.fill_preserve()
context.set_source_rgb(0,0,1)
context.stroke()

# # Draw the crescent moon
# context.set_line_width(1)
# context.arc_negative(450, 100, 30, 5*math.pi/4, math.pi/4)
# context.set_source_rgb(0,0,1)
# context.stroke()

# # Inner circle to create crescent effect
# context.arc(465, 85, 40, 0, 2 * math.pi)
# context.set_source_rgb(1, 1, 1)  # White color to mask part of the circle
# context.set_source_rgb(1,1,1)
# context.fill()

# Save the image
surface.write_to_png("house.png")
print("Image saved as house.png")
