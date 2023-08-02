# KSim Artifact Evaluation

The evaluation will be run on 3 different machines, `base`, `plat-1`, and `plat-2`.
`base` is the "master" machine, and the other two are "slave" machines.

# Quick Evaluation

## System Requirements

Install experiments requirements on all machines,
if you are using our offered computer, all the requirements have been installed.

```bash
pacman -S wget rsync \
  jre11-openjdk-headless sbt \
  base-devel clang llvm \
  python3 python-pip python-numpy python-scipy python-pandas \
  python-matplotlib python-seaborn python-tqdm \
  cmake ninja boost ccache \
  flex bison help2man perf
```

Install texlive on master:

```bash
pacman -S texlive # select all groups in texlive
```

Sometimes language may break the auto scripts, use the following command to reset language before evaluation:

```bash
unset LC_ALL LANG LANGUAGE
```

## SSH Setup

The platform names are shown in `env.sh`.
Configure `~/.ssh/config`, `~/.ssh/authorized_keys` correctly to make sure no password is needed for ssh, i.e. the following command should not require password or throw errors.

```bash
ssh base   # no password is needed
ssh plat-1 # no password is needed
ssh plat-2 # no password is needed
```

## Tools and Simulators Setup

Clone this repo on the `$HOME` directory of the user.

```bash
git clone [this-repo] ~/ksim-ae
```

Tools are in `sims` and `tools` folder, run the following command to set up all simulators.

```bash
make prepare # download git submodule, make sure to run in single thread
make -j$(nproc) setup # setup environment, multi-threading is supported
```

Sometimes `verilator` may fail compilation on multi-thread, you may need to run setup in a single thread after failure.

```bash
make -j1 setup
```

After the setup, run `source env.sh` to check the environment. Please note that `vcs` is only available on `base`. Make sure `vcs` is in `runs` list on `base` and not on `plat-1` and `plat-2`.

```bash
ksim            is at ./sims/install/bin/ksim
llc             is at ./sims/install/bin/llc
verilator       is at ./sims/install/bin/verilator
firtool         is at ./sims/install/bin/firtool
firrtl          is at ./tools/bin/firrtl
g++             is at /usr/bin/g++
clang++         is at /usr/bin/clang++
essent          is at ./sims/bin/essent
repcut          is at ./sims/bin/repcut
KaHyPar         is at ./sims/bin/KaHyPar
firclean        is at ./tools/bin/firclean
timeit          is at ./tools/bin/timeit
vcs             is not found

runs:           circt-verilator verilator-1 verilator-2 verilator-4 ksim essent repcut-1 repcut-2 repcut-4 repcut-6 repcut-8
hosts:          plat-1 plat-2
```

## Run Experiment

The experiment is divided into two phases, first, build executable files and then run the executable file to collect performance data.

Build the executable:

```bash
make -j$(nproc) build
```

Run the executable:

```bash
make -j1 run-all
```

The experiment data is listed in `results` folder, like this:

```bash
$ tree -L 1 results
results
├── cpu-info.json
├── extra-info.csv
├── fuse.csv
├── result.csv
├── runs
└── size.csv
```

## Generate Report

In the `base` machine, run the following command to generate a performance report.

```bash
make report
```

This command will copy results in `base`, `plat-1`, `plat-2` into `analysis/data` and generate a report file according to the template in `analysis/report`.
