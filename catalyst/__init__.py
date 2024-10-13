"Catalyst is the release building tool used by Gentoo Linux"

__maintainer__ = "Catalyst <catalyst@gentoo.org>"

try:
    from .verinfo import version as fullversion

    __version__ = fullversion.split("\n")[0].split()[1]
except ImportError:
    from .version import __version__, get_version

    fullversion = get_version(reset=True)
