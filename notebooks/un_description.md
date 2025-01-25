## UN - Corruption and Economic Crime 

### 1. Basic Information
- **Data Source**: https://dataunodc.un.org/dp-crime-corruption-offences
- **Description**: Includes figures on offences for economic and environmental crimes recorded by the police or other law enforcement agencies. These data are submitted by Member States to UNODC through the United Nations Survey of Crime Trends and Operations of Criminal Justice Systems (UN-CTS) or other means.
- **Year/Coverage**: 2003 - 2022

### 2. Key Variables / Important Features

| **Column Name** | **Type** | **Description** |
|-----------------|----------|-----------------|
| Iso3_code		  | object   | Country ISO3 code    |
| Country		  | object   | Country name    |
| Category        | object   | Type of activity or crime recorded    |
| Year            | object   | Year of the observation         |
| Unit of measurement | object    | Counts or Rate per 100,000 population     |
| Value           | object   | Value of the specific category |



#### Key Categories:

Corruption - Unlawful acts as defined in the United Nations Convention against Corruption and other national and international legal instruments against corruption.

Corruption: Bribery -  Promising, offering, giving, soliciting, or accepting an undue advantage to or from a public official or a person who directs or works in a private sector entity, directly or indirectly, in order that the person act or refrain from acting in the exercise of his or her official duties

Corruption: Other acts of corruption -  Other acts of corruption includes embezzlement, abuse of functions, trading in influence, illicit enrichment and all other acts of corruption not mentioned above. 

Fraud - Conversion or transfer of property, knowing that such property is the proceeds of crime, for the purpose of concealing or disguising the illicit origin of such property or of helping any person who is involved in the commission of the predicate offence to evade the legal  consequences of his or her actions, as well as the concealment or disguise of the true nature, source, location, disposition, movement or ownership of rights with respect to the property.

Money laundering - Conversion or transfer of property, knowing that such property is the proceeds of crime, for the purpose of concealing or disguising the illicit origin of such property or of helping any person who is involved in the commission of the predicate offence to evade the legal consequences of his or her actions, as well as the concealment or disguise of the true nature, source, location, disposition, movement or ownership of rights with respect to the property.


### 3. Data Cleaning / Transformation
- **Original Format**: 
- **Filtering**: Retained only European countries, indicators related with corruption (Corruption, Corruption: Bribery, Corruption: Other acts of corruption, Fraud, Money laundering), data from 2012 to 2022, and Unit of measure 'Rate per 100,000 population'
- **Columns Kept**: Country, Category, VALUE, year
- **Data Type Conversions**: object → float
- **Handling Missing Values**: 


### 4. Data Context & Usage
- **Why This Dataset**: This data shows indicators about actual corruption.
- **Potential Biases**: 
- **Reliability Considerations**: The data for each country is collect by their police or law or other law enforcement agencies, which means it is dependent on the report/investigation of these crimes.

### 5. Additional Notes / References
- **Official Documentation**: https://dataunodc.un.org/sites/dataunodc.un.org/files/metadata_corruption_and_economic_crime.pdf
- **Last Update**: 16/05/2024
- **Date of Retrieval**: 19/01/2025
- **Citation**: UNODC (2024), UNODC Research - Data Portal – Corruption and Economic Crime. https://dataunodc.un.org/dp-crime-corruption-offences (Accessed on [19 JAN 2025]).