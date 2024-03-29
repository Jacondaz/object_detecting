from moviepy.editor import VideoFileClip
import numpy as np
import os
from datetime import timedelta

SAVING_FRAMES_PER_SECOND = 1


def format_timedelta(td):
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return result + ".00".replace(":", "-")

    ms = round(int(ms)/10000)
    return f'{result}.{ms:02}'.replace(":", "-")


def main(video_file):

    video_clip = VideoFileClip(f'src_videos/{video_file}')
    filename, _ = os.path.splitext(video_file)

    if not os.path.isdir(f'src/{filename}'):
        os.mkdir(f'src/{filename}')
        saving_frames_per_second = min(video_clip.fps, SAVING_FRAMES_PER_SECOND)
        step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second
        for current_duration in np.arange(0, video_clip.duration, step):
            frame_duration_formatted = format_timedelta(timedelta(seconds=current_duration)).replace(":", "-")
            frame_filename = os.path.join(f'src/{filename}',
                                          f'{filename}-{frame_duration_formatted}.jpg')
            video_clip.save_frame(frame_filename, current_duration)
    else:
        return


i = 0
for item in os.listdir("src_videos/"):
    if item.split(".")[-1] == "mp4":
        i += 1
        main(item)
        print(f'{i} видео раскадровано')
