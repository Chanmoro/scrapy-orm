from typing import List

from orator import DatabaseManager
from orator import Model

from database import settings

db = DatabaseManager(settings.DATABASES)
Model.set_connection_resolver(db)


def generate_model_class(model_name: str, columns: List[str], table_name: str = None):
    """
    Generate make_item.py model class in dynamically.
    :param model_name:
    :param columns:
    :return:
    """
    cls = type(model_name, (Model,), {'__fillable__': columns, '__table__': table_name})
    return cls
