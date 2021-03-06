"""
YAML-configurable Pandas pipelines.
"""

import os

from confuse import LazyConfig

# get config from environment variable or look in cwd by default
ENV_KEY = "PDPIPEWRENCHDIR"
CONFIG_FILENAME = "config.yaml"
if not os.getenv(ENV_KEY):
    os.environ[ENV_KEY] = os.getcwd()
CONFIG_FOLDERPATH = os.environ[ENV_KEY]
CONFIG = LazyConfig("Pdpipewrench", __name__)

from .pdpipewrench import Source, Sink, Line  # noqa: E402, F401
