# You are working on a project for TikTok. The future project will be a web-site of all public GIF images.
# You need to write a function that converts TikTok video to GIF.
# The input parameter is url address of TikTok video, i.e. "TikTok example".
# The output parameter is path to GIF image, i.e. "/home/user/TikTok-example-1.gif".
import os
import urllib.request
from moviepy.editor import VideoFileClip


def clear_tmp_folder():
    tmp_folder = 'tmp'
    for f in os.listdir(tmp_folder):
        os.remove(os.path.join(tmp_folder, f))


def gif_name():
    dir_path = r'videos'
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1

    return count + 1


def retrieve(video_url):
    name = 'tmp/example.mp4'
    try:
        urllib.request.urlretrieve(video_url, name)
    except Exception as e:
        print(e)


def convert(video_url):
    retrieve(video_url)

    video_clip = VideoFileClip("tmp/example.mp4")
    video_clip.write_gif(f"videos/TikTok-example-{gif_name()}.gif")
    clear_tmp_folder()


if __name__ == '__main__':
    url = "http://techslides.com/demos/sample-videos/small.mp4"
    convert(url)
