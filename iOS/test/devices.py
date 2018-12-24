@staticmethod
def get_ios_devices():
    devices = []
    output = Shell.invoke('idevice_id -l')
    config_file = os.path.join(os.path.dirname(__file__), 'ios_mapping.json')
    with open(config_file, 'r') as f:
        config = json.loads(f.read())

    if len(output) > 0:
        udids = output.strip('\n').split('\t')
        for udid in udids:
            dic = {"os_type": 'iOS', "uid": udid}
            output = Shell.invoke('ideviceinfo -u %s -k ProductType' % udid)
            device_type = config[output.strip('\n')]
            brand = ''
            # -1表示找不到 0表示下标
            if device_type.find("iPhone") != -1:
                brand = 'iPhone'
            elif device_type.find("iPad") != -1:
                brand = 'iPad'
            elif device_type.find("iPod") != -1:
                brand = 'iPod'

            dic['brand'] = brand
            dic['model'] = device_type

            output = Shell.invoke('ideviceinfo -u %s -k ProductVersion' % udid)
            dic['os_type'] = 'iOS'
            dic['os_version'] = output.strip('\n')
            dic['rom_version'] = output.strip('\n')

            output = Shell.invoke('idevicename -u %s' % udid)
            dic['device_name'] = output.strip('\n')
            devices.append(dic)
    return devices