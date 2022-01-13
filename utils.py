# -*- coding: utf-8 -*-

import requests
import json
import logging

FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    logging.debug(text)


def get_province_options():
    url = "https://api.opencovid.ca/other?stat=prov"
    response = requests.get(url)
    logging.info("API query to get province list\nurl: {}\nReturn status code: {}".format(
        url, response.status_code))

    if response.status_code is not 200:
        return []
    response_json = response.json()
    result_dict_list = [
        {  # injecting a value for location 'canada'
            "label": "Canada",
            "value": 'canada'
        }
    ]
    for prov in response_json["prov"]:
        result_dict = {}
        result_dict["label"] = prov["province_full"]
        result_dict["value"] = prov["province_short"]
        result_dict_list.append(result_dict)
    return result_dict_list


def get_regions_options(province):
    result_dict_list = [
        {
            # injecting a value to indicate that data can be queried
            # for the entire provice
            "label": "All Regions",
            "value": 0
        }
    ]
    if str(province) == "ALL":
        return result_dict_list

    url = "https://api.opencovid.ca/other?stat=hr"
    response = requests.get(url)
    logging.info("API query to get health regions list\nurl: {}\nReturn status code: {}".format(
        url, response.status_code))
    if response.status_code is not 200:
        return result_dict_list
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
    url = "https://api.opencovid.ca/summary?loc={}&date={}".format(
        location, date)
    response = requests.get(url)
    logging.info("API query to get summary data\nurl: {}\nReturn status code: {}".format(
        url, response.status_code))
    if response.status_code is not 200:
        return {"summary": []}
    response_json = response.json()
    return response_json


def get_summary_dict_value(summary_base_dict, key):
    summary_dict = summary_base_dict["summary"][0]
    if key not in summary_dict:
        return "___"
    return summary_dict[key]
