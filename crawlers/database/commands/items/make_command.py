import os

import inflection
from orator.commands.models.make_command import ModelMakeCommand

from .stubs import MODEL_DEFAULT_STUB


class ItemMakeCommand(ModelMakeCommand):
    """
    Creates a new Scrapy Item class.
    make:item
        {name : The name of the model to create.}
        {--m|migration : Create a new migration file for the model.}
        {--p|path= : Path to models directory}
    """

    def _get_stub(self):
        """
        Get the model stub template

        :rtype: str
        """
        return MODEL_DEFAULT_STUB

    def _populate_stub(self, name, stub):
        """
        Populate the placeholders in the migration stub.

        :param name: The name of the model
        :type name: str

        :param stub: The stub
        :type stub: str

        :rtype: str
        """
        table_name = inflection.tableize(name)
        stub = stub.replace("DummyClass", name).replace("dummy_table", table_name)

        return stub

    def _get_path(self, name=None):
        if self.option("path"):
            directory = self.option("path")
        else:
            directory = os.path.join(os.getcwd(), "items")

        if name:
            return os.path.join(directory, name)

        return directory
