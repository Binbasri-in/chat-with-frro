# chat-with-frro
A simple chatbot for chatting with FRRO documents for Foreigners in India, I scraped the documents from Foreigners division website and created a RAG


### partition the pdf files using Unstructured library

I have checked the pdf files and they are not very consistant, so I will use the pdf partition function with auto mode so if the text is not extractable then OCR will be performed, so you need to install Full Unstrcutured installation from [here](https://docs.unstructured.io/open-source/installation/full-installation)

Install Unstructured library using pip
```bash
pip install "unstructured[all-docs]"
# or for pdf files only
pip install "unstructured[pdf]"

# then install system dependencies
# tesseract
sudo apt install tesseract-ocr # or brew install tesseract
sudo apt install libtesseract-dev # or brew install tesseract-lang # you will need to set the TESSDATA_PREFIX environment variable to the directory containing the tessdata directory
sudo apt install tesseract-ocr-hin # for support of hindi language

# poppler
sudo apt install poppler-utils # or brew install poppler

# libreoffice
sudo apt install libreoffice # or brew install --cask libreoffice

# pandoc, check the latest version from https://github.com/jgm/pandoc/releases
wget https://github.com/jgm/pandoc/releases/download/3.2.1/pandoc-3.2.1-1-amd64.deb
sudo dpkg -i pandoc-3.2.1-1-amd64.deb

```