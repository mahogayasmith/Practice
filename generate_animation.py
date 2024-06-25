from PIL import Image, ImageDraw
import os

# Create a new image with a white background
width, height = 100, 100
frames = []
for _ in range(20):
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Draw a red circle at different positions for each frame
    draw.ellipse((0, 40, 20, 60), fill="red")

    frames.append(image)

# Save the frames as an animated GIF
frames[0].save("bouncing_ball.gif", save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)

# Remove individual frame images
for frame in frames:
    frame.close()

# Display the animated GIF
os.system("bouncing_ball.gif")
