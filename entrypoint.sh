#!/bin/bash --login
set -e

conda activate $HOME/ramarapi/env
exec "$@"