import pandas as pd

chunk_size = 10  # Size of each chunk
chunks = []

for chunk in pd.read_csv('note/discharge.csv', chunksize=chunk_size):
    # Process each chunk here
    chunks.append(chunk)  # Example: appending the chunk to a list
    break

chunks[0].to_csv('subsample_10.csv', index=False)
# Optionally, concatenate chunks back into a single DataFrame
# df = pd.concat(chunks, axis=0)