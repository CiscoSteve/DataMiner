"""

                           CISCO SAMPLE CODE LICENSE
                                  Version 1.1
                Copyright (c) 2018 Cisco and/or its affiliates

   These terms govern this Cisco Systems, Inc. ("Cisco"), example or demo
   source code and its associated documentation (together, the "Sample
   Code"). By downloading, copying, modifying, compiling, or redistributing
   the Sample Code, you accept and agree to be bound by the following terms
   and conditions (the "License"). If you are accepting the License on
   behalf of an entity, you represent that you have the authority to do so
   (either you or the entity, "you"). Sample Code is not supported by Cisco
   TAC and is not tested for quality or performance. This is your only
   license to the Sample Code and all rights not expressly granted are
   reserved.

   1. LICENSE GRANT: Subject to the terms and conditions of this License,
      Cisco hereby grants to you a perpetual, worldwide, non-exclusive, non-
      transferable, non-sublicensable, royalty-free license to copy and
      modify the Sample Code in source code form, and compile and
      redistribute the Sample Code in binary/object code or other executable
      forms, in whole or in part, solely for use with Cisco products and
      services. For interpreted languages like Java and Python, the
      executable form of the software may include source code and
      compilation is not required.

   2. CONDITIONS: You shall not use the Sample Code independent of, or to
      replicate or compete with, a Cisco product or service. Cisco products
      and services are licensed under their own separate terms and you shall
      not use the Sample Code in any way that violates or is inconsistent
      with those terms (for more information, please visit:
      www.cisco.com/go/terms).

   3. OWNERSHIP: Cisco retains sole and exclusive ownership of the Sample
      Code, including all intellectual property rights therein, except with
      respect to any third-party material that may be used in or by the
      Sample Code. Any such third-party material is licensed under its own
      separate terms (such as an open source license) and all use must be in
      full accordance with the applicable license. This License does not
      grant you permission to use any trade names, trademarks, service
      marks, or product names of Cisco. If you provide any feedback to Cisco
      regarding the Sample Code, you agree that Cisco, its partners, and its
      customers shall be free to use and incorporate such feedback into the
      Sample Code, and Cisco products and services, for any purpose, and
      without restriction, payment, or additional consideration of any kind.
      If you initiate or participate in any litigation against Cisco, its
      partners, or its customers (including cross-claims and counter-claims)
      alleging that the Sample Code and/or its use infringe any patent,
      copyright, or other intellectual property right, then all rights
      granted to you under this License shall terminate immediately without
      notice.

   4. LIMITATION OF LIABILITY: CISCO SHALL HAVE NO LIABILITY IN CONNECTION
      WITH OR RELATING TO THIS LICENSE OR USE OF THE SAMPLE CODE, FOR
      DAMAGES OF ANY KIND, INCLUDING BUT NOT LIMITED TO DIRECT, INCIDENTAL,
      AND CONSEQUENTIAL DAMAGES, OR FOR ANY LOSS OF USE, DATA, INFORMATION,
      PROFITS, BUSINESS, OR GOODWILL, HOWEVER CAUSED, EVEN IF ADVISED OF THE
      POSSIBILITY OF SUCH DAMAGES.

   5. DISCLAIMER OF WARRANTY: SAMPLE CODE IS INTENDED FOR EXAMPLE PURPOSES
      ONLY AND IS PROVIDED BY CISCO "AS IS" WITH ALL FAULTS AND WITHOUT
      WARRANTY OR SUPPORT OF ANY KIND. TO THE MAXIMUM EXTENT PERMITTED BY
      LAW, ALL EXPRESS AND IMPLIED CONDITIONS, REPRESENTATIONS, AND
      WARRANTIES INCLUDING, WITHOUT LIMITATION, ANY IMPLIED WARRANTY OR
      CONDITION OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-
      INFRINGEMENT, SATISFACTORY QUALITY, NON-INTERFERENCE, AND ACCURACY,
      ARE HEREBY EXCLUDED AND EXPRESSLY DISCLAIMED BY CISCO. CISCO DOES NOT
      WARRANT THAT THE SAMPLE CODE IS SUITABLE FOR PRODUCTION OR COMMERCIAL
      USE, WILL OPERATE PROPERLY, IS ACCURATE OR COMPLETE, OR IS WITHOUT
      ERROR OR DEFECT.

   6. GENERAL: This License shall be governed by and interpreted in
      accordance with the laws of the State of California, excluding its
      conflict of laws provisions. You agree to comply with all applicable
      United States export laws, rules, and regulations. If any provision of
      this License is judged illegal, invalid, or otherwise unenforceable,
      that provision shall be severed and the rest of the License shall
      remain in full force and effect. No failure by Cisco to enforce any of
      its rights related to the Sample Code or to a breach of this License
      in a particular situation will act as a waiver of such rights. In the
      event of any inconsistencies with any other terms, this License shall
      take precedence.


Author: Steve Hartman
co=Author: Nick DiNofio
AWS S3 function: Oscar Bustos
Contact: stehartm@cisco.com
Contact: ndinofi@cisco.com
Contact: obustosm@cisco.com
Description:
    This is a sample python script that will extract all the PX Cloud data
for all customers for a single partner. It will gather the JSON data and convert
it to CSV for injecting into any platform that can digest a CSV file.

Reference SDK: https://developer.cisco.com/docs/px-cloud/#!partner-and-customer-data-api

Version Features and enhancements
1. Added progress indicators to the function call to API
2. Removed some counter variables to follow best practice of looping
3. Refactored all variables to follow camelCase naming conventions
4. Moved sensitive config data to a config.ini file
    If no file is found, a template is created automatically in the same folder as the script.
    If no AWS S3 credentials are found within the config.ini file, then S3 uploads are by-passed
5. This version covers the follow API end points: ( * denote code completed for this report)
    A. Customers *
    B. Contracts *
    C. Contract Details *
    E. Partner Offers *
    F. Partner Offer Sessions *
    G. Customer Lifecycle *
    H. Success Tracks *
    I. Customer Data Reports which includes: ( * denotes code is completed for this report in this version)
        A. Assets *
        B. Hardware *
        C. Software *
        D. Security Advisories *
        E. Field Notices *
        F. Priority Bugs *
        G. Purchased Licenses *
        H. Licenses with Assets *
    J. Optimal Software Version
        A. Software Groups *
        B. Software Group suggestions *
        C. Software Group suggestions-Assets *
        D. Software Group suggestions-Bug List *
        E. Software Group suggestions-Field Notices *
        F. Software Group suggestions-Advisories *
    K. Automated Fault Management
        A. Faults *
        B. Fault Summary *
        C. Affected Assets *
    L. Regulatory Compliance Check
        A. Compliance Violations *
        B. Assets violating compliance rule *
        C. Policy Rule Details *
        D. Compliance Suggestions *
        E. Assets with violations *
        F. Asset Violations *
        G. Obtained *
    M. Risk Mitigation Check
        A. Crash Risk Assets *
        B. Crash Risk Factors *
        C. Similar Assets *
        D. Assets Crashed in last 1d, 7d, 15d, 90d *
        E. Asset Crash History *
6. Added the ability to upload to AWS S3 storage
7. Added a flag for 3 levels of debug output
    0 = exceptions only (default)
    1 = exceptions and status messages only
    3 = exceptions, status messages and API response payload
8. Added the ability to export data in raw JSON files as well as CSV's
9. Moved the following parameters to a new section labled "settings" in the config.ini
    A. wait_time = 1  # Used for setting a global wait timer (minimum requirement is 1)
    B. pxc_fault_days = "30"  # Used for Making API Request for number of days in report (default is 30)
    C. max_items = "50"  # Used for the maximum number of items to return in report (max and default is 50)
    D. debug_level = 0  # Used for setting a debug level (0,1,2) default is 0
    E. log_to_file = False  # send all screen logging to a file (True, False) default is False
    F. testLoop = 1  # test the code by running through the entire sequence x times... (default is 1)
    G. outputFormat = 1  # generate output in the form of Both, JSON or CSV. 1=Both 2=JSON 3=CSV
10. Changed the CSV File names to be consistent between all the CSV's
11. Added decriptions of the file naming conventions used for the CSV's and JSON files
12. Fixed bug with Lifecycle func not producing JSON output

"""

import requests
import json
import csv
import os
import shutil
import zipfile
import time
import sys
import math
import base64
from configparser import ConfigParser
import boto3
from botocore.exceptions import ClientError
from botocore.exceptions import NoCredentialsError
from datetime import datetime

"""
Notes on Imports
requests for making API calls
json for parsing json data
csv for parsing csv data
os for file/folder management
shutil for removing entire folders
zipfile for testing/extracting zip files
time for setting a sleep/wait timer
sys for changing the output to log file
math for rounding up to whole numbers
boto3 for accessing the AWS S3 storage
datetime for posting time stamps in the logging
"""

# PXCloud settings
# =======================================================================
# Generic URL Variables
pxc_token_url = "https://id.cisco.com/oauth2/aus1o4emxorc3wkEe5d7/v1/token"
urlProtocol = "https://"
urlHost = "api-cx.cisco.com/"
urlLink = "px/v1/"
urlLinkSandbox = "sandbox/px/v1/"
grant_type = "client_credentials"
pxc_cache_control = "no-cache"

# Customer and Analytics Insights URL Variables
pxc_url_lifecycle = "/lifecycle"
pxc_url_software_groups = "/insights/software/softwareGroups"
pxc_url_software_group_suggestions = pxc_url_software_groups + "/suggestions"
pxc_url_software_group_suggestions_assets = pxc_url_software_groups + "/assets"
pxc_url_software_group_suggestions_bugs = pxc_url_software_group_suggestions + "/bugs"
pxc_url_software_group_suggestions_field_notices = pxc_url_software_group_suggestions + "/fieldNotices"
pxc_url_software_group_suggestions_security_advisories = pxc_url_software_group_suggestions + "/securityAdvisories"
pxc_url_automated_fault_management_faults = "/insights/faults"
pxc_url_automated_fault_management_fault_summary = "/summary"
pxc_url_automated_fault_management_affected_assets = "/affectedAssets"
pxc_url_compliance_violations = "/insights/compliance/violations"
pxc_url_compliance_violations_assets = "/insights/compliance/violations/assets"
pxc_url_compliance_policy_rule_details = "/insights/compliance/policyRuleDetails"
pxc_url_compliance_suggestions = "/insights/compliance/suggestions"
pxc_url_compliance_assets_with_violations = "/insights/compliance/assetsWithViolations"
pxc_url_compliance_asset_violations = "/insights/compliance/assetViolations"
pxc_url_compliance_obtained = "/insights/compliance/optIn"
pxc_url_crash_risk = "/insights/crashRisk/asset"
pxc_url_crash_risk_assets = pxc_url_crash_risk + "s"
pxc_url_crash_risk_factors = "/riskFactors"
pxc_url_crash_risk_similar_assets = "/similarAssets"
pxc_url_crash_risk_assets_last_crashed = pxc_url_crash_risk + "sCrashed"
pxc_url_crash_risk_asset_crash_history = "/crashHistory"

# Data File Variables
codeVersion = str("1.0.0.7")
configFile = "config.ini"
csv_output_dir = "outputcsv/"
json_output_dir = "outputjson/"
log_output_dir = "outputlog/"
temp_dir = "temp/"
customers = (csv_output_dir + "Customers.csv")
contracts = (csv_output_dir + "Contracts.csv")
contractDetails = (csv_output_dir + "Contract_Details.csv")
partnerOffers = (csv_output_dir + "Partner_Offers.csv")
partnerOfferSessions = (csv_output_dir + "Partner_Offer_Sessions.csv")
assets = (csv_output_dir + "Assets.csv")
hardware = (csv_output_dir + "Hardware.csv")
software = (csv_output_dir + "Software.csv")
purchasedLicenses = (csv_output_dir + "Purchased_Licenses.csv")
licenses = (csv_output_dir + "Licenses.csv")
lifecycle = (csv_output_dir + "Lifecycle.csv")
securityAdvisories = (csv_output_dir + "Security_Advisories.csv")
fieldNotices = (csv_output_dir + "Field_Notices.csv")
priorityBugs = (csv_output_dir + "Priority_Bugs.csv")
successTracks = (csv_output_dir + "Success_Track.csv")
SWGroups = (csv_output_dir + "Software_Groups.csv")
SWGroupSuggestionsTrend = (csv_output_dir + "Software_Group_Suggestions_Trend.csv")
SWGroupSuggestionSummaries = (csv_output_dir + "Software_Group_Suggestions_Summaries.csv")
SWGroupSuggestionsReleases = (csv_output_dir + "Software_Group_Suggestions_Releases.csv")
SWGroupSuggestionAssets = (csv_output_dir + "Software_Group_Suggestion_Assets.csv")
SWGroupSuggestionsBugList = (csv_output_dir + "Software_Group_Suggestion_Bug_List.csv")
SWGroupSuggestionsFieldNotices = (csv_output_dir + "Software_Group_Suggestion_Field_Notices.csv")
SWGroupSuggestionsAdvisories = (csv_output_dir + "Software_Group_Suggestion_Security_Advisories.csv")
AFMFaults = (csv_output_dir + "Automated_Fault_Management_Faults.csv")
AFMFaultSummary = (csv_output_dir + "Automated_Fault_Management_Fault_Summary.csv")
AFMFaultAffectedAssets = (csv_output_dir + "Automated_Fault_Management_Fault_Affected_Assets.csv")
RCCComplianceViolations = (csv_output_dir + "Regulatory_Compliance_Violations.csv")
RCCAssetsViolatingComplianceRule = (csv_output_dir + "Regulatory_Compliance_Assets_violating_Compliance_Rule.csv")
RCCPolicyRuleDetails = (csv_output_dir + "Regulatory_Compliance_Policy_Rule_Details.csv")
RCCComplianceSuggestions = (csv_output_dir + "Regulatory_Compliance_Suggestions.csv")
RCCAssetsWithViolations = (csv_output_dir + "Regulatory_Compliance_Assets_With_Violations.csv")
RCCAssetViolations = (csv_output_dir + "Regulatory_Compliance_Asset_Violations.csv")
RCCObtained = (csv_output_dir + "Regulatory_Compliance_Obtained.csv")
CrashRiskAssets = (csv_output_dir + "Crash_Risk_Assets.csv")
CrashRiskFactors = (csv_output_dir + "Crash_Risk_Factors.csv")
CrashRiskSimilarAssets = (csv_output_dir + "Crash_Risk_Similar_Assets.csv")
CrashRiskAssetsLastCrashed = (csv_output_dir + "Crash_Risk_Assets_Last_Crashed.csv")
CrashRiskAssetCrashHistory = (csv_output_dir + "Crash_Risk_Asset_Crash_History.csv")
features = ["features", "fingerprint", "softwares_features"]
timePeriods = [1, 7, 15, 90]
# Configuration File Variables
pxc_client_id = ""  # Used to store the PX Cloud Client ID
pxc_client_secret = ""  # Used to store the PX Cloud Client Secret
s3access_key = ""  # Used to store the Amazon Web Services S3 (Simple Storage Service) Key
s3access_secret = ""  # Used to store the Amazon Web Services S3 (Simple Storage Service) Secret
s3bucket_folder = ""  # Used to store the Amazon Web Services S3 (Simple Storage Service) Bucket Folder
s3bucket_name = ""  # Used to store the Amazon Web Services S3 (Simple Storage Service) Bucket Name

# Data Initializer Variables
payload = {}  # Used for Making API Request
token = ""  # Used for Making API Requests

# the following settings are set in the config.ini "settings" section. Below are default placeholders for those values.
wait_time = 1  # Used for setting a global wait timer (minimum requirement is 1)
pxc_fault_days = "30"  # Used for Making API Request for number of days in report (default is 30)
max_items = "50"  # Used for the maximum number of items to return in report (max and default is 50)
debug_level = 0  # Used for setting a debug level (0 = Low,1 = Medium,2 = High) default is 0
logLevel = "low"  # Text description of log level, default is Low
log_to_file = False  # send all screen logging to a file (True, False) default is False
testLoop = 1  # test the code by running through the entire sequence x times... (default is 1)
outputFormat = "1"  # generate output in the form of Both, JSON or CSV. 1=Both 2=JSON 3=CSV
useProductionURL = True  # if true, use production URL, if false, use sandbox URL
'''
Begin defining functions
=======================================================================
'''


def token_time_check():
    checkTime = time.time()
    tokenTime = math.ceil(int(checkTime - startTime) / 60)
    if debug_level == 1 or debug_level == 2:
        print("Token time is :", tokenTime, "minutes")
    if tokenTime > 110:
        get_pxc_token()


# Function to load configuration from config.ini and continue or create a template if not found and exit
def load_config():
    global pxc_client_id
    global pxc_client_secret
    global s3access_key
    global s3access_secret
    global s3bucket_folder
    global s3bucket_name
    global wait_time
    global pxc_fault_days
    global max_items
    global debug_level
    global log_to_file
    global testLoop
    global outputFormat
    global useProductionURL

    config = ConfigParser()
    if os.path.isfile(configFile):
        print("******************************************************************")
        print("****************** CISCO PX Cloud Data Miner *********************")
        print("******************************************************************")
        print('Config.ini file was found, continuing...')
        config.read(configFile)
        pxc_client_id = (config['credentials']['pxc_client_id'])
        pxc_client_secret = (config['credentials']['pxc_client_secret'])
        s3access_key = (config['credentials']['s3access_key'])
        s3access_secret = (config['credentials']['s3access_secret'])
        s3bucket_folder = (config['credentials']['s3bucket_folder'])
        s3bucket_name = (config['credentials']['s3bucket_name'])
        wait_time = int((config['settings']["wait_time"]))
        pxc_fault_days = int((config['settings']["pxc_fault_days"]))
        max_items = (config['settings']["max_items"])
        debug_level = int((config['settings']["debug_level"]))
        log_to_file = (config['settings']["log_to_file"])
        testLoop = int((config['settings']["testLoop"]))
        outputFormat = int((config['settings']["outputFormat"]))
        useProductionURL = (config['settings']["useProductionURL"])

    else:
        print('Config.ini not found!!!!!!!!!!!!\nCreating config.ini...')
        print('\nNOTE: you must edit the config.ini file with your information\nExiting...')
        config.add_section('credentials')
        config.set("credentials", "pxc_client_id", "PX Cloud API Client ID")
        config.set("credentials", "pxc_client_secret", "PX Cloud API Client Secret")
        config.set("credentials", "s3access_key", "AWS S3 Access Key")
        config.set("credentials", "s3access_secret", "AWS S3 Client Secret")
        config.set("credentials", "s3bucket_folder", "AWS S3 Bucket Folder")
        config.set("credentials", "s3bucket_name", "AWS S3 Bucket Name")
        config.add_section('settings')
        config.set("settings", "# Time to wait between errors in seconds, default", "1")
        config.set("settings", "wait_time", "1")
        config.set("settings", "# The number of days to retrieve fault data for. This value can be 1, 7, 15, 30, "
                               "default", "30")
        config.set("settings", "pxc_fault_days", "30")
        config.set("settings", "# The maximum number of items to return per API call, maximum", "50")
        config.set("settings", "max_items", "50")
        config.set("settings", "# Used for setting a debug level (0 = Low, 1 = Medium, 2 = High), default", "0")
        config.set("settings", "debug_level", "0")
        config.set("settings", "# # send all screen logging to a file (True, False), default", "False")
        config.set("settings", "log_to_file", "False")
        config.set("settings", "# test the code by running through the entire sequence x times..., default", "1")
        config.set("settings", "testLoop", "1")
        config.set("settings", "# generate output in the form of Both, JSON or CSV. 1=Both 2=JSON 3=CSV, default", "1")
        config.set("settings", "outputFormat", "1")
        config.set("settings", "# to use the Sandbox set useProductionURL", "False")
        config.set("settings", "useProductionURL", "True")
        with open(configFile, 'w') as configfile:
            config.write(configfile)
        exit()


# Function to upload all files in the output folders to AWS S3.
def s3_storage():
    if s3access_key:
        print("\nUploading data to S3")
        """Connect to S3 Service"""
        client_s3 = boto3.client('s3', aws_access_key_id=s3access_key, aws_secret_access_key=s3access_secret, )
        """Upload Files to S3 Bucket"""
        data_file_folder = os.path.join(os.getcwd(), csv_output_dir)
        for file in os.listdir(data_file_folder):
            if not file.startswith('~'):
                try:
                    print('Uploading file {0}...'.format(file))
                    client_s3.upload_file(os.path.join(data_file_folder, file),
                                          s3bucket_name,
                                          (s3bucket_folder + '{}').format(file))
                    print("Upload Successful")
                except ClientError as e:
                    print('Credential is incorrect')
                    print(e)
                except Exception as e:
                    print(e)
                except FileNotFoundError:
                    print("The file was not found")
                except NoCredentialsError:
                    print("Credentials not available")
        print("Done!")
        print("====================\n\n")
    else:
        print("\nUploading data to S3 was SKIPPED")
        print("====================\n\n")


# Function to generate or clear output and temp folders for use.
def temp_storage():
    if os.path.isdir(csv_output_dir):
        shutil.rmtree(csv_output_dir)
        os.mkdir(csv_output_dir)
    else:
        os.mkdir(csv_output_dir)
    if os.path.isdir(json_output_dir):
        shutil.rmtree(json_output_dir)
        if outputFormat == 1 or outputFormat == 2:
            os.mkdir(json_output_dir)
    else:
        if outputFormat == 1 or outputFormat == 2:
            os.mkdir(json_output_dir)

    if os.path.isdir(temp_dir):
        shutil.rmtree(temp_dir)
        os.mkdir(temp_dir)
    else:
        os.mkdir(temp_dir)


