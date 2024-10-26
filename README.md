# GitOps Configserver

[![gitops-configserver Test](https://github.com/pprzetacznik/gitops-configserver/actions/workflows/test.yml/badge.svg)](https://github.com/pprzetacznik/gitops-configserver/actions/workflows/test.yml)

Inspired by puppet, kustomized and GitOps practices.

## Planned features

* multitenant templates
* hieradata variables
* flask rest service

## Usage

```
$ python -m gitops_server.cli config_gen -h
usage: cli.py config_gen [-h] --config_dir CONFIG_DIR

options:
  -h, --help            show this help message and exit
  --config_dir CONFIG_DIR
                        Config directory
```
