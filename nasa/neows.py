#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")

    ## update the date below, if you like
    start_date = "start_date=" + input("Enter start date. Format = 'YYYY-MM-DD'")
    end_date = "end_date=" + input("If you'd like to enter an end_date enter it now, otherwise press enter to continue")

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    if end_date == "end_date=":
        neowrequest = requests.get(NEOURL + start_date + "&" + nasacreds)
    else:
        neowrequest = requests.get(NEOURL + start_date + "&" + end_date + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()
