import os
from typing import List
from moviepy.editor import AudioFileClip, TextClip, VideoFileClip, concatenate_videoclips
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip


class TextToVideoConverter:
    """
    Класс для создания видео на основе текстовых переводов.

    Параметры:
    - translations (List[str]): Список переводов в формате 'слово1:слово2'.
    - mp3_folder (str): Путь к папке с MP3 файлами.
    """

    def __init__(self, translations: List[str], mp3_folder: str):
        """
        Инициализация класса TextToVideoConverter.

        :param translations: Список переводов в формате 'слово1:слово2'
        :param mp3_folder: Путь к папке с MP3 файлами
        """
        self.translations = translations
        self.mp3_folder = mp3_folder

        if not os.path.exists(self.mp3_folder):
            os.makedirs(self.mp3_folder)

    def create_single_video(self, word1: str):
        """
        Создание отдельного видео с текстовым переводом.

        Параметры:
        - word1 (str): Английское слово.
        - word2 (str): Переведенное слово.
        """
        word1 = word1.replace(" ", "_")

        mp3_filename = os.path.join(self.mp3_folder, f"{word1}.mp3")
        video_filename = os.path.join(self.mp3_folder, f"{word1}.mp4")

        if not os.path.exists(mp3_filename):
            print(f"MP3 файл для '{word1}' не найден.")
            return

        audioclip = AudioFileClip(mp3_filename).subclip(0, AudioFileClip(mp3_filename).duration)

        video_resolution = (1920, 1080)  # HD разрешение

        txt_clip = TextClip(word1, fontsize=70, color='white')
        txt_clip = txt_clip.set_duration(audioclip.duration)
        txt_clip = txt_clip.set_audio(audioclip)
        txt_clip = txt_clip.set_pos('center')  # Разместить текст по центру кадра

        # Создать CompositeVideoClip для задания разрешения
        video_clip = CompositeVideoClip([txt_clip], size=video_resolution)

        video_clip.write_videofile(video_filename, codec='libx264', audio_codec='aac', fps=24)

    def create_videos(self):
        """Создание отдельных видео для каждого перевода."""
        for line in self.translations:
            word1, word2 = line.split(':')
            self.create_single_video(word1)

    def create_combined_video(self):
        """Создание объединенного видео из отдельных видео."""
        clips = []
        for line in self.translations:
            word1, _ = line.split(':')
            video_filename = os.path.join(self.mp3_folder, f'{word1.replace(" ", "_")}.mp4')
            if os.path.exists(video_filename):
                clips.append(VideoFileClip(video_filename))

        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile('combined_video.mp4', codec='libx264', audio_codec='aac', fps=24)
