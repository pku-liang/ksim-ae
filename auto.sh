#!/bin/bash

# set -xe

# prepare git submodules
make -j1 prepare-setup

# install depedencies
make -j$(nproc) setup

# setup environments
. ./env.sh

# build benchmakrs
make -j$(nproc) build

# run all experiments
make -j1 run-all

# generate report.pdf
# make report