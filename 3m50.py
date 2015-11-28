import TStat

import sys


taddr = '192.168.1.106'  # home
taddr = '173.19.242.234'  # home remote
port = 80
taddr = '192.168.254.24'  # cabin basement
# taddr = '192.168.254.42'  # cabin main level

connect_attempts = 1


def Connect_Tstat(taddr, port=80):
    ' connect using Python-TStat API'
    print "establishing connection with 3m50 at %s port %d...\n" % (taddr, port)
    # tstat = TStat.TStat(taddr, api=API.API_CT30v192(), logger=None)
    tstat = TStat.TStat(taddr, port, logger=None)

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
    print "temporary heat setpoint...%s" % tstat.getIT_heat()
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