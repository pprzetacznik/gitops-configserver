#!/bin/bash

set -xe

python -m gitops_configserver.cli config_gen --config_dir=config
