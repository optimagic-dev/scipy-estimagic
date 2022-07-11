"""Test that the environment is correctly installed."""
from distutils.spawn import find_executable


def is_installed(executable):
    return bool(find_executable(executable))


# ======================================================================================
# Check Installations
# ======================================================================================

required_estimagic_version = "0.4.0"

try:
    import estimagic  # noqa: F401
except ModuleNotFoundError:
    msg = (
        "\n\nestimagic is not installed. Please install it via "
        f"'conda install -c conda-forge estimagic=={required_estimagic_version}'"
    )
    raise ModuleNotFoundError(msg)  # noqa: TC200

from estimagic import __version__  # noqa: E402

if required_estimagic_version not in __version__:
    msg = (
        f"You've installed estimagic version {__version__}, but we require version"
        f"{required_estimagic_version}"
    )
    raise Exception(msg)  # noqa: TC002

from estimagic.config import IS_DFOLS_INSTALLED  # noqa: E402
from estimagic.config import IS_PYGMO_INSTALLED  # noqa: E402
from estimagic.config import IS_PYBOBYQA_INSTALLED  # noqa: E402
from estimagic.config import IS_NLOPT_INSTALLED  # noqa: E402
from estimagic.config import IS_FIDES_INSTALLED  # noqa: E402
from estimagic.config import IS_JAX_INSTALLED  # noqa: E402

not_installed = []

if not is_installed("jupyter"):
    not_installed.append(("jupyter", "conda"))

if not IS_NLOPT_INSTALLED:
    not_installed.append(("nlopt", "conda"))

if not IS_JAX_INSTALLED:
    not_installed.append(("jax", "conda"))

if not IS_PYGMO_INSTALLED:
    not_installed.append(("pygmo", "conda"))

if not IS_FIDES_INSTALLED:
    not_installed.append(("fides", "pip"))

if not IS_DFOLS_INSTALLED:
    not_installed.append(("DFO-LS", "pip"))

if not IS_PYBOBYQA_INSTALLED:
    not_installed.append(("Py-BOBYQA", "pip"))

try:
    import jaxopt  # noqa: E402, F401
except ModuleNotFoundError:
    not_installed(("jaxopt", "pip"))


# ======================================================================================
# Raise Error
# ======================================================================================

not_installed_conda = [pkg for pkg, pkg_mng in not_installed if pkg_mng == "conda"]
not_installed_pip = [pkg for pkg, pkg_mng in not_installed if pkg_mng == "pip"]


msg = "The following packages are missing and need to be installed via:"

if not_installed_conda:
    msg += f"\nconda: {not_installed_conda}."

if not_installed_pip:
    msg += f"\npip: {not_installed_pip}."

if not_installed_conda or not_installed_pip:
    raise ModuleNotFoundError(msg)
else:
    print("\nYour installation is working!!!\n")  # noqa: T201
