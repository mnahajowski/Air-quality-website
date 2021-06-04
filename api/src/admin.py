import os
import yaml
from pydantic import BaseModel
from typing import Optional, List


class Config(BaseModel):
    level1: Optional[List[int]] = None
    level2: Optional[List[int]] = None
    level3: Optional[List[int]] = None
    level4: Optional[List[int]] = None
    level5: Optional[List[int]] = None


def change_config(config):
    config = config.dict()
    file_path = os.path.join(os.path.dirname(__file__), 'color_config.yaml')
    with open(file_path) as f:
        color_data = yaml.safe_load(f)

    for param in color_data:
        for index, threshold in enumerate(sorted(color_data[param].keys()), start=1):
            if config.get(f'level{index}'):
                color_data[param][threshold] = config[f'level{index}'].copy()

    with open(file_path, 'w') as f:
        yaml.safe_dump(color_data, f, default_flow_style=False)


def get_config():
    file_path = os.path.join(os.path.dirname(__file__), 'color_config.yaml')
    with open(file_path) as f:
        color_data = yaml.safe_load(f)

    for config in color_data.values():
        return dict(enumerate(config.values(), start=1))
