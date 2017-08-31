import subprocess as sub

class ControlCanary():

	def __init__(self,ActionSTatus):
		self.ActionSTatus = ActionSTatus

	def SetAction(self):

		if self.ActionSTatus == 'start':
			p = sub.Popen(['/root/djangoWithOpenCan/bin/opencanaryd','--start'],stdout=sub.PIPE,stderr=sub.PIPE)
			output, errors = p.communicate()			
			print output
		else:
			p = sub.Popen(['/root/djangoWithOpenCan/bin/opencanaryd','--stop'],stdout=sub.PIPE,stderr=sub.PIPE)
			output, errors = p.communicate()			
			print output
