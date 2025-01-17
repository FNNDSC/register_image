# ChRIS Register Image Plugin

[![test status](https://github.com/FNNDSC/python-chrisapp-template/actions/workflows/src.yml/badge.svg)](https://github.com/FNNDSC/register_image)
[![MIT License](https://img.shields.io/github/license/FNNDSC/python-chrisapp-template)](LICENSE)

This is a _ChRIS_ plugin applications for image registration and re-slicing in Python.


## About Register Image Plugin

This is a ChRIS plugin that registers a moving image onto a fixed image, and then re-slices the moving image in the
fixed image space. The resultant re-sliced image is saved as a NIfTI file. The moving and fixed images can be of 
different patients.

## About _ChRIS_ Plugins

A _ChRIS_ plugin is a scientific data-processing software which can run anywhere all-the-same:
in the cloud via a [web app](https://github.com/FNNDSC/ChRIS_ui/), or on your own laptop
from the terminal. They are easy to build and easy to understand: most simply, a
_ChRIS_ plugin is a command-line program which processes data from an input directory
and creates data to an output directory with the usage
`commandname [options...] inputdir/ outputdir/`.

For more information, visit our website https://chrisproject.org

## Usage Instructions

_to do_.

## Examples of other ChRIS Plugins

Here are some good, complete examples of _ChRIS_ plugins created from this template.

- https://github.com/FNNDSC/pl-dcm2niix (basic command wrapper example)
- <https://github.com/FNNDSC/pl-adapt_object_mesh> (parallelizes a command)
- https://github.com/FNNDSC/pl-mri-preview (uses [NiBabel](https://nipy.org/nibabel/))
- https://github.com/FNNDSC/pl-pyvista-volume (example using Python package project structure and pytest)
- https://github.com/FNNDSC/pl-fetal-cp-surface-extract (has a good README.md)

## What's Inside

| Path                       | Purpose                                                                                                                                                                                                  |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `app.py`                   | Main scrip that runs the registration                                                                                                                                                                    |
| `register.py`              | Registration module that contains registration algorithms                                                                                                                                                |
| `setup.py`                 | [Python project metadata and installation script](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#setup-py)                                                        |
| `requirements.txt`         | List of Python dependencies                                                                                                                                                                              |
| `Dockerfile`               | [Container image build recipe](https://docs.docker.com/engine/reference/builder/)                                                                                                                        |
| `.github/workflows/ci.yml` | "continuous integration" using [Github Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions): automatic testing, building, and uploads to https://chrisstore.co |

## Contributing

The source code for the `main` branch of this repository is on the
[src](https://github.com/fnndsc/python-chrisapp-template/tree/src)
branch, which has an additional file
[`.github/workflows/src.yml`](https://github.com/FNNDSC/python-chrisapp-template/blob/src/.github/workflows/src.yml)
When tests pass, changes are automatically merged into `main`.
Developers should commit to or make pull requests targeting `src`.
Do not push directly to `main`.

This is a workaround in order to do automatic testing of this template
without including the `.github/workflows/src.yml` file in the template itself.

<!-- BEGIN README TEMPLATE

# ChRIS Plugin Title

[![Version](https://img.shields.io/docker/v/fnndsc/pl-appname?sort=semver)](https://hub.docker.com/r/fnndsc/pl-appname)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-appname)](https://github.com/FNNDSC/pl-appname/blob/main/LICENSE)
[![ci](https://github.com/FNNDSC/pl-appname/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/pl-appname/actions/workflows/ci.yml)

`pl-appname` is a [_ChRIS_](https://chrisproject.org/)
_ds_ plugin which takes in ...  as input files and
creates ... as output files.

## Abstract

...

## Installation

`pl-appname` is a _[ChRIS](https://chrisproject.org/) plugin_, meaning it can
run from either within _ChRIS_ or the command-line.

## Local Usage

To get started with local command-line usage, use [Apptainer](https://apptainer.org/)
(a.k.a. Singularity) to run `pl-appname` as a container:

```shell
apptainer exec docker://fnndsc/pl-appname commandname [--args values...] input/ output/
```

To print its available options, run:

```shell
apptainer exec docker://fnndsc/pl-appname commandname --help
```

## Examples

`commandname` requires two positional arguments: a directory containing
input data, and a directory where to create output data.
First, create the input directory and move input data into it.

```shell
mkdir incoming/ outgoing/
mv some.dat other.dat incoming/
apptainer exec docker://fnndsc/pl-appname:latest commandname [--args] incoming/ outgoing/
```

## Development

Instructions for developers.

### Building

Build a local container image:

```shell
docker build -t localhost/fnndsc/pl-appname .
```

### Running

Mount the source code `app.py` into a container to try out changes without rebuild.

```shell
docker run --rm -it --userns=host -u $(id -u):$(id -g) \
    -v $PWD/app.py:/usr/local/lib/python3.12/site-packages/app.py:ro \
    -v $PWD/in:/incoming:ro -v $PWD/out:/outgoing:rw -w /outgoing \
    localhost/fnndsc/pl-appname commandname /incoming /outgoing
```

### Testing

Run unit tests using `pytest`.
It's recommended to rebuild the image to ensure that sources are up-to-date.
Use the option `--build-arg extras_require=dev` to install extra dependencies for testing.

```shell
docker build -t localhost/fnndsc/pl-appname:dev --build-arg extras_require=dev .
docker run --rm -it localhost/fnndsc/pl-appname:dev pytest
```

## Release

Steps for release can be automated by [Github Actions](.github/workflows/ci.yml).
This section is about how to do those steps manually.

### Increase Version Number

Increase the version number in `setup.py` and commit this file.

### Push Container Image

Build and push an image tagged by the version. For example, for version `1.2.3`:

```
docker build -t docker.io/fnndsc/pl-appname:1.2.3 .
docker push docker.io/fnndsc/pl-appname:1.2.3
```

### Get JSON Representation

Run [`chris_plugin_info`](https://github.com/FNNDSC/chris_plugin#usage)
to produce a JSON description of this plugin, which can be uploaded to _ChRIS_.

```shell
docker run --rm docker.io/fnndsc/pl-appname:1.2.3 chris_plugin_info -d docker.io/fnndsc/pl-appname:1.2.3 > chris_plugin_info.json
```

Intructions on how to upload the plugin to _ChRIS_ can be found here:
https://chrisproject.org/docs/tutorials/upload_plugin

END README TEMPLATE -->
