import discover as disc          # discover module from radiotherm project
import TStat             # TStat class from Python-TStat project

import sys

taddr = []

port = 80


connect_attempts = 1
tstat_dict = {}


def PopulateDict(tdict, key, value=None):
    ''' function populates a dictionary
    '''
    # initialize key
    if key not in tdict.keys():
        tdict.setdefault(key, [])
    # add value as list member to dict
    tdict[key].append(value)


def Connect_Tstat(taddr, port=80):
    ' connect using Python-TStat API'
    taddr = disc.discover_address()
    print "thermostat auto discovery at %s" % taddr
    for x in taddr:
        print "establishing connection with 3m50 at %s port %d...\n" % (x, port)
        # tstat = TStat.TStat(taddr, api=API.API_CT30v192(), logger=None)
        tstat = TStat.TStat(x, port, logger=None)

        print "downloading thermstat data..."
        PopulateDict(tstat_dict, "version", tstat.getVersion())
        PopulateDict(tstat_dict, "temp", tstat.getCurrentTemp())
        PopulateDict(tstat_dict, "tmode", tstat.getTstatMode())
        PopulateDict(tstat_dict, "fmode", tstat.getFanMode())
        PopulateDict(tstat_dict, "override", tstat.getOverride())
        PopulateDict(tstat_dict, "hold", tstat.getHoldState())
        PopulateDict(tstat_dict, "t_heat", tstat.getHeatPoint())
        PopulateDict(tstat_dict, "t_cool", tstat.getCoolPoint())
        PopulateDict(tstat_dict, "it_heat", tstat.getTempHeatSetPoint())
        PopulateDict(tstat_dict, "it_cool", tstat.getTempCoolSetPoint())
        PopulateDict(tstat_dict, "a_heat", "not implemented")
        PopulateDict(tstat_dict, "a_cool", "not implemented")
        PopulateDict(tstat_dict, "a_mode", "not implemented")
        PopulateDict(tstat_dict, "t_type_post", "not implemented")
        PopulateDict(tstat_dict, "tstate", tstat.getTState())
        PopulateDict(tstat_dict, "fstate", tstat.getFanState())
        PopulateDict(tstat_dict, "time", tstat.getTime())
        PopulateDict(tstat_dict, "day", "not implemented")
        PopulateDict(tstat_dict, "hour", "not implemented")
        PopulateDict(tstat_dict, "minute", "not implemented")
        PopulateDict(tstat_dict, "program_mode", tstat.getProgramMode())
        PopulateDict(tstat_dict, "ttarget", "not implemented")
        PopulateDict(tstat_dict, "model", tstat.getModel())
        PopulateDict(tstat_dict, "energy_led", "post-only method")
        PopulateDict(tstat_dict, "rem_mode", "not implemented")
        PopulateDict(tstat_dict, "rem_temp", "not implemented")
        PopulateDict(tstat_dict, "lock_mode", "not implemented")
        PopulateDict(tstat_dict, "simple_mode", "not implemented")
        PopulateDict(tstat_dict, "mode", "not implemented")
        PopulateDict(tstat_dict, "type", "not implemented")
        PopulateDict(tstat_dict, "Delta", "not implemented")
        PopulateDict(tstat_dict, "tswing", "not implemented")
        PopulateDict(tstat_dict, "night_light", "not implemented")
        PopulateDict(tstat_dict, "format", "not implemented")
        PopulateDict(tstat_dict, "baffle_mode", "not implemented")
        PopulateDict(tstat_dict, "uuid", tstat.getUuid())
        PopulateDict(tstat_dict, "api_version", tstat.getAPIVersion())
        PopulateDict(tstat_dict, "fw_version", tstat.getFwVersion())
        PopulateDict(tstat_dict, "wlan_fw_version", tstat.getWlanFwVersion())
        PopulateDict(tstat_dict, "services_names", "not implemented")
        PopulateDict(tstat_dict, "http_handlers", "not implemented")
        PopulateDict(tstat_dict, "ui", "not implemented")
        PopulateDict(tstat_dict, "ai", "not implemented")
        PopulateDict(tstat_dict, "bi", "not implemented")
        PopulateDict(tstat_dict, "name", tstat.getName())
        PopulateDict(tstat_dict, "command", "not implemented")
        PopulateDict(tstat_dict, "mode", tstat.getMode())
        PopulateDict(tstat_dict, "network", "not implemented")
        PopulateDict(tstat_dict, "ssid", tstat.getSsid())
        PopulateDict(tstat_dict, "bssid", tstat.getBssid())
        PopulateDict(tstat_dict, "channel", tstat.getChannel())
        PopulateDict(tstat_dict, "security", tstat.getSecurity())
        PopulateDict(tstat_dict, "ip", tstat.getIP())
        PopulateDict(tstat_dict, "ipaddr", "not implemented")
        PopulateDict(tstat_dict, "ipmask", "not implemented")
        PopulateDict(tstat_dict, "ipgw", "not implemented")
        PopulateDict(tstat_dict, "ipdns1", "not implemented")
        PopulateDict(tstat_dict, "ipdns2", "not implemented")
        PopulateDict(tstat_dict, "rssi", tstat.getRssi())
        # undocumented parameters
        PopulateDict(tstat_dict, "tstat", "not implemented")
        PopulateDict(tstat_dict, "today_heat_runtime", "not implemented")
        PopulateDict(tstat_dict, "today_cool_runtime", "not implemented")
        PopulateDict(tstat_dict, "yesterday_heat_runtime", "not implemented")
        PopulateDict(tstat_dict, "yesterday_cool_runtime", "not implemented")
        PopulateDict(tstat_dict, "errstatus", tstat.isOK())
        PopulateDict(tstat_dict, "power", "not implemented")
        PopulateDict(tstat_dict, "cloud_mode", "not implemented")

        print "thermostat version info:"
        print "current name...%s" % tstat.getName()
        print "current model...%s" % tstat.getModel()
        print "current thermostat api version...%s" % tstat.getVersion()
        print "current UUID...%s" % tstat.getUuid()
        print "current system api version...%s" % tstat.getAPIVersion()
        print "current fw version...%s" % tstat.getFwVersion()
        print "current wlan fw version...%s" % tstat.getWlanFwVersion()
        print "current mode...%s" % tstat.getMode()
        print "current time...%s" % tstat.getTime()
        #  print "current lock mode...%s" % tstat.getLockMode()  returns -1

        print "\nNetwork info:"
        # print "current wifi network...%s" % tstat.getNetwork()
        print "current wifi ssid...%s" % tstat.getSsid()
        print "current wifi bssid...%s" % tstat.getBssid()
        print "current wifi ip...%s" % tstat.getIP()
        print "current wifi rssi...%s dB" % tstat.getRssi()
        print "current wifi security...%s" % tstat.getSecurity()
        print "current wifi channel...%s" % tstat.getChannel()
        # print "current night light status...%s" % tstat.getNightLight()  # hangs on this command
        print "\n"
        print "current settings:"
        print "current temp...%s deg F" % tstat.getCurrentTemp()
        print "current setpoint...%s" % tstat.getHeatPoint()
        print "current override...%s" % tstat.getOverride()
        print "current holdstate...%s" % tstat.getHoldState()
        print "current Power...%s" % tstat.getPower()
        # print "t_heat...%s" % tstat.getT_heat()
        print "temporary heat setpoint...%s" % tstat.getTempHeatSetPoint()
        print "current mode...%s" % tstat.getTstatMode()
        print "current temp state...%s" % tstat.getTState()

        print "fan mode...%s" % tstat.getFanMode()
        print "fan state...%s\n" % tstat.getFanState()

        print "\nRecent usage:"
        print "yesterday heat usage...%s" % tstat.getHeatUsageYesterday()
        print "Today heat usage...%s\n" % tstat.getHeatUsageToday()

        print "Thermostat Status:"
        print "Thermostat is OK?...%s" % tstat.isOK()
        print "Thermostat Error...%s" % tstat.getErrStatus()

    print "thermostat data dump..."
    print tstat_dict
    return tstat


