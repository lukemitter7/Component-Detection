# Component Detection AI

## Overview

This project focuses on component detection using YOLOv8 as the original training AI. YOLOv8, short for You Only Look Once version 8, is a state-of-the-art object detection algorithm known for its speed and accuracy. The goal of this project is to train YOLOv8 to accurately detect components within images.

## Training Process

The YOLOv8 model was trained using a dataset of component images. The training process involved optimizing the model's parameters to improve its ability to detect components accurately. Five different training sessions were conducted, each varying in the number of epochs:

- **1 Epoch**: The model was trained for a single epoch to establish a baseline performance.
- **5 Epochs**: The model underwent training for five epochs to observe incremental improvements.
- **20 Epochs**: A more extensive training session consisting of 20 epochs was conducted to further refine the model's accuracy.
- **100 Epochs**: A longer training session with 100 epochs aimed to achieve a high level of accuracy.
- **200 Epochs**: The model underwent an extended training session of 200 epochs to maximize its detection capabilities.

## Evaluation

After each training session, the trained model was evaluated using various metrics to assess its performance in component detection. Metrics such as precision, recall, and mean average precision (mAP) were calculated to measure the model's accuracy and reliability in identifying components within images.

## Folder Structure

The folder is organized into subdirectories, each corresponding to a specific test batch. Within each subdirectory, you'll find images depicting precision confidence curves for that particular batch. Additionally, there are five versions listed (`v1`, `v2`, etc.) for further organization and reference. The repository also contains datasets located in the folder named `Training Data`.

# Prerequisites

Before using the model, ensure your system meets the following prerequisites:

1. **Python 3**: YOLOv8 requires Python 3 to run. Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **CUDA Toolkit (Optional)**: If you plan to run YOLOv8 with GPU acceleration, you'll need to install the CUDA Toolkit. YOLOv8 is optimized to leverage NVIDIA GPUs for faster inference. Visit the [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) page to download and install the appropriate version for your GPU.

3. **cuDNN (Optional)**: For GPU acceleration, you'll also need cuDNN installed. cuDNN is a GPU-accelerated library for deep neural networks. Download and install cuDNN from the [NVIDIA cuDNN](https://developer.nvidia.com/cudnn) page.

4. **Python Dependencies**: YOLOv8 relies on several Python libraries. You can install these dependencies using pip, the Python package manager. Run the following command to install the required packages:

```
pip install -r requirements.txt
```


## Running `main.py` to Select a Version

To run `main.py` and select a version to analyze:

1. Ensure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the root directory of this repository.
4. Run the following command:
    ```
    python main.py
    ```
The program will ask which version you would like to run.

    Select one: [v1, v2, v3, v4, v5]
    Please input your version:
Then the program will automatically run your files in the folder named Test and all results will appear in the runs folder next to Component_detection.

## Understanding Precision Confidence Curves

Precision confidence curves are graphical representations that illustrate the relationship between precision and confidence levels in our testing results. These curves are essential for assessing the accuracy and reliability of our testing procedures.

## Viewing the Images

To view the precision confidence curves for a specific test batch:

1. Navigate to the corresponding subdirectory in this repository.
2. Open the images using your preferred image viewer.

## Interpreting the Curves

Each curve showcases the precision of our testing process at varying confidence levels. A higher precision value indicates a greater level of accuracy in our test results, while the confidence level represents the reliability or certainty associated with those results.

## BETA Webcam Operation

If you wish to use the `BETA_webcam.py` file, you MUST use an external webcam for best results. Results will be saved whether or not you have an external webcam or not.

## License

This project is licensed under the [MIT License](LICENSE.md) - feel free to use, modify, and distribute the content within the terms of this license.

## Feedback and Support

For any questions, feedback, or support regarding these precision confidence curves or related testing methodologies, please contact lblanche1@arizona.edu or lukemitter7@gmail.com.
