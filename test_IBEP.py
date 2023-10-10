import meraki
import os

# from test import add

# print(add(5, 4))
# exit()


# API Key Meraki dans variables d'environnement
key = os.environ.get('API_KEY_SL')
dashboard = meraki.DashboardAPI(key, suppress_logging=True)

# OrgId IBEP (récupérée en bas de page du dashboard)
orgId = "713638"


# Networks de Lorient
networks = dashboard.organizations.getOrganizationNetworks(orgId, total_pages='all')
for network in networks:
    if network['name'] == "IBEP Lorient":
        print(network)
    
    
    # # Devices de Lorient
    # devices = dashboard.networks.getNetworkDevices(network['id'])
    
    # # MR (bornes wifi) dans les devices de Lorient
    # print("Bornes wifi à Lorient :")
    # for device in devices:
    #     if 'MR' in device['model']:
    #         print(device['name'])
            
    # # MS = switch
    # print("Switch à Lorient :")
    # for device in devices:
    #     if 'MS' in device['model']:
    #         print(device['name'])
            
    # # MV = caméra
    # cameras_found = False

    # print("Caméras à Lorient :")
    # for device in devices:
    #     if 'MV' in device['model']:
    #         print(device['name'])
    #         cameras_found = True

    # if not cameras_found:
    #     print('Pas de caméra')
        
    # # MT = sensor
    # sensors_found = False
    # print("Capteurs à Lorient :")
    # for device in devices:
    #     if 'MT' in device['model']:
    #         print(device['name'])
    #         sensors_found = True

    # if not sensors_found:
    #     print('Pas de capteurs')
        

# # Récupérer les clients actuels du réseau
# clients = dashboard.networks.getNetworkClients(network['id'])
# if clients:
#     for client in clients:
#         print(client)
# else:
#         print('Aucun client actuel dans le réseau.')


print('##################################################################')
print('identifier les périphériques qui subissent des déconnexions fréquentes :')

# # identifier les périphériques qui subissent des déconnexions fréquentes
# # en filtrant ces événements en fonction des périphériques et des ports concernés.

# # Récupérer les journaux d'événements pour les déconnexions
# events_response = dashboard.networks.getNetworkEvents(network['id'], eventTypes=['client disconnect'])

# # Extraire la liste des événements
# events = events_response.get('events', [])

# # Filtrer les événements liés aux changements de statut des ports
# port_events = [event for event in events if event.get('type') in ['stp_port_role_change', 'port_status']]

# # Afficher les événements liés aux changements de statut des ports
# if port_events:
#     for event in port_events:
#         print(event)
# else:
#     print('Aucun événement de changement de statut de port trouvé.')
    

print('##################################################################')

# network Lorient
networkId = 'L_714946440845070894'
connectionStats = dashboard.wireless.getNetworkWirelessConnectionStats(networkId, timespan = 86400)

# print(connectionStats)
# donne {'assoc': 18, 'auth': 34, 'dhcp': 1, 'dns': 0, 'success': 1870}


print('##################################################################')

# getNetworkClient Return the client associated with the given identifier. Clients can be identified 
# by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

# client choisi parmi ceux qui se font déconnecter
# Accueil-HP	10.16.9.203	native	38:94:ed:bd:2e:31   225.8MB 38 minutes	IBEP DG	44

client_id = "38:94:ed:bd:2e:31"

networkClient = dashboard.networks.getNetworkClient(
    networkId, client_id
)

# print(networkClient)
# renvoie :
# {'id': 'k9d6128', 
# 'mac': '38:94:ed:bd:2e:31', 
# 'ip': '10.16.9.203', 
# 'ip6': '', 
# 'description': 'Accueil-HP', 
# 'firstSeen': 1636033202, 
# 'lastSeen': 1696507841, 
# 'manufacturer': 'Netgear', 
# 'os': 'Windows 10', 
# 'user': None, 
# 'vlan': '30', 
# 'ssid': 'IBEP DG', 
# 'wirelessCapabilities': 
# '802.11ac - 2.4 and 5 GHz', 
# 'smInstalled': False, 
# 'recentDeviceMac': 'f8:9e:28:da:82:6e', 
# 'clientVpnConnections': None, 
# 'lldp': None, 
# 'cdp': None, 
# 'status': 'Online'}


# # Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.
# infoClient = dashboard.wireless.getNetworkWirelessClientConnectionStats(
#     networkId, client_id, timespan = 86400
# )
# # print (infoClient)
# # {'mac': '38:94:ed:bd:2e:31', 'connectionStats': {'assoc': 0, 'auth': 0, 'dhcp': 0, 'dns': 0, 'success': 3}}


# # Filtrer les événements pour ne prendre en compte que les déconnexions
# disconnect_events = [
#     event for event in infoClient['connectionStats'] if event['associationEvent'] == 'Disassociation'
# ]

# # Afficher le nombre de déconnexions
# print(f"Le client a subi {len(disconnect_events)} déconnexions au cours des dernières 24 heures.")



# Récupérer les événements de connectivité pour le client au cours des dernières 24 heures
client_events = dashboard.wireless.getNetworkWirelessClientConnectionStats(
    networkId, '38:94:ed:bd:2e:31', timespan=86400
)
print(client_events)
# {'mac': '38:94:ed:bd:2e:31', 'connectionStats': {'assoc': 0, 'auth': 0, 'dhcp': 0, 'dns': 0, 'success': 2}}


# Filtrer les événements pour ne prendre en compte que les déconnexions
disconnect_events = [
    event for event in client_events.get('connectionStats', []) 
    if event.get('associationEvent') == 'Disassociation'
]

# Afficher le nombre de déconnexions
print(f"Le client a subi {len(disconnect_events)} déconnexions au cours des dernières 24 heures.")



