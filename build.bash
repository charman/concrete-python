#!/bin/bash

#
# Copyright 2012-2014 Johns Hopkins University HLTCOE. All rights reserved.
# This software is released under the 2-clause BSD license.
# See LICENSE in the project root directory.
#

#
# THIS SCRIPT SHOULD ONLY BE RUN BY PACKAGE MAINTAINERS.
# If you are not a package maintainer, then you can safely ignore this
# script - all the information you need to use the Concrete-Python
# library can be found in README.md
#
#
# THIS SCRIPT DOES NOT FULLY AUTOMATE THE BUILD PROCESS.
# This script uses the Thrift compiler to generate the Python classes
# from the .thrift definition files.  It then applies a set of required
# modifications to the generated Python classes.  However, these
# changes are not "intelligent"; e.g., if a new field is added, the
# corresponding hash function will need to be updated manually and the
# patch will need to be regenerated.
#
# The Concrete-Thrift repository contains the .thrift definition
# files, but not the Python classes generated by the Thrift compiler.
# This repository (Concrete-Python) contains the Thrift-generated
# Python classes, but not the .thrift definition files.
#
# This script should be run whenever the .thrift definition files in the
# Concrete-Thrift repository are changed.


print_usage() {
    echo "Usage: $0 [--raw] /path/to/concrete/thrift"
    echo "  --raw:  Just generate classes from thrift definitions"
    echo "          (do not apply our modifications)"
}


#
# Parse command-line arguments
#

raw=false

while [ $# -gt 0 ]
do
    case "$1" in
        --raw)
            raw=true
            ;;
        -h)
            print_usage
            exit 0
            ;;
        --help)
            print_usage
            exit 0
            ;;
        *)
            if [ -z "$thrift_path" ]
            then
                thrift_path="$1"
            else
                print_usage >&2
                exit 1
            fi
            ;;
    esac
    shift
done

if [ -z "$thrift_path" ]
then
    print_usage >&2
    exit 1
fi


set -e

echo 'Generating Python classes from thrift definitions...'
for P in `find $1 -name '*.thrift'`
do
    thrift --gen py:new_style,utf8strings $P
done

echo 'Deleting extraneous generated files...'
rm -f gen-py/__init__.py

echo 'Copying newly-generated classes to concrete/...'
cp -a gen-py/concrete/* concrete/

if ! $raw
then
    echo 'Applying our modifications to generated classes...'
    for P in patches/*.patch
    do
        patch -d concrete -p1 < $P
    done
fi

echo 'Done.'