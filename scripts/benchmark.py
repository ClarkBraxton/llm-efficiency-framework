import time
from transformers import pipeline

model = pipeline("text-generation", model="gpt2")

start = time.time()
output = model("Artificial intelligence is", max_length=30)
end = time.time()

print(output)
print("Inference time:", end - start)
