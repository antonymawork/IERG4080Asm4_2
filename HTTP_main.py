import threading
import time
import json
import redis

# Create Redis connection
REDIS_HOST = '44.215.160.99'
REDIS_PORT = 6379
REDIS_DB = 0

r = redis.Redis(host=REDIS_HOST, 
            port=REDIS_PORT, 
            db=REDIS_DB, 
            password=ierg4080, 
            health_check_interval=10,
            socket_timeout=1000, socket_keepalive=True,
            socket_connect_timeout=1000, retry_on_timeout=True
            )

def listen_predictions():
    while True:
        # Now start processing prediction tasks
        _, message = r.blpop("prediction")
        print(f"Received message from Redis: {message}")
        task = json.loads(message)
        print(f"Received task: {task}")
        task_id = task.get("task_id")
        redis_key = f"result:{task_id}"
        redis_value = json.dumps(task)
        r.set(redis_key, redis_value)
        for prediction in task['predictions']:
            print("Language: {}, Score: {:.4f}".format(prediction['label'], prediction['score']))

def perform_prediction(task):
    return task  # Here you might integrate your actual prediction model

if __name__ == "__main__":
    prediction_thread = threading.Thread(target=listen_predictions)
    prediction_thread.start()
