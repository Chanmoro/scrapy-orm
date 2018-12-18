import os
import yaml

# Load databases setting from orator.yml
_self_path = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_self_path, 'orator.yml')) as f:
    yaml_data = yaml.load(f)

DATABASES = yaml_data['databases']
