import TStat

import sys


taddr = '192.168.1.106'  # home
taddr = '173.19.242.234'  # home remote
port = 83
taddr = '192.168.254.24'  # cabin 1
taddr = '192.168.254.42'  # cabin 2
connect_attempts = 1


def Connect_Tstat(taddr, port=80):
    ' connect using Python-TStat API'
    print "establishing connection with 3m50 at %s port %d...\n" % (taddr, port)
    # tstat = TStat.TStat(taddr, api=API.API_CT30v192(), logger=None)
    tstat = TStat.TStat(taddr, port, logger=None)

    print "thermostat version info:"
    print "current model...%s" % tstat.getModel()
    print "current version...%s" % tstat.getVersion()
    print "current mode...%s" % tstat.getMode()
    print "current time...%s" % tstat.getTime()
    print "current wifi security...%s" % tstat.getSecurity()
    # print "current night light status...%s" % tstat.getNightLight()
    print "\n"
    print "current settings:"
    print "current temp...%s" % tstat.getCurrentTemp()
    print "current setpoint...%s" % tstat.getHeatPoint()
    print "current holdstate...%s" % tstat.getHoldState()
    print "current Power...%s" % tstat.getPower()
    # print "it_heat...%s" % tstat.it_heat
    print "current mode...%s" % tstat.getTstatMode()
    print "current temp state...%s\n" % tstat.getTState()

    print "yesterday heat usage...%s" % tstat.getHeatUsageYesterday()
    print "Today heat usage...%s\n" % tstat.getHeatUsageToday()

    print "fan mode...%s" % tstat.getFanMode()
    print "fan state...%s\n" % tstat.getFanState()

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
            TStat._set(param, valu)
            print "\nparam '%s' returns: %s" % (param, TStat._get(param))
        elif method == 'esc':
            print "\nescape sequence detected, exiting interactive mode..."
            sys.exit(0)


if __name__ == "__main__":
    # tstat1 = Connect_radiotherm(taddr)

    tstat1 = Connect_Tstat(taddr)
    interactive_TStat(tstat1)

    # Reboot(tstat1)