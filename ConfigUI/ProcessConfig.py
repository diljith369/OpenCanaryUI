import json
import sys
class Config():

	def __init__(self,name):
		self.name = name

		

	def readAndUpdateFTPConfig(self,ftpEnable ,ftpBanner, ftpPort):

		try:
			config_data = ""
			with open("/root/.opencanary.conf") as data:
				config_data = json.load(data)
			#print json_data

			'''print config_data['ftp.banner']
			print config_data['ftp.enabled']
			print config_data['ftp.port']'''

			#print config_data['logger']['kwargs']['handlers']['syslog-unix']['address'][0]

			config_data['ftp.banner'] = ftpBanner
			config_data['ftp.enabled'] = ftpEnable
			config_data['ftp.port']   = ftpPort

			#config_data['logger']['kwargs']['handlers']['syslog-unix']['address'][1] =  555

			with open("/root/.opencanary.conf", "w") as configFile:
				json.dump(config_data,configFile, indent=4)

		except:
			pass


	def readAndUpdateMySqlConfig(self,mySQLEnable ,mySQLBanner, mySQLPort):

		try:
			config_data = ""
			with open("/root/.opencanary.conf") as data:
				config_data = json.load(data)
			
			config_data['mysql.banner'] = mySQLBanner
			config_data['mysql.enabled'] = mySQLEnable
			config_data['mysql.port']   = mySQLPort


			with open("/root/.opencanary.conf", "w") as configFile:
				json.dump(config_data,configFile, indent=4)

		except:
			pass

	def readAndUpdateSSHConfig(self,sshenable ,sshBanner, sshPort):

		try:
			config_data = ""
			with open("/root/.opencanary.conf") as data:
				config_data = json.load(data)
			
			config_data['ssh.banner'] = sshBanner
			config_data['ssh.enabled'] = sshenable
			config_data['ssh.port']   = sshPort


			with open("/root/.opencanary.conf", "w") as configFile:
				json.dump(config_data,configFile, indent=4)

		except:
			pass


	def readAndUpdateTelnetConfig(self,telnetenable ,telnetBanner, telnetPort):

		try:
			config_data = ""
			with open("/root/.opencanary.conf") as data:
				config_data = json.load(data)
			
			config_data['telnet.banner'] = telnetBanner
			config_data['telnet.enabled'] = telnetenable
			config_data['telnet.port']   = telnetPort


			with open("/root/.opencanary.conf", "w") as configFile:
				json.dump(config_data,configFile, indent=4)

		except:
			pass


	def readAndUpdateOtherServicesConfig(self,RDPenable ,SIPenable, SNMPenable,MSSQLenable, VNCenable):

		try:
			config_data = ""
			with open("/root/.opencanary.conf") as data:
				config_data = json.load(data)
			
			config_data['mssql.enabled'] = MSSQLenable
			config_data['vnc.enabled'] = VNCenable
			config_data['sip.enabled']   = SIPenable
			config_data['snmp.enabled'] = SNMPenable
			config_data['rdp.enabled']   = RDPenable


			with open("/root/.opencanary.conf", "w") as configFile:
				json.dump(config_data,configFile, indent=4)

		except:
			pass







	def readAndUpdateSMTPConfig(self,mailserver, port, fromaddr, toaddr, subject, username , password):

		try:

			print 'inside smtp'

			try:
				with open("/root/.opencanary.conf") as data:
					config_data = json.load(data)
					print config_data
			except:
				print 'json error',sys.exc_info()[0]



			print '---------mail host -----------'
			mailhost =  config_data['logger']['kwargs']['handlers']['SMTP']['mailhost']
			
			serverdetails = [mailserver,port]

			del mailhost[:]
			for val in serverdetails:
				mailhost.append(val)
			
			print mailhost

			print '---------From Address -----------'

			config_data['logger']['kwargs']['handlers']['SMTP']['fromaddr'] = fromaddr

			print config_data['logger']['kwargs']['handlers']['SMTP']['fromaddr']


			print '---------to address -----------'

			toaddressDetails = config_data['logger']['kwargs']['handlers']['SMTP']['toaddrs']
			toaddressVals = [toaddr]

			del toaddressDetails[:]
			for val in toaddressVals:
				toaddressDetails.append(val)
				print val

			print toaddressDetails

			config_data['logger']['kwargs']['handlers']['SMTP']['subject'] = subject


			credentials =  config_data['logger']['kwargs']['handlers']['SMTP']['credentials']
			
			credentialsDetails = [username,password]

			del credentials[:]
			for val in credentialsDetails:
				credentials.append(val)


			print credentials

			print 'after'
			print config_data['logger']['kwargs']['handlers']['SMTP']['mailhost'][0]
			print config_data['logger']['kwargs']['handlers']['SMTP']['mailhost'][1]
			print config_data['logger']['kwargs']['handlers']['SMTP']['fromaddr']
			print config_data['logger']['kwargs']['handlers']['SMTP']['toaddrs']
			print config_data['logger']['kwargs']['handlers']['SMTP']['subject']
			print config_data['logger']['kwargs']['handlers']['SMTP']['credentials'][0]
			print config_data['logger']['kwargs']['handlers']['SMTP']['credentials'][1]


			with open("/root/.opencanary.conf", "w") as configFile:
				json.dump(config_data,configFile,indent=4)



		except:
			print 'exception ' ,sys.exc_info()[0]


	def readAndUpdateHTTPConfig(self,httpEnable ,httpBanner, httpPort,httpSkin):

		try:
			config_data = ""
			with open("/root/.opencanary.conf") as data:
				config_data = json.load(data)
			#print json_data

			'''print config_data['http.banner']
			print config_data['http.enabled']
			print config_data['http.port']
			print config_data['http.skin']'''

			#print config_data['logger']['kwargs']['handlers']['syslog-unix']['address'][0]

			config_data['http.banner'] = httpBanner
			config_data['http.enabled'] = httpEnable
			config_data['http.port']   = httpPort
			config_data['http.skin'] = httpSkin

			#config_data['logger']['kwargs']['handlers']['syslog-unix']['address'][1] =  555

			with open("/root/.opencanary.conf", "w") as configFile:
				json.dump(config_data, configFile, indent=4)

		except:
			pass