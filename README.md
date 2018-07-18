# jvn-doc-summarization usage

0. Download pretrain fasttext word vectors:
```console
foo@bar:~$ cd jvn_doc_summarization/ 
foo@bar:~$ mkdir files 
foo@bar:~$ wget https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.vi.vec
```

1. Make sure python3 is installed on your system

2. Create new virtual environment and activate it:

```console
foo@bar:~$ virtualenv -p python3 env
foo@bar:~$ source env/bin/activate
```

3. Install required libraries:

```console
foo@bar:~/jvn_doc_summarization/$ pip install -r requirements.txt
```

3. To run the program:

```console
foo@bar:~$ python app.py <path-to-your-input-file> <path-to-desired-ouput-file>
```

For example, in "files" directory from the source, we have attached 2 files - one is the vector model file (wiki.en.vec) and the remain is the text file, a sample run:

```console
foo@bar:~/jvn_doc_summarization/$ python app.py files/text.txt files/abstract.txt
```
