import radiotherm

import TStat
import API

import time

taddr = '192.168.1.106'  # home
taddr = '192.168.254.24'  # cabin 1
taddr = '192.168.254.42'  # cabin 2
connect_attempts = 1


def Connect_radiotherm(taddr):
    # tstat = radiotherm.get_thermostat('192.168.0.2')
    print "establishing connection with 3m50 at %s...\n" % taddr
    tstat = radiotherm.get_thermostat(taddr)
    print "current model...%s" % tstat.model
    print "current version...%s" % tstat.version
    print "current time...%s\n" % tstat.time

    print "current temp...%s" % tstat.temp
    print "current setpoint...%s" % tstat.t_heat
    print "it_heat...%s" % tstat.it_heat
    print "current mode...%s" % tstat.tmode
    print "current temp state...%s\n" % tstat.tstate

    print "fan mode...%s" % tstat.fmode
    print "fan state...%s" % tstat.fstate
    return tstat


def Reboot_radiotherm(tstat, dly=30):
    print "rebooting thermostat, wait %d seconds..." % dly
    tstat.reboot()
    time.sleep(dly)
    print "reboot done"


def Connect_Tstat(taddr):
    ' connect using Python-TStat API'
    print "establishing connection with 3m50 at %s...\n" % taddr
    # tstat = TStat.TStat(taddr, api=API.API_CT30v192(), logger=None)
    tstat = TStat.TStat(taddr, logger=None)

    print "current model...%s" % tstat.getModel()
    print "current version...%s" % tstat.getVersion()
    print "current mode...%s" % tstat.getMode()
    print "current time...%s" % tstat.getTime()
    print "current wifi security...%s" % tstat.getSecurity()
    # print "current night light status...%s" % tstat.getNightLight()
    print "\n"

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


if __name__ == "__main__":
    # tstat1 = Connect_radiotherm(taddr)

    tstat1 = Connect_Tstat(taddr)

    # Reboot(tstat1)