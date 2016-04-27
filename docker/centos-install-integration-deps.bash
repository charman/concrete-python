#!/bin/bash

set -e
set -x

yum install -y \
    gcc \
    make

redis_version=redis-3.0.6
curl http://download.redis.io/releases/${redis_version}.tar.gz | tar -xz
pushd ${redis_version}
make
make install
pushd deps/hiredis
make install
popd
popd
rm -rf ${redis_version}*