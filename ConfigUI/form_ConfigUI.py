from django import forms

class ConfigUIForm(forms.Form):

	HTTP_SKINS = (('nasLogin','NasLogin'),('basicLogin','BasicLogin'))

	ftp_banner = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','size': '25'}),label ="Banner",required=False,initial = "FTP server ready")
	ftp_enabled = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),label = "Enable",required =False)
	ftp_port = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),label="Port",required =True,initial=21)

	http_banner = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','size': '25'}),label ="Banner",required=False, initial="Apache/2.2.22 (Ubuntu)")
	http_enabled = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),label = "Enable",required =False)
	http_port = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),label="Port",required =True,initial=80)
	http_skin = forms.ChoiceField(widget=forms.Select(attrs={'name': 'httpSkins'}),label="Skins",required =True,choices=HTTP_SKINS)

	mailserver = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','size': '50'}),label ="Mail Server",required=False)
	mailserverPort = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),label="Port",required =True,initial=587)
	fromaddr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','size': '50'}),label ="From Address",required=False)
	toaddr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','size': '50'}),label ="To Address",required=False)
	subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','size': '50'}),label ="Subject",required=False)
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','size': '50'}),label ="USer name",required=False)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','size': '50'}),label ="Password",required=False)
	#smtp_enabled = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),label = "Enable",required =False)


	mysql_banner = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','size': '25'}),label ="Banner",required=False,initial="5.5.43-0ubuntu0.14.04.1")
	mysql_enabled = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),label = "Enable",required =False)
	mysql_port = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),label="Port",required =True,initial=3306)

	ssh_version = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','size': '25'}),label ="Banner",required=False,initial = "SSH-2.0-OpenSSH_5.1p1 Debian-4")
	ssh_enabled = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),label = "Enable",required =False)
	ssh_port = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),label="Port",required =True,initial=8022)

	rdp_enabled = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),label = "RDP",required =False)
	sip_enabled = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),label = "SIP",required =False)
	snmp_enabled = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),label = "SNMP",required =False)
	#tftp_enabled = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),label = "TFTP Enable",required =False)
	mssql_enabled = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),label = "MS Sql",required =False)
	vnc_enabled = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),label = "VNC",required =False)

	telnet_banner = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','size': '25'}),label ="Banner",required=False, initial="")
	telnet_enabled = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),label = "Enable",required =False)
	telnet_port = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),label="Port",required =True,initial=23)

       
    

