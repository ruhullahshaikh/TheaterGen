from models import sam

sam_model_dict = sam.load_sam()
if sam_model_dict:
    print("SAM Model and Processor loaded successfully.")
else:
    print("Failed to load SAM Model or Processor.")
