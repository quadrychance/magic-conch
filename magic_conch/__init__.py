from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution(__name__).version

except DistributionNotFound:
    pass  # package is not installed

else:
    __all__ = ["get_data_filename"]

    from .load_data import get_data_filename
