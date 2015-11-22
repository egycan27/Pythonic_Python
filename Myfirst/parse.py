from jenkinsapi.jenkins import Jenkins
from jenkinsapi.jenkins import Jenkins
import xml.etree.ElementTree as ET

J = Jenkins('http://localhost:8080')
username='mamdouh'
password='egycan27'
J = Jenkins('http://localhost:8080',username, password)
job = J['My_first']
config = J['My_first'].get_config()
#print(config)
EMPTY_JOB_CONFIG = config
jobname = "new_template"
new_job = J.create_job(jobname, EMPTY_JOB_CONFIG)
new_conf = new_job.get_config()

root = ET.fromstring(new_conf.strip())

builders = root.find('builders')
shell = ET.SubElement(builders, 'hudson.tasks.Shell')
command = ET.SubElement(shell, 'command')
command.text = "ls"

print ET.tostring(root)
J[jobname].update_config(ET.tostring(root))

#xmldoc = minidom.parse(config)
#itemlist = xmldoc.getElementsByTagName('string')
#print(len(itemlist))
#print(itemlist[0].attributes['name'].value)
#for s in itemlist:
#    print(s.attributes['name'].value)