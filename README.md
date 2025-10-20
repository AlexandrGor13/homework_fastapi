### API для взаимодействия с ML-моделями

#### Описание проекта
Проект представляет собой API для работы с предварительно обученными моделями машинного перевода: 
[Helsinki-NLP--opus-mt-ru-en](https://huggingface.co/Helsinki-NLP/opus-mt-ru-en), 
[Helsinki-NLP--opus-mt-en-ru](https://huggingface.co/Helsinki-NLP/opus-mt-en-ru)

End-point ```/translation/ru-en/``` предоставляет возможность переводить текс с русского языка на английский, 
```/translation/en-ru/``` переводит с английского на русский.

Используется метод POST с телом.
```json
{
  "text": "Текст, который требуется перевести"
}
```

#### Установка проекта
Клонируем проект
```bash
git clone https://github.com/AlexandrGor13/homework_fastapi.git
```
Устанавливаем проект
```bash
make setup
```

#### Запуск проекта
Запускаем контейнер с проектом в Docker
```bash
make up
```

Останавливаем контейнер
```bash
make down
```