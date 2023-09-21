from foreign_video_vocab.text_to_video_converter import TextToVideoConverter
from foreign_audio_vocab.text_to_voice_converter import TextToVoiceConverter


def read_file_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


if __name__ == "__main__":
    # Замените 'translations.txt' на путь к вашему файлу с переводами
    input_file = 'translations.txt'

    # Считываем переводы из файла
    translations = read_file_lines(input_file)

    # Параметры для создания экземпляра TextToVoiceConverter
    delimiter = ':'
    langs = 'en:ru'
    delay = 2
    mp3_folder = 'tmp'  # Папка с мп3 словарями

    # Создание экземпляра класса TextToVoiceConverter с заданными параметрами и считанными переводами
    converter_audio = TextToVoiceConverter(translations, delimiter, langs, delay, mp3_folder)

    try:
        converter_audio.process_translations()  # Создание промежуточных аудиофайлов

        # Создание экземпляра класса TextToVoiceConverter с заданными параметрами и считанными переводами
        converter_video = TextToVideoConverter(converter_audio.audio_files, mp3_folder)
        converter_video.create_videos()
        converter_video.create_combined_video()
        #
        # converter_audio.remove_old_audio_files()  # Удаление временных файлов
        print("Обработка завершена.")
    except Exception as e:
        print(f"Произошла ошибка при обработке: {e}")
