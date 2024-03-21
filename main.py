from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os

# Define paths
temp_video_path = "path/to/temp/video"
temp_audio_path = "path/to/temp/audio"
final_video_path = "path/to/final/video"

# Get YouTube video link from user
video_link = input("Enter the YouTube video link: ")

# Get user input for final video title
video_title = input("Enter a title for the final video: ")

try:
  # Create YouTube object
  yt = YouTube(video_link)
  # Get audio and video streams
  audio_stream = yt.streams.filter(only_audio = True).first()
  video_stream = yt.streams.get_highest_resolution()

  # Download audio and video streams
  audio_file_path = os.path.join(temp_audio_path, f"{video_stream.title}.mp3")
  audio_stream.download(output_path=temp_audio_path, filename=f"{video_stream.title}.mp3")
  video_file_path = os.path.join(temp_video_path, f"{video_stream.title}.mp4")
  video_stream.download(output_path=temp_video_path)

  # Load audio and video clips
  audio_clip = AudioFileClip(audio_file_path)
  video_clip = VideoFileClip(video_file_path)

  # Combine audio and video
  final_clip = video_clip.set_audio(audio_clip)

  # Write final video file
  final_video_file_path = os.path.join(final_video_path, f"{video_title}.mp4")
  final_clip.write_videofile(final_video_file_path)

  print("Final video saved successfully at:", final_video_file_path)

except Exception as e:
  print("Error:", e)
