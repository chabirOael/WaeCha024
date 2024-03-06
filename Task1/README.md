# Text Classification Docker Project

This project provides a Dockerized environment for text classification. Follow the steps below to build and run the project.

## Model Training

The model training was performed using Google Colab, which provides access to GPUs for faster computation. The code and data used for training can be found in the notebook [train_and_publish_tc_model.ipynb](https://colab.research.google.com/notebooks/intro.ipynb).

Make sure to follow the instructions in the notebook to set up the environment and run the training process.

## Note

Please note that the code and data used for training are not included in this repository. You will need to download them separately from the provided link.


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
    docker run -d -p 8080:8080 visable_tc_app
    ```

5. Test the application:

    ```bash
    http POST http://localhost:8000/classify text="Spirituosen Grosshandel"  
    ```
    You can change the text content to test the classification made by the model.
## Configuration

You can customize the project by modifying the configuration files located in the `<project-directory>/config` directory.

## Usage

Provide instructions on how to use the text classification application here.
