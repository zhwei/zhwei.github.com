#!/bin/bash
cd "$(dirname "$0")"

slug=$1
title=$2

today=`date '+%Y-%m-%d'`
dir_path="content/post/$today.$slug"

mkdir -p $dir_path
cat <<EOT > "$dir_path/index.md"
---
title: $2
date: $today
slug: $slug
tags:
    - 
---
EOT