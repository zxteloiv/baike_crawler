#!/bin/bash

rotatedir=html$(date +%Y%m%d%H%M)
cd /home/zxteloiv/codes/baike_crawler/data/ 

mkdir $rotatedir 

mv *.htm $rotatedir
