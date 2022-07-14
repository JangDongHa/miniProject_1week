import requests
from flask import request

from model import areaXYDao
from model.ipDto import ipDTO


def get_realIP(addr):
    url = 'https://api.ipify.org?format=json{}'.format(addr)
    r = requests.get(url)
    return r.text


def request_ip():
    ip = get_realIP(request.remote_addr)
    url = 'http://ip-api.com/json/{}'.format(
        ip)  # https://geo.ipify.org/api/v2/country?apiKey=at_FdSmA4fv6gyfMetoA3YOCtPPpuc1f&ipAddress={}
    r = requests.get(url)
    return r


def get_address_from_ip():
    r = request_ip()
    ip_data_type_json = r.json()

    ipdto = ipDTO(ip_data_type_json)

    lat, lon = ipdto.get_lat_lon()
