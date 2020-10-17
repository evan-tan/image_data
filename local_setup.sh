#!/bin/bash
cd ..
mkdir darknet/build/darknet/x64/data/obj
cp -r image_data/data/img/* darknet/build/darknet/x64/data/obj/
cp image_data/data/obj.data darknet/build/darknet/x64/data/
cp image_data/data/obj.names darknet/build/darknet/x64/data/
cp image_data/data/train.txt darknet/build/darknet/x64/data/
cp image_data/cfg/custom-yolov4-detector.cfg darknet/cfg/