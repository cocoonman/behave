# -*- coding: utf-8 -*-
"""
Deprecated module. Functionality was split-up into:

  * behave.formatter._registry  (generic core functionality)
  * behave.formatter._builtins  (registration of known, builtin formatters)

.. since:: 1.2.5a1
    Deprecated, use "behave.formatter._registry" or "behave.formatter._builtin".
"""

from behave.formatter import _registry
import warnings

warnings.simplefilter("once", DeprecationWarning)
warnings.warn("Use 'behave.formatter._registry' instead.", DeprecationWarning)

# -----------------------------------------------------------------------------
# FORMATTER REGISTRY:
# -----------------------------------------------------------------------------
def register_as(formatter_class, name):
    """
    Register formatter class with given name.

    :param formatter_class:  Formatter class to register.
    :param name:  Name for this formatter (as identifier).
    """
    warnings.warn("Use behave.formatter._registry.register_as() instead.",
                  warnings.DeprecationWarning)
    _registry.register_as(name, formatter_class)


def register(formatter_class):
    register_as(formatter_class, formatter_class.name)


def get_formatter(config, stream_openers):
    warnings.warn("Use make_formatters() instead", DeprecationWarning)
    return _registry.make_formatters(config, stream_openers)


# -----------------------------------------------------------------------------
# SETUP:
# -----------------------------------------------------------------------------
def setup_formatters():
    warnings.warn("Use behave.formatter._builtins instead", DeprecationWarning)
    from behave.formatter import _builtins
    _builtins.setup_formatters()


# -----------------------------------------------------------------------------
# MODULE-INIT:
# -----------------------------------------------------------------------------
# DISABLED: setup_formatters()
