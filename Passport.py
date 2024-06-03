from PIL import Image

# Open the individual photo
original_photo = Image.open("photo.jpg")

# Define the desired size for the final image (4x6 inches at 300 DPI)
final_width = 1200  # 4 inches * 300 DPI
final_height = 1800  # 6 inches * 300 DPI

# Calculate the size for each individual photo, maintaining the aspect ratio
aspect_ratio = original_photo.width / original_photo.height

if aspect_ratio > 1:
    # Landscape orientation
    photo_height = final_height // 2
    photo_width = int(photo_height * aspect_ratio)
else:
    # Portrait orientation
    photo_width = final_width // 2
    photo_height = int(photo_width / aspect_ratio)

# Resize the original photo
resized_photo = original_photo.resize((photo_width, photo_height))

# Create a new blank image with white background
final_image = Image.new("RGB", (final_width, final_height), (255, 255, 255))

# Calculate positions to paste the resized photos
x_offset = (final_width // 2 - photo_width) // 2
y_offset = (final_height // 2 - photo_height) // 2

# Paste the resized photos onto the final image
final_image.paste(resized_photo, (x_offset, y_offset))
final_image.paste(resized_photo, (x_offset + final_width // 2, y_offset))
final_image.paste(resized_photo, (x_offset, y_offset + final_height // 2))
final_image.paste(resized_photo, (x_offset + final_width // 2, y_offset + final_height // 2))

# Save the final image
final_image.save("4x6_fixed_print.jpg")
