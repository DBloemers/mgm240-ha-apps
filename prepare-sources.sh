#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
source sources.lock

work_dir=$(mktemp -d)
trap 'rm -rf "$work_dir"' EXIT

checkout() {
    local repo="$1" revision="$2" path="$work_dir/$1"
    git init -q "$path"
    git -C "$path" fetch --depth 1 "https://github.com/DBloemers/${repo}.git" "$revision"
    git -C "$path" checkout --quiet --detach FETCH_HEAD
}

checkout esphome "$ESPHOME_REV"
checkout device-builder "$DEVICE_BUILDER_REV"
python3 package_sources.py "$work_dir"
