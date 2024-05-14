
#         # This code allows you to install a orion-ld broker in a linux system
#         # The manuals are here https://github.com/FIWARE/context.Orion-LD/tree/develop/doc/manuals-ld
#         
#         # INSTALL NGSI LD broker (OrionLD)
#         sudo docker pull mongo:3.6
#         sudo docker pull fiware/orion-ld
#         sudo docker network create fiware_default
#         sudo docker run -d --name=mongo-db --network=fiware_default --expose=27017 mongo:3.6 --bind_ip_all --smallfiles
#         sudo docker run -d --name fiware-orionld -h orion --network=fiware_default -p 1026:1026  fiware/orion-ld -dbhost mongo-db
#         
#         # TO RELAUNCH (only if you have already installed a broker in the same machine)
#         sudo docker stop fiware-orionld
#         sudo docker rm fiware-orionld
#         sudo docker stop mongo-db
#         sudo docker rm mongo-db
#         sudo docker network rm fiware_default
#         
#         # CHECK INSTANCES
#         # Check the broker is running
#         curl -X GET 'http://localhost:1026/version'
#         
#         # Check what entities are in the broker
#         curl -X GET http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000
#         
#         # now the python code you can use to insert some value in the context broker according to the data model
#         
from pysmartdatamodels import pysmartdatamodels as sdm
import subprocess
serverUrl = "http://localhost:1026" # supposed that your broker is installed in localhost. Edit to match your configuration
dataModel = "Medication"
subject = "dataModel.Hl7"
resourceType = "{'type': 'Property', 'value': 'Medication'}"
attribute = "resourceType"
value = resourceType
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

text = {'type': 'StructuredValue', 'value': {'status': 'generated', 'div': "<div xmlns='http://www.w3.org/1999/xhtml'><p><b>Generated Narrative</b></p><div style='display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%'><p style='margin-bottom: 0px'>Resource &quot;med0301&quot; </p></div><p><b>code</b>: Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE) <span style='background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki'> (<a href='http://terminology.hl7.org/3.1.0/CodeSystem-v3-ndc.html'>National drug codes</a>#0409-6531-02)</span></p><p><b>status</b>: active</p><p><b>manufacturer</b>: <a name='org4'> </a></p><blockquote><div style='display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%'><p style='margin-bottom: 0px'>Resource &quot;org4&quot; </p></div><p><b>name</b>: Pfizer Laboratories Div Pfizer Inc</p></blockquote><p><b>form</b>: Injection Solution (qualifier value) <span style='background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki'> (<a href='https://browser.ihtsdotools.org/'>SNOMED CT</a>#385219001)</span></p><h3>Ingredients</h3><table class='grid'><tr><td>-</td><td><b>Item[x]</b></td><td><b>IsActive</b></td><td><b>Strength</b></td></tr><tr><td>*</td><td>Vancomycin Hydrochloride <span style='background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki'> (<a href='http://terminology.hl7.org/3.1.0/CodeSystem-v3-rxNorm.html'>RxNorm</a>#66955)</span></td><td>true</td><td>500 mg<span style='background: LightGoldenRodYellow'> (Details: UCUM code mg = 'mg')</span>/10 mL<span style='background: LightGoldenRodYellow'> (Details: UCUM code mL = 'mL')</span></td></tr></table><h3>Batches</h3><table class='grid'><tr><td>-</td><td><b>LotNumber</b></td><td><b>ExpirationDate</b></td></tr><tr><td>*</td><td>9494788</td><td>2017-05-22</td></tr></table></div>"}}
attribute = "text"
value = text
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

contained = {'type': 'Property', 'value': [{'resourceType': 'Organization', 'id': 'org4', 'name': 'Pfizer Laboratories Div Pfizer Inc'}]}
attribute = "contained"
value = contained
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

code = {'type': 'Property', 'value': {'coding': [{'system': 'http://hl7.org/fhir/sid/ndc', 'code': '0409-6531-02', 'display': 'Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)'}]}}
attribute = "code"
value = code
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
