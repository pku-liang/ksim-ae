#!/bin/bash

# set -xe

# prepare git submodules
make prepare-setup

# install depedencies
make -j$(nproc) setup

# setup environments
. ./env.sh

# build benchmakrs
make -j$(nproc) build

# run all experiments
make run-all

# generate report.pdf
# make report