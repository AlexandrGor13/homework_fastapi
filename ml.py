from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from schemas import Text

langlist = ["ru", "en"]
tokenizer = {}
model = {}
for i in range(len(langlist)):
    key = f"{langlist[i % 2]}-{langlist[(i + 1) % 2]}"
    tokenizer[key] = AutoTokenizer.from_pretrained(f"Helsinki-NLP/opus-mt-{key}")
    model[key] = AutoModelForSeq2SeqLM.from_pretrained(f"Helsinki-NLP/opus-mt-{key}")


def translate(original_text: Text, src: str, dest: str):
    current_model = model.get(f"{src}-{dest}")
    current_tokenizer = tokenizer.get(f"{src}-{dest}")
    translated_text = ""
    if current_model and current_tokenizer:
        # подготовка входных данных
        tokenized_text = current_tokenizer([original_text.text], return_tensors='pt')
        # перевод
        translation = current_model.generate(**tokenized_text)
        translated_text = current_tokenizer.batch_decode(translation, skip_special_tokens=True)[0]
    return Text(text=translated_text)


if __name__ == "__main__":
    assert translate(Text(text="hello world"), src="en", dest="ru").text == "Приветствую мир", "Error"