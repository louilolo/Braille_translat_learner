from fastapi import FastAPI, UploadFile, HTTPException
from .middlewares.upload import LimitUploadSize
import cv2 as cv
import numpy as np


app = FastAPI()
app.add_middleware(LimitUploadSize, max_upload_size=3_000_000) # ~5MB

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg'] # SUPPORTED FILES

@app.get('/')
async def hello():
    return {'health': 'ok'}


@app.post('/upload/')
async def upload(file: UploadFile | None = None):
    if not file:
        raise HTTPException(status_code=400, detail='Nenhum arquivo foi enviado.')
    else:
        extension = file.content_type.split('/')[-1]
        if extension in ALLOWED_EXTENSIONS:
            # TODO: Refatorar tudo isso
            array_image = np.frombuffer(file.file.read(), dtype=np.uint8)
            buffer_image = cv.imdecode(array_image, 1)
            # imgray = cv.cvtColor(buffer_image, cv.COLOR_BGR2GRAY)
            return {"detail": f"Arquivo processado"}
        else:
            raise HTTPException(status_code=422, detail='Tipo de arquivo não suportado.')
