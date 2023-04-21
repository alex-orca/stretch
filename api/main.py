from fastapi import FastAPI
import os
import openai

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/category/new')
async def make_new_category(categories:list)->list:
    template=gen_template(categories,mode='category')
    response=call_openai(template)
    new_categories=parse_response(response)
    return new_categories

@app.get('/description/new')
async def make_new_description(categories:list)->list:
    raise NotImplementedError

#------------------HELPER FUNCTIONS------------------#


def gen_template(categories,mode:str)->str:
    raise NotImplementedError

def call_openai(prompt:str,model:str="text-davinci-003"):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
    model=model,
    prompt=prompt,
    temperature=0,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\"\"\""]
    )

    return response

def parse_response(response)->list:
    raise NotImplementedError