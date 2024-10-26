#!/bin/bash

set -xeuo pipefail

ACTION=${1:-config_gen}

case $ACTION in
  config_gen)
    python -m gitops_configserver.cli config_gen --config_dir=config
    ;;
  server)
    python -m gitops_configserver.cli server --config_dir=config
    ;;
esac
