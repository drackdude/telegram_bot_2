# download pytube and moviepy
from pytube import YouTube
from moviepy.editor import *
import os


# for downloading low quality videos from YouTube
def download_video_low(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_lowest_resolution()
        file = stream.download()
        print("Download successful!")
        return file
    except Exception as e:
        print("An error occurred:", str(e))



# for downloading high quality videos from YouTube
def download_video_high(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file = stream.download()
        print("Download successful!")
        return file
    except Exception as e:
        print("An error occurred:", str(e))


# for downloading specific resolutions videos from youtube
def download_video_with_resol(url,resolution):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(res=resolution).first()
        file = stream.download()
        print("Download successful!")
        return file
    except Exception as e:
        print("An error occurred:", str(e))


# to find available stream resolutions
def get_available_resolutions(url):
    try:
        yt = YouTube(url)
        streams = yt.streams
        resolutions = set()
        for stream in streams:
            if stream.resolution:
                resolutions.add(stream.resolution)
        return resolutions
    except Exception as e:
        print("An error occurred:", str(e))
        return None


# download processed video
def download_video_with_range(url, start_time, end_time,resolution):
    yt = YouTube(url)

    
    # Get the video stream with the desired resolution
    stream = yt.streams.filter(res=resolution).first()

    start_time_seconds = int(start_time)
    end_time_seconds = int(end_time)
    file = stream.download(start=start_time_seconds, end=end_time_seconds)
    return file









# download audio files as mp3 or mp4 files
def download_audio(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        audio_file = stream.download()
        print("Audio download successful!")

        
        # Convert the audio file to MP3
        audio_clip = AudioFileClip(audio_file)
        mp3_file = audio_file.split('.')[0] + ".mp3"
        audio_clip.write_audiofile(mp3_file)
        print("Audio conversion to MP3 successful!")
        

        # Delete the original audio file
        os.remove(audio_file)
        print("Original audio file deleted.")
        return mp3_file
    except Exception as e:
        print("An error occurred:", str(e))
    return "error"


# for downloading the audio files in a processed manner
# Process the audio (cut from start_time to end_time)
def process_audio(url, start_time=0, end_time=None):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        audio_file = stream.download()
        print("Audio download successful!")

        
        audio_clip = AudioFileClip(audio_file)
        processed_clip = audio_clip.subclip(start_time, end_time)
        mp3_file = audio_clip.split('.')[0] + ".mp3"
        processed_clip.write_audiofile(mp3_file)
        print("Audio processing successful!")

        # Delete the original audio file
        os.remove(audio_file)
        print("Original audio file deleted.")
        return mp3_file
    except Exception as e:
        print("An error occurred:", str(e))
    return "error"


