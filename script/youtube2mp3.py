from pytube import YouTube
from moviepy.editor import *
import os


def download_youtube_video(youtube_link, output_path):
    try:
        yt = YouTube(youtube_link)
        video_stream = yt.streams.filter(only_audio=True).first()
        video_stream.download(output_path)
        video_title = yt.title
        return True, video_title
    
    except Exception as e:
        print("Gagal mengunduh video:", e)
        return False, ""


def convert_to_mp3(input_path, output_path):
    try:
        video_clip = AudioFileClip(input_path)
        video_clip.write_audiofile(output_path, codec='mp3')
        video_clip.close()
        return True
    
    except Exception as e:
        return False


def remove_mp4(path):
    try:
        os.remove(path)
        print(f"File {path} berhasil dihapus.")
    except FileNotFoundError:
        print(f"File {path} tidak ditemukan.")
    except Exception as e:
        print(f"Gagal menghapus file: {path}")


def save_mp3_file(path_input, path_output, auto):
    if auto:
        output_filename = f"{path_input}.mp3"        
    else:
        output_filename = os.path.splitext(path_output)[0] + ".mp3"
    
    output_path = os.path.join(path_output, output_filename)
    if convert_to_mp3(path_input, output_path):
        print("Konversi ke mp3 berhasil!")
        remove_mp4(path_input)
    else:
        print("Konversi ke mp3 gagal!")


def main_program(link_youtube, path_folder, auto=True):
    if auto:
        success, video_title = download_youtube_video(link_youtube, path_folder)
        if success:
            print(f"berhasil mendownload '{video_title}.mp4'")
            video_path = os.path.join(path_folder, f"{video_title}.mp4")
            save_mp3_file(video_path, path_folder, True)
        else:
            print("Gagal mengunduh video.") 
    else:
        save_mp3_file(path_folder, path_folder, False)


#----------------------------------------------------------
# use true if using youtube to convert mp3 automatic
# and use false if using offline file or (failed convert from youtube)
# folder_path is for save youtube2mp3 or offline path

if __name__ == "__main__":
    link_youtube = r""
    folder_path = r""
    main_program(link_youtube, folder_path, False)