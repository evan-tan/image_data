# image_data
Currently, the image dataset contains labelled data for images 0-2000.


## data_prep.py
Created to properly name images of sheep and coke from collected data in https://github.com/evan-tan/ece4078-team2-05 M3 folder
Place selected unlabelled data into `sheep/` and `coke/` folders respectively.
Then run `python data_prep.py`
Apart from the unlabelled data bins, and `cfg/` this folder structure is used in https://github.com/AlexeyAB/Yolo_mark. The only difference is that the original `img/` folder has been renamed to `obj/` as instructed when shifting images for training in https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects Step 4

## If testing/training on a local machine
Run the bash script `local_setup.sh`, please ensure that you have the [darknet](https://github.com/AlexeyAB/darknet) repository in the parent folder where you clone this repository!