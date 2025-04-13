from datasets import load_dataset

# Load the dataset
dataset = load_dataset('divaroffical/real_estate_ads')

# Save the dataset to a local directory
local_directory = '/home/ali/ProgrammingProjects/divar_data_hawk'
dataset.save_to_disk(local_directory)

print(f"Dataset saved to {local_directory}")