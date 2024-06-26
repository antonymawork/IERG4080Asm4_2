import json
import redis
from transformers import pipeline

# Initialize a Redis connection.
REDIS_HOST = '44.215.160.99'
REDIS_PORT = 6379
REDIS_DB = 0

r = redis.Redis(host=REDIS_HOST, 
            port=REDIS_PORT, 
            db=REDIS_DB, 
            password='ierg4080', 
            health_check_interval=10,
            socket_timeout=1000, socket_keepalive=True,
            socket_connect_timeout=1000, retry_on_timeout=True
            )

# Load the language detection model
model_ckpt = "papluca/xlm-roberta-base-language-detection"
pipe = pipeline("text-classification", model=model_ckpt, device=-1)

def generate_predictions(text):
    predictions = pipe(text, top_k=1, truncation=True)
    return predictions

def continuously_receive_messages():
    while True:
        try:
            print("Waiting for text...")
            _, message = r.brpop("text")
            data = json.loads(message)
            print(f"Received message for processing: {data}")

            text = data["text"]
            task_id = data["task_id"]
            timestamp = data["timestamp"]
            print(f"Processing text: {text}")

            predictions = generate_predictions(text)
            result_message = {
                "task_id": task_id,
                "timestamp": timestamp,
                "text": text,
                "predictions": predictions
            }
            print(f"Generated result_message: {result_message}")
            r.lpush("prediction", json.dumps(result_message))
        except Exception as e:
            print(f"An error occurred during message processing: {e}")

if __name__ == "__main__":
    continuously_receive_messages()
