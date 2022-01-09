import requests
import json


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def get_province_list():
    prov_query_url = "https://api.opencovid.ca/other?stat=prov"
    response = requests.get(prov_query_url)
    print("Querying province list. Return status code: {}".format(
        response.status_code))
    if response.status_code is not 200:
        return []  # TODO
    response_json = response.json()
    result_dict_list = []
    for prov in response_json["prov"]:
        result_dict = {}
        result_dict["label"] = prov["province_full"]
        result_dict["value"] = prov["province_short"]
        result_dict_list.append(result_dict)
    return result_dict_list

def get_regions_options(province):
    hr_query_url = "https://api.opencovid.ca/other?stat=hr"
    response = requests.get(hr_query_url)
    print("Querying Health Regions list. Return status code: {}".format(
        response.status_code))
    if response.status_code is not 200:
        return []  # TODO
    response_json = response.json()
    result_dict_list = []
    for region in response_json["hr"]:
        if region["province_short"] != str(province):
            continue
        result_dict = {}
        result_dict["label"] = region["health_region_esri"]
        result_dict["value"] = region["HR_UID"]
        result_dict_list.append(result_dict)
    return result_dict_list

