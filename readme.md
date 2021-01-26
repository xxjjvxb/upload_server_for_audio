
# Upload server for audio file
Only pcm and wav files are supported.

## Usage
### install python3 and pip3 
Install python3 and  pip3.
```bash
sudo apt-get install python3 python3-pip
```

### Make virtualenv 
```bash
python3 -m virtualenv venv
source venv/bin/activate
```

### Run server
```bash
pip install flask scipy numpy
python dump_server.py
```

### Upload file
```bash
curl -X POST http://localhost:2193/dump -H "Api-Key:YWRtaW46YnJhMW5zb2Z0ZG90YSE=" -F file=@sample.wav
```

