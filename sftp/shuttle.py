from datetime import datetime, timedelta
import requests
import os
import io

def newest_files(directory: str):
    files = []
    for root, _dirs, filenames in os.walk(directory):
        for name in filenames:
            full_path = os.path.join(root, name)
            file_time = os.path.getmtime(full_path)
            if name.startswith('.') or name in ['Thumbs.db', 'desktop.ini']:
                pass
            else:
                files.append((full_path, file_time))
    files.sort(key=lambda x: x[1])
    newest_file = files[0]
    return newest_file[0]

def send_file(file_path: str):
    with open(file_path, 'rb') as contents:
        file_bytes = io.BytesIO(contents.read())
        file_bytes.seek(0)

    file_name = file_path.split('/')[-1]
    post_params = {
        'file_name': file_name,
        'uploaded_at': datetime.utcfromtimestamp(os.stat(file_path).st_mtime).isoformat(),
    }
    file = {
        'file': file_bytes
    }
    print(file, post_params)
    r = requests.post(
        'http://34.220.204.122:5000/upload',
        params=post_params,
        files=file,
    )
    return r.status_code

new_file = newest_files('/home/hello/here')
return_code = send_file(new_file)
if return_code == 200:
    print('Successfully sent', new_file)
