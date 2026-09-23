#!/usr/bin/env bash
set -euo pipefail

RELEASE=${1:-rawhide}
IMAGE="docker.io/fedora:${RELEASE}"
CHROOT="fedora-${RELEASE}-x86_64"

docker run --rm -it \
  --privileged \
  -v "${PWD}:/repo" \
  -w /repo \
  "${IMAGE}" bash -c "
set -e
dnf install -y mock rpmdevtools >/dev/null
useradd -G mock builder

su builder -c '
	set -e
	spectool -g --directory /repo /repo/aqua.spec
	mock -r ${CHROOT} --enable-network \
		--spec /repo/aqua.spec \
		--sources /repo \
		--resultdir /repo/.build-output
'
"

echo "Built RPMs are in ${PWD}/.build-output"
