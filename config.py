import os
from typing import Dict, Optional

import yaml


class Config:
    """
    Configuration manager for the image generator.
    Loads settings from config.yaml and provides defaults.
    """

    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = config_path
        self.settings: Dict = self._load_config()

    def _load_config(self) -> Dict:
        """
        Load configuration from YAML file with defaults.
        """
        defaults = {
            "font": {
                "path": "fonts/arial.ttf",
                "size": 30,
                "color": (255, 255, 255),  # White
            },
            "image": {
                "width": 800,
                "height": 600,
                "background_color": (0, 0, 0),  # Black
            },
            "text": {
                "position": (50, 50),
                "alignment": "left",  # left, center, right
            },
            "output": {
                "directory": "output",
                "format": "PNG",  # PNG, JPEG, etc.
            },
        }

        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    user_config = yaml.safe_load(f)
                return self._merge_configs(defaults, user_config)
            except yaml.YAMLError as e:
                raise RuntimeError(f"Failed to parse config file: {e}")
        else:
            return defaults

    def _merge_configs(self, defaults: Dict, user_config: Dict) -> Dict:
        """
        Recursively merge user configuration with defaults.
        """
        merged = defaults.copy()
        for key, value in user_config.items():
            if isinstance(value, dict) and key in merged and isinstance(merged[key], dict):
                merged[key] = self._merge_configs(merged[key], value)
            else:
                merged[key] = value
        return merged

    def get(self, key: str, default=None):
        """
        Get a configuration value with dot notation.
        Example: get('font.size')
        """
        keys = key.split(".")
        value = self.settings
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

    def validate(self) -> None:
        """
        Validate critical configuration settings.
        """
        required_fonts = self.get("font.path")
        if not os.path.isfile(required_fonts):
            raise FileNotFoundError(f"Font file not found: {required_fonts}")

        output_dir = self.get("output.directory")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)


# Singleton instance for easy access
config = Config()