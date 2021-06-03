import os
import yaml
from pydantic import BaseModel
from typing import Optional


class Config(BaseModel):
    level1: Optional[str] = None
    level2: Optional[str] = None
    level3: Optional[str] = None
    level4: Optional[str] = None
    level5: Optional[str] = None


def change_config(config):
    with open(os.path.join(os.path.dirname(__file__), 'color_config.yaml')) as f:
        color_data = yaml.safe_load(f)


