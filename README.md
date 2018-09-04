# putty2html
A quick tool to convert Putty logs in HTML while giving some colors to predefined keywords

## Version 1.1
Now, you have a configuration file where you can store the color associated with each keyword (*config/config.ini*)
 
## Basic usage
```bash
python putty2html.py -i <inputfile> -o <outputfile>
```
### Parameters
- inputfile: a text file. Any extension will be fine
- outputfile: a basic **.html** file
### Sample configuration file
- config/config.ini : R, G and B for 3 keywords. Other words are printed in black.

## Perspectives
- Customizable list of keywords
- Other font features (bold, italic)
- Other features (line numbers for instance)
- Is it possible to export the Putty output to a text file from command lines?
