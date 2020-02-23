# artstation-crawler
A crawler retrieving pictures from a certain web page using their search terms.

## Note
This a public version of a private project which is only supposed fill my GitHub page. 
For several reasons only the private version is functional.

## Usage
First, write the paths of the target directory for the pictures and the directory of the log file into `config.json`. Make sure to use `\\` if using Windows as path seperator. <br>
Example: you want to have 150 images of a cityscape at night, then your command will be
```sh
python main.py --search-terms cityscape night --number-pictures 150
```
or
```
python main.py -s cityscape night -n 150
```
for short.

## Parameters
* `--search-terms`, `-s`: Required: the search terms with pictures will be 
searched for.
* `--number-pictures`, `-n`: Required: the number of pictures you want to 
download.

## Dependencies
Take a look at the `requirements.txt` if you want to create an environment with conda.
* Python 2.7
* Splinter brower
    * Take a look at https://splinter.readthedocs.io/en/latest/install.html
    * Using `geckodriver.exe` which has to be put into source directory of Python
* `bs4` library (BeautifulSoup)
* `Pillow` library
