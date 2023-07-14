from database import questions, options


def preprocess_data():
    return dict(zip(questions, options))
