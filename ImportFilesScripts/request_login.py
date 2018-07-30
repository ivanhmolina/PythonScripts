"""A"""
import requests

with requests.Session() as c:
    URL = 'https://fs.itesm.mx/adfs/ls/?wa=wsignin1.0&wtrealm=urn\
    %3asharepoint%3amitec&wctx=https%3a%2f%2fmitec.itesm.mx\
    %2f_layouts%2f15%2fAuthenticate.aspx%3fSource%3d%252F'
    USERNAME = ''
    PASSWORD = ''
    c.get(URL)
    LOGIN_DATA = dict(UsernameTextBox=USERNAME, PasswordTextBox=PASSWORD)
    c.post(URL, data=LOGIN_DATA, headers={"Referer":"https://mitec.itesm.mx/"})
    PAGE = c.get('https://mitec.itesm.mx/')
    print(PAGE.content)
