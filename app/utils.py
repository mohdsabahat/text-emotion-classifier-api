import pickle


def load_model(model_path):

    pickled_model = pickle.load(open(model_path, 'rb'))

    return pickled_model
