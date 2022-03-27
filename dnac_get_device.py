#!/usr/bin/env python3
#Colin Coyne
#Generate list of devices within DNA Center

#Import modules
import json
import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth

#Base URL
BASE_URL = "https://sandboxdnac.cisco.com"

#Credentials
username = input("Please enter in the username: ")
password = getpass("Please enter in the password: ")

#Generate token
token_url = BASE_URL + "/dna/system/api/v1/auth/token"
token_request_payload = {}
token_request_headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}
token_request = requests.post(token_url, auth=HTTPBasicAuth(username, password), headers=token_request_headers, data = token_request_payload)
token_json = token_request.json()
TOKEN = token_json['Token']

#Generate list of devices
devicelist_url = BASE_URL + "/dna/intent/api/v1/network-device"
devicelist_request_payload = {}
devicelist_request_headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-Auth-Token': TOKEN
}
devicelist_request = requests.get(devicelist_url, headers=devicelist_request_headers, data = devicelist_request_payload)

#Print out device list
print("Device list API resonse:")
print(devicelist_request.text)