# Function to get a valid API token from PX Cloud
def get_pxc_token():
    global token
    print("\nGetting PX Cloud Token")
    url = (
            pxc_token_url + "?grant_type=" +
            grant_type + "&client_id=" +
            pxc_client_id + "&client_secret=" +
            pxc_client_secret + "&cache-control=" +
            pxc_cache_control + "&scope=" +
            pxc_scope
    )
    headers = {
        'Content-type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    reply = json.loads(response.text)
    token = (reply["access_token"])
    if debug_level == 1 or debug_level == 2:
        print("API Token: ", token)
    print("Done!")
    print("====================\n\n")


# Function to get the raw API JSON data from PX Cloud
def get_json_reply(url, tag):
    tries = 1
    response = []
    while True:
        try:
            headers = {
                'Authorization': f'Bearer {token}'
            }
            response = requests.request("GET", url, headers=headers, data=payload, verify=True)
            reply = json.loads(response.text)
            items = reply[tag]
            if debug_level == 2:
                print("URL Request:", url,
                      "\nURL Tag:", tag,
                      "\nHTTP Code:", response.status_code,
                      "\nReview API Headers:", response.headers,
                      "\nResponse Body:", response.content)
            if response.status_code == 500:
                if debug_level == 2:
                    print("URL Request:", url,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                    print("Error retrieving API response")
            if response.status_code == 403:
                print("\nFailed getting API data due to... \nResponse Body:", response.content)
                print("URL Request:", url,
                      "\nHTTP Code:", response.status_code,
                      "\nReview API Headers:", response.headers,
                      "\nResponse Body:", response.content)
            try:
                if response.status_code == 200:
                    if len(items) > 0:
                        if tries >= 2:
                            print("\nSuccess on retry! \nContinuing.\n", end="")
                        return items
            finally:
                if response.status_code == 200:
                    return items
        except Exception as Error:
            if response.text.__contains__("Customer admin has not provided access."):
                if debug_level == 2:
                    print("\nResponse Body:", response.content)
                if tag == "items":
                    print("Customer admin has not provided access....Skipping")
                break
            elif response.text.__contains__("Not found"):
                if debug_level == 2:
                    print("\nResponse Body:", response.content)
                if tag == "items":
                    print("No Data Found....Skipping")
                break
            elif response.status_code == 500 or response.status_code == 400:
                if debug_level == 2:
                    print("URL Request:", url,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                    print("Error retrieving API response")
                break
            if tag == "items":
                print("\nResponse Content:", response.content)
                print("\nAttempt #", tries, "Failed getting:", Error,
                      "\nRetrying in", wait_time, "seconds\n", end="")
                time.sleep(wait_time)
            if tries >= 3:
                break
        finally:
            tries += 1


# Function to get the Customer List from PX Cloud
# The objective of this API is to provide the list of all the customers
# CSV Naming Convention: Customer.csv
# JSON Naming Convention: Customer.json
def get_pxc_customers():
    print("******************************************************************")
    print("****************** Running Customer Report ***********************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    items = (get_json_reply(url=(pxc_url_customers + "?max=" + max_items), tag="items"))
    with open(customers, 'w', encoding="utf-8", newline='') as target:
        CSV_Header = "customerId,customerName,successTrackId,successTrackAccess"
        writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
        writer.writerow(CSV_Header.split())
    for item in items:
        customerId = str(item['customerId'])
        customerName = str(item['customerName']).replace(",", " ")
        successTrack = item['successTracks']
        print(f"Found Customer {customerName}")
        if not successTrack:
            successTrack = [{'id': 'N/A', 'access': 'N/A'}]
        for track in successTrack:
            successTrackId = str(track['id'])
            trackAccess = str(track['access'])
            with open(customers, 'a', encoding="utf-8", newline='') as target:
                writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                CSV_Data = (customerId + ',' +
                            customerName + ',' +
                            successTrackId + ',' +
                            trackAccess)
                writer.writerow(CSV_Data.split())
    if outputFormat == 1 or outputFormat == 2:
        if items is not None:
            if len(items) > 0:
                with open(json_output_dir + 'Customers.json', 'w') as json_file:
                    json.dump(items, json_file)
                print(f"Saving {json_file.name}")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to get the Contract List from PX Cloud
# This API will fetch list of partner contracts transacted with Cisco.
# CSV Naming Convention: Contract.csv
# JSON Naming Convention: Contract.json
def get_pxc_contracts():
    print("******************************************************************")
    print("****************** Running Contract Report ***********************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    items = (get_json_reply(url=pxc_url_contracts, tag="items"))
    with open(contracts, 'w', encoding="utf-8", newline='') as target:
        CSV_Header = "customerName," \
                     "contractNumber," \
                     "cuid," \
                     "cavid," \
                     "contractStatus," \
                     "contractValue," \
                     "currency," \
                     "serviceLevel," \
                     "startDate," \
                     "endDate," \
                     "currencySymbol," \
                     "onboardedstatus"
        writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
        writer.writerow(CSV_Header.split())
        for item in items:
            contractNumber = str(item['contractNumber'])
            try:
                cuid = str(item['cuid'])
            except KeyError:
                cuid = "N/A"
                pass
            try:
                cavid = str(item['cavid'])
            except KeyError:
                cavid = "N/A"
                pass
            contractStatus = str(item['contractStatus'])
            contractValue = str(item['contractValue'])
            customerName = str(item['customerName'].replace(",", " "))
            currency = str(item['currency'])
            serviceLevel = str(item['serviceLevel'].replace(",", "|"))
            startDate = str(item['startDate'])
            endDate = str(item['endDate'])
            currencySymbol = str(item['currencySymbol'])
            onboardedstatus = str(item['onboardedstatus'])
            print(f"Found contract number {contractNumber} for {customerName}")
            CSV_Data = (customerName + ',' +
                        contractNumber + ',' +
                        cuid + ',' +
                        cavid + ',' +
                        contractStatus + ',' +
                        contractValue + ',' +
                        currency + ',' +
                        serviceLevel + ',' +
                        startDate + ',' +
                        endDate + ',' +
                        currencySymbol + ',' +
                        onboardedstatus)
            writer.writerow(CSV_Data.split())
    if outputFormat == 1 or outputFormat == 2:
        if items is not None:
            if len(items) > 0:
                with open(json_output_dir + 'Contracts.json', 'w') as json_file:
                    json.dump(items, json_file)
                print(f"Saving {json_file.name}")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to get the Contract List from PX Cloud
# This API will fetch list of partner contract line items transacted with Cisco.
# CSV Naming Convention: Contract_Details.csv
# JSON Naming Convention: {Customer Name}_Contract_Details_{ContractNumber}_Page_{page}_of_{total}.json
def get_pxc_contracts_details():
    print("******************************************************************")
    print("****************** Running Contract Details **********************")
    print("******************************************************************")
    print("Searching ......", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(contractDetails, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerName," \
                         "customerGUName," \
                         "customerHQName," \
                         "contractNumber," \
                         "productId," \
                         "serialNumber," \
                         "contractStatus," \
                         "componentType," \
                         "serviceLevel," \
                         "coverageStartDate," \
                         "coverageEndDate," \
                         "installationQuantity," \
                         "instanceNumber"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(contracts, 'r') as target:
        contractList = csv.DictReader(target)
        for row in contractList:
            customerName = row["customerName"]
            contractNumber = row["contractNumber"]
            headers = {'Authorization': f'Bearer {token}'}
            url = (pxc_url_contracts_details +
                   "?contractNumber=" + contractNumber
                   )
            response = requests.request("GET", url, headers=headers, data=payload, verify=True)
            reply = json.loads(response.text)
            try:
                if response.status_code == 200:
                    totalCount = reply["totalCount"]
                    pages = math.ceil(totalCount / int(max_items))
                    if debug_level == 1 or debug_level == 2:
                        print("\nTotal Pages:", pages,
                              "\nTotal Records: ", totalCount,
                              "\nURL Request:", url,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content,
                              "\n====================")
                    page = 0
                    print(f"\nFound details on contract number {contractNumber} for {customerName}")
                    while page < pages:
                        off_set = (page * int(max_items))
                        if off_set <= int(max_items):
                            off_set = 0
                        url = (pxc_url_contracts_details +
                               "?contractNumber=" + contractNumber +
                               "&offset=" + str(off_set) +
                               "&max=" + max_items
                               )
                        items = (get_json_reply(url, tag="items"))
                        if outputFormat == 1 or outputFormat == 2:
                            if items is not None:
                                if len(items) > 0:
                                    with open(json_output_dir + customerName +
                                              "_Contract_Details_" + contractNumber +
                                              "_Page_" + str(page + 1) +
                                              "_of_" + str(pages) +
                                              ".json", 'w') as json_file:
                                        json.dump(items, json_file)
                                    print(f"Saving {json_file.name}")
                        if outputFormat == 1 or outputFormat == 3:
                            if items is not None:
                                if len(items) > 0:
                                    for item in items:
                                        customerGUName = str(item['customerGUName'].replace(",", " "))
                                        customerHQName = str(item['customerHQName'].replace(",", " "))
                                        productId = str(item['productId'].replace(",", " "))
                                        serialNumber = str(item['serialNumber'])
                                        contractStatus = str(item['contractStatus'])
                                        componentType = str(item['componentType'].replace(",", " "))
                                        serviceLevel = str(item['serviceLevel'].replace(",", " "))
                                        coverageStartDate = str(item['coverageStartDate'])
                                        coverageEndDate = str(item['coverageEndDate'])
                                        installationQuantity = str(item['installationQuantity'])
                                        instanceNumber = str(item['instanceNumber'])
                                        with open(contractDetails, 'a', encoding="utf-8", newline='') as details_target:
                                            writer = csv.writer(details_target,
                                                                delimiter=' ',
                                                                quotechar=' ',
                                                                quoting=csv.QUOTE_MINIMAL)
                                            CSV_Data = (customerName + ',' +
                                                        customerGUName + ',' +
                                                        customerHQName + ',' +
                                                        contractNumber + ',' +
                                                        productId + ',' +
                                                        serialNumber + ',' +
                                                        contractStatus + ',' +
                                                        componentType + ',' +
                                                        serviceLevel + ',' +
                                                        coverageStartDate + ',' +
                                                        coverageEndDate + ',' +
                                                        installationQuantity + ',' +
                                                        instanceNumber)
                                            writer.writerow(CSV_Data.split())
                        else:
                            print("\nNo Data Found .... Skipping")
                        page += 1
            except KeyError:
                print("No Data to process... Skipping.")
                pass
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to get the Partner Offers from PX Cloud
# This API will fetch all the offers created by the Partners.
# CSV Naming Convention: Partner_Offers.csv
# JSON Naming Convention: Partner_Offers.json
def get_pxc_partner_offers():
    print("******************************************************************")
    print("**************** Running All Partner Offers **********************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(partnerOffers, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "offerId," \
                         "offerType," \
                         "title," \
                         "description," \
                         "duration," \
                         "accTimeRequiredHours," \
                         "imageFileName," \
                         "customerRating," \
                         "status," \
                         "userFirstName," \
                         "userLastName," \
                         "userEmailId," \
                         "createdBy," \
                         "createdOn," \
                         "modifiedBy," \
                         "modifiedOn," \
                         "language," \
                         "mappingId," \
                         "successTrackId," \
                         "successTrackName," \
                         "usecaseId," \
                         "usecase," \
                         "pitstopId," \
                         "pitstop," \
                         "mappingChecklistId," \
                         "checklistId," \
                         "checklist," \
                         "publishedToAllCustomers," \
                         "customerEntryId," \
                         "companyName"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    items = (get_json_reply(url=pxc_url_partner_offers, tag="items"))
    if not items:
        print("No Data Found.")
    if outputFormat == 1 or outputFormat == 3:
        if items is not None:
            if len(items) > 0:
                for item in items:
                    offerId = str(item['offerId']).replace(",", " ")
                    offerType = str(item['offerType']).replace(",", " ")
                    title = str(item['title']).replace(",", " ")
                    description = str(item['description']).replace(",", " ")
                    duration = str(item['duration'])
                    accTimeRequiredHours = str(item['accTimeRequiredHours'])
                    imageFileName = str(item['imageFileName']).replace(",", " ")
                    customerRating = str(item['customerRating'])
                    status = str(item['status']).replace(",", " ")
                    userFirstName = str(item['userFirstName']).replace(",", " ")
                    userLastName = str(item['userLastName']).replace(",", " ")
                    userEmailId = str(item['userEmailId']).replace(",", " ")
                    createdBy = str(item['createdBy']).replace(",", " ")
                    createdOn = str(item['created'])
                    modifiedBy = item['offerType'].replace(",", " ")
                    modifiedOn = str(item['modified'])
                    language = str(item['language']).replace(",", " ")
                    mappings = item['mapping']
                    publishedToAllCustomers = str(item['publishedToAllCustomers'])
                    customerList = item['customerList']
                    print(f"Found Partner Offer ID {offerId}")
                    for customer in customerList:
                        customerEntryId = str(customer['customerEntryId']).replace(",", " ")
                        customerId = str(customer['customerId']).replace(",", " ")
                        companyName = str(customer['companyName']).replace(",", " ")
                        for mapping in mappings:
                            mappingId = str(mapping['mappingId']).replace(",", " ")
                            successTrackId = str(mapping['successTrackId']).replace(",", " ")
                            successTrackName = str(mapping['successTrackName']).replace(",", " ")
                            usecaseId = str(mapping['usecaseId']).replace(",", " ")
                            usecase = str(mapping['usecase']).replace(",", " ")
                            pitstopId = str(mapping['pitstopId']).replace(",", " ")
                            pitstop = str(mapping['pitstop']).replace(",", " ")
                            checklists = mapping['checklists']
                            for row in checklists:
                                mappingChecklistId = str(row['mappingChecklistId'])
                                checklistId = str(row['checklistId'])
                                try:
                                    checklist = str(row['checklist'])
                                except KeyError:
                                    checklist = "N/A"
                                    pass
                                with open(partnerOffers, 'a', encoding="utf-8", newline='') as target:
                                    writer = csv.writer(target,
                                                        delimiter=' ',
                                                        quotechar=' ',
                                                        quoting=csv.QUOTE_MINIMAL)
                                    CSV_Data = (customerId + ',' +
                                                offerId + ',' +
                                                offerType + ',' +
                                                title + ',' +
                                                description + ',' +
                                                duration + ',' +
                                                accTimeRequiredHours + ',' +
                                                imageFileName + ',' +
                                                customerRating + ',' +
                                                status + ',' +
                                                userFirstName + ',' +
                                                userLastName + ',' +
                                                userEmailId + ',' +
                                                createdBy + ',' +
                                                createdOn + ',' +
                                                modifiedBy + ',' +
                                                modifiedOn + ',' +
                                                language + ',' +
                                                mappingId + ',' +
                                                successTrackId + ',' +
                                                successTrackName + ',' +
                                                usecaseId + ',' +
                                                usecase + ',' +
                                                pitstopId + ',' +
                                                pitstop + ',' +
                                                mappingChecklistId + ',' +
                                                checklistId + ',' +
                                                checklist + ',' +
                                                publishedToAllCustomers + ',' +
                                                customerEntryId + ',' +
                                                companyName)
                                    writer.writerow(CSV_Data.split())
        else:
            print("\nNo Data Found .... Skipping")
    if outputFormat == 1 or outputFormat == 2:
        if items is not None:
            with open(json_output_dir + "Partner_Offers.json", 'w') as json_file:
                json.dump(items, json_file)
            print(f"Saving {json_file.name}")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to get the Partner Offer Sessions from PX Cloud
# This API will fetch all the active and inactive sessions of all the Offers created by the Partners.
# CSV Naming Convention: Partner_Offer_Sessions.csv
# JSON Naming Convention: Partner_Offer_Sessions.json
def get_pxc_partner_offer_sessions():
    print("******************************************************************")
    print("************** Running All Partner Offers Sessions ***************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(partnerOfferSessions, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "companyName," \
                         "offerId," \
                         "sessionId," \
                         "timezone," \
                         "status," \
                         "attendeeId," \
                         "ccoId," \
                         "attendeeUserEmail," \
                         "attendeeUserFullName," \
                         "noOfAttendees," \
                         "preferredSlot," \
                         "businessOutcome," \
                         "reasonForInterest," \
                         "createdDate," \
                         "modifiedDate"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    items = (get_json_reply(url=pxc_url_partner_offers_sessions, tag="items"))
    if not items:
        print("No Data Found.")
    if outputFormat == 1 or outputFormat == 3:
        if items is not None:
            if len(items) > 0:
                for item in items:
                    offerId = item['offerId'].replace(",", " ")
                    sessions = item['sessions']
                    for session in sessions:
                        sessionId = session['sessionId'].replace(",", " ")
                        timezone = session['timezone'].replace(",", " ")
                        status = session['status'].replace(",", " ")
                        noOfAttendees = str(session['noOfAttendees'])
                        try:
                            preferredSlot = session['preferredSlot'].replace(",", " ")
                        except KeyError:
                            preferredSlot = "N/A"
                            pass
                        try:
                            businessOutcome = session['businessOutcome'].replace(",", " ")
                        except KeyError:
                            businessOutcome = "N/A"
                            pass
                        try:
                            reasonForInterest = session['reasonForInterest'].replace(",", " ")
                        except KeyError:
                            reasonForInterest = "N/A"
                            pass
                        createdDate = str(session['createdDate'])
                        modifiedDate = str(session['modifiedDate'])
                        attendeeList = session['attendeeList']
                        if not attendeeList:
                            attendeeList = [{'attendeeId': 'N/A',
                                             'ccoId': 'N/A',
                                             'attendeeUserEmail': 'N/A',
                                             'attendeeUserFullName': 'N/A',
                                             'customerId': 'N/A',
                                             'companyName': 'N/A'}]
                        for attendee in attendeeList:
                            attendeeId = attendee['attendeeId'].replace(",", " ")
                            try:
                                ccoId = attendee['ccoId'].replace(",", " ")
                            except KeyError:
                                ccoId = "N/A"
                                pass
                            attendeeUserEmail = attendee['attendeeUserEmail'].replace(",", " ")
                            attendeeUserFullName = attendee['attendeeUserFullName'].replace(",", " ")
                            customerId = attendee['customerId'].replace(",", " ")
                            companyName = attendee['companyName'].replace(",", " ")
                            with open(partnerOfferSessions, 'a', encoding="utf-8", newline='') as target:
                                writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                                print(f"Found Partner Offer Sessions for Session ID {sessionId}")
                                CSV_Data = (customerId + ',' +
                                            companyName + ',' +
                                            offerId + ',' +
                                            sessionId + ',' +
                                            timezone + ',' +
                                            status + ',' +
                                            attendeeId + ',' +
                                            ccoId + ',' +
                                            attendeeUserEmail + ',' +
                                            attendeeUserFullName + ',' +
                                            noOfAttendees + ',' +
                                            preferredSlot + ',' +
                                            businessOutcome + ',' +
                                            reasonForInterest + ',' +
                                            createdDate + ',' +
                                            modifiedDate)
                                writer.writerow(CSV_Data.split())
        else:
            print("\nNo Data Found .... Skipping")
    if outputFormat == 1 or outputFormat == 2:
        if items is not None:
            if len(items) > 0:
                with open(json_output_dir + 'Partner_Offer_Sessions.json', 'w') as json_file:
                    json.dump(items, json_file)
                print(f"Saving {json_file.name}")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to get the Success Track data from PX Cloud
# This API will get customer success tracks which will provide the usecase details.
# CSV Naming Convention: SuccessTracks.csv
# JSON Naming Convention: SuccessTracks.json
def get_pxc_succsstracks():
    print("******************************************************************")
    print("******************** Running Success Track ***********************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(successTracks, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "successTracksId," \
                         "successTrackName," \
                         "useCaseName," \
                         "useCaseId"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    tries = 1
    while True:
        items = (get_json_reply(url=pxc_url_successTracks, tag="items"))
        try:
            if len(items) > 0:
                for item in items:
                    successTrackName = item['successTrack'].replace(",", " ")
                    successTracksId = item['id'].replace(",", " ")
                    useCases = item['usecases']
                    for useCase in useCases:
                        useCaseName = useCase['name'].replace(",", " ")
                        useCaseId = useCase['id'].replace(",", " ")
                        if outputFormat == 1 or outputFormat == 3:
                            with open(successTracks, 'a', encoding="utf-8", newline='') as target:
                                writer = csv.writer(target,
                                                    delimiter=' ',
                                                    quotechar=' ',
                                                    quoting=csv.QUOTE_MINIMAL)
                                print(f"Found Success Track {successTrackName} for use case {useCaseName}")
                                CSV_Data = (successTracksId + ','
                                            + successTrackName + ',' +
                                            useCaseName + ',' +
                                            useCaseId)
                                writer.writerow(CSV_Data.split())
                if outputFormat == 1 or outputFormat == 2:
                    if items is not None:
                        if len(items) > 0:
                            with open(json_output_dir + "SuccessTracks.json",
                                      'w') as json_file:
                                json.dump(items, json_file)
                            print(f"Saving {json_file.name}")
            else:
                print("\nError")
                raise Exception("Error")
        except Exception as Error:
            print("\n", str(Error) + "\nRetrying....", end="")
            print(f"Pausing for {wait_time} seconds before retrying...", end="")
            time.sleep(wait_time + tries)  # increase the wait with the number of retries
            if tries >= 2:
                break
        else:
            break
        finally:
            tries += 1
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to request, download and process Asset report data from PX Cloud
# Assets report gives the list of all assets (products like network element and other devices) owned by customer.
# CSV Naming Convention: Assets.csv
# JSON Naming Convention: {Customer ID}_Assets_{UniqueReportID}.json
def pxc_assets_reports():
    print("******************************************************************")
    print("********************* Running Asset Report ***********************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(assets, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "successTrackId," \
                         "useCaseId," \
                         "assetId," \
                         "assetName," \
                         "productFamily," \
                         "productType," \
                         "serialNumber," \
                         "productId," \
                         "ipAddress," \
                         "productDescription," \
                         "softwareType," \
                         "softwareRelease," \
                         "role," \
                         "location," \
                         "coverageStatus," \
                         "lastScan," \
                         "endOfLifeAnnounced," \
                         "endOfSale," \
                         "lastShip," \
                         "endOfRoutineFailureAnalysis," \
                         "endOfNewServiceAttach," \
                         "endOfServiceContractRenewal," \
                         "ldosDate," \
                         "connectionStatus," \
                         "managedBy," \
                         "contractNumber," \
                         "coverageEndDate," \
                         "coverageStartDate," \
                         "supportType," \
                         "advisories," \
                         "assetType," \
                         "criticalSecurityAdvisories," \
                         "addressLine1," \
                         "addressLine2," \
                         "addressLine3," \
                         "licenseStatus," \
                         "licenseLevel," \
                         "profileName," \
                         "hclStatus," \
                         "ucsDomain," \
                         "hxCluster," \
                         "subscriptionId," \
                         "subscriptionStartDate," \
                         "subscriptionEndDate"
            writeheader = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writeheader.writerow(CSV_Header.split())
    with open(customers, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            successTrackId = row['successTrackId']
            customerName = row['customerName']
            if debug_level == 1 or debug_level == 2:
                print("====================\n\n")
                print("Asset data for Customer:", customerName,
                      "on Success Tracks:", successTrackId)
            if not successTrackId == "N/A":
                url = (pxc_url_customers + "/" + customerId + "/reports")
                data_payload = json.dumps({"reportName": "Assets", "successTrackId": successTrackId})
                headers = {'Authorization': f'Bearer {token}'}
                response = requests.request(
                    "POST",
                    url,
                    headers=headers,
                    data=data_payload,
                    verify=True
                )
                if debug_level == 2:
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                try:
                    if bool(response.headers["location"]) is True:
                        pass
                    else:
                        raise KeyError
                except KeyError:
                    print("\n!!!!!!!!\nException Thrown for", "Customer:",
                          customerId, "on Success Tracks:", successTrackId,
                          "Report Failed to Download\n")
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                    while response.status_code >= 400:
                        print(f"Pausing for {wait_time} seconds before re-request...")
                        time.sleep(wait_time)
                        print("Resuming...")
                        print("Making API Call again with the following...")
                        print("URL: ", url)
                        print("Data Payload: ", data_payload)
                        response = requests.request(
                            "POST",
                            url,
                            headers=headers,
                            data=data_payload,
                            verify=True
                        )
                        print("Report request URL:", url,
                              "\nReport details:", data_payload,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content)
                        print("Review for", "Customer:", customerId, "on Success Tracks:", successTrackId,
                              "Report Failed to Download\n")
                location = response.headers["location"]
                json_filename = (location.split('/')[-1] + '.json')
                tries = 1
                print("")
                while True:
                    time.sleep(tries)
                    print("Scanning for data...")
                    filename = (temp_dir + location.split('/')[-1] + '.zip')
                    headers = {'Authorization': f'Bearer {token}'}
                    response = requests.request("GET", location, headers=headers, data=payload)
                    if debug_level == 2:
                        print("\nLocation URL Returned:", location,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content, "\nWait Time:", tries)
                    try:
                        with open(filename, 'wb') as file:
                            file.write(response.content)
                        with open(filename, "rb") as file:
                            if file.read() and response.status_code == 200:
                                with zipfile.ZipFile(filename, 'r') as zip_file:
                                    zip_file.extractall(temp_dir)
                                    if tries >= 2:
                                        if debug_level == 2:
                                            print("Success on retry!\nContinuing\n", end="")
                            else:
                                print("\nDownload Failed")
                                raise Exception("File Corrupted")
                        os.remove(filename)
                    except Exception as FileCorruptError:
                        if debug_level == 2:
                            print("\nDeleting file..." + str(filename) + " " +
                                  str(FileCorruptError) + "\nRetrying....", end="")
                            print(f"Pausing for {wait_time} seconds before retrying...", end="")
                        time.sleep(wait_time + tries)  # increase the wait with the number of retries
                        if tries >= 10:
                            break
                    else:
                        break
                    finally:
                        tries += 1
                if useProductionURL == "True":
                    input_json_file = str(temp_dir + customerId + "_Assets_" + json_filename)
                else:
                    input_json_file = str(temp_dir + json_filename)
                if debug_level == 1 or debug_level == 2:
                    print("\nReading file:", input_json_file)
                with open(input_json_file, 'r', encoding='utf-8') as inputTarget:
                    data = json.load(inputTarget)
                    customerId = data['metadata']['customerId']
                    totalCount = data['metadata']['totalCount']
                    items = data['items']
                if outputFormat == 1 or outputFormat == 3:
                    if totalCount > 0:
                        print(f"\nFound Asset Data on Success Track {successTrackId} for customer {customerName}")
                        if len(items) > 0:
                            for item in items:
                                assetId = str(item['assetId']).replace(",", "_")
                                assetName = str(item['assetName'])
                                productFamily = str(item['productFamily']).replace(",", " ")
                                productType = str(item['productType']).replace(",", " ")
                                serialNumber = str(item['serialNumber'])
                                productId = str(item['productId'])
                                ipAddress = str(item['ipAddress'])
                                productDescription = str(item['productDescription']).replace(",", " ")
                                softwareType = str(item['softwareType']).replace(",", " ")
                                softwareRelease = str(item['softwareRelease'])
                                try:
                                    role = str((item['role']))
                                except KeyError:
                                    role = "N/A"
                                    pass
                                assetLocation = str(item['location']).replace(",", " ")
                                coverageStatus = str(item['coverageStatus'])
                                try:
                                    lastScan = str(item['lastScan'])
                                    if lastScan == "None":
                                        lastScan = ""
                                except KeyError:
                                    lastScan = ""
                                    pass
                                successTrack = item['successTrack']
                                endOfLifeAnnounced = str(item['endOfLifeAnnounced'])
                                if endOfLifeAnnounced == "None":
                                    endOfLifeAnnounced = ""
                                endOfSale = str(item['endOfSale'])
                                if endOfSale == "None":
                                    endOfSale = ""
                                lastShip = str(item['lastShip'])
                                if lastShip == "None":
                                    lastShip = ""
                                endOfRoutineFailureAnalysis = str(item['endOfRoutineFailureAnalysis'])
                                if endOfRoutineFailureAnalysis == "None":
                                    endOfRoutineFailureAnalysis = ""
                                endOfNewServiceAttach = str(item['endOfNewServiceAttach'])
                                if endOfNewServiceAttach == "None":
                                    endOfNewServiceAttach = ""
                                endOfServiceContractRenewal = str(item['endOfServiceContractRenewal'])
                                if endOfServiceContractRenewal == "None":
                                    endOfServiceContractRenewal = ""
                                ldosDate = str(item['ldosDate'])
                                if ldosDate == "None":
                                    ldosDate = ""
                                connectionStatus = str(item['connectionStatus'])
                                try:
                                    managedBy = str(item['managedBy'])
                                except KeyError:
                                    managedBy = "N/A"
                                    pass
                                contractNumber = str(item['contractNumber'])
                                coverageEndDate = str(item['coverageEndDate'])
                                if coverageEndDate == "None":
                                    coverageEndDate = ""
                                coverageStartDate = str(item['coverageStartDate'])
                                if coverageStartDate == "None":
                                    coverageStartDate = ""
                                supportType = str(item['supportType'])
                                advisories = str(item['advisories'])
                                assetType = str(item['assetType'])
                                try:
                                    criticalSecurityAdvisories = str(item['criticalSecurityAdvisories'])
                                except KeyError:
                                    criticalSecurityAdvisories = ""
                                    pass
                                try:
                                    addressLine1 = str(item['addressLine1']).replace(",", " ")
                                except KeyError:
                                    addressLine1 = ""
                                    pass
                                try:
                                    addressLine2 = str(item['addressLine2']).replace(",", " ")
                                except KeyError:
                                    addressLine2 = ""
                                    pass
                                try:
                                    addressLine3 = str(item['addressLine3']).replace(",", " ")
                                except KeyError:
                                    addressLine3 = ""
                                    pass
                                try:
                                    licenseStatus = str(item['licenseStatus'])
                                except KeyError:
                                    licenseStatus = ""
                                    pass
                                try:
                                    licenseLevel = str(item['licenseLevel'])
                                except KeyError:
                                    licenseLevel = ""
                                    pass
                                try:
                                    profileName = str(item['profileName']).replace(",", " ")
                                except KeyError:
                                    profileName = ""
                                    pass
                                try:
                                    hclStatus = str(item['hclStatus'])
                                except KeyError:
                                    hclStatus = ""
                                    pass
                                try:
                                    ucsDomain = str(item['ucsDomain'])
                                except KeyError:
                                    ucsDomain = ""
                                    pass
                                try:
                                    hxCluster = str(item['hxCluster'])
                                except KeyError:
                                    hxCluster = ""
                                    pass
                                try:
                                    subscriptionId = str(item['subscriptionId'])
                                except KeyError:
                                    subscriptionId = ""
                                    pass
                                try:
                                    subscriptionStartDate = str(item['subscriptionStartDate'])
                                    if subscriptionStartDate == "None":
                                        subscriptionStartDate = ""
                                except KeyError:
                                    subscriptionStartDate = ""
                                    pass
                                try:
                                    subscriptionEndDate = str(item['subscriptionEndDate'])
                                    if subscriptionEndDate == "None":
                                        subscriptionEndDate = ""
                                except KeyError:
                                    subscriptionEndDate = ""
                                    pass
                                for track in successTrack:
                                    successTrackId = track['id']
                                    useCases = track['useCases']
                                    for useCase in useCases:
                                        if outputFormat == 1 or outputFormat == 3:
                                            with open(assets, 'a', encoding="utf-8", newline='') as report_target:
                                                writer = csv.writer(report_target,
                                                                    delimiter=' ',
                                                                    quotechar=' ',
                                                                    quoting=csv.QUOTE_MINIMAL)
                                                CSV_Data = (customerId + ',' +
                                                            successTrackId + ',' +
                                                            useCase + ',' +
                                                            assetId + ',' +
                                                            assetName + ',' +
                                                            productFamily + ',' +
                                                            productType + ',' +
                                                            serialNumber + ',' +
                                                            productId + ',' +
                                                            ipAddress + ',' +
                                                            productDescription + ',' +
                                                            softwareType + ',' +
                                                            softwareRelease + ',' +
                                                            role + ',' +
                                                            assetLocation + ',' +
                                                            coverageStatus + ',' +
                                                            lastScan + ',' +
                                                            endOfLifeAnnounced + ',' +
                                                            endOfSale + ',' +
                                                            lastShip + ',' +
                                                            endOfRoutineFailureAnalysis + ',' +
                                                            endOfNewServiceAttach + ',' +
                                                            endOfServiceContractRenewal + ',' +
                                                            ldosDate + ',' +
                                                            connectionStatus + ',' +
                                                            managedBy + ',' +
                                                            contractNumber + ',' +
                                                            coverageEndDate + ',' +
                                                            coverageStartDate + ',' +
                                                            supportType + ',' +
                                                            advisories + ',' +
                                                            assetType + ',' +
                                                            criticalSecurityAdvisories + ',' +
                                                            addressLine1 + ',' +
                                                            addressLine2 + ',' +
                                                            addressLine3 + ',' +
                                                            licenseStatus + ',' +
                                                            licenseLevel + ',' +
                                                            profileName + ',' +
                                                            hclStatus + ',' +
                                                            ucsDomain + ',' +
                                                            hxCluster + ',' +
                                                            subscriptionId + ',' +
                                                            subscriptionStartDate + ',' +
                                                            subscriptionEndDate)
                                                writer.writerow(CSV_Data.split())
                        if debug_level == 1 or debug_level == 2:
                            print("Success")
                else:
                    print("\nNo Asset Data Found For Customer:", customerName,
                          "\nSkipping this record and continuing....\n", end="")
                if outputFormat == 1 or outputFormat == 2:
                    if totalCount > 0:
                        print(f"Saving {json_output_dir}{customerId}_Assets_{json_filename}")
                        shutil.copy(input_json_file, json_output_dir)
                    os.remove(input_json_file)
            else:
                print("\nNo Asset Data Found For Customer:", customerName,
                      "\nSkipping this record and continuing....")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to request, download and process Hardware report data from PX Cloud
# The Hardware report will provide hardware inventory details for a specific device and customer.
# CSV Naming Convention: Hardware.csv
# JSON Naming Convention: {Customer ID}_Hardware_{UniqueReportID}.json
def pxc_hardware_reports():
    print("******************************************************************")
    print("****************** Running Hardware Report ***********************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(hardware, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "successTrackId," \
                         "useCaseId," \
                         "assetId," \
                         "hwInstanceId," \
                         "assetName," \
                         "productFamily," \
                         "productId," \
                         "serialNumber," \
                         "endOfLifeAnnounced," \
                         "endOfSale," \
                         "lastShip," \
                         "endOfRoutineFailureAnalysis," \
                         "endOfNewServiceAttach," \
                         "endOfServiceContractRenewal," \
                         "ldosDate," \
                         "coverageEndDate," \
                         "coverageStartDate," \
                         "contractNumber," \
                         "coverageStatus"
            writeheader = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writeheader.writerow(CSV_Header.split())
    with open(customers, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            successTrackId = row['successTrackId']
            customerName = row['customerName']
            if debug_level == 1 or debug_level == 2:
                print("====================\n\n")
                print("Hardware data for Customer:", customerName,
                      "on Success Tracks:", successTrackId)
            if not successTrackId == "N/A":
                url = (pxc_url_customers + "/" + customerId + "/reports")
                data_payload = json.dumps({"reportName": "hardware", "successTrackId": successTrackId})
                headers = {'Authorization': f'Bearer {token}'}
                response = requests.request(
                    "POST",
                    url,
                    headers=headers,
                    data=data_payload,
                    verify=True
                )
                if debug_level == 2:
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                try:
                    if bool(response.headers["location"]) is True:
                        pass
                    else:
                        raise KeyError
                except KeyError:
                    print("\n!!!!!!!!\nException Thrown for", "Customer:", customerName,
                          "on Success Tracks:", successTrackId,
                          "Report Failed to Download\n")
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                    while response.status_code >= 400:
                        print(f"Pausing for {wait_time} seconds before re-request...")
                        time.sleep(wait_time)
                        print("Resuming...")
                        print("Making API Call again with the following...")
                        print("URL: ", url)
                        print("Data Payload: ", data_payload)
                        response = requests.request(
                            "POST",
                            url,
                            headers=headers,
                            data=data_payload,
                            verify=True
                        )
                        print("Report request URL:", url,
                              "\nReport details:", data_payload,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content)
                        print(f"Review for Customer: {customerName} on Success Tracks:{successTrackId} "
                              f"Report Failed to Download\n")
                location = response.headers["location"]
                json_filename = (location.split('/')[-1] + '.json')
                tries = 1
                print("")
                while True:
                    time.sleep(tries)
                    print("Scanning for data...")
                    filename = (temp_dir + location.split('/')[-1] + '.zip')
                    headers = {'Authorization': f'Bearer {token}'}
                    response = requests.request("GET", location, headers=headers, data=payload)
                    if debug_level == 2:
                        print("\nLocation URL Returned:", location,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content, "\nWait Time:", tries)
                    try:
                        with open(filename, 'wb') as file:
                            file.write(response.content)
                        with open(filename, "rb") as file:
                            if file.read() and response.status_code == 200:
                                with zipfile.ZipFile(filename, 'r') as zip_file:
                                    zip_file.extractall(temp_dir)
                                    if tries >= 2:
                                        if debug_level == 2:
                                            print("Success on retry!\nContinuing\n", end="")
                            else:
                                print("\nDownload Failed")
                                raise Exception("File Corrupted")
                        os.remove(filename)
                    except Exception as FileCorruptError:
                        if debug_level == 2:
                            print("\nDeleting file..." + str(filename) + " " +
                                  str(FileCorruptError) + "\nRetrying....", end="")
                            print(f"Pausing for {wait_time} seconds before retrying...", end="")
                        time.sleep(wait_time + tries)  # increase the wait with the number of retries
                        if tries >= 10:
                            break
                    else:
                        break
                    finally:
                        tries += 1
                if useProductionURL == "True":
                    input_json_file = str(temp_dir + customerId + "_Hardware_" + json_filename)
                else:
                    input_json_file = str(temp_dir + json_filename)
                if debug_level == 1 or debug_level == 2:
                    print("\nReading file:", input_json_file)
                with open(input_json_file, 'r', encoding='utf-8') as inputTarget:
                    data = json.load(inputTarget)
                    customerId = data['metadata']['customerId']
                    totalCount = data['metadata']['totalCount']
                    items = data['items']
                if outputFormat == 1 or outputFormat == 3:
                    if totalCount > 0:
                        print(f"\nFound Hardware Data on Success Track {successTrackId} for customer {customerName}")
                        for item in items:
                            assetId = str(item['assetId']).replace(",", "_")
                            hwInstanceId = str(item['hwInstanceId']).replace(",", " ")
                            assetName = str(item['assetName'])
                            productFamily = str(item['productFamily']).replace(",", " ")
                            productId = str(item['productId'])
                            serialNumber = str(item['serialNumber'])
                            successTrack = item['successTrack']
                            endOfLifeAnnounced = str(item['endOfLifeAnnounced'])
                            if endOfLifeAnnounced == "None":
                                endOfLifeAnnounced = ""
                            endOfSale = str(item['endOfSale'])
                            if endOfSale == "None":
                                endOfSale = ""
                            lastShip = str(item['lastShip'])
                            if lastShip == "None":
                                lastShip = ""
                            endOfRoutineFailureAnalysis = str(item['endOfRoutineFailureAnalysis'])
                            if endOfRoutineFailureAnalysis == "None":
                                endOfRoutineFailureAnalysis = ""
                            endOfNewServiceAttach = str(item['endOfNewServiceAttach'])
                            if endOfNewServiceAttach == "None":
                                endOfNewServiceAttach = ""
                            endOfServiceContractRenewal = str(item['endOfServiceContractRenewal'])
                            if endOfServiceContractRenewal == "None":
                                endOfServiceContractRenewal = ""
                            ldosDate = str(item['ldosDate'])
                            if ldosDate == "None":
                                ldosDate = ""
                            coverageEndDate = str(item['coverageEndDate'])
                            if coverageEndDate == "None":
                                coverageEndDate = ""
                            coverageStartDate = str(item['coverageStartDate'])
                            if coverageStartDate == "None":
                                coverageStartDate = ""
                            contractNumber = str(item['contractNumber'])
                            if contractNumber == "None":
                                contractNumber = ""
                            coverageStatus = str(item['coverageStatus'])
                            for track in successTrack:
                                successTracksId = track['id']
                                useCases = track['useCases']
                                for useCase in useCases:
                                    if outputFormat == 1 or outputFormat == 3:
                                        with open(hardware, 'a', encoding="utf-8", newline='') as report_target:
                                            writer = csv.writer(report_target,
                                                                delimiter=' ',
                                                                quotechar=' ',
                                                                quoting=csv.QUOTE_MINIMAL)
                                            CSV_Data = (customerId + ',' +
                                                        successTracksId + ',' +
                                                        useCase + ',' +
                                                        assetId + ',' +
                                                        hwInstanceId + ',' +
                                                        assetName + ',' +
                                                        productFamily + ',' +
                                                        productId + ',' +
                                                        serialNumber + ',' +
                                                        endOfLifeAnnounced + ',' +
                                                        endOfSale + ',' +
                                                        lastShip + ',' +
                                                        endOfRoutineFailureAnalysis + ',' +
                                                        endOfNewServiceAttach + ',' +
                                                        endOfServiceContractRenewal + ',' +
                                                        ldosDate + ',' +
                                                        coverageEndDate + ',' +
                                                        coverageStartDate + ',' +
                                                        contractNumber + ',' +
                                                        coverageStatus)
                                            writer.writerow(CSV_Data.split())
                        if debug_level == 1 or debug_level == 2:
                            print("Success")
                else:
                    print("\nNo Hardware Data Found .... Skipping for Customer:", customerName,
                          "on Success Tracks:", successTrackId,
                          "\nSkipping this record and continuing....\n", end="")
                if outputFormat == 1 or outputFormat == 2:
                    if totalCount > 0:
                        print(f"Saving {json_output_dir}{customerId}_Hardware_{json_filename}")
                        shutil.copy(input_json_file, json_output_dir)
                    os.remove(input_json_file)
            else:
                print("\nNo Hardware Data Found For Customer:", customerName,
                      "\nSkipping this record and continuing....")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to request, download and process Software report data from PX Cloud
# Software report will provide details about the software installed on a device.
# CSV Naming Convention: Software.csv
# JSON Naming Convention: {Customer ID}_Software_{UniqueReportID}.json
def pxc_software_reports():
    print("******************************************************************")
    print("******************* Running Software Report **********************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(software, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "successTrackId," \
                         "useCaseId," \
                         "assetName," \
                         "assetId," \
                         "productId," \
                         "softwareType," \
                         "softwareRelease," \
                         "endOfLifeAnnounced," \
                         "endOfSoftwareMaintenance," \
                         "endOfSale," \
                         "lastShip," \
                         "endOfVulnerabilitySecuritySupport," \
                         "ldosDate"
            writeheader = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writeheader.writerow(CSV_Header.split())
    with open(customers, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            successTrackId = row['successTrackId']
            customerName = row['customerName']
            if debug_level == 1 or debug_level == 2:
                print("====================\n\n")
                print("Software data for Customer:", customerName,
                      "on Success Tracks:", successTrackId)
            if not successTrackId == "N/A":
                url = (pxc_url_customers + "/" + customerId + "/reports")
                data_payload = json.dumps({"reportName": "software", "successTrackId": successTrackId})
                headers = {'Authorization': f'Bearer {token}'}
                response = requests.request(
                    "POST",
                    url,
                    headers=headers,
                    data=data_payload,
                    verify=True
                )
                if debug_level == 2:
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                try:
                    if bool(response.headers["location"]) is True:
                        pass
                    else:
                        raise KeyError
                except KeyError:
                    print("\n!!!!!!!!\nException Thrown for", "Customer:", customerName,
                          "on Success Tracks:", successTrackId,
                          "Report Failed to Download\n")
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                    while response.status_code >= 400:
                        print(f"Pausing for {wait_time} seconds before re-request...")
                        time.sleep(wait_time)
                        print("Resuming...")
                        print("Making API Call again with the following...")
                        print("URL: ", url)
                        print("Data Payload: ", data_payload)
                        response = requests.request(
                            "POST",
                            url,
                            headers=headers,
                            data=data_payload,
                            verify=True
                        )
                        print("Report request URL:", url,
                              "\nReport details:", data_payload,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content)
                        print("Review for", "Customer:", customerName, "on Success Tracks:", successTrackId,
                              "Report Failed to Download\n")
                location = response.headers["location"]
                json_filename = (location.split('/')[-1] + '.json')
                tries = 1
                print("")
                while True:
                    time.sleep(tries)
                    print("Scanning for data...")
                    filename = (temp_dir + location.split('/')[-1] + '.zip')
                    headers = {'Authorization': f'Bearer {token}'}
                    response = requests.request("GET", location, headers=headers, data=payload)
                    if debug_level == 2:
                        print("\nLocation URL Returned:", location,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content, "\nWait Time:", tries)
                    try:
                        with open(filename, 'wb') as file:
                            file.write(response.content)
                        with open(filename, "rb") as file:
                            if file.read() and response.status_code == 200:
                                with zipfile.ZipFile(filename, 'r') as zip_file:
                                    zip_file.extractall(temp_dir)
                                    if tries >= 2:
                                        if debug_level == 2:
                                            print("Success on retry!\nContinuing\n", end="")
                            else:
                                print("\nDownload Failed")
                                raise Exception("File Corrupted")
                        os.remove(filename)
                    except Exception as FileCorruptError:
                        if debug_level == 2:
                            print("\nDeleting file..." + str(filename) + " " +
                                  str(FileCorruptError) + "\nRetrying....", end="")
                            print(f"Pausing for {wait_time} seconds before retrying...", end="")
                        time.sleep(wait_time + tries)  # increase the wait with the number of retries
                        if tries >= 10:
                            break
                    else:
                        break
                    finally:
                        tries += 1
                if useProductionURL == "True":
                    input_json_file = str(temp_dir + customerId + "_Software_" + json_filename)
                else:
                    input_json_file = str(temp_dir + json_filename)
                if debug_level == 1 or debug_level == 2:
                    print("\nReading file:", input_json_file)
                with open(input_json_file, 'r', encoding='utf-8') as inputTarget:
                    data = json.load(inputTarget)
                    customerId = data['metadata']['customerId']
                    totalCount = data['metadata']['totalCount']
                    items = data['items']
                if outputFormat == 1 or outputFormat == 3:
                    if totalCount > 0:
                        print(f"\nFound Software Data on Success Track {successTrackId} for customer {customerName}")
                        for item in items:
                            assetName = str(item['assetName'])
                            assetId = str(item['assetId']).replace(",", "_")
                            productId = str(item['productId'])
                            softwareType = str(item['softwareType']).replace(",", " ")
                            softwareRelease = str(item['softwareRelease'])
                            successTrack = item['successTrack']
                            endOfLifeAnnounced = str(item['endOfLifeAnnounced'])
                            if endOfLifeAnnounced == "None":
                                endOfLifeAnnounced = ""
                            endOfSoftwareMaintenance = str(item['endOfSoftwareMaintenance'])
                            if endOfSoftwareMaintenance == "None":
                                endOfSoftwareMaintenance = ""
                            endOfSale = str(item['endOfSale'])
                            if endOfSale == "None":
                                endOfSale = ""
                            lastShip = str(item['lastShip'])
                            if lastShip == "None":
                                lastShip = ""
                            endOfVulnerabilitySecuritySupport = str(item['endOfVulnerabilitySecuritySupport'])
                            if endOfVulnerabilitySecuritySupport == "None":
                                endOfVulnerabilitySecuritySupport = ""
                            ldosDate = str(item['ldosDate'])
                            if ldosDate == "None":
                                ldosDate = ""
                            for track in successTrack:
                                successTrackId = track['id']
                                useCases = track['useCases']
                                for useCase in useCases:
                                    if outputFormat == 1 or outputFormat == 3:
                                        with open(software, 'a', encoding="utf-8", newline='') as report_target:
                                            writer = csv.writer(report_target,
                                                                delimiter=' ',
                                                                quotechar=' ',
                                                                quoting=csv.QUOTE_MINIMAL)
                                            CSV_Data = (customerId + ',' +
                                                        successTrackId + ',' +
                                                        useCase + ',' +
                                                        assetName + ',' +
                                                        assetId + ',' +
                                                        productId + ',' +
                                                        softwareType + ',' +
                                                        softwareRelease + ',' +
                                                        endOfLifeAnnounced + ',' +
                                                        endOfSoftwareMaintenance + ',' +
                                                        endOfSale + ',' +
                                                        lastShip + ',' +
                                                        endOfVulnerabilitySecuritySupport + ',' +
                                                        ldosDate)
                                            writer.writerow(CSV_Data.split())
                        if debug_level == 1 or debug_level == 2:
                            print("Success")
                else:
                    print("\nNo Software Data Found for Customer:", customerName,
                          "\nSkipping this record and continuing....\n", end="")
                if outputFormat == 1 or outputFormat == 2:
                    if totalCount > 0:
                        print(f"Saving {json_output_dir}{customerId}_Software_{json_filename}")
                        shutil.copy(input_json_file, json_output_dir)
                    os.remove(input_json_file)
            else:
                print("\nNo Software Data Found For Customer:", customerName,
                      "\nSkipping this record and continuing....")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to request, download and process Purchased Licenses report data from PX Cloud
# This report provide details of all the licenses.
# CSV Naming Convention: Purchased_Licenses.csv
# JSON Naming Convention: {Customer ID}_Purchased_Licenses_{UniqueReportID}.json
def pxc_purchased_licenses_reports():
    print("******************************************************************")
    print("****************** Running Purchased Licenses ********************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(purchasedLicenses, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "successTrackId," \
                         "useCaseId," \
                         "licenseId," \
                         "licenseLevel," \
                         "purchasedQuantity," \
                         "productFamily," \
                         "licenseStartDate," \
                         "licenseEndDate," \
                         "contractNumber"
            writeheader = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writeheader.writerow(CSV_Header.split())
    with open(customers, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            successTrackId = row['successTrackId']
            customerName = row['customerName']
            if debug_level == 1 or debug_level == 2:
                print("====================\n\n")
                print("Purchased Licenses data for Customer:", customerName,
                      "on Success Tracks:", successTrackId)
            if not successTrackId == "N/A":
                url = (pxc_url_customers + "/" + customerId + "/reports")
                data_payload = json.dumps({"reportName": "PurchasedLicenses", "successTrackId": successTrackId})
                headers = {'Authorization': f'Bearer {token}'}
                response = requests.request(
                    "POST",
                    url,
                    headers=headers,
                    data=data_payload,
                    verify=True
                )
                if debug_level == 2:
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                try:
                    if bool(response.headers["location"]) is True:
                        pass
                    else:
                        raise KeyError
                except KeyError:
                    print("\n!!!!!!!!\nException Thrown for", "Customer:", customerName,
                          "on Success Tracks:", successTrackId,
                          "Report Failed to Download\n")
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                    while response.status_code >= 400:
                        print(f"Pausing for {wait_time} seconds before re-request...")
                        time.sleep(wait_time)
                        print("Resuming...")
                        print("Making API Call again with the following...")
                        print("URL: ", url)
                        print("Data Payload: ", data_payload)
                        response = requests.request(
                            "POST",
                            url,
                            headers=headers,
                            data=data_payload,
                            verify=True
                        )
                        print("Report request URL:", url,
                              "\nReport details:", data_payload,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content)
                        print("Review for", "Customer:", customerId, "on Success Tracks:", successTrackId,
                              "Report Failed to Download\n")
                location = response.headers["location"]
                json_filename = (location.split('/')[-1] + '.json')
                tries = 1
                print("")
                while True:
                    time.sleep(tries)
                    print("Scanning for data...")
                    filename = (temp_dir + location.split('/')[-1] + '.zip')
                    headers = {'Authorization': f'Bearer {token}'}
                    response = requests.request("GET", location, headers=headers, data=payload)
                    if debug_level == 2:
                        print("\nLocation URL Returned:", location,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content, "\nWait Time:", tries)
                    try:
                        with open(filename, 'wb') as file:
                            file.write(response.content)
                        with open(filename, "rb") as file:
                            if file.read() and response.status_code == 200:
                                with zipfile.ZipFile(filename, 'r') as zip_file:
                                    zip_file.extractall(temp_dir)
                                    if tries >= 2:
                                        if debug_level == 2:
                                            print("Success on retry!\nContinuing\n", end="")
                            else:
                                print("Download Failed")
                                raise Exception("File Corrupted")
                        os.remove(filename)
                    except Exception as FileCorruptError:
                        if debug_level == 2:
                            print("\nDeleting file..." + str(filename) + " " +
                                  str(FileCorruptError) + "\nRetrying....", end="")
                            print(f"Pausing for {wait_time} seconds before retrying...", end="")
                        time.sleep(wait_time + tries)  # increase the wait with the number of retries
                        if tries >= 10:
                            break
                    else:
                        break
                    finally:
                        tries += 1
                if useProductionURL == "True":
                    input_json_file = str(temp_dir + customerId + "_PurchasedLicenses_" + json_filename)
                else:
                    input_json_file = str(temp_dir + json_filename)
                if debug_level == 1 or debug_level == 2:
                    print("\nReading file:", input_json_file)
                with open(input_json_file, 'r', encoding='utf-8') as inputTarget:
                    data = json.load(inputTarget)
                    customerId = data['metadata']['customerId']
                    totalCount = data['metadata']['totalCount']
                    items = data['items']
                if outputFormat == 1 or outputFormat == 3:
                    if totalCount > 0:
                        print(f"\nFound Purchased Licenses Data on Success Track {successTrackId} "
                              f"for customer {customerName}")
                        for item in items:
                            licenseId = str(item['license'])
                            licenseLevel = str(item['licenseLevel'])
                            purchasedQuantity = str(item['purchasedQuantity'])
                            productFamily = str(item['productFamily'])
                            licenseStartDate = str(item['licenseStartDate'])
                            if licenseStartDate == "None":
                                licenseStartDate = ""
                            licenseEndDate = str(item['licenseEndDate'])
                            if licenseEndDate == "None":
                                licenseEndDate = ""
                            contractNumber = str(item['contractNumber'])
                            if contractNumber == "None":
                                contractNumber = ""
                            successTrack = item['successTrack']
                            for track in successTrack:
                                successTracksId = track['id']
                                useCases = track['useCases']
                                for useCase in useCases:
                                    useCaseId = useCase
                                    if outputFormat == 1 or outputFormat == 3:
                                        with open(purchasedLicenses, 'a', encoding="utf-8", newline='') \
                                                as report_target:
                                            writer = csv.writer(report_target,
                                                                delimiter=' ',
                                                                quotechar=' ',
                                                                quoting=csv.QUOTE_MINIMAL)
                                            CSV_Data = (customerId + ',' +
                                                        successTracksId + ',' +
                                                        useCaseId + "," +
                                                        licenseId + ',' +
                                                        licenseLevel + ',' +
                                                        purchasedQuantity + ',' +
                                                        productFamily + ',' +
                                                        licenseStartDate + ',' +
                                                        licenseEndDate + ',' +
                                                        contractNumber)
                                            writer.writerow(CSV_Data.split())
                        if debug_level == 1 or debug_level == 2:
                            print("Success")
                else:
                    print("\nNo Purchased Licenses Data Found .... Skipping for Customer:", customerName,
                          "\nSkipping this record and continuing....\n", end="")
                if outputFormat == 1 or outputFormat == 2:
                    if totalCount > 0:
                        print(f"Saving {json_output_dir}{customerId}_Purchased Licenses_{json_filename}")
                        shutil.copy(input_json_file, json_output_dir)
                    os.remove(input_json_file)
            else:
                print("\nNo Purchased Licenses Data Found For Customer:", customerName,
                      "\nSkipping this record and continuing....")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to request, download and process Licenses report data from PX Cloud
# It provides License details along with related asset information.
# CSV Naming Convention: Licenses.csv
# JSON Naming Convention: {Customer ID}_Licenses_{UniqueReportID}.json
def pxc_licenses_reports():
    print("******************************************************************")
    print("******************** Running License Report **********************")
    print("******************************************************************")
    print("Searching ......")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(licenses, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "successTrackId," \
                         "useCaseId," \
                         "assetName," \
                         "assetId," \
                         "productFamily," \
                         "productType," \
                         "connectionStatus," \
                         "productDescription," \
                         "licenseId," \
                         "licenseStartDate," \
                         "licenseEndDate," \
                         "contractNumber," \
                         "subscriptionId," \
                         "supportType"
            writeheader = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writeheader.writerow(CSV_Header.split())
    with open(customers, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            successTrackId = row['successTrackId']
            customerName = row['customerName']
            if debug_level == 1 or debug_level == 2:
                print("====================\n\n")
                print("License data for Customer:", customerName,
                      "on Success Tracks:", successTrackId)
            if not successTrackId == "N/A":
                url = (pxc_url_customers + "/" + customerId + "/reports")
                data_payload = json.dumps({"reportName": "Licenses", "successTrackId": successTrackId})
                headers = {'Authorization': f'Bearer {token}'}
                response = requests.request(
                    "POST",
                    url,
                    headers=headers,
                    data=data_payload,
                    verify=True
                )
                if debug_level == 2:
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                try:
                    if bool(response.headers["location"]) is True:
                        pass
                    else:
                        raise KeyError
                except KeyError:
                    print("\n!!!!!!!!\nException Thrown for", "Customer:", customerName,
                          "on Success Tracks:", successTrackId,
                          "Report Failed to Download\n")
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                    while response.status_code >= 400:
                        print(f"Pausing for {wait_time} seconds before re-request...")
                        time.sleep(wait_time)
                        print("Resuming...")
                        print("Making API Call again with the following...")
                        print("URL: ", url)
                        print("Data Payload: ", data_payload)
                        response = requests.request(
                            "POST",
                            url,
                            headers=headers,
                            data=data_payload,
                            verify=True
                        )
                        print("Report request URL:", url,
                              "\nReport details:", data_payload,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content)
                        print("Review for", "Customer:", customerName, "on Success Tracks:", successTrackId,
                              "Report Failed to Download\n")
                location = response.headers["location"]
                json_filename = (location.split('/')[-1] + '.json')
                tries = 1
                print("")
                while True:
                    time.sleep(tries)
                    print("Scanning for data...")
                    filename = (temp_dir + location.split('/')[-1] + '.zip')
                    headers = {'Authorization': f'Bearer {token}'}
                    response = requests.request("GET", location, headers=headers, data=payload)
                    if debug_level == 2:
                        print("\nLocation URL Returned:", location,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content, "\nWait Time:", tries)

                    try:
                        with open(filename, 'wb') as file:
                            file.write(response.content)
                        with open(filename, "rb") as file:
                            if file.read() and response.status_code == 200:
                                with zipfile.ZipFile(filename, 'r') as zip_file:
                                    zip_file.extractall(temp_dir)
                                    if tries >= 2:
                                        if debug_level == 2:
                                            print("Success on retry!\nContinuing\n", end="")
                            else:
                                print("Download Failed")
                                raise Exception("File Corrupted")
                        os.remove(filename)
                    except Exception as FileCorruptError:
                        if debug_level == 2:
                            print("\nDeleting file..." + str(filename) + " " +
                                  str(FileCorruptError) + "\nRetrying....", end="")
                            print(f"Pausing for {wait_time} seconds before retrying...", end="")
                        time.sleep(wait_time + tries)  # increase the wait with the number of retries
                        if tries >= 10:
                            break
                    else:
                        break
                    finally:
                        tries += 1
                if useProductionURL == "True":
                    input_json_file = str(temp_dir + customerId + "_Licenses_" + json_filename)
                else:
                    input_json_file = str(temp_dir + json_filename)
                if debug_level == 1 or debug_level == 2:
                    print("\nReading file:", input_json_file)
                with open(input_json_file, 'r', encoding='utf-8') as inputTarget:
                    data = json.load(inputTarget)
                    customerId = data['metadata']['customerId']
                    totalCount = data['metadata']['totalCount']
                    items = data['items']
                if outputFormat == 1 or outputFormat == 3:
                    if totalCount > 0:
                        print(f"\nFound License Data on Success Track {successTrackId} for customer {customerName}")
                        for item in items:
                            assetId = str(item['assetId']).replace(",", "_")
                            assetName = str(item['assetName']).replace(",", " ")
                            productFamily = str(item['productFamily']).replace(",", " ")
                            productType = str(item['productType']).replace(",", " ")
                            connectionStatus = str(item['connectionStatus'])
                            productDescription = str(item['productDescription']).replace(",", " ")
                            licenseId = str(item['license'])
                            try:
                                licenseStartDate = str(item['licenseStartDate'])
                                if licenseStartDate == "None":
                                    licenseStartDate = ""
                            except KeyError:
                                licenseStartDate = ""
                                pass
                            try:
                                licenseEndDate = str(item['licenseEndDate'])
                                if licenseEndDate == "None":
                                    licenseEndDate = ""
                            except KeyError:
                                licenseEndDate = ""
                                pass
                            try:
                                contractNumber = str(item['contractNumber'])
                                if contractNumber == "None":
                                    contractNumber = ""
                            except KeyError:
                                contractNumber = ""
                                pass
                            subscriptionId = str(item['subscriptionId'])
                            supportType = str(item['supportType']).replace(",", " ")
                            successTrack = item['successTrack']
                            for track in successTrack:
                                successTracksId = track['id']
                                useCases = track['useCases']
                                for useCase in useCases:
                                    useCaseId = useCase
                                    if outputFormat == 1 or outputFormat == 3:
                                        with open(licenses, 'a', encoding="utf-8", newline='') as report_target:
                                            writer = csv.writer(report_target,
                                                                delimiter=' ',
                                                                quotechar=' ',
                                                                quoting=csv.QUOTE_MINIMAL)
                                            CSV_Data = (customerId + ',' +
                                                        successTracksId + ',' +
                                                        useCaseId + ',' +
                                                        assetName + ',' +
                                                        assetId + ',' +
                                                        productFamily + ',' +
                                                        productType + ',' +
                                                        connectionStatus + ',' +
                                                        productDescription + ',' +
                                                        licenseId + ',' +
                                                        licenseStartDate + ',' +
                                                        licenseEndDate + ',' +
                                                        contractNumber + ',' +
                                                        subscriptionId + ',' +
                                                        supportType)
                                            writer.writerow(CSV_Data.split())
                        if debug_level == 1 or debug_level == 2:
                            print("Success")
                else:
                    print("\nNo License Data Found .... Skipping for Customer:", customerName,
                          "\nSkipping this record and continuing....\n", end="")
                if outputFormat == 1 or outputFormat == 2:
                    if totalCount > 0:
                        print(f"Saving JSON file for customer {customerName} on success track {successTrackId}")
                        shutil.copy(input_json_file, json_output_dir)
                    os.remove(input_json_file)
            else:
                print(f"\nNo License Data Found For Customer: {customerName} on success track:{successTrackId}"
                      f"\nSkipping this record and continuing....")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to get the Lifecycle data from PX Cloud
# This API will return customer lifecycle which will provide the following:CX solution, Use case and Pitstop info.
# CSV Naming Convention: Lifecycle.csv
# JSON Naming Convention: {Customer ID}_Lifecycle.json
def get_pxc_lifecycle():
    print("******************************************************************")
    print("****************** Running Lifecycle Report **********************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(lifecycle, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerName," \
                         "successTracksId," \
                         "successTrackName," \
                         "useCaseName," \
                         "useCaseId," \
                         "currentPitstopName," \
                         "pitStopName," \
                         "pitstopActionName," \
                         "pitstopActionId," \
                         "pitstopActionCompleted"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(customers, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            if debug_level == 1 or debug_level == 2:
                print("====================\n\n")
                print("Lifecycle data for Customer:", customerName,
                      "on Success Tracks:", successTrackId)
            if not successTrackId == "N/A":
                items = (get_json_reply(url=(
                        pxc_url_customers + "/" +
                        customerId +
                        pxc_url_lifecycle +
                        "?successTrackId=" + successTrackId), tag="items"))
                if outputFormat == 1 or outputFormat == 3:
                    if items is not None:
                        if len(items) > 0:
                            print(f"\nFound Lifecycle Data on Success Track {successTrackId} for customer "
                                  f"{customerName}")
                            for item in items:
                                successTrackName = item['successTrack'].replace(",", " ")
                                successTracksId = item['id'].replace(",", " ")
                                useCases = item['usecases']
                                for useCase in useCases:
                                    useCaseName = useCase['name'].replace(",", " ")
                                    useCaseId = useCase['id'].replace(",", " ")
                                    currentPitstopName = useCase['currentPitstop'].replace(",", " ")
                                    pitstops = useCase['pitstops']
                                    for pitstop in pitstops:
                                        pitstopName = pitstop['name'].replace(",", " ")
                                        pitstopActions = pitstop['pitstopActions']
                                        for pitstopAction in pitstopActions:
                                            pitstopActionName = pitstopAction['name'].replace(",", " ")
                                            pitstopActionId = pitstopAction['id'].replace(",", " ")
                                            pitstopActionCompleted = pitstopAction['completed']
                                            if outputFormat == 1 or outputFormat == 3:
                                                with open(lifecycle, 'a', encoding="utf-8", newline='') \
                                                        as lifecycle_target:
                                                    writer = csv.writer(lifecycle_target,
                                                                        delimiter=' ',
                                                                        quotechar=' ',
                                                                        quoting=csv.QUOTE_MINIMAL)
                                                    CSV_Data = (customerName + ',' +
                                                                successTracksId + ',' +
                                                                successTrackName + ',' +
                                                                useCaseName + ',' +
                                                                useCaseId + ',' +
                                                                currentPitstopName + ',' +
                                                                pitstopName + ',' +
                                                                pitstopActionName + ',' +
                                                                pitstopActionId + ',' +
                                                                str(pitstopActionCompleted))
                                                    writer.writerow(CSV_Data.split())
                if outputFormat == 1 or outputFormat == 2:
                    if items is not None:
                        if len(items) > 0:
                            with open(json_output_dir + customerId + "_Lifecycle_" + successTrackId + ".json",
                                      'w') as json_file:
                                json.dump(items, json_file)
                            print(f"Saving {json_file.name}")
            else:
                print(f"\nNo Data Found For Customer: {customerName} on success track:{successTrackId}"
                      f"\nSkipping this record and continuing....")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to request, download and process Security Advisories report data from PX Cloud
# This API provides security vulnerability information including CVE and CVSS for devices associated with customer ID.
# CSV Naming Convention: Security_Advisories.csv
# JSON Naming Convention: {Customer ID}_SecurityAdvisories_{UniqueReportID}.json
def pxc_security_advisories_reports():
    print("******************************************************************")
    print("****************** Running Security Advisories *******************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(securityAdvisories, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "successTrackId," \
                         "useCaseId," \
                         "assetName," \
                         "assetId," \
                         "ipAddress," \
                         "serialNumber," \
                         "advisoryId," \
                         "impact," \
                         "cvss," \
                         "version," \
                         "cve," \
                         "published," \
                         "updated," \
                         "advisory," \
                         "summary," \
                         "url," \
                         "additionalNotes," \
                         "affectedStatus," \
                         "affectedReason," \
                         "softwareRelease," \
                         "productId"
            writeheader = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writeheader.writerow(CSV_Header.split())
    with open(customers, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            successTrackId = row['successTrackId']
            customerName = row['customerName']
            if debug_level == 1 or debug_level == 2:
                print("====================\n\n")
                print("Security Advisories for Customer:", customerName,
                      "on Success Tracks:", successTrackId)
            if not successTrackId == "N/A":
                url = (pxc_url_customers + "/" + customerId + "/reports")
                data_payload = json.dumps({"reportName": "securityadvisories", "successTrackId": successTrackId})
                headers = {'Authorization': f'Bearer {token}'}
                response = requests.request(
                    "POST",
                    url,
                    headers=headers,
                    data=data_payload,
                    verify=True
                )
                if debug_level == 2:
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                try:
                    if bool(response.headers["location"]) is True:
                        pass
                    else:
                        raise KeyError
                except KeyError:
                    print("\n!!!!!!!!\nException Thrown for", "Customer:", customerName,
                          "on Success Tracks:", successTrackId,
                          "Report Failed to Download\n")
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                    while response.status_code >= 400:
                        print(f"Pausing for {wait_time} seconds before re-request...")
                        time.sleep(wait_time)
                        print("Resuming...")
                        print("Making API Call again with the following...")
                        print("URL: ", url)
                        print("Data Payload: ", data_payload)
                        response = requests.request(
                            "POST",
                            url,
                            headers=headers,
                            data=data_payload,
                            verify=True
                        )
                        print("Report request URL:", url,
                              "\nReport details:", data_payload,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content)
                        print("Review for", "Customer:", customerName, "on Success Tracks:", successTrackId,
                              "Report Failed to Download\n")
                location = response.headers["location"]
                json_filename = (location.split('/')[-1] + '.json')
                tries = 1
                print("")
                while True:
                    time.sleep(tries)
                    print("Scanning for data...")
                    filename = (temp_dir + location.split('/')[-1] + '.zip')
                    headers = {'Authorization': f'Bearer {token}'}
                    response = requests.request("GET", location, headers=headers, data=payload)
                    if debug_level == 2:
                        print("\nLocation URL Returned:", location,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content, "\nWait Time:", tries)
                    try:
                        with open(filename, 'wb') as file:
                            file.write(response.content)
                        with open(filename, "rb") as file:
                            if file.read() and response.status_code == 200:
                                with zipfile.ZipFile(filename, 'r') as zip_file:
                                    zip_file.extractall(temp_dir)
                                    if tries >= 2:
                                        if debug_level == 2:
                                            print("Success on retry!\nContinuing\n", end="")
                            else:
                                print("\nDownload Failed :", filename)
                                raise Exception("File Corrupted")
                        os.remove(filename)
                    except Exception as FileCorruptError:
                        if debug_level == 2:
                            print("\nDeleting file..." + str(filename) + " " +
                                  str(FileCorruptError) + "\nRetrying....", end="")
                            print(f"Pausing for {wait_time} seconds before retrying...", end="")
                        time.sleep(wait_time + tries)  # increase the wait with the number of retries
                        if tries >= 10:
                            break
                    else:
                        break
                    finally:
                        tries += 1
                if useProductionURL == "True":
                    input_json_file = str(temp_dir + customerId + "_SecurityAdvisories_" + json_filename)
                else:
                    input_json_file = str(temp_dir + json_filename)
                if debug_level == 1 or debug_level == 2:
                    print("\nReading file:", input_json_file)
                with open(input_json_file, 'r', encoding='utf-8') as inputTarget:
                    data = json.load(inputTarget)
                    customerId = data['metadata']['customerId']
                    totalCount = data['metadata']['totalCount']
                    items = data['items']
                if outputFormat == 1 or outputFormat == 3:
                    if totalCount > 0:
                        print(f"\nFound Security Advisories on Success Track {successTrackId} for customer "
                              f"{customerName}")
                        for item in items:
                            assetName = str(item['assetName'])
                            assetId = str(item['assetId']).replace(",", "_")
                            ipAddress = str(item['ipAddress'])
                            serialNumber = str(item['serialNumber'])
                            successTrack = item['successTrack']
                            advisoryId = str(item['advisoryId']).replace(",", " ")
                            impact = str(item['impact']).replace(",", " ")
                            cvss = str(item['cvss']).replace(",", " ")
                            version = str(item['version'])
                            cve = str(item['cve']).replace(",", " ")
                            published = str(item['published']).replace(",", " ")
                            updated = str(item['updated'])
                            advisory = str(item['advisory']).replace(",", " ")
                            summary = str(item['summary']).replace(",", " ")
                            url = str(item['url']).replace(",", " ")
                            additionalNotes = str(item['additionalNotes']).replace(",", " ")
                            affectedStatus = str(item['affectedStatus'])
                            affectedReasons = item['affectedReason']
                            softwareRelease = str(item['softwareRelease'])
                            productId = str(item['productId'])
                            for track in successTrack:
                                successTrackId = track['id']
                                useCases = track['useCases']
                                for useCase in useCases:
                                    useCaseId = useCase
                                    for reason in affectedReasons:
                                        affectedReason = reason
                                        with open(securityAdvisories, 'a', encoding="utf-8", newline='') \
                                                as report_target:
                                            writer = csv.writer(report_target,
                                                                delimiter=' ',
                                                                quotechar=' ',
                                                                quoting=csv.QUOTE_MINIMAL)
                                            CSV_Data = (customerId + ',' +
                                                        successTrackId + ',' +
                                                        useCaseId + ',' +
                                                        assetName + ',' +
                                                        assetId + ',' +
                                                        ipAddress + ',' +
                                                        serialNumber + ',' +
                                                        advisoryId + ',' +
                                                        impact + ',' +
                                                        cvss + ',' +
                                                        version + ',' +
                                                        cve + ',' +
                                                        published + ',' +
                                                        updated + ',' +
                                                        advisory + ',' +
                                                        summary + ',' +
                                                        url + ',' +
                                                        additionalNotes + ',' +
                                                        affectedStatus + ',' +
                                                        affectedReason + ',' +
                                                        softwareRelease + ',' +
                                                        productId)
                                            writer.writerow(CSV_Data.split())
                        if debug_level == 1 or debug_level == 2:
                            print("Success")
                else:
                    print("\nNo Security Advisories Data Found For Customer:", customerId,
                          "\nSkipping this record and continuing....\n", end="")
                if outputFormat == 1 or outputFormat == 2:
                    if totalCount > 0:
                        print(f"Saving {json_output_dir}{customerId}_SecurityAdvisories_{json_filename}")
                        shutil.copy(input_json_file, json_output_dir)
                    os.remove(input_json_file)
            else:
                print("\nNo Security Advisories Data Found For Customer:", customerName,
                      "\nSkipping this record and continuing....")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to request, download and process Field Notices report data from PX Cloud
# This API gives details of all the notifications published and their associated details.
# CSV Naming Convention: Field_Notices.csv
# JSON Naming Convention: {Customer ID}_Field_Notices_{UniqueReportID}.json
def pxc_field_notices_reports():
    print("******************************************************************")
    print("******************** Running Field Notices ***********************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(fieldNotices, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "successTrackId," \
                         "useCaseId," \
                         "assetName," \
                         "assetId," \
                         "hwInstanceId," \
                         "productId," \
                         "serialNumber," \
                         "fieldNoticeId," \
                         "updated," \
                         "title," \
                         "created," \
                         "url," \
                         "additionalNotes," \
                         "affectedStatus," \
                         "affectedReason," \
                         "fieldNoticeDescription," \
                         "softwareRelease," \
                         "ipAddress"
            writeheader = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writeheader.writerow(CSV_Header.split())
    with open(customers, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            successTrackId = row['successTrackId']
            customerName = row['customerName']
            if debug_level == 1 or debug_level == 2:
                print("====================\n\n")
                print("Field Notices for Customer:", customerName,
                      "on Success Tracks:", successTrackId)
            if not successTrackId == "N/A":
                url = (pxc_url_customers + "/" + customerId + "/reports")
                data_payload = json.dumps({"reportName": "FieldNotices", "successTrackId": successTrackId})
                headers = {'Authorization': f'Bearer {token}'}
                response = requests.request(
                    "POST",
                    url,
                    headers=headers,
                    data=data_payload,
                    verify=True
                )
                if debug_level == 2:
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                try:
                    if bool(response.headers["location"]) is True:
                        pass
                    else:
                        raise KeyError
                except KeyError:
                    print("\n!!!!!!!!\nException Thrown for", "Customer:", customerName,
                          "on Success Tracks:", successTrackId,
                          "Report Failed to Download\n")
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                    while response.status_code >= 400:
                        print(f"Pausing for {wait_time} seconds before re-request...")
                        time.sleep(wait_time)
                        print("Resuming...")
                        print("Making API Call again with the following...")
                        print("URL: ", url)
                        print("Data Payload: ", data_payload)
                        response = requests.request(
                            "POST",
                            url,
                            headers=headers,
                            data=data_payload,
                            verify=True
                        )
                        print("Report request URL:", url,
                              "\nReport details:", data_payload,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content)
                        print("Review for", "Customer:", customerName, "on Success Tracks:", successTrackId,
                              "Report Failed to Download\n")
                location = response.headers["location"]
                json_filename = (location.split('/')[-1] + '.json')
                tries = 1
                print("")
                while True:
                    time.sleep(tries)
                    print("Scanning for data...")
                    filename = (temp_dir + location.split('/')[-1] + '.zip')
                    headers = {'Authorization': f'Bearer {token}'}
                    response = requests.request("GET", location, headers=headers, data=payload)
                    if debug_level == 2:
                        print("\nLocation URL Returned:", location,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content, "\nWait Time:", tries)
                    try:
                        with open(filename, 'wb') as file:
                            file.write(response.content)
                        with open(filename, "rb") as file:
                            if file.read() and response.status_code == 200:
                                with zipfile.ZipFile(filename, 'r') as zip_file:
                                    zip_file.extractall(temp_dir)
                                    if tries >= 2:
                                        if debug_level == 2:
                                            print("Success on retry!\nContinuing\n", end="")
                            else:
                                print("\nDownload Failed")
                                raise Exception("File Corrupted")
                        os.remove(filename)
                    except Exception as FileCorruptError:
                        if debug_level == 2:
                            print("\nDeleting file..." + str(filename) + " " +
                                  str(FileCorruptError) + "\nRetrying....", end="")
                            print(f"Pausing for {wait_time} seconds before retrying...", end="")
                        time.sleep(wait_time + tries)  # increase the wait with the number of retries
                        if tries >= 10:
                            break
                    else:
                        break
                    finally:
                        tries += 1
                if useProductionURL == "True":
                    input_json_file = str(temp_dir + customerId + "_FieldNotices_" + json_filename)
                else:
                    input_json_file = str(temp_dir + json_filename)
                if debug_level == 1 or debug_level == 2:
                    print("\nReading file:", input_json_file)
                with open(input_json_file, 'r', encoding='utf-8') as inputTarget:
                    data = json.load(inputTarget)
                    customerId = data['metadata']['customerId']
                    totalCount = data['metadata']['totalCount']
                    items = data['items']
                if outputFormat == 1 or outputFormat == 3:
                    if totalCount > 0:
                        print(f"\nFound Field Notices on Success Track {successTrackId} for customer {customerName}")
                        for item in items:
                            assetId = str(item['assetId']).replace(",", "_")
                            hwInstanceId = str(item['hwInstanceId']).replace(",", " ")
                            assetName = str(item['assetName'])
                            productId = str(item['productId'])
                            serialNumber = str(item['serialNumber'])
                            successTrack = item['successTrack']
                            fieldNoticeId = str(item['fieldNoticeId'])
                            updated = str(item['updated']).replace(",", " ")
                            title = str(item['title']).replace(",", " ")
                            created = str(item['created'])
                            url = str(item['url']).replace(",", " ")
                            additionalNotes = str(item['additionalNotes']).replace(",", " ")
                            affectedStatus = str(item['affectedStatus'])
                            affectedReasons = item['affectedReason']
                            fieldNoticeDescription = str(item['fieldNoticeDescription']).replace(",", " ")
                            softwareRelease = str(item['softwareRelease'])
                            if not softwareRelease:
                                softwareRelease = "N/A"
                            ipAddress = str(item['ipAddress'])
                            if not ipAddress:
                                ipAddress = 'N/A'
                            for track in successTrack:
                                successTrackId = track['id']
                                useCases = track['useCases']
                                for useCase in useCases:
                                    useCaseId = useCase
                                    for reason in affectedReasons:
                                        affectedReason = reason
                                        if outputFormat == 1 or outputFormat == 3:
                                            with open(fieldNotices, 'a', encoding="utf-8", newline='') \
                                                    as report_target:
                                                writer = csv.writer(report_target,
                                                                    delimiter=' ',
                                                                    quotechar=' ',
                                                                    quoting=csv.QUOTE_MINIMAL)
                                                CSV_Data = (customerId + ',' +
                                                            successTrackId + ',' +
                                                            useCaseId + ',' +
                                                            assetName + ',' +
                                                            assetId + ',' +
                                                            hwInstanceId + ',' +
                                                            productId + ',' +
                                                            serialNumber + ',' +
                                                            fieldNoticeId + ',' +
                                                            updated + ',' +
                                                            title + ',' +
                                                            created + ',' +
                                                            url + ',' +
                                                            additionalNotes + ',' +
                                                            affectedStatus + ',' +
                                                            affectedReason + ',' +
                                                            fieldNoticeDescription + ',' +
                                                            softwareRelease + ',' +
                                                            ipAddress)
                                                writer.writerow(CSV_Data.split())
                        if debug_level == 1 or debug_level == 2:
                            print("Success")
                else:
                    print("\nNo Field Notice Data Found For Customer:", customerName, "on success track id",
                          successTrackId, "\nSkipping this record and continuing....\n", end="")
                if outputFormat == 1 or outputFormat == 2:
                    if totalCount > 0:
                        print(f"Saving {json_output_dir}{customerId}_FieldNotices_{json_filename}")
                        shutil.copy(input_json_file, json_output_dir)
                    os.remove(input_json_file)
            else:
                print("\nNo Field Notice Data Found For Customer:", customerName,
                      "\nSkipping this record and continuing....")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to request, download and process Priority Bugs report data from PX Cloud
# This API provides many bug details including asset name and ID, serial number, IP address and other fields
# CSV Naming Convention: Priority_Bugs.csv
# JSON Naming Convention: {Customer ID}_Priority_Bugs_{UniqueReportID}.json
def pxc_priority_bugs_reports():
    print("******************************************************************")
    print("***************** Running Priority Bugs report *******************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(priorityBugs, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "successTrackId," \
                         "useCaseId," \
                         "assetName," \
                         "assetId," \
                         "serialNumber," \
                         "ipAddress," \
                         "softwareRelease," \
                         "productId," \
                         "bugId," \
                         "bugTitle," \
                         "description," \
                         "url," \
                         "bugSeverity," \
                         "impact"
            writeheader = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writeheader.writerow(CSV_Header.split())
    with open(customers, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            successTrackId = row['successTrackId']
            customerName = row['customerName']
            if debug_level == 1 or debug_level == 2:
                print("====================\n\n")
                print("Priority Bugs for Customer:", customerName, "on Success Tracks:", successTrackId)
            if not successTrackId == "N/A":
                url = (pxc_url_customers + "/" + customerId + "/reports")
                data_payload = json.dumps({"reportName": "prioritybugs", "successTrackId": successTrackId})
                headers = {'Authorization': f'Bearer {token}'}
                response = requests.request(
                    "POST",
                    url,
                    headers=headers,
                    data=data_payload,
                    verify=True
                )
                if debug_level == 2:
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                try:
                    if bool(response.headers["location"]) is True:
                        pass
                    else:
                        raise KeyError
                except KeyError:
                    print("\n!!!!!!!!\nException Thrown for", "Customer:",
                          customerName, "on Success Tracks:", successTrackId,
                          "Report Failed to Download\n")
                    print("Report request URL:", url,
                          "\nReport details:", data_payload,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
                    while response.status_code >= 400:
                        print(f"Pausing for {wait_time} seconds before re-request...")
                        print("Resuming...")
                        print("Making API Call again with the following...")
                        print("URL: ", url)
                        print("Data Payload: ", data_payload)
                        response = requests.request(
                            "POST",
                            url,
                            headers=headers,
                            data=data_payload,
                            verify=True
                        )
                        print("Report request URL:", url,
                              "\nReport details:", data_payload,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content)
                        print("Review for", "Customer:", customerName, "on Success Tracks:", successTrackId,
                              "Report Failed to Download\n")
                location = response.headers["location"]
                json_filename = (location.split('/')[-1] + '.json')
                tries = 1
                print("")
                while True:
                    time.sleep(tries)
                    print("Scanning for data...")
                    filename = (temp_dir + location.split('/')[-1] + '.zip')
                    headers = {'Authorization': f'Bearer {token}'}
                    response = requests.request("GET", location, headers=headers, data=payload)
                    if debug_level == 2:
                        print("\nLocation URL Returned:", location,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content, "\nWait Time:", tries)
                    try:
                        with open(filename, 'wb') as file:
                            file.write(response.content)
                        with open(filename, "rb") as file:
                            if file.read() and response.status_code == 200:
                                with zipfile.ZipFile(filename, 'r') as zip_file:
                                    zip_file.extractall(temp_dir)
                                    if tries >= 2:
                                        if debug_level == 2:
                                            print("Success on retry!\nContinuing\n", end="")
                            else:
                                print("\nDownload Failed")
                                raise Exception("File Corrupted")
                        os.remove(filename)
                    except Exception as FileCorruptError:
                        if debug_level == 2:
                            print("\nDeleting file..." + str(filename) + " " +
                                  str(FileCorruptError) + "\nRetrying....", end="")
                            print(f"Pausing for {wait_time} seconds before retrying...", end="")
                        time.sleep(wait_time + tries)  # increase the wait with the number of retries
                        if tries >= 10:
                            break
                    else:
                        break
                    finally:
                        tries += 1
                if useProductionURL == "True":
                    input_json_file = str(temp_dir + customerId + "_PriorityBugs_" + json_filename)
                else:
                    input_json_file = str(temp_dir + json_filename)
                if debug_level == 1 or debug_level == 2:
                    print("\nReading file:", input_json_file)
                with open(input_json_file, 'r', encoding='utf-8') as inputTarget:
                    data = json.load(inputTarget)
                    customerId = data['metadata']['customerId']
                    totalCount = data['metadata']['totalCount']
                    items = data['items']
                if outputFormat == 1 or outputFormat == 3:
                    if totalCount > 0:
                        print(f"\nFound Priority Bugs on Success Track {successTrackId} for customer {customerName}")
                        for item in items:
                            assetName = str(item['assetName'])
                            assetId = str(item['assetId']).replace(",", "_")
                            serialNumber = str(item['serialNumber'])
                            ipAddress = str(item['ipAddress'])
                            softwareRelease = str(item['softwareRelease'])
                            productId = str(item['productId'])
                            bugId = str(item['bugId']).replace(",", " ")
                            bugTitle = str(item['bugTitle']).replace(",", " ")
                            description = str(item['description']).replace(",", " ")
                            url = str(item['url']).replace(",", " ")
                            bugSeverity = str(item['bugSeverity']).replace(",", " ")
                            successTrack = item['successTrack']
                            impact = str(item['impact']).replace(",", " ")
                            for track in successTrack:
                                successTrackId = track['id']
                                useCases = track['useCases']
                                for useCase in useCases:
                                    useCaseId = useCase
                                    if outputFormat == 1 or outputFormat == 3:
                                        with open(priorityBugs, 'a', encoding="utf-8", newline='') as report_target:
                                            writer = csv.writer(report_target,
                                                                delimiter=' ',
                                                                quotechar=' ',
                                                                quoting=csv.QUOTE_MINIMAL)
                                            CSV_Data = (customerId + ',' +
                                                        successTrackId + ',' +
                                                        useCaseId + ',' +
                                                        assetName + ',' +
                                                        assetId + ',' +
                                                        serialNumber + ',' +
                                                        ipAddress + ',' +
                                                        softwareRelease + ',' +
                                                        productId + ',' +
                                                        bugId + ',' +
                                                        bugTitle + ',' +
                                                        description + ',' +
                                                        url + ',' +
                                                        bugSeverity + ',' +
                                                        impact)
                                            writer.writerow(CSV_Data.split())
                        if debug_level == 1 or debug_level == 2:
                            print("Success")
                else:
                    print("\nNo Priority Bug Data Found For Customer:", customerName, "on Success Tracks:",
                          successTrackId, "\nSkipping this record and continuing....")
                if outputFormat == 1 or outputFormat == 2:
                    if totalCount > 0:
                        print(f"Saving {json_output_dir}{customerId}_PriorityBugs_{json_filename}")
                        shutil.copy(input_json_file, json_output_dir)
                    os.remove(input_json_file)
            else:
                print("\nNo Priority Bug Data Found For Customer", customerName,
                      "\nSkipping this record and continuing....")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")
    exit()


# Functions to get the Optimal Software Version data from PX Cloud (currently only for Campus Network Success Tracks)
# This API returns the Software Group information for the given customerID.
# CSV Naming Convention: SoftwareGroup.csv
# JSON Naming Convention: SoftwareGroup.json
def pxc_software_groups():
    print("******************************************************************")
    print("******************* Running Software Groups **********************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(SWGroups, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "suggestionId," \
                         "riskLevel," \
                         "softwareGroupName," \
                         "sourceId," \
                         "productFamily," \
                         "softwareType," \
                         "currentReleases," \
                         "selectedRelease," \
                         "assetCount," \
                         "suggestions," \
                         "sourceSystemId," \
                         "softwareGroupId"
            writeheader = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writeheader.writerow(CSV_Header.split())
    with open(customers, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            if not successTrackId == "N/A":
                print(" ")
                print("Found Software Groups for Customer:", customerId,
                      "on Success Tracks:", successTrackId)
                url = (pxc_url_customers + "/" +
                       customerId +
                       pxc_url_software_groups +
                       "?offset=1" +
                       "&max=" + max_items +
                       "&successTrackId=" + successTrackId)
                items = (get_json_reply(url, tag="items"))
                if items:
                    if outputFormat == 1 or outputFormat == 2:
                        if items is not None:
                            if len(items) > 0:
                                with open(json_output_dir + customerId + "_SoftwareGroups.json",
                                          'w') as json_file:
                                    json.dump(items, json_file)
                                print(f"Saving {json_file.name}")
                    if outputFormat == 1 or outputFormat == 3:
                        for item in items:
                            riskLevel = item['riskLevel'].replace(",", " ")
                            softwareGroupName = item['softwareGroupName'].replace(",", " ")
                            sourceId = item['sourceId'].replace(",", " ")
                            productFamily = item['productFamily'].replace(",", " ")
                            softwareType = item['softwareType']
                            currentReleases = item['currentReleases'].replace(",", " ")
                            selectedRelease = item['selectedRelease'].replace(",", " ")
                            assetCount = item['assetCount']
                            suggestionId = item['suggestionId']
                            suggestions = item['suggestions']
                            sourceSystemId = item['sourceSystemId'].replace(",", " ")
                            softwareGroupId = item['softwareGroupId'].replace(",", " ")
                            with open(SWGroups, 'a', encoding="utf-8", newline='') as temp_target:
                                writer = csv.writer(temp_target,
                                                    delimiter=' ',
                                                    quotechar=' ',
                                                    quoting=csv.QUOTE_MINIMAL)
                                CSV_Data = (customerId + ',' +
                                            customerName + ',' +
                                            successTrackId + ',' +
                                            suggestionId + ',' +
                                            riskLevel + ',' +
                                            softwareGroupName + ',' +
                                            sourceId + ',' +
                                            productFamily + ',' +
                                            softwareType + ',' +
                                            currentReleases + ',' +
                                            selectedRelease + ',' +
                                            assetCount + ',' +
                                            suggestions + ',' +
                                            sourceSystemId + ',' +
                                            softwareGroupId)
                                writer.writerow(CSV_Data.split())
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# This API returns Software Group suggestions, including detailed information about Cisco software release
# recommendations and current Cisco software releases running on assets in the Software Group.
# CSV Naming Convention: SoftwareGroup_Suggestions_Trends.csv
#                        SoftwareGroup_Suggestions_Summaries.csv
#                        SoftwareGroup_Suggestions_Releases.csv
# JSON Naming Convention: {Customer ID}_SoftwareGroup_Suggestions_{Success Track ID}_{Suggestion ID}.json
def pxc_software_group_suggestions():
    print("******************************************************************")
    print("************* Running Software Groups Suggestions ****************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(SWGroupSuggestionsTrend, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "suggestionId," \
                         "suggestionsInterval," \
                         "suggestionUpdatedDate," \
                         "suggestionSelectedDate," \
                         "changeFromPrev," \
                         "riskCategory," \
                         "trendDate," \
                         "riskScore"
            writeheader = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writeheader.writerow(CSV_Header.split())
        with open(SWGroupSuggestionsReleases, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "suggestionId," \
                         "suggestionsInterval," \
                         "suggestionUpdatedDate," \
                         "suggestionSelectedDate," \
                         "releaseSummaryName," \
                         "releaseSummaryReleaseDate," \
                         "releaseSummaryRelease"
            writeheader = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writeheader.writerow(CSV_Header.split())
    with open(SWGroupSuggestionSummaries, 'w', encoding="utf-8", newline='') as target:
        CSV_Header = "customerId," \
                     "customerName," \
                     "successTrackId," \
                     "suggestionId," \
                     "suggestionsInterval," \
                     "suggestionUpdatedDate," \
                     "suggestionSelectedDate," \
                     "machineSuggestionId," \
                     "expectedSoftwareGroupRisk," \
                     "expectedSoftwareGroupRiskCategory," \
                     "name," \
                     "releaseDate," \
                     "release," \
                     "releaseNotesUrl," \
                     "fieldNoticeSeverityFixedHigh," \
                     "fieldNoticeSeverityFixedMedium," \
                     "fieldNoticeSeverityFixedLow," \
                     "fieldNoticeSeverityNewExposedHigh," \
                     "fieldNoticeSeverityNewExposedMedium," \
                     "fieldNoticeSeverityNewExposedLow," \
                     "fieldNoticeSeverityExposedHigh," \
                     "fieldNoticeSeverityExposedMedium," \
                     "fieldNoticeSeverityExposedLow," \
                     "advisoriesSeverityFixedHigh," \
                     "advisoriesSeverityFixedMedium," \
                     "advisoriesSeverityFixedLow," \
                     "advisoriesSeverityNewExposedHigh," \
                     "advisoriesSeverityNewExposedMedium," \
                     "advisoriesSeverityNewExposedLow," \
                     "advisoriesSeverityExposedHigh," \
                     "advisoriesSeverityExposedMedium," \
                     "advisoriesSeverityExposedLow," \
                     "bugSeverityFixedHigh," \
                     "bugSeverityFixedMedium," \
                     "bugSeverityFixedLow," \
                     "bugSeverityNewExposedHigh," \
                     "bugSeverityNewExposedMedium," \
                     "bugSeverityNewExposedLow," \
                     "bugSeverityExposedHigh," \
                     "bugSeverityExposedMedium," \
                     "bugSeverityExposedLow," \
                     "featuresCountActiveFeaturesCount," \
                     "featuresCountAffectedFeaturesCount," \
                     "featuresCountFixedFeaturesCount"
        writeheader = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
        writeheader.writerow(CSV_Header.split())
    with open(SWGroups, 'r') as target:
        csvreader = csv.DictReader(target)
        for row in csvreader:
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            suggestionId = row['suggestionId']
            if not successTrackId == "N/A":
                print(" ")
                print(f"Found Software Group Suggestion ID {suggestionId} for {customerName}")
                url = (pxc_url_customers + "/" +
                       customerId +
                       pxc_url_software_group_suggestions +
                       "?successTrackId=" + successTrackId +
                       "&suggestionId=" + suggestionId)
                try:
                    headers = {
                        'Authorization': f'Bearer {token}'
                    }
                    response = requests.request("GET", url, headers=headers, verify=True)
                    reply = json.loads(response.text)
                    if response.status_code == 200:
                        jsonDump = {'items': [reply]}
                        suggestionsInterval = str(reply['suggestionsInterval'])
                        suggestionUpdatedDate = str(reply['suggestionUpdatedDate'])
                        suggestionSelectedDate = str(reply['suggestionSelectedDate'])
                    else:
                        jsonDump = []
                    if debug_level == 2:
                        print("URL Request:", url,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content)
                except Exception as Error:
                    print(Error)
                    jsonDump = []
                finally:
                    if outputFormat == 1 or outputFormat == 2:
                        if not jsonDump == []:
                            with open(json_output_dir + customerId + "_SoftwareGroup_Suggestions_" + successTrackId
                                      + "_" + suggestionId + ".json", 'w') as json_file:
                                json.dump(jsonDump, json_file)
                            print(f"Saving {json_file.name}")
                try:
                    softwareGroupRiskTrend = (get_json_reply(url, tag="softwareGroupRiskTrend"))
                except Exception as Error:
                    print(Error)
                    softwareGroupRiskTrend = []
                print(f"Saving Software Group Risk Trend to CSV")
                if softwareGroupRiskTrend is not None:
                    for item in softwareGroupRiskTrend:
                        changeFromPrev = str(item['changeFromPrev'])
                        riskCategory = str(item['riskCategory'])
                        trendDate = str(item['date'])
                        riskScore = str(item['riskScore'])
                        with open(SWGroupSuggestionsTrend, 'a', encoding="utf-8", newline='') \
                                as temp_target:
                            writer = csv.writer(temp_target,
                                                delimiter=' ',
                                                quotechar=' ',
                                                quoting=csv.QUOTE_MINIMAL)
                            CSV_Data = (customerId + ',' +
                                        customerName + ',' +
                                        successTrackId + ',' +
                                        suggestionId + ',' +
                                        suggestionsInterval + ',' +
                                        suggestionUpdatedDate + ',' +
                                        suggestionSelectedDate + ',' +
                                        changeFromPrev + ',' +
                                        riskCategory + ',' +
                                        trendDate + ',' +
                                        riskScore)
                            writer.writerow(CSV_Data.split())
                try:
                    releaseSummary = (get_json_reply(url, tag="releaseSummary"))
                except Exception as Error:
                    print(Error)
                    releaseSummary = []
                print(f"Saving Software Group Release Summaries to CSV")
                if releaseSummary is not None:
                    for item in releaseSummary:
                        releaseSummaryName = str(item['name'])
                        releaseSummaryReleaseDate = str(item['releaseDate'])
                        releaseSummaryRelease = str(item['release']).replace(",", "-")
                        with open(SWGroupSuggestionsReleases, 'a', encoding="utf-8", newline='') \
                                as temp_target:
                            writer = csv.writer(temp_target,
                                                delimiter=' ',
                                                quotechar=' ',
                                                quoting=csv.QUOTE_MINIMAL)
                            CSV_Data = (customerId + ',' +
                                        customerName + ',' +
                                        successTrackId + ',' +
                                        suggestionId + ',' +
                                        suggestionsInterval + ',' +
                                        suggestionUpdatedDate + ',' +
                                        suggestionSelectedDate + ',' +
                                        releaseSummaryName + ',' +
                                        releaseSummaryReleaseDate + ',' +
                                        releaseSummaryRelease)
                            writer.writerow(CSV_Data.split())
                try:
                    suggestionSummaries = (get_json_reply(url, tag="suggestionSummaries"))
                except Exception as Error:
                    print(Error)
                    suggestionSummaries = []
                print(f"Saving Software Group Summaries to CSV\n")
                if suggestionSummaries is not None:
                    for item in suggestionSummaries:
                        machineSuggestionId = str(item['machineSuggestionId'])
                        expectedSoftwareGroupRisk = str(item['expectedSoftwareGroupRisk'])
                        expectedSoftwareGroupRiskCategory = str(item['expectedSoftwareGroupRiskCategory'])
                        name = str(item['name'])
                        releaseDate = str(item['releaseDate'])
                        release = str(item['release']).replace(",", "-")
                        releaseNotesUrl = str(item['releaseNotesUrl'])
                        fieldNoticeSeverity = (item['fieldNoticeSeverity'])
                        try:
                            exposed = fieldNoticeSeverity['Exposed']
                            fieldNoticeSeverityExposedHigh = str(exposed['High'])
                        except KeyError:
                            fieldNoticeSeverityExposedHigh = "0"
                        try:
                            exposed = fieldNoticeSeverity['Exposed']
                            fieldNoticeSeverityExposedMedium = str(exposed['Medium'])
                        except KeyError:
                            fieldNoticeSeverityExposedMedium = "0"
                        try:
                            exposed = fieldNoticeSeverity['Exposed']
                            fieldNoticeSeverityExposedLow = str(exposed['Low'])
                        except KeyError:
                            fieldNoticeSeverityExposedLow = "0"
                        try:
                            fixed = fieldNoticeSeverity['Fixed']
                            fieldNoticeSeverityFixedHigh = str(fixed['High'])
                        except KeyError:
                            fieldNoticeSeverityFixedHigh = "0"
                        try:
                            fixed = fieldNoticeSeverity['Fixed']
                            fieldNoticeSeverityFixedMedium = str(fixed['Medium'])
                        except KeyError:
                            fieldNoticeSeverityFixedMedium = "0"
                        try:
                            fixed = fieldNoticeSeverity['Fixed']
                            fieldNoticeSeverityFixedLow = str(fixed['Low'])
                        except KeyError:
                            fieldNoticeSeverityFixedLow = "0"
                        try:
                            newExposed = fieldNoticeSeverity['New_Exposed']
                            fieldNoticeSeverityNewExposedHigh = str(newExposed['High'])
                        except KeyError:
                            fieldNoticeSeverityNewExposedHigh = "0"
                        try:
                            newExposed = fieldNoticeSeverity['New_Exposed']
                            fieldNoticeSeverityNewExposedMedium = str(newExposed['Medium'])
                        except KeyError:
                            fieldNoticeSeverityNewExposedMedium = "0"
                        try:
                            newExposed = fieldNoticeSeverity['New_Exposed']
                            fieldNoticeSeverityNewExposedLow = str(newExposed['Low'])
                        except KeyError:
                            fieldNoticeSeverityNewExposedLow = "0"
                        advisoriesSeverity = (item['advisoriesSeverity'])
                        try:
                            exposed = advisoriesSeverity['Exposed']
                            advisoriesSeverityExposedHigh = str(exposed['High'])
                        except KeyError:
                            advisoriesSeverityExposedHigh = "0"
                        try:
                            exposed = advisoriesSeverity['Exposed']
                            advisoriesSeverityExposedMedium = str(exposed['Medium'])
                        except KeyError:
                            advisoriesSeverityExposedMedium = "0"
                        try:
                            exposed = advisoriesSeverity['Exposed']
                            advisoriesSeverityExposedLow = str(exposed['Low'])
                        except KeyError:
                            advisoriesSeverityExposedLow = "0"
                        try:
                            fixed = advisoriesSeverity['Fixed']
                            advisoriesSeverityFixedHigh = str(fixed['High'])
                        except KeyError:
                            advisoriesSeverityFixedHigh = "0"
                        try:
                            fixed = advisoriesSeverity['Fixed']
                            advisoriesSeverityFixedMedium = str(fixed['Medium'])
                        except KeyError:
                            advisoriesSeverityFixedMedium = "0"
                        try:
                            fixed = advisoriesSeverity['Fixed']
                            advisoriesSeverityFixedLow = str(fixed['Low'])
                        except KeyError:
                            advisoriesSeverityFixedLow = "0"
                        try:
                            newExposed = advisoriesSeverity['New_Exposed']
                            advisoriesSeverityNewExposedHigh = str(newExposed['High'])
                        except KeyError:
                            advisoriesSeverityNewExposedHigh = "0"
                        try:
                            newExposed = advisoriesSeverity['New_Exposed']
                            advisoriesSeverityNewExposedMedium = str(newExposed['Medium'])
                        except KeyError:
                            advisoriesSeverityNewExposedMedium = "0"
                        try:
                            newExposed = advisoriesSeverity['New_Exposed']
                            advisoriesSeverityNewExposedLow = str(newExposed['Low'])
                        except KeyError:
                            advisoriesSeverityNewExposedLow = "0"
                        bugSeverity = (item['bugSeverity'])
                        try:
                            exposed = bugSeverity['Exposed']
                            bugSeverityExposedHigh = str(exposed['High'])
                        except KeyError:
                            bugSeverityExposedHigh = "0"
                        try:
                            exposed = bugSeverity['Exposed']
                            bugSeverityExposedMedium = str(exposed['Medium'])
                        except KeyError:
                            bugSeverityExposedMedium = "0"
                        try:
                            exposed = bugSeverity['Exposed']
                            bugSeverityExposedLow = str(exposed['Low'])
                        except KeyError:
                            bugSeverityExposedLow = "0"
                        try:
                            fixed = bugSeverity['Fixed']
                            bugSeverityFixedHigh = str(fixed['High'])
                        except KeyError:
                            bugSeverityFixedHigh = "0"
                        try:
                            fixed = bugSeverity['Fixed']
                            bugSeverityFixedMedium = str(fixed['Medium'])
                        except KeyError:
                            bugSeverityFixedMedium = "0"
                        try:
                            fixed = bugSeverity['Fixed']
                            bugSeverityFixedLow = str(fixed['Low'])
                        except KeyError:
                            bugSeverityFixedLow = "0"
                        try:
                            newExposed = bugSeverity['New_Exposed']
                            bugSeverityNewExposedHigh = str(newExposed['High'])
                        except KeyError:
                            bugSeverityNewExposedHigh = "0"
                        try:
                            newExposed = bugSeverity['New_Exposed']
                            bugSeverityNewExposedMedium = str(newExposed['Medium'])
                        except KeyError:
                            bugSeverityNewExposedMedium = "0"
                        try:
                            newExposed = bugSeverity['New_Exposed']
                            bugSeverityNewExposedLow = str(newExposed['Low'])
                        except KeyError:
                            bugSeverityNewExposedLow = "0"
                        featuresCount = (item['featuresCount'])
                        try:
                            featuresCountActiveFeaturesCount = str(featuresCount['activeFeaturesCount'])
                        except KeyError:
                            featuresCountActiveFeaturesCount = "0"
                        try:
                            featuresCountAffectedFeaturesCount = str(featuresCount['affectedFeaturesCount'])
                        except KeyError:
                            featuresCountAffectedFeaturesCount = "0"
                        try:
                            featuresCountFixedFeaturesCount = str(featuresCount['fixedFeaturesCount'])
                        except KeyError:
                            featuresCountFixedFeaturesCount = "0"
                        with open(SWGroupSuggestionSummaries, 'a', encoding="utf-8", newline='') \
                                as temp_target:
                            writer = csv.writer(temp_target,
                                                delimiter=' ',
                                                quotechar=' ',
                                                quoting=csv.QUOTE_MINIMAL)
                            CSV_Data = (customerId + ',' +
                                        customerName + ',' +
                                        successTrackId + ',' +
                                        suggestionId + ',' +
                                        suggestionsInterval + ',' +
                                        suggestionUpdatedDate + ',' +
                                        suggestionSelectedDate + ',' +
                                        machineSuggestionId + ',' +
                                        expectedSoftwareGroupRisk + ',' +
                                        expectedSoftwareGroupRiskCategory + ',' +
                                        name + ',' +
                                        releaseDate + ',' +
                                        release + ',' +
                                        releaseNotesUrl + ',' +
                                        fieldNoticeSeverityFixedHigh + ',' +
                                        fieldNoticeSeverityFixedMedium + ',' +
                                        fieldNoticeSeverityFixedLow + ',' +
                                        fieldNoticeSeverityNewExposedHigh + ',' +
                                        fieldNoticeSeverityNewExposedMedium + ',' +
                                        fieldNoticeSeverityNewExposedLow + ',' +
                                        fieldNoticeSeverityExposedHigh + ',' +
                                        fieldNoticeSeverityExposedMedium + ',' +
                                        fieldNoticeSeverityExposedLow + ',' +
                                        advisoriesSeverityFixedHigh + ',' +
                                        advisoriesSeverityFixedMedium + ',' +
                                        advisoriesSeverityFixedLow + ',' +
                                        advisoriesSeverityNewExposedHigh + ',' +
                                        advisoriesSeverityNewExposedMedium + ',' +
                                        advisoriesSeverityNewExposedLow + ',' +
                                        advisoriesSeverityExposedHigh + ',' +
                                        advisoriesSeverityExposedMedium + ',' +
                                        advisoriesSeverityExposedLow + ',' +
                                        bugSeverityFixedHigh + ',' +
                                        bugSeverityFixedMedium + ',' +
                                        bugSeverityFixedLow + ',' +
                                        bugSeverityNewExposedHigh + ',' +
                                        bugSeverityNewExposedMedium + ',' +
                                        bugSeverityNewExposedLow + ',' +
                                        bugSeverityExposedHigh + ',' +
                                        bugSeverityExposedMedium + ',' +
                                        bugSeverityExposedLow + ',' +
                                        featuresCountActiveFeaturesCount + ',' +
                                        featuresCountAffectedFeaturesCount + ',' +
                                        featuresCountFixedFeaturesCount
                                        )
                            writer.writerow(CSV_Data.split())

    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# This API returns information about assets in the Software Group based on the customerID and softwareGroupId provided.
# CSV Naming Convention: SoftwareGroup_Suggestions_Assets.csv
# JSON Naming Convention: {Customer ID}_SoftwareGroup_Suggestion_Assets_{Software Group ID}.json
def pxc_software_group_suggestions_assets():
    print("******************************************************************")
    print("*********** Running Software Groups Suggestions Assets ***********")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(SWGroupSuggestionAssets, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "softwareGroupId," \
                         "deploymentStatus," \
                         "selectedRelease," \
                         "assetName," \
                         "ipAddress," \
                         "softwareType," \
                         "currentRelease"
            writeheader = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writeheader.writerow(CSV_Header.split())
    with open(SWGroups, 'r') as target:
        csvreader = csv.DictReader(target)
        for row in csvreader:
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            softwareGroupId = row['softwareGroupId']
            if not successTrackId == "N/A":
                print(" ")
                print(f"Found Software Group ID {softwareGroupId} Suggestion Asset for {customerName}")
                url = (pxc_url_customers + "/" +
                       customerId +
                       pxc_url_software_group_suggestions_assets +
                       "?softwareGroupId=" + softwareGroupId +
                       "&successTrackId=" + successTrackId)
                items = (get_json_reply(url, tag="items"))
                if outputFormat == 1 or outputFormat == 2:
                    if items is not None:
                        if len(items) > 0:
                            with open(
                                    json_output_dir + customerId + "_SoftwareGroup_Suggestion_Assets_" +
                                    softwareGroupId + ".json", 'w') as json_file:
                                json.dump(items, json_file)
                            print(f"Saving {json_file.name}")
                if outputFormat == 1 or outputFormat == 3:
                    if items:
                        for item in items:
                            deploymentStatus = str(item['deploymentStatus'])
                            selectedRelease = str(item['selectedRelease'])
                            try:
                                assetName = str(item['assetName'].replace(",", " "))
                            except KeyError:
                                assetName = str(item['assetHostName'].replace(",", " "))
                                pass
                            ipAddress = str(item['ipAddress'])
                            softwareType = str(item['softwareType'].replace(",", "|"))
                            currentRelease = str(item['currentRelease'])
                            with open(SWGroupSuggestionAssets, 'a', encoding="utf-8", newline='') \
                                    as temp_target:
                                writer = csv.writer(temp_target,
                                                    delimiter=' ',
                                                    quotechar=' ',
                                                    quoting=csv.QUOTE_MINIMAL)
                                CSV_Data = (customerId + ',' +
                                            customerName + ',' +
                                            successTrackId + ',' +
                                            softwareGroupId + ',' +
                                            deploymentStatus + ',' +
                                            selectedRelease + ',' +
                                            assetName + ',' +
                                            ipAddress + ',' +
                                            softwareType + ',' +
                                            currentRelease)
                                writer.writerow(CSV_Data.split())

    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# This API returns information on bugs, including ID, description, and affected software releases.
# CSV Naming Convention: SoftwareGroup_Suggestions_Bug_Lists.csv
# JSON Naming Convention:
# {Customer ID}_SoftwareGroup_Suggestions_Bug_Lists_{Machine Suggestion ID}_Page_{page}_of_{total}.json
def pxc_software_group_suggestions_bug_list():
    print("******************************************************************")
    print("********* Running Software Groups Suggestions Bug List ***********")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(SWGroupSuggestionsBugList, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "machineSuggestionId," \
                         "bugId," \
                         "severity," \
                         "title," \
                         "state," \
                         "affectedAssets," \
                         "features"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(SWGroupSuggestionSummaries, 'r') as target:
        csvreader = csv.DictReader(target)
        for row in csvreader:
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            machineSuggestionId = row['machineSuggestionId']
            headers = {'Authorization': f'Bearer {token}'}
            if not successTrackId == "N/A":
                print(" ")
                print(f"Found Software Group Suggestions Bug List for {customerName} "
                      f"with machine suggestion ID of {machineSuggestionId}")
                url = (pxc_url_customers + "/" +
                       customerId +
                       pxc_url_software_group_suggestions_bugs +
                       "?offset=1" +
                       "&max=" + max_items +
                       "&machineSuggestionId=" + machineSuggestionId +
                       "&successTrackId=" + successTrackId)
            response = requests.request("GET", url, headers=headers, data=payload, verify=True)
            reply = json.loads(response.text)
            try:
                if response.status_code == 200:
                    totalCount = reply["totalCount"]
                    pages = math.ceil(totalCount / int(max_items))
                    if debug_level == 1 or debug_level == 2:
                        print("\nTotal Pages:", pages,
                              "\nTotal Records: ", totalCount,
                              "\nURL Request:", url,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content)
                    page = 0
                    while page < pages:
                        url = (pxc_url_customers + "/" +
                               customerId +
                               pxc_url_software_group_suggestions_bugs +
                               "?offset=" + str(page + 1) +
                               "&max=" + max_items +
                               "&machineSuggestionId=" + machineSuggestionId +
                               "&successTrackId=" + successTrackId)
                        items = (get_json_reply(url, tag="items"))
                        if outputFormat == 1 or outputFormat == 2:
                            with open(json_output_dir + customerId +
                                      "_SoftwareGroup_Suggestions_Bug_Lists_" + machineSuggestionId +
                                      "_Page_" + str(page + 1) +
                                      "_of_" + str(pages) +
                                      ".json", 'w') as json_file:
                                json.dump(items, json_file)
                                print(f"Saving {json_file.name}")
                        if outputFormat == 1 or outputFormat == 3:
                            if items is not None:
                                for item in items:
                                    bugId = str(item['bugId'])
                                    severity = str(item['severity'])
                                    title = str(item['title']).replace(",", " ")
                                    state = str(item['state'])
                                    affectedAssets = str(item['affectedAssets'])
                                    featureCount = str(item['features'])
                                    with open(SWGroupSuggestionsBugList, 'a', encoding="utf-8", newline='') \
                                            as temp_target:
                                        writer = csv.writer(temp_target,
                                                            delimiter=' ',
                                                            quotechar=' ',
                                                            quoting=csv.QUOTE_MINIMAL)
                                        CSV_Data = (customerId + ',' +
                                                    customerName + ',' +
                                                    successTrackId + ',' +
                                                    machineSuggestionId + ',' +
                                                    bugId + ',' +
                                                    severity + ',' +
                                                    title + ',' +
                                                    state + ',' +
                                                    affectedAssets + ',' +
                                                    featureCount)
                                        writer.writerow(CSV_Data.split())
                        else:
                            print("No Data Found .... Skipping")
                        page += 1
            except KeyError:
                print("No Data to process... Skipping.")
                pass
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# This API returns field notice information, including ID number, title, and publish date.
# CSV Naming Convention: SoftwareGroup_Suggestions_Field_Notices.csv
# JSON Naming Convention:
# {Customer ID}_SoftwareGroup_Suggestions_Field_Notices_{Machine Suggestion ID}_Page_{page}_of_{total}.json
def pxc_software_group_suggestions_field_notices():
    print("******************************************************************")
    print("******* Running Software Groups Suggestions Field Notices ********")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(SWGroupSuggestionsFieldNotices, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "machineSuggestionId," \
                         "fieldNoticeId," \
                         "title," \
                         "state," \
                         "firstPublished," \
                         "lastUpdated"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(SWGroupSuggestionSummaries, 'r') as target:
        csvreader = csv.DictReader(target)
        for row in csvreader:
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            machineSuggestionId = row['machineSuggestionId']
            headers = {'Authorization': f'Bearer {token}'}
            if debug_level == 1 or debug_level == 2:
                print("====================\n\n")
                print("Software Group Suggestions Field Notices for Customer:", customerId,
                      "on Success Tracks:", successTrackId)
            if not successTrackId == "N/A":
                url = (pxc_url_customers + "/" +
                       customerId +
                       pxc_url_software_group_suggestions_field_notices +
                       "?offset=1" +
                       "&max=" + max_items +
                       "&machineSuggestionId=" + machineSuggestionId +
                       "&successTrackId=" + successTrackId)
                response = requests.request("GET", url, headers=headers, data=payload, verify=True)
                reply = json.loads(response.text)
                totalCount = reply["totalCount"]
            try:
                if response.status_code == 200:
                    pages = math.ceil(totalCount / int(max_items))
                    if debug_level == 1 or debug_level == 2:
                        print("\nTotal Pages:", pages,
                              "\nTotal Records: ", totalCount,
                              "\nURL Request:", url,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content)
                    page = 0
                    while page < pages:
                        url = (pxc_url_customers + "/" +
                               customerId +
                               pxc_url_software_group_suggestions_field_notices +
                               "?offset=" + str(page + 1) +
                               "&max=" + max_items +
                               "&machineSuggestionId=" + machineSuggestionId +
                               "&successTrackId=" + successTrackId)
                        items = (get_json_reply(url, tag="items"))
                        print(f"Found Software Group Suggestions Field Notice for {customerName} "
                              f"with machine suggestion ID of {machineSuggestionId}")
                        if outputFormat == 1 or outputFormat == 2:
                            if items is not None:
                                if len(items) > 0:
                                    with open(json_output_dir + customerId +
                                              "_SoftwareGroup_Suggestions_Field_Notices_" + machineSuggestionId +
                                              "_Page_" + str(page + 1) +
                                              "_of_" + str(pages) +
                                              ".json", 'w') as json_file:
                                        json.dump(items, json_file)
                                    print(f"Saving {json_file.name}")
                        if outputFormat == 1 or outputFormat == 3:
                            if items is not None:
                                if len(items) > 0:
                                    for item in items:
                                        fieldNoticeId = str(item['fieldNoticeId']).replace(",", " ")
                                        title = str(item['title']).replace(",", " ")
                                        state = str(item['state']).replace(",", " ")
                                        firstPublished = str(item['firstPublished']).replace(",", " ")
                                        lastUpdated = str(item['lastUpdated']).replace(",", " ")
                                        with open(SWGroupSuggestionsFieldNotices, 'a', encoding="utf-8", newline='') \
                                                as temp_target:
                                            writer = csv.writer(temp_target,
                                                                delimiter=' ',
                                                                quotechar=' ',
                                                                quoting=csv.QUOTE_MINIMAL)
                                            CSV_Data = (customerId + ',' +
                                                        customerName + ',' +
                                                        successTrackId + ',' +
                                                        machineSuggestionId + ',' +
                                                        fieldNoticeId + ',' +
                                                        title + ',' +
                                                        state + ',' +
                                                        firstPublished + ',' +
                                                        lastUpdated)
                                            writer.writerow(CSV_Data.split())
                        else:
                            print("No Data Found .... Skipping")
                        page += 1
            except KeyError:
                print("No Data to process... Skipping.")
                pass
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# This API returns software advisory information, including ID number, version number, and severity level.
# CSV Naming Convention: SoftwareGroup_Suggestions_Security_Advisories.csv
# JSON Naming Convention:
# {Customer ID}_SoftwareGroup_Suggestions_Security_Advisories_{Machine Suggestion ID}_Page_{page}_of_{total}.json
def pxc_software_group_suggestions_advisories():
    print("******************************************************************")
    print("**** Running Software Groups Suggestions Security Advisories *****")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(SWGroupSuggestionsAdvisories, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "machineSuggestionId," \
                         "state," \
                         "advisoryId," \
                         "impact," \
                         "title," \
                         "updated," \
                         "advisoryVersion"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(SWGroupSuggestionSummaries, 'r') as target:
        csvreader = csv.DictReader(target)
        for row in csvreader:
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            machineSuggestionId = row['machineSuggestionId']
            headers = {'Authorization': f'Bearer {token}'}
            if debug_level == 1 or debug_level == 2:
                print("====================\n\n")
                print("Software Group Suggestions Security Advisories for Customer:", customerId,
                      "on Success Tracks:", successTrackId)
            url = (pxc_url_customers + "/" +
                   customerId +
                   pxc_url_software_group_suggestions_security_advisories +
                   "?offset=1" +
                   "&max=" + max_items +
                   "&machineSuggestionId=" + machineSuggestionId +
                   "&successTrackId=" + successTrackId)
            response = requests.request("GET", url, headers=headers, data=payload, verify=True)
            reply = json.loads(response.text)
            totalCount = reply["totalCount"]
            try:
                if response.status_code == 200:
                    pages = math.ceil(totalCount / int(max_items))
                    if debug_level == 1 or debug_level == 2:
                        print("\nTotal Pages:", pages,
                              "\nTotal Records: ", totalCount,
                              "\nURL Request:", url,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content)
                    page = 0
                    while page < pages:
                        url = (pxc_url_customers + "/" +
                               customerId +
                               pxc_url_software_group_suggestions_security_advisories +
                               "?offset=" + str(page + 1) +
                               "&max=" + max_items +
                               "&machineSuggestionId=" + machineSuggestionId +
                               "&successTrackId=" + successTrackId)
                        items = (get_json_reply(url, tag="items"))
                        print(f"\nFound Software Group Suggestions Security Advisory for {customerName} "
                              f"with machine suggestion ID of {machineSuggestionId}")
                        if outputFormat == 1 or outputFormat == 2:
                            if items is not None:
                                if len(items) > 0:
                                    with open(json_output_dir + customerId +
                                              "_Security_Advisories_" + machineSuggestionId +
                                              "_Page_" + str(page + 1) +
                                              "_of_" + str(pages) +
                                              ".json", 'w') as json_file:
                                        json.dump(items, json_file)
                                    print(f"Saving {json_file.name}")
                            else:
                                print("No Data Found .... Skipping")
                        if outputFormat == 1 or outputFormat == 3:
                            if items is not None:
                                if len(items) > 0:
                                    for item in items:
                                        state = str(item['state']).replace(",", " ")
                                        advisoryId = str(item['advisoryId']).replace(",", " ")
                                        impact = str(item['impact']).replace(",", " ")
                                        title = str(item['title']).replace(",", " ")
                                        updated = str(item['updated']).replace(",", " ")
                                        advisoryVersion = str(item['advisoryVersion']).replace(",", " ")
                                        with open(SWGroupSuggestionsAdvisories, 'a', encoding="utf-8", newline='') \
                                                as temp_target:
                                            writer = csv.writer(temp_target,
                                                                delimiter=' ',
                                                                quotechar=' ',
                                                                quoting=csv.QUOTE_MINIMAL)
                                            CSV_Data = (customerId + ',' +
                                                        customerName + ',' +
                                                        successTrackId + ',' +
                                                        machineSuggestionId + ',' +
                                                        state + ',' +
                                                        advisoryId + ',' +
                                                        impact + ',' +
                                                        title + ',' +
                                                        updated + ',' +
                                                        advisoryVersion)
                                            writer.writerow(CSV_Data.split())
                        else:
                            print("No Data Found .... Skipping")
                        page += 1
            except KeyError:
                print("No Data to process... Skipping.")
                pass
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Functions to get the Automated Fault Management data from PX Cloud (currently only for Campus Network Success Tracks)
# This API returns fault information for the customerId provided.
# CSV Naming Convention: Automated_Fault_Management_Faults.csv
# JSON Naming Convention: {Customer ID}_Automated_Fault_Management_Faults_{Success Track ID}.json
def pxc_automated_fault_management_faults():
    print("******************************************************************")
    print("*********** Running Automated Fault Management Faults ************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(AFMFaults, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "severity," \
                         "title," \
                         "lastOccurence," \
                         "condition," \
                         "caseAutomation," \
                         "faultId," \
                         "category," \
                         "openCases," \
                         "affectedAssets," \
                         "occurences," \
                         "ignoredAssets"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(customers, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            if not row["successTrackId"] == "N/A":
                customerId = row['customerId']
                customerName = row['customerName']
                successTrackId = row['successTrackId']
                url = (pxc_url_customers + "/" +
                       customerId +
                       pxc_url_automated_fault_management_faults +
                       "?successTrackId=" + successTrackId +
                       "&days=30" +
                       "&max=" + max_items)
                print("\nFound Automated Fault Management Faults for Customer:", row["customerName"],
                      "on Success Tracks:", row["successTrackId"])
                items = get_json_reply(url, tag="items")
                if outputFormat == 1 or outputFormat == 2:
                    if items is not None:
                        if len(items) > 0:
                            with open(json_output_dir + customerId +
                                      "_Automated_Fault_Management_Faults_" + successTrackId +
                                      ".json", 'w') as json_file:
                                json.dump(items, json_file)
                            print(f"Saving {json_file.name}")
                        else:
                            print("No Data Found ... Skipping")
                if items:
                    for item in items:
                        severity = item['severity'].replace(",", " ")
                        title = item['title'].replace(",", " ")
                        lastOccurence = str(item['lastOccurence'])
                        condition = item['condition'].replace(",", " ")
                        caseAutomation = item['caseAutomation'].replace(",", " ")
                        faultId = str(item['faultId'])
                        category = item['category'].replace(",", " ")
                        openCases = str(item['openCases'])
                        affectedAssets = str(item['affectedAssets'])
                        occurences = str(item['occurences'])
                        ignoredAssets = str(item['ignoredAssets'])
                        with open(AFMFaults, 'a', encoding="utf-8", newline='') as target:
                            writer = csv.writer(target,
                                                delimiter=' ',
                                                quotechar=' ',
                                                quoting=csv.QUOTE_MINIMAL)
                            CSV_Data = (customerId + ',' +
                                        customerName + ',' +
                                        successTrackId + ',' +
                                        severity + ',' +
                                        title + ',' +
                                        lastOccurence + ',' +
                                        condition + ',' +
                                        caseAutomation + ',' +
                                        faultId + ',' +
                                        category + ',' +
                                        openCases + ',' +
                                        affectedAssets + ',' +
                                        occurences + ',' +
                                        ignoredAssets)
                            writer.writerow(CSV_Data.split())

    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# This API returns detailed information for a fault based on the fault signatureId and customerId provided.
# CSV Naming Convention: Automated_Fault_Management_Fault_Summary.csv
# JSON Naming Convention:{Customer ID}_Automated_Fault_Management_Fault_Summary_{Fault ID}_{Success Track ID}.json
def pxc_automated_fault_management_fault_summary():
    print("******************************************************************")
    print("******* Running Automated Fault Management Faults Summary ********")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(AFMFaultSummary, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "faultId," \
                         "suggestion," \
                         "impact," \
                         "description," \
                         "severity," \
                         "title," \
                         "condition," \
                         "category," \
                         "supportedProductSeries"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(AFMFaults, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            if not row["successTrackId"] == "N/A":
                customerId = row['customerId']
                customerName = row['customerName']
                successTrackId = row['successTrackId']
                faultId = row['faultId']
                print(
                    f"Automated Fault Management Fault Summary for {customerName} "
                    f"on Success Tracks {successTrackId} with FaultId of {faultId}")
                url = (pxc_url_customers + "/" +
                       customerId +
                       pxc_url_automated_fault_management_faults +
                       "/" + faultId +
                       pxc_url_automated_fault_management_fault_summary +
                       "?successTrackId=" + successTrackId)
                items = get_json_reply(url, tag="items")
                if outputFormat == 1 or outputFormat == 2:
                    if items is not None:
                        if len(items) > 0:
                            with open(json_output_dir + customerId +
                                      "_Automated_Fault_Management_Fault_Summary_" +
                                      faultId + "_" + successTrackId +
                                      ".json", 'w') as json_file:
                                json.dump(items, json_file)
                            print(f"Saving {json_file.name}\n")
                if outputFormat == 1 or outputFormat == 3:
                    if items:
                        for item in items:
                            suggestion = item['suggestion'].replace(",", " ")
                            impact = item['impact'].replace(",", " ")
                            description = item['description'].replace(",", " ")
                            severity = item['severity'].replace(",", " ")
                            title = item['title'].replace(",", " ")
                            condition = item['condition'].replace(",", " ")
                            category = item['category'].replace(",", " ")
                            supportedProductSeries = item['supportedProductSeries'].replace(",", " ")
                            with open(AFMFaultSummary,
                                      'a', encoding="utf-8", newline='') as target:
                                writer = csv.writer(target,
                                                    delimiter=' ',
                                                    quotechar=' ',
                                                    quoting=csv.QUOTE_MINIMAL)
                                CSV_Data = (customerId + ',' +
                                            customerName + ',' +
                                            successTrackId + ',' +
                                            faultId + ',' +
                                            suggestion + ',' +
                                            impact + ',' +
                                            description + ',' +
                                            severity + ',' +
                                            title + ',' +
                                            condition + ',' +
                                            category + ',' +
                                            supportedProductSeries)
                                writer.writerow(CSV_Data.split())
            else:
                print("\nNo Data Found .... Skipping")
                print("====================\n\n")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# This API returns information about the customer assets affected by the fault, based on the signatureId and customerId.
# CSV Naming Convention: Automated_Fault_Management_Fault_Summary.csv
# JSON Naming Convention:
# {Customer ID}_Automated_Fault_Management_Fault_Summary_Affected_Assets_{Fault ID}_{Success Track ID}.json
def pxc_automated_fault_management_affected_assets():
    print("******************************************************************")
    print("******* Running Automated Fault Management Affected Assets ******")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(AFMFaultAffectedAssets, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "faultId," \
                         "assetName," \
                         "productId," \
                         "caseNumber," \
                         "caseAction," \
                         "occurrences," \
                         "firstOccurrence," \
                         "lastOccurrence," \
                         "serialNumber"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(AFMFaults, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            if not row["successTrackId"] == "N/A":
                customerId = row['customerId']
                customerName = row['customerName']
                successTrackId = row['successTrackId']
                faultId = row['faultId']
                print(
                    f"Automated Fault Management Affected Assets for {customerName} "
                    f"on Success Tracks {successTrackId} with FaultId of {faultId}")
                url = (pxc_url_customers + "/" +
                       customerId +
                       pxc_url_automated_fault_management_faults +
                       "/" + faultId +
                       pxc_url_automated_fault_management_affected_assets +
                       "?successTrackId=" + successTrackId +
                       "&days=30" +
                       "&max=" + max_items)
                items = get_json_reply(url, tag="items")
                if outputFormat == 1 or outputFormat == 2:
                    if items is not None:
                        if len(items) > 0:
                            with open(json_output_dir + customerId +
                                      "_Automated_Fault_Management_Fault_Summary_Affected_Assets_" +
                                      faultId + "_" + successTrackId +
                                      ".json", 'w') as json_file:
                                json.dump(items, json_file)
                            print(f"Saving {json_file.name}\n")
                if outputFormat == 1 or outputFormat == 3:
                    if items:
                        for item in items:
                            assetName = str(item['assetName'].replace(",", " "))
                            productId = str(item['productId'].replace(",", " "))
                            caseNumber = str(item['caseNumber'])
                            caseAction = str(item['caseAction'].replace(",", " "))
                            occurrences = str(item['occurrences'])
                            firstOccurrence = str(item['firstOccurrence'].replace(",", " "))
                            lastOccurrence = str(item['lastOccurrence'].replace(",", " "))
                            serialNumber = str(item['serialNumber'].replace(",", " "))
                            with open(AFMFaultAffectedAssets,
                                      'a', encoding="utf-8", newline='') as target:
                                writer = csv.writer(target,
                                                    delimiter=' ',
                                                    quotechar=' ',
                                                    quoting=csv.QUOTE_MINIMAL)
                                CSV_Data = (customerId + ',' +
                                            customerName + ',' +
                                            successTrackId + ',' +
                                            faultId + ',' +
                                            assetName + ',' +
                                            productId + ',' +
                                            caseNumber + ',' +
                                            caseAction + ',' +
                                            occurrences + ',' +
                                            firstOccurrence + ',' +
                                            lastOccurrence + ',' +
                                            serialNumber)
                                writer.writerow(CSV_Data.split())
            else:
                print("\nNo Data Found .... Skipping")
                print("====================\n\n")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Functions to get the Compliance Violations data from PX Cloud (currently only for Campus Network Success Tracks)
# This API returns information about the rules violated for the customerId provided
# CSV Naming Convention: Regulatory_Compliance_Violations.csv
# JSON Naming Convention:{Customer ID}_Regulatory_Compliance_Violations_{Success Track ID}.json
def pxc_compliance_violations():
    print("******************************************************************")
    print("************** Running Compliance Violations Report **************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(RCCComplianceViolations, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "severity," \
                         "severityId," \
                         "policyGroupId," \
                         "policyGroupName," \
                         "policyId," \
                         "ruleId," \
                         "policyName," \
                         "ruleTitle," \
                         "violationCount," \
                         "affectedAssetsCount," \
                         "policyCategory"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(customers, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            if debug_level == 1 or debug_level == 2:
                print("Compliance Violations for Customer:", row["customerId"],
                      "on Success Tracks:", row["successTrackId"])
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            headers = {'Authorization': f'Bearer {token}'}
            if not successTrackId == "N/A":
                print(" ")
                print(f"Found Customer:", row["customerName"])
                url = (pxc_url_customers + "/" +
                       customerId +
                       pxc_url_compliance_violations +
                       "?successTrackId=" + successTrackId +
                       "&days=30" +
                       "&max=" + max_items)
                response = requests.request("GET", url, headers=headers, data=payload, verify=True)
                reply = json.loads(response.text)
                page = 0
                try:
                    if response.status_code == 403:
                        print("Customer admin has not provided access.")
                    if response.status_code == 200:
                        totalCount = reply["totalCount"]
                        if totalCount == 0:
                            print("No Data Found .... Skipping")
                        pages = math.ceil(totalCount / int(max_items))
                        if debug_level == 1 or debug_level == 2:
                            print("\nTotal Pages:", pages,
                                  "\nTotal Records: ", totalCount,
                                  "\nURL Request:", url,
                                  "\nHTTP Code:", response.status_code,
                                  "\nReview API Headers:", response.headers,
                                  "\nResponse Body:", response.content)
                        while page < pages:
                            url = (pxc_url_customers + "/" +
                                   customerId +
                                   pxc_url_compliance_violations +
                                   "?offset=" + str(page + 1) +
                                   "&max=" + max_items +
                                   "&successTrackId=" + successTrackId)
                            items = (get_json_reply(url, tag="items"))
                            if outputFormat == 1 or outputFormat == 2:
                                if items is not None:
                                    if len(items) > 0:
                                        with open(json_output_dir + customerId +
                                                  "_Regulatory_Compliance_Violations_" + successTrackId +
                                                  "_Page_" + str(page + 1) +
                                                  "_of_" + str(pages) +
                                                  ".json", 'w') as json_file:
                                            json.dump(items, json_file)
                                        print(f"Saving {json_file.name}")
                            if outputFormat == 1 or outputFormat == 3:
                                if items is not None:
                                    if len(items) > 0:
                                        for item in items:
                                            severity = item['severity'].replace(",", " ")
                                            severityId = item['severityId'].replace(",", " ")
                                            policyGroupId = str(item['policyGroupId']).replace(",", " ")
                                            policyGroupName = item['policyGroupName'].replace(",", " ")
                                            policyId = item['policyId'].replace(",", " ")
                                            ruleId = str(item['ruleId']).replace(",", " ")
                                            policyName = item['policyName'].replace(",", " ")
                                            ruleTitle = str(item['ruleTitle']).replace(",", " ")
                                            violationCount = str(item['violationCount'])
                                            affectedAssetsCount = str(item['affectedAssetsCount'])
                                            policyCategory = str(item['policyCategory']).replace(",", " ")
                                            with open(RCCComplianceViolations, 'a', encoding="utf-8",
                                                      newline='') as target:
                                                writer = csv.writer(target,
                                                                    delimiter=' ',
                                                                    quotechar=' ',
                                                                    quoting=csv.QUOTE_MINIMAL)
                                                CSV_Data = (customerId + ',' +
                                                            customerName + ',' +
                                                            successTrackId + ',' +
                                                            severity + ',' +
                                                            severityId + ',' +
                                                            policyGroupId + ',' +
                                                            policyGroupName + ',' +
                                                            policyId + ',' +
                                                            ruleId + ',' +
                                                            policyName + ',' +
                                                            ruleTitle + ',' +
                                                            violationCount + ',' +
                                                            affectedAssetsCount + ',' +
                                                            policyCategory)
                                                writer.writerow(CSV_Data.split())
                            page += 1
                except KeyError:
                    print("No Data to process... Skipping.")
                    page -= 1
                    pass
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to get Assets violating compliance rule data from PX Cloud (currently only for Campus Network Success Tracks)
# This API returns information about the customer assets in violation of the rule based customer, policy, and rules.
# CSV Naming Convention: Regulatory_Compliance_Assets_violating_Compliance_Rule.csv
# JSON Naming Convention:
# {Customer ID}_Assets_Violating_Compliance_Rule_{Success Track ID}_{File #}.json
def pxc_assets_violating_compliance_rule():
    print("******************************************************************")
    print("*********** Running Assets Violating Compliance Rules ************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(RCCAssetsViolatingComplianceRule, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "mgmtSystemHostname," \
                         "ipAddress," \
                         "productFamily," \
                         "violationCount," \
                         "role," \
                         "assetId," \
                         "assetName," \
                         "softwareType," \
                         "softwareRelease," \
                         "productId," \
                         "severity," \
                         "lastChecked," \
                         "policyId," \
                         "ruleId," \
                         "scanStatus"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(RCCComplianceViolations, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        fileNum = 0
        for row in custList:
            fileNum += 1
            if debug_level == 1 or debug_level == 2:
                print("Assets Violating Compliance Rule for Customer:", row["customerId"],
                      "on Success Tracks:", row["successTrackId"])
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            policyCategory = row['policyCategory']
            policyGroupId = row['policyGroupId']
            policyId = row['policyId']
            ruleId = row['ruleId']
            severity = row['severity']
            url = (pxc_url_customers + "/" +
                   customerId +
                   pxc_url_compliance_violations_assets +
                   "?policyCategory=" + policyCategory +
                   "&policyGroupId=" + policyGroupId +
                   "&policyId=" + policyId +
                   "&ruleId=" + ruleId +
                   "&severity=" + severity +
                   "&successTrackId=" + successTrackId +
                   "&max=" + max_items)
            items = (get_json_reply(url, tag="items"))
            print(" ")
            print(f"Found Assets Violating Compliance Rules on Success Track {successTrackId} "
                  f"for {customerName}")
            if outputFormat == 1 or outputFormat == 2:
                if items is not None:
                    if len(items) > 0:
                        with open(json_output_dir + customerId +
                                  "_Assets_Violating_Compliance_Rule_" + successTrackId +
                                  "_Page_" + str(fileNum) +
                                  ".json", 'w') as json_file:
                            json.dump(items, json_file)
                        print(f"Saving {json_file.name}")
            if outputFormat == 1 or outputFormat == 3:
                try:
                    if items is not None:
                        if len(items) > 0:
                            for item in items:
                                mgmtSystemHostname = item['mgmtSystemHostname'].replace(",", " ")
                                ipAddress = str(item['ipAddress']).replace(",", " ")
                                productFamily = str(item['productFamily']).replace(",", " ")
                                violationCount = str(item['violationCount']).replace(",", " ")
                                role = str(item['role']).replace(",", " ")
                                assetId = str(item['assetId']).replace(",", "_")
                                assetName = item['assetName'].replace(",", " ")
                                softwareType = item['softwareType'].replace(",", " ")
                                softwareRelease = item['softwareRelease'].replace(",", " ")
                                productId = item['productId'].replace(",", " ")
                                severity = str(item['severity']).replace(",", " ")
                                lastChecked = str(item['lastChecked']).replace(",", " ")
                                scanStatus = str(item['scanStatus']).replace(",", " ")
                                with open(RCCAssetsViolatingComplianceRule, 'a',
                                          encoding="utf-8",
                                          newline='') \
                                        as target:
                                    writer = csv.writer(target,
                                                        delimiter=' ',
                                                        quotechar=' ',
                                                        quoting=csv.QUOTE_MINIMAL)
                                    CSV_Data = (customerId + ',' +
                                                customerName + ',' +
                                                successTrackId + ',' +
                                                mgmtSystemHostname + ',' +
                                                ipAddress + ',' +
                                                productFamily + ',' +
                                                violationCount + ',' +
                                                role + ',' +
                                                assetId + ',' +
                                                assetName + ',' +
                                                softwareType + ',' +
                                                softwareRelease + ',' +
                                                productId + ',' +
                                                severity + ',' +
                                                lastChecked + ',' +
                                                policyId + ',' +
                                                ruleId + ',' +
                                                scanStatus)
                                    writer.writerow(CSV_Data.split())
                        else:
                            print("\nNo Data Found .... Skipping")
                            print("====================\n\n")
                except KeyError:
                    print("No Data to process... Skipping.")
                    pass
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to get Assets violating compliance rule data from PX Cloud (currently only for Campus Network Success Tracks)
# This API returns information about the policy the rule belongs to.
# CSV Naming Convention: Regulatory_Compliance_Policy_Rule_Details.csv
# JSON Naming Convention:
# {Customer ID}_Policy_Rule_Details_{Success Track ID}_{Page #}.json
def pxc_compliance_rule_details():
    print("******************************************************************")
    print("************* Running Compliance Rule Detail Report **************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(RCCPolicyRuleDetails, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "policyName," \
                         "policyDescription," \
                         "ruleId," \
                         "policyId	"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(RCCComplianceViolations, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        fileNum = 0
        for row in custList:
            fileNum += 1
            if debug_level == 1 or debug_level == 2:
                print("Compliance Rule Detail for Customer:", row["customerId"],
                      "on Success Tracks:", row["successTrackId"])
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            policyCategory = row['policyCategory']
            policyGroupId = row['policyGroupId']
            policyId = row['policyId']
            ruleId = row['ruleId']
            severity = row['severity']
            url = (pxc_url_customers + "/" +
                   customerId +
                   pxc_url_compliance_policy_rule_details +
                   "?policyCategory=" + policyCategory +
                   "&policyGroupId=" + policyGroupId +
                   "&policyId=" + policyId +
                   "&ruleId=" + ruleId +
                   "&severity=" + severity +
                   "&successTrackId=" + successTrackId +
                   "&max=" + max_items)
            try:
                headers = {
                    'Authorization': f'Bearer {token}'
                }
                response = requests.request("GET", url, headers=headers, verify=True)
                reply = json.loads(response.text)
                if response.status_code == 200:
                    items = {'items': [reply]}
                    policyName = str(reply['policyName'])
                    policyDescription = str(reply['policyDescription'])
                    ruleId = str(reply['ruleId'])
                    policyId = str(reply['policyId'])
                    print(f"\nFound Policy {policyName}")
                if debug_level == 2:
                    print("URL Request:", url,
                          "\nHTTP Code:", response.status_code,
                          "\nReview API Headers:", response.headers,
                          "\nResponse Body:", response.content)
            except Exception as Error:
                print(f"\nFailed to collect {Error} due to reply from API: ", reply['message'])
                items = []
            finally:
                if outputFormat == 1 or outputFormat == 2:
                    with open(json_output_dir + customerId +
                              "_Policy_Rule_Details_" + successTrackId +
                              "_Page_" + str(fileNum) +
                              ".json", 'w') as json_file:
                        json.dump(items, json_file)
                        print(f"Saving {json_file.name}")
                if outputFormat == 1 or outputFormat == 3:
                    with open(RCCPolicyRuleDetails, 'a', encoding="utf-8", newline='') as target:
                        writer = csv.writer(target,
                                            delimiter=' ',
                                            quotechar=' ',
                                            quoting=csv.QUOTE_MINIMAL)
                        CSV_Data = (customerId + ',' +
                                    customerName + ',' +
                                    successTrackId + ',' +
                                    policyName + ',' +
                                    policyDescription + ',' +
                                    ruleId + ',' +
                                    policyId)
                        writer.writerow(CSV_Data.split())
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Functions to get the Compliance Suggestions data from PX Cloud (currently only for Campus Network Success Tracks)
# This API returns information about the violated rule conditions based on the policy, and rule information provided.
# CSV Naming Convention: Compliance_Suggestions.csv
# JSON Naming Convention:{Customer ID}_Compliance_Suggestions__{Success Track ID}_{Page #}.json
def pxc_compliance_suggestions():
    print("******************************************************************")
    print("***************** Running Compliance Suggestions *****************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(RCCComplianceSuggestions, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "policyId," \
                         "policyCategory," \
                         "policyGroupId," \
                         "ruleId," \
                         "severity," \
                         "violationMessage," \
                         "suggestion," \
                         "affectedAssetsCount"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(RCCComplianceViolations, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        fileNum = 0
        for row in custList:
            fileNum += 1
            if debug_level == 1 or debug_level == 2:
                print("Compliance Suggestions for Customer :", row["customerId"],
                      "on Success Tracks:", row["successTrackId"])
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            policyId = row['policyId']
            policyCategory = row['policyCategory']
            policyGroupId = row['policyGroupId']
            ruleId = row['ruleId']
            headers = {'Authorization': f'Bearer {token}'}
            url = (pxc_url_customers + "/" +
                   customerId +
                   pxc_url_compliance_suggestions +
                   "?successTrackId=" + successTrackId +
                   "&policyId=" + policyId +
                   "&policyCategory=" + policyCategory +
                   "&policyGroupId=" + policyGroupId +
                   "&ruleId=" + ruleId +
                   "&max=" + max_items)
            if fileNum == 1:
                print(f"\nFound Compliance Suggestions on Success Track {successTrackId} "
                      f"for {customerName}")
            response = requests.request("GET", url, headers=headers, data=payload, verify=True)
            reply = json.loads(response.text)
            if debug_level == 1 or debug_level == 2:
                print(reply)
            try:
                if response.status_code == 200:
                    totalCount = reply["totalCount"]
                    pages = math.ceil(totalCount / int(max_items))
                    if debug_level == 1 or debug_level == 2:
                        print("\nTotal Pages:", pages,
                              "\nTotal Records: ", totalCount,
                              "\nURL Request:", url,
                              "\nHTTP Code:", response.status_code,
                              "\nReview API Headers:", response.headers,
                              "\nResponse Body:", response.content)
                    page = 0
                    while page < pages:
                        url = (pxc_url_customers + "/" +
                               customerId +
                               pxc_url_compliance_suggestions +
                               "?successTrackId=" + successTrackId +
                               "&policyId=" + policyId +
                               "&policyCategory=" + policyCategory +
                               "&policyGroupId=" + policyGroupId +
                               "&ruleId=" + ruleId +
                               "&days=30" +
                               "&max=" + max_items)
                        items = (get_json_reply(url, tag="items"))
                        if items is not None:
                            if len(items) > 0:
                                if outputFormat == 1 or outputFormat == 2:
                                    with open(json_output_dir + customerId +
                                              "_Compliance_Suggestions_" + successTrackId + "_Page_" + str(fileNum) +
                                              ".json", 'w') as json_file:
                                        json.dump(items, json_file)
                                    print(f"Saving {json_file.name}")
                                if outputFormat == 1 or outputFormat == 3:
                                    for item in items:
                                        severity = item['severity'].replace(",", " ")
                                        violationMessage = item['violationMessage'].replace(",", " ")
                                        suggestion = str(item['suggestion']).replace(",", " ")
                                        affectedAssetsCount = str(item['affectedAssetsCount'])
                                        with open(RCCComplianceSuggestions, 'a', encoding="utf-8", newline='') \
                                                as target:
                                            writer = csv.writer(target,
                                                                delimiter=' ',
                                                                quotechar=' ',
                                                                quoting=csv.QUOTE_MINIMAL)
                                            CSV_Data = (customerId + ',' +
                                                        customerName + ',' +
                                                        successTrackId + ',' +
                                                        policyId + ',' +
                                                        policyCategory + ',' +
                                                        policyGroupId + ',' +
                                                        ruleId + ',' +
                                                        severity + ',' +
                                                        violationMessage + ',' +
                                                        suggestion + ',' +
                                                        affectedAssetsCount)
                                            writer.writerow(CSV_Data.split())
                            else:
                                print("No Data Found .... Skipping")
                        page += 1
            except KeyError:
                print("No Data to process... Skipping.")
                pass
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to get the Assets with Violations data from PX Cloud
# This API returns information about assets that have at least one rule violation based on the customerId provided.
# CSV Naming Convention: Regulatory_Compliance_Assets_With_Violations.csv
# JSON Naming Convention: {Customer ID}_Assets_with_Violations_{successTrackId}.json
def pxc_assets_with_violations():
    print("******************************************************************")
    print("***************** Running Assets with Violations *****************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(RCCAssetsWithViolations, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "ipAddress," \
                         "serialNumber," \
                         "violationCount," \
                         "assetGroup," \
                         "role," \
                         "sourceSystemId," \
                         "assetId," \
                         "assetName," \
                         "lastChecked," \
                         "softwareType," \
                         "softwareRelease," \
                         "severity," \
                         "severityId," \
                         "policyId," \
                         "ruleId," \
                         "scanStatus"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(RCCComplianceViolations, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        fileNum = 0
        for row in custList:
            fileNum += 1
            if debug_level == 1 or debug_level == 2:
                print("====================\n\n")
                print("Assets with Violations for Customer:", row["customerId"],
                      "on Success Tracks:", row["successTrackId"])
            if not row["successTrackId"] == "N/A":
                customerName = row["customerName"]
                customerId = row["customerId"]
                successTrackId = row["successTrackId"]
                policyId = row["policyId"]
                ruleId = row["ruleId"]
                url = (
                        pxc_url_customers + "/" + customerId +
                        pxc_url_compliance_assets_with_violations +
                        "?successTrackId=" + successTrackId)
                if fileNum == 1:
                    print(f"Found Customer", row["customerName"], "on Success Track", row["successTrackId"])
                items = (get_json_reply(url, tag="items"))
                if outputFormat == 1 or outputFormat == 2:
                    if items is not None:
                        if len(items) > 0:
                            with open(
                                    json_output_dir + customerId + "_Assets_with_Violations_" + successTrackId +
                                    "_Page_" + str(fileNum) + ".json", 'w') as json_file:
                                json.dump(items, json_file)
                            print(f"Saving {json_file.name}")
                if outputFormat == 1 or outputFormat == 3:
                    if items is not None:
                        if len(items) > 0:
                            for item in items:
                                ipAddress = str(item['ipAddress'])
                                serialNumber = str(item['serialNumber'])
                                violationCount = str(item['violationCount'])
                                assetGroups = str(item['assetGroups'])
                                role = str(item['role'])
                                sourceSystemId = str(item['sourceSystemId'])
                                assetId = str(item['assetId']).replace(",", "_")
                                assetName = str(item['assetName'])
                                lastChecked = str(item['lastChecked'])
                                softwareType = str(item['softwareType'])
                                softwareRelease = str(item['softwareRelease'])
                                severity = str(item['severity'])
                                severityId = str(item['severityId'])
                                scanStatus = str(item['scanStatus'])
                                with open(RCCAssetsWithViolations, 'a', encoding="utf-8", newline='') as target:
                                    writer = csv.writer(target,
                                                        delimiter=' ',
                                                        quotechar=' ',
                                                        quoting=csv.QUOTE_MINIMAL)
                                    CSV_Data = (customerId + ',' +
                                                customerName + ',' +
                                                successTrackId + ',' +
                                                ipAddress + ',' +
                                                serialNumber + ',' +
                                                violationCount + ',' +
                                                assetGroups + ',' +
                                                role + ',' +
                                                sourceSystemId + ',' +
                                                assetId + ',' +
                                                assetName + ',' +
                                                lastChecked + ',' +
                                                softwareType + ',' +
                                                softwareRelease + ',' +
                                                severity + ',' +
                                                severityId + ',' +
                                                policyId + ',' +
                                                ruleId + ',' +
                                                scanStatus)
                                    writer.writerow(CSV_Data.split())
            else:
                print("\nNo Data Found .... Skipping")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to get the Asset Violations data from PX Cloud
# This API returns information about the rules violated by an asset based on the information provided.
# CSV Naming Convention: Regulatory_Compliance_Asset_Violations.csv
# JSON Naming Convention: {Customer ID}_Asset_Violations_{sourceSystemId}_Page_##.json
def pxc_asset_violations():
    print("******************************************************************")
    print("************** Running Assets Violations Report ******************")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(RCCAssetViolations, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "sourceSystemId," \
                         "assetId," \
                         "successTrackId," \
                         "severity," \
                         "regulatoryType," \
                         "violationMessage," \
                         "suggestion," \
                         "violationAge," \
                         "policyDescription," \
                         "ruleTitle," \
                         "ruleDescription"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(RCCAssetsWithViolations, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        fileNum = 0
        for row in custList:
            fileNum += 1
            if debug_level == 1 or debug_level == 2:
                print("Asset Violations for Customer:", row["customerId"],
                      "on Success Tracks:", row["successTrackId"])
            customerId = row['customerId']
            customerName = row['customerName']
            sourceSystemId = row['sourceSystemId']
            assetId = row['assetId'].replace("_", ",")
            successTrackId = row['successTrackId']
            url = (pxc_url_customers + "/" +
                   customerId +
                   pxc_url_compliance_asset_violations +
                   "?sourceSystemId=" + sourceSystemId +
                   "&assetId=" + assetId +
                   "&successTrackId=" + successTrackId +
                   "&max=" + max_items)
            if fileNum == 1:
                print(f"Found Customer", row["customerName"], "on Success Track", row["successTrackId"])
            items = (get_json_reply(url, tag="items"))
            if not items:
                print("No data found... Skipping")
            if outputFormat == 1 or outputFormat == 2:
                if items is not None:
                    if len(items) > 0:
                        with open(json_output_dir + customerId +
                                  "_Asset_Violations_" + sourceSystemId +
                                  "_Page_" + str(fileNum) +
                                  ".json", 'w') as json_file:
                            json.dump(items, json_file)
                        print(f"Saving {json_file.name}")
            try:
                if outputFormat == 1 or outputFormat == 3:
                    if items is not None:
                        if len(items) > 0:
                            for item in items:
                                assetId = str(row['assetId']).replace(",", "_")
                                severity = str(item['severity']).replace(",", " ")
                                regulatoryType = str(item['regulatoryType']).replace(",", " ")
                                violationMessage = str(item['violationMessage']).replace(",", " ")
                                suggestion = str(item['suggestion']).replace(",", " ")
                                violationAge = str(item['violationAge']).replace(",", " ")
                                policyDescription = str(item['policyDescription']).replace(",", " ")
                                ruleTitle = str(item['ruleTitle']).replace(",", " ")
                                ruleDescription = str(item['ruleDescription']).replace(",", " ")
                                with open(RCCAssetViolations, 'a', encoding="utf-8", newline='') as target:
                                    writer = csv.writer(target,
                                                        delimiter=' ',
                                                        quotechar=' ',
                                                        quoting=csv.QUOTE_MINIMAL)
                                    CSV_Data = (customerId + ',' +
                                                customerName + ',' +
                                                sourceSystemId + ',' +
                                                assetId + ',' +
                                                successTrackId + ',' +
                                                severity + ',' +
                                                regulatoryType + ',' +
                                                violationMessage + ',' +
                                                suggestion + ',' +
                                                violationAge + ',' +
                                                policyDescription + ',' +
                                                ruleTitle + ',' +
                                                ruleDescription)
                                    writer.writerow(CSV_Data.split())
                        else:
                            print("\nNo Data Found .... Skipping")
                            print("====================\n\n")
            except KeyError:
                print("No Data to process... Skipping.")
                pass
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Function to get the Obtained data from PX Cloud
# This API returns information about whether the customer has successfully configured the regulatory compliance feature
#   and has violation data available
# CSV Naming Convention: Regulatory_Compliance_Obtained.csv
# JSON Naming Convention: {Customer ID}_Obtained_{successTrackId}.json
def pxc_obtained():
    print("******************************************************************")
    print("********* Running Regulatory Compliance Obtained Report **********")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(RCCObtained, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTracksId," \
                         "status," \
                         "hasQualifiedAssets"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(customers, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            if debug_level == 1 or debug_level == 2:
                print("====================\n\n")
                print("Obtained data for Customer:", customerId,
                      "on Success Tracks:", successTrackId)
            if not successTrackId == "N/A":
                print(f"Found Customer", customerName, "on Success Track", successTrackId)
                url = (pxc_url_customers + "/" +
                       customerId +
                       pxc_url_compliance_obtained +
                       "?successTrackId=" + successTrackId)
                try:
                    headers = {
                        'Authorization': f'Bearer {token}'
                    }
                    response = requests.request("GET", url, headers=headers, verify=True)
                    reply = json.loads(response.text)
                    if response.status_code == 200:
                        if len(reply) > 0:
                            items = {'items': [reply]}
                            status = str(reply['status'])
                            hasQualifiedAssets = str(reply['hasQualifiedAssets'])
                        if debug_level == 2:
                            print("URL Request:", url,
                                  "\nHTTP Code:", response.status_code,
                                  "\nReview API Headers:", response.headers,
                                  "\nResponse Body:", response.content)
                except Exception as Error:
                    if response.text.__contains__("Customer admin has not provided access."):
                        if debug_level == 2:
                            print("\nResponse Body:", response.content)
                            print(Error)
                        print("Customer admin has not provided access....Skipping")
                if outputFormat == 1 or outputFormat == 2:
                    if items is not None:
                        if len(items) > 0:
                            with open(json_output_dir + customerId + "_Obtained_" + successTrackId + ".json",
                                      'w') as json_file:
                                json.dump(items, json_file)
                            print(f"Saving {json_file.name}\n")
                    if outputFormat == 1 or outputFormat == 3:
                        with open(RCCObtained, 'a', encoding="utf-8", newline='') as target:
                            writer = csv.writer(target,
                                                delimiter=' ',
                                                quotechar=' ',
                                                quoting=csv.QUOTE_MINIMAL)
                            CSV_Data = (customerId + ',' +
                                        customerName + ',' +
                                        successTrackId + ',' +
                                        str(status) + ',' +
                                        str(hasQualifiedAssets))
                            writer.writerow(CSV_Data.split())
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Functions to get the Crash Risk Assets data from PX Cloud (currently only for Campus Network Success Tracks)
# This API returns information about assets with a crash risk value of Medium or High for the customerId provided.
# CSV Naming Convention: Crash_Risk_Assets.csv
# JSON Naming Convention:{Customer ID}_Crash_Risk_Assets_{Success Track ID}.json
def pxc_crash_risk_assets():
    print("******************************************************************")
    print("******* Running Risk Mitigation Checks on Crash Risk Assets ******")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(CrashRiskAssets, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "crashPredicted," \
                         "assetId," \
                         "assetUniqueId," \
                         "assetName," \
                         "ipAddress," \
                         "productId," \
                         "productFamily," \
                         "softwareRelease," \
                         "softwareType," \
                         "serialNumber," \
                         "risk," \
                         "endDate"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(customers, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            if not row["successTrackId"] == "N/A":
                print(f"\nFound Customer", customerName, "on Success Track", successTrackId)
                url = (pxc_url_customers + "/" +
                       customerId +
                       pxc_url_crash_risk_assets +
                       "?successTrackId=" + successTrackId +
                       "&max=" + max_items)
                items = get_json_reply(url, tag="items")
                crashPredicted = str(get_json_reply(url, tag="crashPredicted"))
                if items is not None:
                    if len(items) > 0:
                        if outputFormat == 1 or outputFormat == 2:
                            with open(json_output_dir + customerId +
                                      "_Crash_Risk_Assets_" + successTrackId +
                                      ".json", 'w') as json_file:
                                json.dump(items, json_file)
                            print(f"Saving {json_file.name}")
                        if outputFormat == 1 or outputFormat == 3:
                            if items:
                                for item in items:
                                    assetId = item['assetId'].lower()
                                    assetId_bytes = assetId.lower().encode('ascii')
                                    assetIdBase64_bytes = base64.b64encode(assetId_bytes)
                                    assetUniqueId = assetIdBase64_bytes.decode('ascii')
                                    assetName = str(item['assetName']).replace(",", " ")
                                    ipAddress = str(item['ipAddress'])
                                    productId = str(item['productId']).replace(",", " ")
                                    productFamily = str(item['productFamily']).replace(",", " ")
                                    softwareRelease = str(item['softwareRelease'])
                                    softwareType = str(item['softwareType']).replace(",", " ")
                                    serialNumber = str(item['serialNumber'])
                                    risk = str(item['risk'])
                                    endDate = str(item['endDate'])
                                    if debug_level == 1 or debug_level == 2:
                                        print(f"assetId From CSV: {assetId} -- "
                                              f"assetId converted: {assetId_bytes} -- "
                                              f"assetUniqueId: {assetUniqueId}")
                                    with open(CrashRiskAssets, 'a', encoding="utf-8", newline='') as target:
                                        writer = csv.writer(target,
                                                            delimiter=' ',
                                                            quotechar=' ',
                                                            quoting=csv.QUOTE_MINIMAL)
                                        CSV_Data = (customerId + ',' +
                                                    customerName + ',' +
                                                    successTrackId + ',' +
                                                    crashPredicted + ',' +
                                                    assetId.replace(",", "_") + ',' +
                                                    assetUniqueId + ',' +
                                                    assetName + ',' +
                                                    ipAddress + ',' +
                                                    productId + ',' +
                                                    productFamily + ',' +
                                                    softwareRelease + ',' +
                                                    softwareType + ',' +
                                                    serialNumber + ',' +
                                                    risk + ',' +
                                                    endDate)
                                        writer.writerow(CSV_Data.split())
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Functions to get the Crash Risk Factors data from PX Cloud (currently only for Campus Network Success Tracks)
# This API returns the risk factors that contribute to the crash risk value of the asset.
# CSV Naming Convention: Crash_Risk_Factors.csv
# JSON Naming Convention:{Customer ID}_Crash_Risk_Factors_{Success Track ID}_{Asset ID}.json
def pxc_crash_risk_factors():
    print("******************************************************************")
    print("****** Running Risk Mitigation Checks on Crash Risk Factors ******")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(CrashRiskFactors, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "assetId," \
                         "factor," \
                         "factorType"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(CrashRiskAssets, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            assetId = row["assetId"]
            assetUniqueId = row["assetUniqueId"]
            if not row["successTrackId"] == "N/A":
                print(f"\nFound Customer", customerName, "on Success Track", successTrackId)
                url = (pxc_url_customers + "/" +
                       customerId +
                       pxc_url_crash_risk_assets + "/" + assetUniqueId +
                       pxc_url_crash_risk_factors +
                       "?successTrackId=" + successTrackId +
                       "&max=" + max_items)
                if debug_level == 1 or debug_level == 2:
                    print(url)
                items = get_json_reply(url, tag="items")
                if outputFormat == 1 or outputFormat == 2:
                    if items is not None:
                        if len(items) > 0:
                            with open(json_output_dir + customerId +
                                      "_Crash_Risk_Factors_" + successTrackId + "_" + assetId.upper() +
                                      ".json", 'w') as json_file:
                                json.dump(items, json_file)
                            print(f"Saving {json_file.name}")
                if outputFormat == 1 or outputFormat == 3:
                    if items is not None:
                        if len(items) > 0:
                            for item in items:
                                factor = str(item['factor']).replace(",", " ")
                                factorType = str(item['factorType']).replace(",", " ")
                                with open(CrashRiskFactors, 'a', encoding="utf-8", newline='') as target:
                                    writer = csv.writer(target,
                                                        delimiter=' ',
                                                        quotechar=' ',
                                                        quoting=csv.QUOTE_MINIMAL)
                                    CSV_Data = (customerId + ',' +
                                                customerName + ',' +
                                                successTrackId + ',' +
                                                assetId + ',' +
                                                factor + ',' +
                                                factorType)
                                    writer.writerow(CSV_Data.split())
            else:
                print("\nNo Data Found .... Skipping")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Functions to get the Similar Asset's data from PX Cloud (currently only for Campus Network Success Tracks)
# This API returns information about similar assets with a lower crash risk rating than the specified assetId based on
#   the similarityCriteria and customerId provided.
# CSV Naming Convention: Similar_Assets.csv
# JSON Naming Convention:{Customer ID}_Similar_Assets_{Success Track ID}_{Asset ID}_{Features}.json
def pxc_similar_assets():
    print("******************************************************************")
    print("******** Running Risk Mitigation Checks on Similar Assets ********")
    print("******************************************************************")
    print("Searching ......\n\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(CrashRiskSimilarAssets, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "crashPredicted," \
                         "assetId," \
                         "assetName," \
                         "productId," \
                         "productFamily," \
                         "softwareRelease," \
                         "softwareType," \
                         "serialNumber," \
                         "risk," \
                         "feature," \
                         "similarityScore"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(CrashRiskAssets, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            assetId = row["assetId"]
            assetUniqueId = row["assetUniqueId"]
            if not row["successTrackId"] == "N/A":
                print(f"\nFound Asset ID", assetId, "for Customer", customerName, "on Success Track", successTrackId)
                for feature in features:
                    url = (pxc_url_customers + "/" +
                           customerId +
                           pxc_url_crash_risk_assets + "/" +
                           assetUniqueId +
                           pxc_url_crash_risk_similar_assets +
                           "?similarityCriteria=" + feature +
                           "&successTrackId=" + successTrackId + "&max=" + max_items)
                    print(f"Scanning for Similar Assets for asset ID {assetId} for {customerName} with same {feature}")
                    items = get_json_reply(url, tag="items")
                    crashPredicted = str(get_json_reply(url, tag="crashPredicted"))
                    if outputFormat == 1 or outputFormat == 2:
                        if items is not None:
                            if len(items) > 0:
                                with open(json_output_dir + customerId +
                                          "_Similar_Assets_" + successTrackId + "_" + assetId.upper() + "_" + feature +
                                          ".json", 'w') as json_file:
                                    json.dump(items, json_file)
                                print(f"Saving {json_file.name}")
                    if outputFormat == 1 or outputFormat == 3:
                        if items is not None:
                            if len(items) > 0:
                                for item in items:
                                    assetId = str(item['assetId']).replace(",", "_")
                                    assetName = str(item['assetName']).replace(",", " ")
                                    productId = str(item['productId']).replace(",", " ")
                                    productFamily = str(item['productFamily']).replace(",", " ")
                                    softwareRelease = str(item['softwareRelease']).replace(",", " ")
                                    softwareType = str(item['softwareType']).replace(",", " ")
                                    serialNumber = str(item['serialNumber']).replace(",", " ")
                                    risk = str(item['risk']).replace(",", " ")
                                    similarityScore = str(item['similarityScore']).replace(",", " ")
                                    with open(CrashRiskSimilarAssets, 'a', encoding="utf-8", newline='') as target:
                                        writer = csv.writer(target,
                                                            delimiter=' ',
                                                            quotechar=' ',
                                                            quoting=csv.QUOTE_MINIMAL)
                                        CSV_Data = (customerId + ',' +
                                                    customerName + ',' +
                                                    successTrackId + ',' +
                                                    crashPredicted + ',' +
                                                    assetId + ',' +
                                                    assetName + ',' +
                                                    productId + ',' +
                                                    productFamily + ',' +
                                                    softwareRelease + ',' +
                                                    softwareType + ',' +
                                                    serialNumber + ',' +
                                                    risk + ',' +
                                                    feature + ',' +
                                                    similarityScore)
                                        writer.writerow(CSV_Data.split())
            else:
                print(f"No data found for {feature}\n")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Functions to get the Assets Crashed in last 1d, 7d, 15d, 90d data from PX Cloud.
# This API provides the list of devices with details (i.e. Asset, Product Id, Product Family, Software Version,
#   Crash Count, First Occurrence and Last Occurrence) by customer ID that have crashed in the last 1d,7d,15d,90d based
#   on the filter input. Default sort is by lastCrashDate.
# CSV Naming Convention: Crash_Risk_Assets_Last_Crashed.csv
# JSON Naming Convention:{Customer ID}_Crash_Risk_Assets_Last_Crashed_In_{timePeriod}_Days_{Success Track ID}.json
def pxc_crash_in_last():
    print("******************************************************************")
    print("*** Running Risk Mitigation Checks on Assets last Crashed date ***")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(CrashRiskAssetsLastCrashed, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "daysLastCrashed," \
                         "assetId," \
                         "assetName," \
                         "productId," \
                         "productFamily," \
                         "softwareRelease," \
                         "softwareType," \
                         "serialNumber," \
                         "firstCrashDate," \
                         "lastCrashDate," \
                         "crashCount," \
                         "ipAddress"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(CrashRiskAssets, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            serialNumber = row['serialNumber']
            for daysLastCrashed in timePeriods:
                if not row["successTrackId"] == "N/A":
                    print(f"Scanning Serial Number {serialNumber} with a last crashed date within {daysLastCrashed} "
                          f"days for {customerName} ")
                    url = (pxc_url_customers + "/" +
                           customerId +
                           pxc_url_crash_risk_assets_last_crashed +
                           "?successTrackId=" + successTrackId +
                           "&timePeriod=" + str(daysLastCrashed))
                    if debug_level == 1 or debug_level == 2:
                        print(url)
                    items = get_json_reply(url, tag="items")
                    if outputFormat == 1 or outputFormat == 2:
                        if items is not None:
                            if len(items) > 0:
                                with open(json_output_dir + customerId +
                                          "_Crash_Risk_Assets_Last_Crashed_In_" + str(daysLastCrashed) + "_Days_" +
                                          successTrackId + ".json", 'w') as json_file:
                                    json.dump(items, json_file)
                                print(f"Saving {json_file.name}")
                    if outputFormat == 1 or outputFormat == 3:
                        if items:
                            for item in items:
                                assetId = str(item['assetId']).replace(",", "_")
                                assetName = str(item['assetName']).replace(",", " ")
                                productId = str(item['productId']).replace(",", " ")
                                productFamily = str(item['productFamily']).replace(",", " ")
                                softwareRelease = str(item['softwareRelease']).replace(",", " ")
                                softwareType = str(item['softwareType']).replace(",", " ")
                                serialNumber = str(item['serialNumber']).replace(",", " ")
                                firstCrashDate = str(item['firstCrashDate']).replace(",", " ")
                                lastCrashDate = str(item['lastCrashDate']).replace(",", " ")
                                crashCount = str(item['crashCount']).replace(",", " ")
                                ipAddress = str(item['ipAddress']).replace(",", " ")
                                with open(CrashRiskAssetsLastCrashed, 'a', encoding="utf-8", newline='') as target:
                                    writer = csv.writer(target,
                                                        delimiter=' ',
                                                        quotechar=' ',
                                                        quoting=csv.QUOTE_MINIMAL)
                                    CSV_Data = (customerId + ',' +
                                                customerName + ',' +
                                                successTrackId + ',' +
                                                str(daysLastCrashed) + ',' +
                                                assetId + ',' +
                                                assetName + ',' +
                                                productId + ',' +
                                                productFamily + ',' +
                                                softwareRelease + ',' +
                                                softwareType + ',' +
                                                serialNumber + ',' +
                                                firstCrashDate + ',' +
                                                lastCrashDate + ',' +
                                                crashCount + ',' +
                                                ipAddress)
                                    writer.writerow(CSV_Data.split())
                else:
                    print("\nNo Data Found .... Skipping")
                    print("====================\n\n")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


# Functions to get the Asset Crash History from PX Cloud (currently only for Campus Network Success Tracks)
# This API returns information for each crash that occurred during the last 365 days for the assetId and customerId
#   provided in the last 1 year.Default sort is by timeStamp.
# CSV Naming Convention: Asset_Crash_History.csv
# JSON Naming Convention:{Customer ID}_Asset_Crash_History_{Success Track ID}_{Base64 Asset ID}.json
def pxc_asset_crash_history():
    print("******************************************************************")
    print("***** Running Risk Mitigation Checks on Assets Crash History *****")
    print("******************************************************************")
    print("Searching ......\n", end="")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Start DateTime:', now)
    if outputFormat == 1 or outputFormat == 3:
        with open(CrashRiskAssetCrashHistory, 'w', encoding="utf-8", newline='') as target:
            CSV_Header = "customerId," \
                         "customerName," \
                         "successTrackId," \
                         "assetId," \
                         "resetReason," \
                         "timeStamp"
            writer = csv.writer(target, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_NONE)
            writer.writerow(CSV_Header.split())
    with open(CrashRiskAssets, 'r') as cust_target:
        custList = csv.DictReader(cust_target)
        for row in custList:
            customerId = row['customerId']
            customerName = row['customerName']
            successTrackId = row['successTrackId']
            assetUniqueId = row["assetUniqueId"]
            assetId = row["assetId"]
            if not row["successTrackId"] == "N/A":
                print(f"\nScanning Asset ID", assetId, "for Customer", customerName, "on Success Track", successTrackId)
                url = (pxc_url_customers + "/" +
                       customerId +
                       pxc_url_crash_risk + "/" +
                       assetUniqueId +
                       pxc_url_crash_risk_asset_crash_history +
                       "?successTrackId=" + successTrackId +
                       "&max=" + max_items)
                items = get_json_reply(url, tag="items")
                if outputFormat == 1 or outputFormat == 2:
                    if items is not None:
                        if len(items) > 0:
                            with open(json_output_dir + customerId +
                                      "_Asset_Crash_History_" + successTrackId + "_" + assetUniqueId +
                                      ".json", 'w') as json_file:
                                json.dump(items, json_file)
                            print(f"Saving {json_file.name}")
                if outputFormat == 1 or outputFormat == 3:
                    if items:
                        for item in items:
                            resetReason = str(item['resetReason']).replace(",", "_")
                            timeStamp = str(item['timeStamp']).replace(",", " ")
                            with open(CrashRiskAssetCrashHistory, 'a', encoding="utf-8", newline='') as target:
                                writer = csv.writer(target,
                                                    delimiter=' ',
                                                    quotechar=' ',
                                                    quoting=csv.QUOTE_MINIMAL)
                                CSV_Data = (customerId + ',' +
                                            customerName + ',' +
                                            successTrackId + ',' +
                                            assetUniqueId + ',' +
                                            resetReason + ',' +
                                            timeStamp)
                                writer.writerow(CSV_Data.split())
            else:
                print("\nNo Data Found .... Skipping")
                print("====================\n\n")
    print("\nSearch Completed!")
    if debug_level == 1 or debug_level == 2:
        now = datetime.now()
        print('Stop DateTime:', now)
    print("====================\n\n")


'''
Begin main application control
=======================================================================
'''
# call function to load config.ini data into variables
load_config()
# clear log folder before the script runs if logging is enabled
if log_to_file == "True" or log_to_file == "true":
    if outputFormat == 1:
        print("Saving data in JSON and CSV formats")
    if outputFormat == 2:
        print("Saving data in JSON format")
    if outputFormat == 3:
        print("Saving data in CSV format")
    if os.path.isdir(log_output_dir):
        shutil.rmtree(log_output_dir)
        os.mkdir(log_output_dir)
    else:
        os.mkdir(log_output_dir)

# Set URL to Sandbox if useProductionURL is false
if useProductionURL == "False" or useProductionURL == "false":
    pxc_url_base = urlProtocol + urlHost + urlLinkSandbox
    pxc_scope = "api.customer.assets.manage"
    environment = "Sandbox"
else:
    pxc_url_base = urlProtocol + urlHost + urlLink
    pxc_scope = "api.authz.iam.manage"
    environment = "Production"
pxc_url_customers = pxc_url_base + "customers"
pxc_url_contracts = pxc_url_base + "contracts"
pxc_url_contracts_details = pxc_url_base + "contract/details"
pxc_url_partner_offers = pxc_url_base + "partnerOffers"
pxc_url_partner_offers_sessions = pxc_url_base + "partnerOffersSessions"
pxc_url_successTracks = pxc_url_base + "successTracks"

# Set number of itterations for testing, time stamp, logging level and if the log should be written to file
for x in range(0, testLoop):
    if debug_level == 0:
        logLevel = "Low"
    elif debug_level == 1:
        logLevel = "Medium"
    elif debug_level == 2:
        logLevel = "High"
    if log_to_file == "True" or log_to_file == "true":
        print("Logging output to file PXCloud_##.log with debug level set to", logLevel, "for version ", codeVersion)
        sys.stdout = open(log_output_dir + 'PXCLoud_' + str(x + 1) + '.log', 'wt')
    startTime = time.time()
    print('Start Time:', datetime.now())
    print("Execution:", x + 1, "of", testLoop, "\nDebug level is:", logLevel, "\nVersion is", codeVersion,
          "\nEnvironment is", environment)
    if outputFormat == 1:
        print("Saving data in JSON and CSV formats")
    if outputFormat == 2:
        print("Saving data in JSON format")
    if outputFormat == 3:
        print("Saving data in CSV format")

    # delete temp and output directories and recreate before every run
    temp_storage()

    # call the function to get a valid PX Cloud API token
    get_pxc_token()

    # call the function to get the PX Cloud Customer List
    get_pxc_customers()

    # call the function to get the PX Cloud Contract List
    get_pxc_contracts()  # requires CSV data from get_pxc_customers

    # call the function to get the PX Cloud Contract Details
    get_pxc_contracts_details()  # requires CSV data from get_pxc_contracts

    # call the function to get the PX Cloud Partner Offers
    get_pxc_partner_offers()

    # call the function to get the PX Cloud Partner Offer Sessions
    get_pxc_partner_offer_sessions()

    # call the function to get the PX Success Tracks List
    get_pxc_succsstracks()

    # call the function to get a valid PX Cloud API token if needed
    token_time_check()

    # call the function to request and process the PX Cloud Assets Reports data
    pxc_assets_reports()  # requires CSV data from get_pxc_customers

    # call the function to request and process the PX Cloud Hardware Reports data
    pxc_hardware_reports()  # requires CSV data from get_pxc_customers

    # call the function to request and process the PX Cloud Software Reports data
    pxc_software_reports()  # requires CSV data from get_pxc_customers

    # call the function to request and process the PX Cloud Purchased Licenses Reports data
    pxc_purchased_licenses_reports()  # requires CSV data from get_pxc_customers

    # call the function to request and process the PX Cloud Licenses Reports data
    pxc_licenses_reports()  # requires CSV data from get_pxc_customers

    # call the function to get the PX Cloud Lifecycle data
    get_pxc_lifecycle()  # requires CSV data from get_pxc_customers

    # call the function to get a valid PX Cloud API token if needed
    token_time_check()

    # call the function to request and process the PX Cloud Security Advisories Reports data
    pxc_security_advisories_reports()  # requires CSV data from get_pxc_customers

    # call the function to request and process the PX Cloud Field Notices Reports data
    pxc_field_notices_reports()  # requires CSV data from get_pxc_customers

    # call the function to request and process the PX Cloud Priority Bugs Reports data
    pxc_priority_bugs_reports()  # requires CSV data from get_pxc_customers

    # call the Optimal Software Version data from PX Cloud (currently only for Campus Network Success Tracks)
    pxc_software_groups()  # requires CSV data from get_pxc_customers
    pxc_software_group_suggestions()  # requires CSV data from pxc_software_groups
    pxc_software_group_suggestions_assets()  # requires CSV data from pxc_software_groups
    pxc_software_group_suggestions_bug_list()  # requires CSV data from pxc_software_group_suggestions
    pxc_software_group_suggestions_field_notices()  # requires CSV data from pxc_software_group_suggestions
    pxc_software_group_suggestions_advisories()  # requires CSV data from pxc_software_group_suggestions

    # call the Automated Fault Management data from PX Cloud (currently only for Campus Network Success Tracks)
    pxc_automated_fault_management_faults()  # requires CSV data from get_pxc_customers
    pxc_automated_fault_management_fault_summary()  # requires CSV data from pxc_automated_fault_management_faults
    pxc_automated_fault_management_affected_assets()  # requires CSV data from pxc_automated_fault_management_faults

    # call the function to get a valid PX Cloud API token if needed
    token_time_check()

    # call the Regulatory Compliance Check data from PX Cloud (currently only for Campus Network Success Tracks)
    pxc_compliance_violations()  # requires CSV data from get_pxc_customers
    pxc_assets_violating_compliance_rule()  # requires CSV data from pxc_compliance_violations
    pxc_compliance_rule_details()  # requires CSV data from pxc_compliance_violations
    pxc_compliance_suggestions()  # requires CSV data from pxc_compliance_violations
    pxc_assets_with_violations()  # requires CSV data from get_pxc_customers
    pxc_asset_violations()  # requires CSV data from pxc_assets_with_violations
    pxc_obtained()  # requires CSV data from get_pxc_customers

    # call the Risk Mitigation Check data from PX Cloud (currently only for Campus Network Success Tracks)
    pxc_crash_risk_assets()  # requires CSV data from get_pxc_customers
    pxc_crash_risk_factors()  # requires CSV data from pxc_crash_risk_assets
    pxc_similar_assets()  # requires CSV data from pxc_crash_risk_assets
    pxc_crash_in_last()  # requires CSV data from pxc_crash_risk_assets
    pxc_asset_crash_history()  # requires CSV data from pxc_crash_risk_assets

    # Send all CSV files in the output data folder to AWS S3 storage
    s3_storage()

    # Record time and cleanly exit or run next itteration
    print("******************************************************************")
    print("**************** Script Executed Successfully ********************")
    print("******************************************************************")
    stopTime = time.time()
    print('Stop Time:', datetime.now(), '\n\n')
    print("Total Time:", math.ceil(int(stopTime - startTime) / 60), "minutes")
    if x + 1 == testLoop:
        # Clean exit
        if outputFormat == 2:
            shutil.rmtree(csv_output_dir)
        exit()
    else:
        print("pausing for 5 secs")
        time.sleep(5)  # pause 5 sec between each itteration
