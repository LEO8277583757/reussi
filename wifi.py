import os

def create_hotspot(name, password):
    # Créez et configurez le fichier hostapd.conf
    with open('/etc/hostapd/hostapd.conf', 'w') as f:
        f.write(f'interface=wlan0\n'
                f'driver=nl80211\n'
                f'ssid={name}\n'
                f'hw_mode=g\n'
                f'channel=7\n'
                f'wmm_enabled=0\n'
                f'macaddr_acl=0\n'
                f'auth_algs=1\n'
                f'ignore_broadcast_ssid=0\n'
                f'wpa=2\n'
                f'wpa_passphrase={password}\n'
                f'wpa_key_mgmt=WPA-PSK\n'
                f'wpa_pairwise=TKIP\n'
                f'rsn_pairwise=CCMP')

    # Configurez dnsmasq
    with open('/etc/dnsmasq.conf', 'w') as f:
        f.write('interface=wlan0\n'
                'dhcp-range=192.168.1.2,192.168.1.30,255.255.255.0,12h')

    # Configurez la connexion Internet
    os.system("ifconfig wlan0 192.168.1.1")

    # Démarrez hostapd et dnsmasq
    os.system("service hostapd start")
    os.system("service dnsmasq start")

hotspot_name = 'MyHotspot'   # Insérez le nom de votre hotspot
hotspot_password = 'MyPassword'   # Insérez votre mot de passe

create_hotspot(hotspot_name, hotspot_password)