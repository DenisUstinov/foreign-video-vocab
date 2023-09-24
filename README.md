# ForeignVideoVocab

Проект `ForeignVideoVocab` представляет собой инструмент для создания видеофайлов на основе текстовых переводов. Этот инструмент расширяет возможности библиотеки [ForeignAudioVocab](https://github.com/DenisUstinov/foreign-audio-vocab) и использует библиотеку moviepy для преобразования аудио словарей в видеоролики и объединения их в видеофайлов.

## Используйте в своих проектах

Вы можете установить `ForeignVideoVocab` с помощью инструмента `pip` следующим образом:

```bash
pip install git+https://github.com/DenisUstinov/foreign-video-vocab.git --use-pep517
````
```python
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
```

## Клонирование репозитория

Для того чтобы начать работу с проектом, выполните следующие шаги:

1. Клонируйте этот репозиторий на свой компьютер:

```bash
git clone https://github.com/DenisUstinov/foreign-video-vocab.git
```


2. Перейдите в директорию проекта:

```bash
cd foreign-video-vocab
```


## Установка

Для использования проекта вам потребуется установить Python (версия 3.6 или выше) и необходимые библиотеки. Выполните следующие шаги:

1. Убедитесь, что у вас установлен Python версии 3.6 или выше. Если нет, вы можете скачать его с [официального сайта](https://www.python.org/downloads/).

2. Установите необходимые библиотеки, выполнив следующую команду в командной строке:


```bash
pip install moviepy git+https://github.com/DenisUstinov/foreign-audio-vocab.git --use-pep517
```


## Использование

1. Создайте файл `translations.txt` и добавьте в него переводы в формате `слово:перевод` для каждой строки.

2. В файле `main.py` укажите путь к файлу `translations.txt`, а также задайте параметры для создания экземпляра класса `TextToVoiceConverter`.

3. Запустите скрипт `main.py`:

```bash
python main.py
```

Это создаст аудиофайлы на основе переводов и объединит их в один аудиофайл.

## Лицензия

Этот проект лицензирован в соответствии с лицензией [MIT](LICENSE).
