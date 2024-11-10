import pickle
import os

model_path = "notebook\artifacts\Linear.pkl"

# Check if the model file exists before loading
if os.path.exists(model_path):
    try:
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
    except pickle.UnpicklingError:
        print("Error: The file is not a valid pickle file or is corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
else:
    print(f"Model file not found at: {model_path}")
