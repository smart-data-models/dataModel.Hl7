# dataModel.Hl7
Data models mapped from the HL7 official version. Available at http://hl7.org/fhir/R4B/ according to the license http://www.hl7.org/implement/standards/fhir/license.html. Changes include the limitation of the recursive properties of the schemas to 4 levels and the replacement of the 'const' clause of the json schema to enum with single value to be compatible with yaml. Besides this lack of data types in the original schema is also fixed.

### List of data models

The following entity types are available:
- [Account](https://github.com/smart-data-models/dataModel.Hl7/blob/master/Account/README.md). A financial tool for tracking value accrued for a particular purpose.  In the healthcare field, used to track charges for a patient, cost centers, etc.

- [Citation](https://github.com/smart-data-models/dataModel.Hl7/blob/master/Citation/README.md). The Citation Resource enables reference to any knowledge artifact for purposes of identification and attribution. The Citation Resource supports existing reference structures and developing publication practices such as versioning, expressing complex contributorship roles, and referencing computable resources.

- [Claim](https://github.com/smart-data-models/dataModel.Hl7/blob/master/Claim/README.md). A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.

- [Immunization](https://github.com/smart-data-models/dataModel.Hl7/blob/master/Immunization/README.md). Describes the event of a patient being administered a vaccine or a record of an immunization as reported by a patient, a clinician or another party.

- [Medication](https://github.com/smart-data-models/dataModel.Hl7/blob/master/Medication/README.md). This resource is primarily used for the identification and definition of a medication for the purposes of prescribing, dispensing, and administering a medication as well as for making statements about medication use.

- [MedicationAdministration](https://github.com/smart-data-models/dataModel.Hl7/blob/master/MedicationAdministration/README.md). Describes the event of a patient consuming or otherwise being administered a medication.  This may be as simple as swallowing a tablet or it may be a long running infusion.  Related resources tie this event to the authorizing prescription, and the specific encounter between patient and health care practitioner.

- [Organization](https://github.com/smart-data-models/dataModel.Hl7/blob/master/Organization/README.md). A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action.  Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc.

- [Patient](https://github.com/smart-data-models/dataModel.Hl7/blob/master/Patient/README.md). Demographics and other administrative information about an individual or animal receiving care or other health-related services.

- [Practitioner](https://github.com/smart-data-models/dataModel.Hl7/blob/master/Practitioner/README.md). A person who is directly or indirectly involved in the provisioning of healthcare.



### Contributors
[Link](https://github.com/smart-data-models/dataModel.Hl7/blob/master/CONTRIBUTORS.yaml) to the 1 current contributors of the data models of this Subject.


### Contribution
You can raise an [issue](https://github.com/smart-data-models/dataModel.Hl7/issues) or submit your [PR](https://github.com/smart-data-models/dataModel.Hl7/pulls) on existing data models
