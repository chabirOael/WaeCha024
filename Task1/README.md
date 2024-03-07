# Text Classification Docker Project

This project provides a Dockerized environment for text classification. Follow the steps below to build and run the project.

## Model Training

The model training was performed using <b>Google Colab</b>, which provides access to GPUs for faster computation. The code used for training can be found in the notebook [train_and_publish_tc_model.ipynb](https://github.com/chabirOael/WaeCha024/blob/master/Task1/train_and_publish_tc_model.ipynb).

Make sure to follow the instructions in the notebook to set up the environment and run the training process.

<b>[Local Run]</b> The following packages are required if you wish to train the model locally (using `pip`):
- transformers
- datasets
- transformers[torch]
- evaluate
- pytorch
    
The above packages can be installed using the following code:

```bash
pip install transformers datasets evaluate torch transformers[torch]
```

# Testing the Text Classifier (In Docker environment)


## Prerequisites

- Docker: Make sure you have Docker installed on your machine. You can download it from [here](https://www.docker.com/get-started).


## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/chabirOael/WaeCha024.git
    ```

2. Navigate to the project directory:

    ```bash
    cd <project-directory>
    ```

3. Build the Docker image:

    ```bash
    docker build -t visable_tc_app .
    ```

4. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 visable_tc_app
    ```

5. Test the application:

    ```bash
    http POST http://localhost:8000/classify text="Spirituosen Grosshandel"  
    ```
    You can change the text content to test more the capabilities of classification made by the model.

    You can also use `Postman` for testing. Do not forget to set the body as follow:
    ```json
    {
    "text": "Spirituosen Grosshandel"
    }
    ```

