from pathlib import Path
import requests
from tqdm import tqdm

def download_from_sciebo(public_url, to_filename, is_file = True):
    """
    Downloads a file or folder from a shared URL on Sciebo.
    """
    # Create the folder if a longer path was described
    path = Path(to_filename)
    if len(path.parts) > 1:
        Path(to_filename).parent.mkdir(parents=True, exist_ok=True)
    r = requests.get(public_url + "/download", stream=True)
    progress_bar = tqdm(desc=f"Downloading {to_filename}", unit='B', unit_scale=True, total=int(r.headers['Content-Length'])) if is_file else tqdm()
    with open(to_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
            progress_bar.update(len(chunk))