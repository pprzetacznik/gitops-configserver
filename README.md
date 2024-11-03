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
