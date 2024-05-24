
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
#         # Version Warning! 
#         # This code is designed to work with the version 0.8 of pysmartdatamodels or later
#         # to work with earlier version you need to replace the import instruction for
#         # from pysmartdatamodels import pysmartdatamodels as sdm
#         
#         
import pysmartdatamodels as sdm
import subprocess
serverUrl = "http://localhost:1026" # supposed that your broker is installed in localhost. Edit to match your configuration
dataModel = "MedicationAdministration"
subject = "dataModel.Hl7"
resourceType = "MedicationAdministration"
attribute = "resourceType"
value = resourceType
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

text = {'status': 'generated', 'div': '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Generated Narrative</b></p><div style="display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%"><p style="margin-bottom: 0px">Resource &quot;medadmin0301&quot; </p></div><p><b>status</b>: in-progress</p><p><b>medication</b>: <a name="med0301"> </a></p><blockquote><div style="display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%"><p style="margin-bottom: 0px">Resource &quot;med0301&quot; </p></div><p><b>code</b>: Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE) <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> (<a href="http://terminology.hl7.org/3.1.0/CodeSystem-v3-ndc.html">National drug codes</a>#0409-6531-02)</span></p></blockquote><p><b>subject</b>: <a href="patient-pat1.html">Patient/pat1: Donald Duck</a> &quot;Duck DONALD&quot;</p><p><b>context</b>: <a href="encounter-f001.html">Encounter/f001: encounter who leads to this prescription</a></p><p><b>effective</b>: 2015-01-15T14:30:00+01:00 --&gt; (ongoing)</p><h3>Performers</h3><table class="grid"><tr><td>-</td><td><b>Actor</b></td></tr><tr><td>*</td><td><a href="practitioner-f007.html">Practitioner/f007: Patrick Pump</a> &quot;Simone HEPS&quot;</td></tr></table><p><b>reasonCode</b>: Given as Ordered <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> (<a href="codesystem-reason-medication-given-codes.html">Reason Medication Given Codes</a>#b)</span></p><p><b>request</b>: <a href="medicationrequest-medrx0318.html">MedicationRequest/medrx0318</a></p><h3>Dosages</h3><table class="grid"><tr><td>-</td><td><b>Text</b></td><td><b>Route</b></td><td><b>Method</b></td><td><b>Dose</b></td></tr><tr><td>*</td><td>500mg IV q6h x 3 days</td><td>Intravenous route (qualifier value) <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> (<a href="https://browser.ihtsdotools.org/">SNOMED CT</a>#47625008)</span></td><td>IV Push <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> ()</span></td><td>500 mg<span style="background: LightGoldenRodYellow"> (Details: UCUM code mg = \'mg\')</span></td></tr></table><p><b>eventHistory</b>: <a name="signature"> </a></p><blockquote><div style="display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%"><p style="margin-bottom: 0px">Resource &quot;signature&quot; </p></div><p><b>target</b>: <a href="servicerequest-physiotherapy.html">ServiceRequest/physiotherapy</a></p><p><b>recorded</b>: 02/02/2017 4:23:07 AM</p><h3>Agents</h3><table class="grid"><tr><td>-</td><td><b>Role</b></td><td><b>Who</b></td></tr><tr><td>*</td><td>author (originator) <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> (<a href="http://terminology.hl7.org/3.1.0/CodeSystem-v3-ParticipationType.html">ParticipationType</a>#AUT)</span></td><td><a href="practitioner-example.html">Practitioner/example: Dr Adam Careful</a> &quot;Adam CAREFUL&quot;</td></tr></table></blockquote></div>'}
attribute = "text"
value = text
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

contained = [{'resourceType': 'Medication', 'id': 'med0301', 'code': {'coding': [{'system': 'http://hl7.org/fhir/sid/ndc', 'code': '0409-6531-02', 'display': 'Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)'}]}}, {'resourceType': 'Provenance', 'id': 'signature', 'target': [{'reference': 'ServiceRequest/physiotherapy'}], 'recorded': '2017-02-01T17:23:07Z', 'agent': [{'role': [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-ParticipationType', 'code': 'AUT'}]}], 'who': {'reference': 'Practitioner/example', 'display': 'Dr Adam Careful'}}], 'signature': [{'type': [{'system': 'urn:iso-astm:E1762-95:2013', 'code': '1.2.840.10065.1.12.1.1', 'display': "Author's Signature"}], 'when': '2017-02-01T17:23:07Z', 'who': {'reference': 'Practitioner/example', 'display': 'Dr Adam Careful'}, 'targetFormat': 'application/fhir+xml', 'sigFormat': 'application/signature+xml', 'data': 'dGhpcyBibG9iIGlzIHNuaXBwZWQ='}]}]
attribute = "contained"
value = contained
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

status = "in-progress"
attribute = "status"
value = status
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
