from moviepy import VideoFileClip, CompositeVideoClip, ColorClip
import time

# Start timer
start_time = time.time()

# Load the original video
clip = VideoFileClip("input.mp4")
h = clip.h
w = clip.w

# Working field: width x5, same height, duration same as video + 4 seconds delay for last clip
canvas_width = w * 5
canvas_height = h
duration = clip.duration + 4  # last clip starts at 4 sec

# Create blank background (white, can change to (0,0,0) for black)
background = ColorClip(size=(canvas_width, canvas_height), color=(255, 255, 255), duration=duration)

# Generate 5 clips with increasing start times and horizontal offsets
clips = []
for i in range(5):
    new_clip = (
        clip.with_start(i)  # Start after i seconds
            .with_position((w * i, 0))  # Horizontal position
    )
    clips.append(new_clip)

# Combine all clips on top of the background
final = CompositeVideoClip([background] + clips)

# Export the final video
final.write_videofile("output.mp4", fps=24)

# Calculate and print processing time
end_time = time.time()
processing_time = end_time - start_time
print(f"Processing completed in {processing_time:.2f} seconds")