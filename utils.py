import logging
import requests
import json


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_province_options():
    prov_query_url = "https://api.opencovid.ca/other?stat=prov"
    response = requests.get(prov_query_url)
    print("Querying province list\nurl: {}\nReturn status code: {}".format(
        prov_query_url, response.status_code))
    result_dict_list = [
        {
            "label": "Canada",
            "value": 'canada'
        }
    ]
    if response.status_code is not 200:
        return result_dict_list  # TODO
    response_json = response.json()
    for prov in response_json["prov"]:
        result_dict = {}
        result_dict["label"] = prov["province_full"]
        result_dict["value"] = prov["province_short"]
        result_dict_list.append(result_dict)
    return result_dict_list


def get_regions_options(province):
    result_dict_list = [
        {
            "label": "All Regions",
            "value": 0
        }
    ]
    if str(province) == "ALL":
        return result_dict_list
    hr_query_url = "https://api.opencovid.ca/other?stat=hr"
    response = requests.get(hr_query_url)
    print("Querying Health Regions list\nurl: {}\nReturn status code: {}".format(
        hr_query_url, response.status_code))
    if response.status_code is not 200:
        return result_dict_list  # TODO error handling
    response_json = response.json()
    for region in response_json["hr"]:
        if region["province_short"] != str(province):
            continue
        result_dict = {}
        result_dict["label"] = region["health_region_esri"]
        result_dict["value"] = region["HR_UID"]
        result_dict_list.append(result_dict)
    return result_dict_list


def get_summary(location, date):
    # sample: https://api.opencovid.ca/summary?loc=AB&date=01-09-2020
    print("Querying summary for location {} and date {}".format(location, date))
    url = "https://api.opencovid.ca/summary?loc={}&date={}".format(location, date)
    response = requests.get(url)
    if response.status_code is not 200: 
        return {"summary":[]} # TODO error handling
    response_json = response.json()        
    return response_json

def get_summary_dict_value(summary_base_dict, key):
    summary_dict = summary_base_dict["summary"][0]
    if key not in summary_dict:
        return "___"
    return summary_dict[key]