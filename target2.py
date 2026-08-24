import pickle

def load_user_preferences(data_bytes):
    """Loads a user's saved preferences from serialized data."""
    preferences = pickle.loads(data_bytes)
    return preferences
