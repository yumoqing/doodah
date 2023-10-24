#!/bin/bash

VERSION=$(echo "echo $(grep -e "[\'\"].*[\'\"]" -o version.py)" | sh)
rm ./bin/*
buildozer android clean
buildozer android release
apksigning.sh ./bin/doodah-${VERSION}-armeabi-v7a-release-unsigned.apk ${HOME}/apks/doodah_${VERSION}.apk "ymq_kivyapp"
