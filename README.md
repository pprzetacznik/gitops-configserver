# GitOps Configserver

[![gitops-configserver Release](https://github.com/pprzetacznik/gitops-configserver/actions/workflows/release.yml/badge.svg)](https://github.com/pprzetacznik/gitops-configserver/actions/workflows/release.yml)
[![gitops-configserver Test](https://github.com/pprzetacznik/gitops-configserver/actions/workflows/test.yml/badge.svg)](https://github.com/pprzetacznik/gitops-configserver/actions/workflows/test.yml)
[![PyPI version](https://badge.fury.io/py/gitops-configserver.svg)](https://pypi.org/project/gitops-configserver/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gitops-configserver)](https://pypi.org/project/gitops-configserver/)
[![Documentation Status](https://readthedocs.org/projects/gitops-configserver/badge/?version=latest)](https://gitops-configserver.readthedocs.io/en/latest/?badge=latest)

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

Example target repository:
* see `config` directory for example configuration with templates,
* https://github.com/pprzetacznik/gitops-configserver-tests

```
$ python -m gitops_server.cli server --config_dir=config
...
$ curl http://localhost:8002/configs
{"tenants":["tenant1"]}
```

## Setting up GitHub tokens

* Go to Setting -> Developer Settings -> Fine-grained personal access tokens
* Create a token with following settings:
  * `Only select repositories` and select your repository
  * `Repository permissions` and select `Content`

Set the token as `$GH_PAT` in your local environment.

## Publish new release

```
$ git tag v1.0
$ git push origin v1.0
```
