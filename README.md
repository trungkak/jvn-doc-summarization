# jvn-doc-summarization usage

1. Make sure python3 is installed on your system

2. Create new virtual environment and activate it:

```console
foo@bar:~$ virtualenv -p python3 env
foo@bar:~$ source env/bin/activate
```

3. Nagivate to the project:

```console
foo@bar:~$ cd jvn_doc_summarization/
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