import moviepy.editor

video = moviepy.editor.VideoFileClip("video.mp4")

audio_data = video.audio

audio_data.write_audiofile("audio_video.mp3")