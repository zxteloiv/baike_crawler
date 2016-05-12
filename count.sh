#!/bin/bash

# output:
# total_num_of_html_pages \t webpages_crawled_more_than_once \t duplicated_webpages_count_in_total

find . | awk -F "/" '{if ($3 != "") print $3}' | sort | uniq -c | awk -v thedate="$(date '+%Y-%m-%d %H:%M:%S')" '{if ($1 > 1) {s+=$1;u+=1;}all+=$1}END{print thedate"\t"all"\t"u"\t"s}'


