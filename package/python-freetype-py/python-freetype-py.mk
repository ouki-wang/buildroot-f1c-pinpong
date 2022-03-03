################################################################################
#
# python-freetype-py
#
################################################################################

PYTHON_FREETYPE_PY_VERSION = 2.1.0
PYTHON_FREETYPE_PY_SOURCE = freetype-py-2.1.0.tar.gz
PYTHON_FREETYPE_PY_SITE = https://files.pythonhosted.org/packages/9b/3e/cd9c2a46e9cb8b70988df3e636db7525e752288aca610ec7289b925c42aa
PYTHON_FREETYPE_PY_LICENSE = BSD-3-Clause
PYTHON_FREETYPE_PY_LICENSE_FILES = LICENSE
PYTHON_FREETYPE_PY_SETUP_TYPE = setuptools

$(eval $(python-package))
