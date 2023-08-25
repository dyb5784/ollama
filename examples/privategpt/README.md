# PrivateGPT with Llama 2 uncensored

https://github.com/jmorganca/ollama/assets/3325447/20cf8ec6-ff25-42c6-bdd8-9be594e3ce1b

> Note: this example is a slightly modified version of PrivateGPT using models such as Llama 2 Uncensored. All credit for PrivateGPT goes to Iván Martínez who is the creator of it, and you can find his GitHub repo [here](https://github.com/imartinez/privateGPT).

### Setup

Set up a virtual environment (optional):

```
python3 -m venv .venv
source .venv/bin/activate
```

Install the Python dependencies:

```shell
pip install -r requirements.txt
### Win 10/11: if hnswlib wheels issue need MS C++ build tools and SDK see  https://stackoverflow.com/questions/73969269/error-could-not-build-wheels-for-hnswlib-which-is-required-to-install-pyprojec
```
If you get error "Detecting C compiler ABI info - failed"
first run
```
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
```
the pip3 install -r requirements.txt

if you get "This error might have occurred since this system does not have Windows Long Path support enabled."
open PS as admin and enable long path 
```
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

If you get a validation error for the model and path and checksum is correct, downgrade gpt4all to v 0.2.3 https://github.com/imartinez/privateGPT/issues/691
```
pip3 install --upgrade gpt4all==0.2.3 
```


if you get "warning: Unable to connect optimized C data functions [No module named '_testbuffer'], falling back to pure Python #723" https://github.com/imartinez/privateGPT/issues/723#issuecomment-1597372760
downgrade clickhouse-connect to v 0.5.22
```
pip install --upgrade clickhouse-connect==0.5.22
```

To check the MD5 hash of your models (eg for ggml-gpt4all-j-v1.3-groovy.bin MD5 it's 81a09a0ddf89690372fc296ff7f625af ) https://raw.githubusercontent.com/nomic-ai/gpt4all/main/gpt4all-chat/metadata/models.json
----
Pull the model you'd like to use:

```
ollama pull llama2-uncensored
```

### Getting WeWork's latest quarterly earnings report (10-Q)

```
mkdir source_documents
curl https://d18rn0p25nwr6d.cloudfront.net/CIK-0001813756/975b3e9b-268e-4798-a9e4-2a9a7c92dc10.pdf -o source_documents/wework.pdf
```

### Ingesting files

```shell
python ingest.py
```

Output should look like this:

```shell
Creating new vectorstore
Loading documents from source_documents
Loading new documents: 100%|██████████████████████| 1/1 [00:01<00:00,  1.73s/it]
Loaded 1 new documents from source_documents
Split into 90 chunks of text (max. 500 tokens each)
Creating embeddings. May take some minutes..
Using embedded DuckDB with persistence: data will be stored in: db
Ingestion complete! You can now run privateGPT.py to query your documents
```

### Ask questions

```shell
python privateGPT.py

Enter a query: How many locations does WeWork have?

> Answer (took 17.7 s.):
As of June 2023, WeWork has 777 locations worldwide, including 610 Consolidated Locations (as defined in the section entitled Key Performance Indicators).
```

### Try a different model:

```
ollama pull llama2:13b
MODEL=llama2:13b python privateGPT.py
```

## Adding more files

Put any and all your files into the `source_documents` directory

The supported extensions are:

- `.csv`: CSV,
- `.docx`: Word Document,
- `.doc`: Word Document,
- `.enex`: EverNote,
- `.eml`: Email,
- `.epub`: EPub,
- `.html`: HTML File,
- `.md`: Markdown,
- `.msg`: Outlook Message,
- `.odt`: Open Document Text,
- `.pdf`: Portable Document Format (PDF),
- `.pptx` : PowerPoint Document,
- `.ppt` : PowerPoint Document,
- `.txt`: Text file (UTF-8),
