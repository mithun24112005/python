from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url,save_path):
    try:
        yt=YouTube(url)
        streams=yt.streams.filter(progressive=True,file_extension="mp4")
        highest_res_stream=streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("video downloaded ")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder=filedialog.askdirectory()
    if folder:
        print(f"selected folder: {folder}")
        return folder


if __name__=="__main__":
    root=tk.Tk()
    root.withdraw()
    url=input("enter the youtube url: ")
    save_path=open_file_dialog()
    if save_path:
        print("starting download..")
        download_video(url,save_path)
    else:
        print("invalid save location")
    download_video(url,save_path)