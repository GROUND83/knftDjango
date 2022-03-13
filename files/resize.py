from PIL import Image, ImageSequence
import os.path
from config.settings import MEDIA_ROOT
from django.conf import settings
from moviepy.editor import VideoFileClip


def resize_gif(image, width, name, caption):
    # self.avator 확인 동영상 ? 이미지? gif?
    basewidth = width
    im = Image.open(image)
    wpercent = basewidth / float(im.size[0])
    hsize = int((float(im.size[1]) * float(wpercent)))
    frames = ImageSequence.Iterator(im)

    def thumbnails(frames):
        for frame in frames:
            thumbnail = frame.copy()
            thumbnail.thumbnail((basewidth, hsize), Image.ANTIALIAS)
            yield thumbnail

    frames = thumbnails(frames)
    filename = image.name.split(".")
    upladName = caption + "." + filename[1]
    # Save output
    om = next(frames)  # Handle first frame separately
    om.info = im.info  # Copy sequence info

    om.save(
        os.path.join(MEDIA_ROOT, f"{name}/{caption}/{width}_{upladName}"),
        save_all=True,
        append_images=list(frames),
        loop=0,
    )
    downName = f"{name}/{caption}/{width}_{upladName}"
    return downName


def resize_jpg(image, width, name, caption):
    filename = image.name.split(".")
    upladName = caption + "." + filename[1]
    base_dir = settings.MEDIA_ROOT
    # self.avator 확인 동영상 ? 이미지? gif?
    basewidth = width
    im = Image.open(image)
    wpercent = basewidth / float(im.size[0])
    hsize = int((float(im.size[1]) * float(wpercent)))
    im.thumbnail((basewidth, hsize))
    print(MEDIA_ROOT)
    if os.path.isdir(os.path.join(MEDIA_ROOT, f"{name}")):
        pass
    else:
        os.mkdir(os.path.join(MEDIA_ROOT, f"{name}"))
    im.save(os.path.join(MEDIA_ROOT, f"{name}/{caption}/{width}_{upladName}"))
    # im.save(f"{MEDIA_ROOT}/{name}/{width}_{upladName}")
    #  f"{base_dir}/{name}/{width}_{upladName}",
    # Save output
    im.close()
    downName = f"{name}/{caption}/{width}_{upladName}"
    return downName


def resize_viedo(image, name, caption):
    filename = image.split(".")
    upladName360 = caption + "." + filename[1]
    upladName800 = caption + "." + filename[1]
    imgupladName = caption + "." + "jpg"
    # self.avator 확인 동영상 ? 이미지? gif?
    clip = VideoFileClip(image)
    clip_resized360 = clip.resize(width=360)
    clip_resized800 = clip.resize(width=800)
    if os.path.isdir(os.path.join(MEDIA_ROOT, f"{name}/{caption}")):
        pass
    else:
        os.mkdir(os.path.join(MEDIA_ROOT, f"{name}/{caption}"))
    clip_resized360.write_videofile(
        os.path.join(MEDIA_ROOT, f"{name}/{caption}/360_{upladName360}")
    )
    clip_resized800.write_videofile(
        os.path.join(MEDIA_ROOT, f"{name}/{caption}/800{upladName800}")
    )
    # 프리뷰
    clip_resized360.save_frame(
        os.path.join(MEDIA_ROOT, f"{name}/{caption}/thum_{imgupladName}"),
        t=1.00,
    )
    d = dict()
    d["upladName360"] = upladName360
    d["upladName800"] = upladName800
    d["imgupladName"] = imgupladName
    return d


# def resize_video(video):
#     print(video)
#     clip = VideoFileClip(video)
#     clip_resized = clip.resize(
#         width=360
#     )  # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
#     clip_resized.write_videofile("movie_resized.mp4")
#     return
