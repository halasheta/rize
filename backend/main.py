from fastapi import FastAPI, UploadFile, File, Response
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from starlette.responses import JSONResponse

from summary import Summary
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


class SummaryModel(BaseModel):
    summary: str
    concepts: dict
    images: list


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/home")
async def home():
    # load UI
    return "welcome to rize!"


@app.post("/upload") #, response_model=SummaryModel)
async def upload(uploadfile: UploadFile = File(...)):
    contents = await uploadfile.read()
    await uploadfile.close()

    s = Summary(contents.decode())
    json_format = s.json_format()
    json = JSONResponse(content=json_format)
    return json

# @app.get("/get_summary")
# async def get



# @app.post("/upload")
# async def create_upload_text(uploadfile: UploadFile = File(...)):
#     # read file contents
#     contents = await uploadfile.read()
#     await uploadfile.close()
#
#     s = Summary(contents.decode())
#     # json_compatible_sum = jsonable_encoder(s)
#     # return JSONResponse(content=json_compatible_sum)
#     # print(s.summary)
#     # return Response(content=s, media_type="application/json")
#     return
