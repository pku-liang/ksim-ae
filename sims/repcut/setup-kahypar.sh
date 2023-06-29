#!/bin/bash
cd kahypar

git submodule update --init

if ! [ -d build ] || ! [ -f build/Makefile ]; then
  [ -d build ] || mkdir build
  cd build
  cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF
fi

