from transformers import pipeline

pipe = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")

sentence = "I love this product! It's amazing and works perfectly."
result = pipe(sentence)

print(result)
