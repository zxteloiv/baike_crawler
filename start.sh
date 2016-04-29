#!/bin/bash

#SCRAPY=~/.local/bin/scrapy
SCRAPY=scrapy
JOBDIR=./job

mkdir -p $JOBDIR

$SCRAPY crawl baike -s JOBDIR=$JOBDIR
