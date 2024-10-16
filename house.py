import cairo
import math

# Set up the canvas dimensions
WIDTH, HEIGHT = 600, 500
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)
context.set_source_rgb(1,1,1)
context.paint()

# Draw the house body
context.set_line_width(1)
context.move_to(100,200)#a
context.line_to(500,200)#b
context.line_to(500,280)#c
context.line_to(450,280)#d
context.line_to(450,440)#e
context.line_to(150,440)#f
context.line_to(150,280)#g
context.line_to(100,280)#h
context.set_source_rgb(0,0,1)
context.close_path()
context.stroke()

# Draw the dome
context.arc(300, 200, 100, math.pi, 2 * math.pi)
context.stroke()

# Draw windows (two square windows)
context.set_line_width(1)

# Left window
context.rectangle(190, 300, 60, 60)
context.set_source_rgb(0,1,0)
context.stroke()
context.move_to(190 + 30, 300)  # Vertical line
context.line_to(190 + 30, 360)
context.set_source_rgb(0,0,1)
context.stroke()
context.move_to(190, 300 + 30)  # Horizontal line
context.line_to(250, 300 + 30)
context.set_source_rgb(0,0,1)
context.stroke()

# Right window
context.rectangle(350, 300, 60, 60)
context.set_source_rgb(0,1,0)
context.stroke()
context.move_to(350 + 30, 300)  # Vertical line
context.line_to(350 + 30, 360)
context.set_source_rgb(0,0,1)
context.stroke()
context.move_to(350, 300 + 30)  # Horizontal line
context.line_to(410, 300 + 30)
context.set_source_rgb(0,0,1)
context.stroke()

# Draw the door
context.rectangle(270, 300, 60, 140)
context.set_source_rgb(0,1,0)
context.stroke()

# Draw door knob
context.arc(320, 370, 5, 0, 2 * math.pi)
context.set_source_rgb(0,0,1)
context.fill_preserve()
context.set_source_rgb(0,0,0.5 )
context.set_line_width(3)
context.stroke()


# Draw the crescent moon
context.set_line_width(1)
context.arc_negative(450, 100, 40, 5*math.pi/4, math.pi/4)
context.curve_to(450,125,420,120,422,70)
context.set_source_rgb(0.8,0.8,0)
context.fill_preserve()
context.set_source_rgb(0,0,1)
context.stroke()

# Save the image
surface.write_to_png("house.png")
print("Image saved as house.png")
