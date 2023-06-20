#memory.py
import torch
import openai
from transformers import GPTNeoForCausalLM, GPT2Tokenizer

class Memory:
    def __init__(self, openai_api_key, model_name):
        self.openai_api_key = openai_api_key
        self.model_name = model_name
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
        self.memory = {}
        self.model = GPTNeoForCausalLM.from_pretrained(self.model_name)

    def store_information(self, data):
        encoded_data = self.tokenizer.encode(data, return_tensors="pt")
        generated_output = self.model.generate(encoded_data, max_length=100)[0]
        self.memory[data] = generated_output
        self._clear_memory(encoded_data, generated_output)

    def retrieve_information(self, query):
        if self.requires_openai_processing(query):
            response = self.process_with_openai(query)
        else:
            encoded_query = self.tokenizer.encode(query, return_tensors="pt")
            input_ids = torch.cat(list(self.memory.values()), dim=0)
            outputs = self.model.generate(encoded_query, input_ids=input_ids, max_length=100)
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            self._clear_memory(encoded_query, input_ids, outputs)
        return response

    def requires_openai_processing(self, query):
        return len(self.tokenizer.tokenize(query)) > 20

    def process_with_openai(self, query):
        try:
            openai_response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=query,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.7,
                api_key=self.openai_api_key
            )
            response = openai_response.choices[0].text.strip()
            self._clear_memory(openai_response)
            return response
        except Exception as e:
            print("OpenAI processing error:", str(e))
            return None

    def _clear_memory(self, *variables):
        for var in variables:
            if isinstance(var, torch.Tensor):
                del var
            elif isinstance(var, list):
                for item in var:
                    if isinstance(item, torch.Tensor):
                        del item

# Example usage
def main():
    openai_api_key = "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"
    model_name = "EleutherAI/gpt-neo-1.3B"
    memory = Memory(openai_api_key, model_name)

    # Update memory with new information
    memory.store_information("Some example data")

    # Retrieve information from memory
    result = memory.retrieve_information("Query")
    print(result)

if __name__ == "__main__":
    main()