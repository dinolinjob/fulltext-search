# Tap Search  - Full Text Search  (<https://tap-search-dino.herokuapp.com>)
    
## What it Does?

### It takes in multiple paragraphs of text, assigns a unique ID To each paragraph and stores the words to paragraph mappings on an inverted index. This is similar to what elasticsearch does. This paragraph can also be referred to as a ‘document’.

### Given a word to search for, it lists out the top 10 paragraphs in which the word is present.

## Constraints Check list

- [x] Tokenize to words by splitting at whitespace
- [x] Convert all words to lowercase
- [x] TIndex these words against the documents they are from.
- [x] Generate a unique ID for every document that is index.
- [x] A paragraph is defined by two newline characters

## Features

1. clear - Clear the index and all indexed documents.

2. index - Index a given document (After having split the input into paragraphs a.k.a document ).

3. Search - Given a word, search for it and retrieve the top 10 paragraphs (Documents) that contain it.

## Local Installation 

## Steps

* **Step 0** - Clone the Tap search repository and ```cd ``` into the directory.
```sh
git clone https://github.com/dinolinjob/tap-search-dino.git
cd tap-search-dino
```
* **Step 1** - Open a terminal and enter the following commands to setup a virtual environment

```sh
sudo apt-get install python3.
virtualenv -p python3 tap_venv
. tap_venv/bin/activate
```
* **Step 2** - Now to install the dependencies using pip, type

```sh
pip3 install -r requirements.txt
```
#### Dependencies in requirements.txt

* Click==7.0
* Flask==1.1.1
* gunicorn==20.0.3
* itsdangerous==1.1.0
* Jinja2==2.10.3
* MarkupSafe==1.1.1
* Werkzeug==0.16.0

* **Step 3** - To run the application, type

```
python app.py
```
* **Step 4** - Go to `localhost:5000` in your web browser to see the application live.

## Tap Search Demo

![demo](tap.gif)
