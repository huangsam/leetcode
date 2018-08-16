#!/bin/bash

find algorithms -type f | xargs grep 'http' | awk '{ print $NF }'
find shell -type f | xargs grep 'http' | awk '{ print $NF }'
