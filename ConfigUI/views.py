# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect

from ConfigUI import form_ConfigUI,DeceptionController,ProcessConfig,Canarycontroller


def ControlDeception(request):

	actionform = DeceptionController.ControlDeception()

	if request.method == "POST":
		print 'inside control'
		actionform = DeceptionController.ControlDeception(request.POST)
		print request.POST

	if actionform.is_valid():
		actionToSend = actionform.cleaned_data['controller']
		actionControl = Canarycontroller.ControlCanary(actionToSend)
		actionControl.SetAction()

	return render(request,'DeceptionController.html',{'form': actionform})

def index(request):

	form_UI = form_ConfigUI.ConfigUIForm()


	if request.method == "POST":
		form_UI = form_ConfigUI.ConfigUIForm(request.POST)
		print request.POST

		if form_UI.is_valid():

			ftpbanner = form_UI.cleaned_data['ftp_banner']
			ftpEnabled = form_UI.cleaned_data['ftp_enabled']
			ftpPort = form_UI.cleaned_data['ftp_port']

			httpbanner = form_UI.cleaned_data['http_banner']
			httpEnabled = form_UI.cleaned_data['http_enabled']
			httpPort = form_UI.cleaned_data['http_port']
			httpSkin = form_UI.cleaned_data['http_skin']

			mailserver = form_UI.cleaned_data['mailserver']
			mailport = form_UI.cleaned_data['mailserverPort']
			fromaddr = form_UI.cleaned_data['fromaddr']
			toaddr = form_UI.cleaned_data['toaddr']
			subject = form_UI.cleaned_data['subject']
			username = form_UI.cleaned_data['username']
			password = form_UI.cleaned_data['password']

			sshbanner = form_UI.cleaned_data['ssh_version']
			sshEnabled = form_UI.cleaned_data['ssh_enabled']
			sshPort = form_UI.cleaned_data['ssh_port']

			mysqlbanner = form_UI.cleaned_data['mysql_banner']
			mysqlEnabled = form_UI.cleaned_data['mysql_enabled']
			mysqlPort = form_UI.cleaned_data['mysql_port']

			telnetbanner = form_UI.cleaned_data['telnet_banner']
			telnetEnabled = form_UI.cleaned_data['telnet_enabled']
			telnetPort = form_UI.cleaned_data['telnet_port']


			rdpEnabled = form_UI.cleaned_data['rdp_enabled']
			sipEnabled = form_UI.cleaned_data['sip_enabled']
			snmpEnabled = form_UI.cleaned_data['snmp_enabled']
			mssqlEnabled = form_UI.cleaned_data['mssql_enabled']
			vncEnabled = form_UI.cleaned_data['vnc_enabled']

			'''print password
			print username
			print mailserver'''

			configUpdate = ProcessConfig.Config('test')			
			
			if ftpEnabled:
				configUpdate.readAndUpdateFTPConfig(ftpEnabled,ftpbanner,ftpPort)
			if httpEnabled:
				configUpdate.readAndUpdateHTTPConfig(httpEnabled,httpbanner,httpPort,httpSkin)
			if sshEnabled:
				configUpdate.readAndUpdateSSHConfig(sshEnabled,sshbanner,sshPort)
			if mysqlEnabled:
				configUpdate.readAndUpdateMySqlConfig(mysqlEnabled,mysqlbanner,mysqlPort)
			if telnetEnabled:
				configUpdate.readAndUpdateTelnetConfig(telnetEnabled,telnetbanner,telnetPort)


			print '----------------------------'
			print mailserver
			print mailport
			print fromaddr
			print toaddr
			print username
			print password
			print '----------------------------'
			configUpdate.readAndUpdateSMTPConfig(mailserver, mailport, fromaddr, toaddr, subject, username , password)

			configUpdate.readAndUpdateOtherServicesConfig(rdpEnabled ,sipEnabled, snmpEnabled,mssqlEnabled, vncEnabled)

			'''print 'render controller'
			actionform = DeceptionController.ControlDeception()

			render(request,'DeceptionController.html',{})'''
			return HttpResponseRedirect('cntd/')
			
		else:
			print 'Invalid form'

	return render(request,'configUI.html',{'form': form_UI})


		



# Create your views here.
