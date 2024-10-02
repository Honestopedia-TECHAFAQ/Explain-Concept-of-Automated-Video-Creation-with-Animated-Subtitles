import moviepy.editor as mp
from moviepy.video.tools.drawing import color_split
from moviepy.config import IMAGEMAGICK_BINARY

IMAGEMAGICK_BINARY = r'C:\Program Files\ImageMagick-<version>\magick.exe'
video = mp.VideoFileClip("output_video_final_with_music.mp4")
class Word:
    def __init__(self, text, start, end, confidence):
        self.text = text
        self.start = start
        self.end = end
        self.confidence = confidence

transcript = type('Transcript', (object,), {
    'words': [
        Word(text='Hensel', start=160, end=488, confidence=0.69857),
        Word(text='and', start=494, end=662, confidence=1.0),
        # Add other Word instances here
    ]
})

def create_blue_box(word):
    box_clip = mp.ColorClip(size=(300, 50), color=(0, 0, 255), duration=word.end - word.start)

    text_clip = mp.TextClip(word.text, fontsize=24, color='white', bg_color='blue')
    text_clip = text_clip.set_position(('center', 'center')).set_duration(word.end - word.start)
    combined_clip = mp.CompositeVideoClip([box_clip, text_clip])
    combined_clip = combined_clip.set_start(word.start).set_duration(word.end - word.start)
    
    return combined_clip
blue_boxes = [create_blue_box(word) for word in transcript.words]
final_video = mp.CompositeVideoClip([video] + blue_boxes)
final_video.write_videofile("output_with_blue_box.mp4", codec="libx264")
