#!/bin/bash

git clone https://github.com/linkedin/Burrow

cd Burrow
docker build . -t hy22-burrow:0.1
cd ..
