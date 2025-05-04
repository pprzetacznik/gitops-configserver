#!/bin/bash

set -xeuo pipefail

ENVIRONMENT=dev
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
  template_gen)
    python -m gitops_configserver.cli \
      template_gen \
      --config_dir=resources/test_config \
      --tenant_name=tenant2 \
      --template_name=build_variants.yaml \
      --facts='{"environment": "test"}'
    ;;
esac
