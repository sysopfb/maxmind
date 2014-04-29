import sys
import pygeoip

def get_data(ip):
        #arg1 = sys.argv[1]
	gip = pygeoip.GeoIP('GeoLiteCity.dat')
	rec = gip.record_by_name(ip)
	for key,val in rec.items():
		print "%s: %s" % (key,val)

