import pickle

def load_data(data):
    # Vulnerable: unsafe deserialization
    return pickle.loads(data)
