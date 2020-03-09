

# -*- coding: utf-8 -*-
# Criado por: Diego Fernandes Rodrigues em 20181007
# Implementacao da busca por palavras chave no LinkedIn, Indeed e Vagas.com.br
# Atualizado por:
# Geting information from web page

# Importing the lib webbrowser
import webbrowser
import time
import requests

# List of key words for search
# ['FEA', 'NVH', 'MEF', 'FEM', 'CFD', 'ANSYS', 'CFX', 'simulacao',
# 'fluidos', 'fluid', 'nastran', 'abaqus', 'Star-CCM', 'FEMAP', 'simulink',
# 'ncode', 'fadiga', 'calculista', 'elementos%20finitos', 'moldflow', 'HVAC',
# 'hypermesh', 'AVL', 'sap2000', 'CAE', 'PSD', 'modelica', 'dymola', 'ls-dyna']

""" 
search_keys = list(keyword, language) #lang> 0 = N/A, 1 EN, 2 PT, 3 DE
Here you can set your keywords (based on your skills) and its language
"""
search_keys = [
    ('FEA', 0),
    ('MEF', 2),
    ('Elementos Finitos', 2),
    ('FEM', 0),
    ('ANSYS', 0),
    ('Junior Softwareentwickler', 3),
    ('Junior Berechnungsingenieur', 3),
    ('Finite Element Method', 1),
    ('simulacao', 2),
    ('simulation', 0),
    ('CAE', 0),
    ('Finite Element Analysis', 1),
]

""" HERE YOU CAN SETUP YOUR SEARCH """
desired_domain = '.com.br'  # .com, .com.br, .de, .us (this will filter the region)
derided_languages = [0, 1, 2]  # 0 = NA, 1 EN, 2 PT, 3 DE


# Dictionary: domain: LinkedIn Location
location = {
    '.com': 'WorldWide',
    '.com.br': 'Brazil',
    '.de': 'Germany',
}

# setting domain
websites = ['https://www.linkedin.com/jobs/search/?sortBy=DD&location=' + location[desired_domain] + '&keywords=',
            'https://www.indeed'+desired_domain+'/jobs?sort=date&q=']
if desired_domain == '.com.br':
    websites.append('https://www.vagas.com.br/vagas-de-')

# creating search links
links = [website + key[0]
         for website in websites for key in search_keys if key[1] in derided_languages]

# filtering empty results
found = [link for link in links if requests.get(
    link, timeout=2.0).status_code == 200]

# opening links
for link in found:
    webbrowser.open_new_tab(link)

# Other links
if desired_domain == '.com.br':
    webbrowser.open_new_tab('https://semcon.com/join-us/jobs/')

    webbrowser.open_new_tab('http://www.soditech.com.br/jobs.php')

    webbrowser.open_new_tab(
        'https://curriculos.esss.co/RM/Rhu-BancoTalentos/#/RM/Rhu-BancoTalentos/painelVagas/lista')
