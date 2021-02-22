__all__ = ["get_data_filename"]

import os
import pkg_resources


def get_data_filename(filename):
    return pkg_resources.resource_filename(
        __name__, os.path.join("data", filename)
    )
