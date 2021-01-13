#!/usr/bin/python3
import requests
import json

## uncomment this import if you run in a GUI
## and want to open the URL in a browser
## import webbrowser

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    ## Define creds
    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()
        
    ## remove any "extra" new line feeds on our key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    
    # Based off of date
    searchdate = input("Type search date in YYYY-MM-DD format")

    ## Call the webservice with our key
    apod = requests.get(NASAAPI + nasacreds + "&date=" + searchdate).json()
    print(NASAAPI + nasacreds + "date=" + searchdate)
    ## read the file-like object
    ## apodread = apodurlobj.read()
    
    ## decode JSON to Python data structure
    ## apod = json.loads(apodread.decode("utf-8"))
    
    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(apod)

    print()
    
    ## Uncomment the code below if running in a GUI
    ## and you want to open the URL in a browser
    ## use Firefox to open the HTTPS URL
    ## input("\nPress Enter to open NASA Picture of the Day in Firefox")
    ## webbrowser.open(decodeapod["url"])
if __name__ == "__main__":
    main()

