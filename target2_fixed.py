import json

def load_user_preferences(data_bytes):
    """Loads a user's saved preferences from serialized data."""
    try:
        preferences = json.loads(data_bytes.decode('utf-8'))
        if not isinstance(preferences, dict):
            raise ValueError("Preferences must be a dictionary")
        return preferences
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON data") from e