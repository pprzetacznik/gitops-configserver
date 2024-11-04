#!/bin/bash

set -xeuo pipefail

ACTION=${1:-config_gen}

function generate_version () {
  VERSION=($(cat VERSION | tr '.' '\n'))
  echo "${VERSION[0]}.${VERSION[1]}.$(date '+%Y%m%d%H%M%S')" > VERSION
}

case $ACTION in
  generate_version)
    generate_version
    ;;
  config_gen)
    python -m gitops_configserver.cli config_gen --config_dir=config
    ;;
  server)
    python -m gitops_configserver.cli server --config_dir=config
    ;;
esac
