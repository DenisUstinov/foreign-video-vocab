from foreign_video_vocab.text_to_video_converter import TextToVideoConverter
from foreign_audio_vocab.text_to_voice_converter import TextToVoiceConverter


def read_file_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


if __name__ == "__main__":
    input_file = 'translations.txt'
    translations = read_file_lines(input_file)

    delimiter = ':'
    langs = 'en:ru'
    delay = 2
    tmp_dir = 'tmp'
    converter_audio = TextToVoiceConverter(translations, delimiter, langs, delay, tmp_dir)

    try:
        converter_audio.process_translations()  # Создание промежуточных аудиофайлов

        # Создание экземпляра класса TextToVoiceConverter с заданными параметрами и считанными переводами
        converter_video = TextToVideoConverter(translations, delay, tmp_dir)
        converter_video.create_combined_video()

        # converter_audio.remove_old_audio_files()  # Удаление временных файлов
        print("Обработка завершена.")
    except Exception as e:
        print(f"Произошла ошибка при обработке: {e}")
