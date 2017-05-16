#!/usr/bin/python
# -*- coding: utf-8 -*-

# import http.client

import httplib
import urllib

import json
import yaml
import pprint

import os
################### ################### ################### 
#print ()
################### 
path = os.path.dirname(os.path.abspath(__file__))
with open(path + '/config.yml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

cred = cfg['credentials']
client_id = cred['client_id']
client_secret = cred['client_secret']
username = cred['username']
password = cred['password']
host = cred['host']
base_url = cred['base_url']
wave_base_url = cred['wave_base_url']
login_url = cred['login_url']
grant_service = cred['grant_service']
base_soql_url = cred['base_soql_url']
apex_rest = cred['apex_rest']
apex_limits = cred['apex_limits']

# removed urllib.parse.urlencode "parse"

params = urllib.urlencode({
    'grant_type': 'password',
    'client_id': client_id,
    'client_secret': client_secret,
    'username': username,
    'password': password,
    'response_type': 'code',
    })

headers = {'Content-type': 'application/x-www-form-urlencoded',
           'Accept': 'text/json'}


def get_connection():
    conn = httplib.HTTPSConnection(host)
    return conn


def get_login_connection():
    conn = httplib.HTTPSConnection('login.salesforce.com')
    return conn


def get_access_token():
    conn = get_login_connection()
    conn.request('POST', '/services/oauth2/token', params, headers)
    response = conn.getresponse()
    data = response.read().decode('ascii')

    # print data session_id

    data_json = json.loads(data)
    if 'error' in data_json:
        print 'Error: ' + str(data_json)
        exit()
    return data_json


def create_sobject(object_name, data):
    access_token = get_access_token()['access_token']
    access_token_header = {'Authorization': 'Bearer ' + access_token,
                           'Content-type': 'application/json'}

    url = base_url + object_name
    json_data = json.dumps(data)

    conn = get_connection()
    conn.request('POST', url, json_data, access_token_header)
    res = conn.getresponse()
    data = res.read().decode('utf-8')
    return data


def patch_sobject(object_name, id, data):
    access_token = get_access_token()['access_token']
    access_token_header = {'Authorization': 'Bearer ' + access_token,
                           'Content-type': 'application/json'}

    url = base_url + object_name + '/' + id
    json_data = json.dumps(data)
    conn = get_connection()
    conn.request('PATCH', url, json_data, access_token_header)
    res = conn.getresponse()
    data = res.read().decode('utf-8')
    return data


def delete_sobject(object_name, object_id):
    access_token = get_access_token()['access_token']
    access_token_header = {'Authorization': 'Bearer ' + access_token,
                           'Content-type': 'application/json'}
    url = base_url + object_name + '/' + object_id
    conn = get_connection()
    conn.request('DELETE', url, '', access_token_header)
    res = conn.getresponse()
    data = res.read().decode('utf-8')
    print data


def get_sobject_list(object_name):
    access_token = get_access_token()['access_token']
    access_token_header = {'Authorization': 'Bearer ' + access_token,
                           'Content-type': 'application/json'}
    url = base_url + object_name
    conn = get_connection()
    conn.request('GET', url, '', access_token_header)
    res = conn.getresponse()
    data = res.read().decode('utf-8')
    return data


def get_sobject_list_wave(local_base_url, object_name):
    access_token = get_access_token()['access_token']
    access_token_header = {'Authorization': 'Bearer ' + access_token,
                           'Content-type': 'application/json'}
    url = local_base_url + object_name
    conn = get_connection()
    conn.request('GET', url, '', access_token_header)
    res = conn.getresponse()
    data = res.read().decode('utf-8')
    return data


def execute_soql(soql):
    access_token = get_access_token()['access_token']

    access_token_header = {'Authorization': 'Bearer ' + access_token,
                           'Content-type': 'application/json'}

    url = base_soql_url + soql

    # print url;

    conn = get_connection()
    conn.request('GET', url, '', access_token_header)
    res = conn.getresponse()
    data = res.read().decode('utf-8')
    return data


#####################################Apex Rest Get################################################################

def apexrest(soql):
    access_token = get_access_token()['access_token']

    access_token_header = {'Authorization': 'Bearer ' + access_token,
                           'Content-type': 'application/json'}

    url = apex_rest + soql

    # print url;

    conn = get_connection()
    conn.request('GET', url, '', access_token_header)
    res = conn.getresponse()
    data = res.read().decode('utf-8')
    return data


    # ####################################Apex Rest Get################################################################

#####################################Apex Rest Api Post################################################################

def apexrest_post(object_name, data):
    access_token = get_access_token()['access_token']
    # print access_token
    access_token_header = {'Authorization': 'Bearer ' + access_token,
                           'Content-type': 'application/json'}
    url = apex_rest + object_name
     # ####json_data = json.dumps(data).decode('unicode-escape')################Working Code##################33
    # data=repr(data)
    json_data = data
    conn = get_connection()
    conn.request('POST', url, json_data, access_token_header)
    res = conn.getresponse()
    data = res.read().decode('utf-8')
    return data


#####################################Apex Rest Api Post################################################################

#####################################Apex Rest Api patch################################################################
# def apexrest_patch(object_name, id, data):
# removed id

def apexrest_patch(object_name, data):
    access_token = get_access_token()['access_token']
    access_token_header = {'Authorization': 'Bearer ' + access_token,
                           'Content-type': 'application/json'}

    # url = apex_rest + object_name + "/" + id

    url = apex_rest + object_name
    json_data = json.dumps(data)
    conn = get_connection()
    conn.request('PATCH', url, json_data, access_token_header)
    res = conn.getresponse()
    data = res.read().decode('utf-8')
    return data


    # ####################################Apex Rest Api Patch################################################################
 # ####################################Apex Rest Api Delete################################################################

def apexrest_delete(object_name, object_id):
    access_token = get_access_token()['access_token']
    access_token_header = {'Authorization': 'Bearer ' + access_token,
                           'Content-type': 'application/json'}
    url = apex_rest + object_name + '/' + object_id
    conn = get_connection()
    conn.request('DELETE', url, '', access_token_header)
    res = conn.getresponse()
    data = res.read().decode('utf-8')
    print data


 # ####################################Apex Rest Api Delete################################################################

def apexlimit():
    access_token = get_access_token()['access_token']

    access_token_header = {'Authorization': 'Bearer ' + access_token,
                           'Content-type': 'application/json'}

    url = apex_limits

    # print url;

    conn = get_connection()
    conn.request('GET', url, '', access_token_header)
    res = conn.getresponse()
    data = res.read().decode('utf-8')
    return data






			
