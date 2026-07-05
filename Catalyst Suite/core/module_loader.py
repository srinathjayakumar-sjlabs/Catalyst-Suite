"""
=========================================================
CATALYST Suite
File      : module_loader.py
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : Registers and manages application modules
=========================================================
"""

# =========================================================
# MODULE LOADER
# =========================================================

class ModuleLoader:

    def __init__(self):

        # Dictionary to store all registered modules
        self._modules = {}

    # -----------------------------------------------------

    def register_module(self, module_id, module_info):
        """
        Register a module.
        """

        self._modules[module_id] = module_info

    # -----------------------------------------------------

    def get_module(self, module_id):
        """
        Return a module by ID.
        """

        return self._modules.get(module_id)

    # -----------------------------------------------------

    def list_modules(self):
        """
        Return all registered modules.
        """

        return self._modules