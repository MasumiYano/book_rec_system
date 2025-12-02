from transformers import pipeline 
from utils  import get_prompt

class NlToJson:
    def __init__(self, prompt_path: str, device:str , model="google/gemma-2-9b"):
        self.prompt = get_prompt(prompt_path) 
        self.device = device
        self.model = model
        self.pipe = None

    def setup_pipeline(self):
        self.pipe = pipeline(
                "text-generation",
                model = self.model,
                device =self.device,
                )

    def get_result(self):
        prompt = self.prompt
        print(prompt)
        outputs = self.pipe(prompt, max_new_tokens=256)
        response = outputs[0]["generated_text"]
        return response
