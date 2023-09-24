import os
from typing import List
from moviepy.editor import AudioFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.VideoClip import TextClip as MoviePyTextClip


class TextToVideoConverter:
    """
    Класс для конвертации текста в видео с аудио.

    Args:
        translations (List[str]): Список строк, содержащих переводы для создания видео.
        delay (float): Задержка между текстовыми клипами и аудиофайлами.
        tmp_dir (str): Директория для временных файлов и аудиофайлов.

    Attributes:
        translations (List[str]): Список строк с переводами.
        delay (float): Задержка между текстовыми клипами и аудиофайлами.
        tmp_dir (str): Директория для временных файлов и аудиофайлов.
    """

    def __init__(self, translations: List[str], delay: float, tmp_dir: str):
        self.translations = translations
        self.delay = float(delay)
        self.tmp_dir = tmp_dir

        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)

    def create_text_clip_for_word(self, word: str, current_time: float) -> MoviePyTextClip:
        """
        Создает текстовый клип для заданного слова.

        Args:
            word (str): Слово, для которого создается текстовый клип.
            current_time (float): Текущее время в видео для установки начального времени клипа.

        Returns:
            MoviePyTextClip: Созданный текстовый клип или None, если аудиофайл не найден.
        """
        audio_filename = os.path.join(self.tmp_dir, f"{word}.mp3")
        if not os.path.exists(audio_filename):
            print(f"Аудио файл для {word} не найден.")
            return None

        audioclip = AudioFileClip(audio_filename).subclip(0, AudioFileClip(audio_filename).duration)

        txt_clip = MoviePyTextClip(word, fontsize=70, color='white')
        txt_clip = txt_clip.set_duration(audioclip.duration + self.delay)
        txt_clip = txt_clip.set_audio(audioclip)
        txt_clip = txt_clip.set_start(current_time)
        txt_clip = txt_clip.set_position('center')

        return txt_clip

    def create_combined_video(self):
        """
        Создает общее видео из текстовых клипов и сохраняет его в файл 'combined_video.mp4'.
        """
        text_clips = []
        current_time = 0

        for line in self.translations:
            word = line.split(':')[0]
            word = word.replace(" ", "_")

            clip = self.create_text_clip_for_word(word, current_time)
            if clip:
                text_clips.append(clip)

            current_time += clip.duration if clip else 0

        video_resolution = (1920, 1080)
        video_clip = CompositeVideoClip(text_clips, size=video_resolution)
        video_clip.write_videofile('combined_video.mp4', codec='libx264', audio_codec='aac', fps=24)