def interactive_TStat(TStat):
    ''' function provides interactive dialog
    '''
    # methods supported
    # keys = ['set', 'get', 'esc']

    key_dict = []
    while True:
        key_input = raw_input("\n\ninteractive mode, enter method and parameter ('esc' to exit): ")
        key_input.strip('\t\n\r')
        if ' ' in key_input:
            key_dict = key_input.split(' ')
        else:
            key_dict.append(key_input)
        if len(key_dict) >= 1:
            method = key_dict[0]
        if len(key_dict) >= 2:
            param = key_dict[1]
        if len(key_dict) >= 3:
            valu = key_dict[2]

        if method == 'get':
            if len(key_dict) != 2:
                print "\nparse error in string '%s', 'get' method requires 1 parameter, exiting..." % key_input
                sys.exit(-1)
            print "\nparam '%s' returns: %s" % (param, TStat._get(param))
        if method == 'set':
            if len(key_dict) != 3:
                print "\nparse error in string '%s', 'set' method requires 2 parameters, exiting..." % key_input
                sys.exit(-1)
            print "\nparam '%s' was set to: %s, changing to: %s" % (param, TStat._get(param), valu)
            TStat._post(param, valu)
            print "\nparam '%s' returns: %s" % (param, TStat._get(param))
        elif method == 'esc':
            print "\nescape sequence detected, exiting interactive mode..."
            sys.exit(0)


if __name__ == "__main__":
    # tstat1 = Connect_radiotherm(taddr)

    tstat1 = Connect_Tstat(taddr, port)
    interactive_TStat(tstat1)

    # Reboot(tstat1)
