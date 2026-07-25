import re
import ast

class Kite:
    def __init__(self, filepath="base.kite"):
        self._data = {}
        if filepath:
            self.load(filepath)

    def load(self, filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("//") or line.startswith("#"):
                    continue

                bracket_match = re.match(r'^kite\["([^"]+)"\]\s*=\s*(.+)$', line)
                if bracket_match:
                    key, raw_value = bracket_match.groups()
                    self._data[key] = self._parse_value(raw_value)
                    continue

                dot_match = re.match(r'^kite\.([a-zA-Z0-9_]+)\s*=\s*(.+)$', line)
                if dot_match:
                    key, raw_value = dot_match.groups()
                    parsed_value = self._parse_value(raw_value)
                    self._data[key] = parsed_value
                    setattr(self, key, parsed_value)

    def _parse_value(self, value_string):
        value_string = value_string.strip()
        if (value_string.startswith('"') and value_string.endswith('"')) or (value_string.startswith("'") and value_string.endswith("'")):
            return value_string[1:-1]
        try:
            return ast.literal_eval(value_string)
        except (ValueError, SyntaxError):
            return value_string

    def __getitem__(self, key):
        return self._data.get(key, None)

kite = Kite("base.kite")
