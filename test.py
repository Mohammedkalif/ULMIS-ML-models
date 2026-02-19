import kagglehub

# Download latest version
path = kagglehub.dataset_download("tea340yashjoshi/sepsis-prediction-dataset")

print("Path to dataset files:", path)