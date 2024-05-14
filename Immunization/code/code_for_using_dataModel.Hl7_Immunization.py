
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
dataModel = "Immunization"
subject = "dataModel.Hl7"
resourceType = "{'type': 'string', 'value': 'Immunization'}"
attribute = "resourceType"
value = resourceType
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

text = {'type': 'Property', 'value': {'status': 'generated', 'div': '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Generated Narrative</b></p><div style="display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%"><p style="margin-bottom: 0px">Resource &quot;example&quot; </p></div><p><b>identifier</b>: id: urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234</p><p><b>status</b>: completed</p><p><b>vaccineCode</b>: Fluvax (Influenza) <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> (unknown#FLUVAX)</span></p><p><b>patient</b>: <a href="patient-example.html">Patient/example</a> &quot;Peter CHALMERS&quot;</p><p><b>encounter</b>: <a href="encounter-example.html">Encounter/example</a></p><p><b>occurrence</b>: 2013-01-10</p><p><b>primarySource</b>: true</p><p><b>location</b>: <a href="location-1.html">Location/1</a> &quot;South Wing, second floor&quot;</p><p><b>manufacturer</b>: <a href="organization-hl7.html">Organization/hl7</a> &quot;Health Level Seven International&quot;</p><p><b>lotNumber</b>: AAJN11K</p><p><b>expirationDate</b>: 2015-02-15</p><p><b>site</b>: left arm <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> (<a href="http://terminology.hl7.org/3.1.0/CodeSystem-v3-ActSite.html">ActSite</a>#LA)</span></p><p><b>route</b>: Injection, intramuscular <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> (<a href="http://terminology.hl7.org/3.1.0/CodeSystem-v3-RouteOfAdministration.html">RouteOfAdministration</a>#IM)</span></p><p><b>doseQuantity</b>: 5 mg<span style="background: LightGoldenRodYellow"> (Details: UCUM code mg = \'mg\')</span></p><blockquote><p><b>performer</b></p><p><b>function</b>: Ordering Provider <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> (<a href="http://terminology.hl7.org/3.1.0/CodeSystem-v2-0443.html">providerRole</a>#OP)</span></p><p><b>actor</b>: <a href="practitioner-example.html">Practitioner/example</a> &quot;Adam CAREFUL&quot;</p></blockquote><blockquote><p><b>performer</b></p><p><b>function</b>: Administering Provider <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> (<a href="http://terminology.hl7.org/3.1.0/CodeSystem-v2-0443.html">providerRole</a>#AP)</span></p><p><b>actor</b>: <a href="practitioner-example.html">Practitioner/example</a> &quot;Adam CAREFUL&quot;</p></blockquote><p><b>note</b>: Notes on adminstration of vaccine</p><p><b>reasonCode</b>: Procedure to meet occupational requirement <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> (<a href="https://browser.ihtsdotools.org/">SNOMED CT</a>#429060002)</span></p><p><b>isSubpotent</b>: true</p><h3>Educations</h3><table class="grid"><tr><td>-</td><td><b>DocumentType</b></td><td><b>PublicationDate</b></td><td><b>PresentationDate</b></td></tr><tr><td>*</td><td>253088698300010311120702</td><td>2012-07-02</td><td>2013-01-10</td></tr></table><p><b>programEligibility</b>: Not Eligible <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> (<a href="codesystem-immunization-program-eligibility.html">Immunization Event Program Eligibility</a>#ineligible)</span></p><p><b>fundingSource</b>: Private <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> (<a href="codesystem-immunization-funding-source.html">Immunization Event Funding Source</a>#private)</span></p></div>'}}
attribute = "text"
value = text
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

identifier = {'type': 'Property', 'value': [{'system': 'urn:ietf:rfc:3986', 'value': 'urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234'}]}
attribute = "identifier"
value = identifier
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

status = "{'type': 'Property', 'value': 'completed'}"
attribute = "status"
value = status
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
