from typing import Annotated

import uvicorn
from fastapi import FastAPI, HTTPException, Body, Path

from ml import translate
from schemas import Text

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the text translation API"}


@app.post("/translation/{src}-{dest}", response_model=Text)
def translation(
        text: Annotated[Text, Body()],
        src: Annotated[str, Path(pattern=r'^(ru|en)$')],
        dest: Annotated[str, Path(pattern=r'^(ru|en)$')]
):
    try:
        translated_text = translate(text, src, dest) if src != dest else text
        return translated_text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
