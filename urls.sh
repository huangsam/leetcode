#!/bin/bash

find algorithms shell -type f | xargs grep 'https' | awk '{ print $NF }'
