# Dog Breed Classifier

This project uses a pre-trained image classifier to identify dog breeds. The project is divided into several steps and uses three different model architectures (resnet, alexnet, and vgg).

## Project Structure

- `.devcontainer/`: Contains the setup for the development container.
- `pet_images/`: Folder containing the images to classify.
- `uploaded_images/`: Folder for uploading new images to test.
- `check_images.py`: Main script to run the classification.
- `print_results.py`: Script to print the results.
- `get_input_args.py`: Script to get input arguments.
- `get_pet_labels.py`: Script to get pet labels.
- `classify_images.py`: Script to classify images.
- `adjust_results4_isadog.py`: Script to adjust results to determine if the label is a dog.
- `calculates_results_stats.py`: Script to calculate results statistics.
- `requirements.txt`: Python dependencies.
- `run_models_batch.sh`: Script to run all models on `pet_images`.
- `run_models_batch_uploaded.sh`: Script to run all models on `uploaded_images`.

## Setup

To get started, ensure you have Docker installed and open this project in GitHub Codespaces.

## Running the Project

1. To classify images in the `pet_images` folder:
   ```bash
   sh run_models_batch.sh
