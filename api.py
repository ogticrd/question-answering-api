from fastapi import FastAPI
from fastapi import Request

from transformers import AutoTokenizer
from transformers import AutoModelForQuestionAnswering
from transformers import QuestionAnsweringPipeline

app = FastAPI()

tokenizer = AutoTokenizer.from_pretrained(
    "PlanTL-GOB-ES/roberta-base-bne-sqac")
model = AutoModelForQuestionAnswering.from_pretrained(
    "PlanTL-GOB-ES/roberta-base-bne-sqac")
pipeline = QuestionAnsweringPipeline(model, tokenizer)

context = "El español es el segundo idioma más hablado del mundo con más de 442 millones de hablantes"


@app.post('/webhook/v1/dialogflow/qa')
async def root(req: Request):
    req_json = await req.json()

    answer = pipeline(question=req_json['text'], context=context)['answer']

    res = {
        'fulfillment_response': {
            'messages': [
                {
                    'text': {
                        'text': [
                            answer
                        ]
                    }
                }
            ]
        }
    }
    return res
