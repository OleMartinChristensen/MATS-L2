# MATS-L2

Repository for MATS level 2 processing tools

## Installing invlib

### Requirements

- GCC > 7.0
- Intel MKL

The `invlib` Python interface uses Intel MKL for efficient matrix operations,
which can be installed from the (intel homepage)[https://software.intel.com/en-us/mkl].
After successful installation it is recommended to source the `compilervars.sh` script
which declares environment variables informing other code about the MKL installation.

```
source <intel_install_dir>/bin/compilervars.sh
```

Alternatively, it should suffice to set the environment variable `MKL_ROOT` to point
to the `mkl` folder in the intel install folder.

```
export MKL_ROOT=<intel_install_dir>/mkl
```

### Getting the source code

To get the invlib source code clone the [invlib](https://github.com/simonpf/invlib) repository
to a destination of your choice.

```
git clone https://github.com/simonpf/invlib
```

### Building the interface

To build the interface `cd` into the invlib source directory and run `setuptools`:

```
cd invlib
python setup.py install
```

## Running the code

The `test/mats.py` provides an example on how to run an OEM calculation using invlib.




