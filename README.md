# Language Detection using Machine Learning

This repository demonstrates language detection using machine learning to classify text content into different languages. The model used is based on the [papluca/xlm-roberta-base-language-detection](https://huggingface.co/papluca/xlm-roberta-base-language-detection) model from Hugging Face.

## Local Setup

To run the language detection locally, follow these steps:

1. Download the following files:
   - `HTTP_predict.py`
   - `HTTP_main.py` 
   - `server.py`

2. Install Redis on your local machine based on your operating system.

3. Ensure Redis is running.

4. Install the required Python packages:
   ```
   pip install redis transformers requests torch
   ```

5. Open three separate terminals and run each of the following commands in a different terminal:
   ```
   python HTTP_predict.py
   python HTTP_main.py
   python server.py
   ```

6. Open a web browser and enter the URL: `http://127.0.0.1:5000`

7. Type in some text content into the text field and click "Submit". The result will display the probabilities of the most likely languages detected.

## AWS Setup

To run the language detection on AWS, follow these steps:

1. Set up two EC2 instances:
   - One instance for running the Python files (t2.large)
   - One instance for hosting Redis (t2.micro)

2. Associate Elastic IPs to both instances.

3. Set the security group for both instances to accept traffic on ports 80, 443, 6379, and 5000 (or all traffic for testing).

4. On the Redis instance:
   - Update packages: `sudo apt update`
   - Install Redis: `sudo apt install redis-server`
   - Edit the Redis configuration file: `sudo nano /etc/redis/redis.conf`
     - Replace `bind 127.0.0.1 -::1` with `bind 0.0.0.0`
     - Replace `# requirepass foobared` with `requirepass ierg4080`
   - Restart Redis: `sudo systemctl restart redis-server`

5. On the ML application instance:
   - Update packages: `sudo apt update`
   - Install Python and required packages: `sudo apt install python3 python3-pip python3-venv`
   - Create a virtual environment: `python3 -m venv article2topic`
   - Activate the virtual environment: `source ./article2topic/bin/activate`
   - Install required packages: `pip install flask redis requests torch transformers`
   - Modify the `server.py` file to replace the `REDIS_HOST` IP with your Redis instance's Elastic IP.
   - Run the server: `python3 server.py`

6. Open a web browser and enter the URL: `http://{ML Application Instance's Elastic IP}:5000`

7. Type in some text content into the text field and click "Submit". The result will display the probabilities of the most likely languages detected.

## Reference

This project uses the [papluca/xlm-roberta-base-language-detection](https://huggingface.co/papluca/xlm-roberta-base-language-detection) model from Hugging Face.
```

This README provides an overview of the language detection project, instructions for local setup and AWS setup, and references the open-source model used. Feel free to customize and expand upon this README based on your specific project details and requirements.
