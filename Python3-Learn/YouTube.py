from pytube import YouTube
url = input("Enter the url to download:")
video = YouTube(url)
stream = video.streams.get_highest_resolution()
path = input("Enter the path to save the video:")
stream.download(output_path=path)
print("Task Completed")
