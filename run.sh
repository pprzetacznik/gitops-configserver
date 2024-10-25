#!/bin/bash

set -xe

python -m gitops_mt.cli config_gen --config_dir=config
