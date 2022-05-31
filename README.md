# CSV2UserModel

CSV2UserModel generates a file compliant with the following structure [Sitecore CDP guest identifiers data model for Batch API](https://doc.sitecore.com/cdp/en/developers/sitecore-customer-data-platform--data-model-2-0/sitecore-cdp-guest-identifiers-data-model-for-batch-api.html). It requires an input file with the following structure:
````
postCode,firstName,lastName,identifiers.0.provider,identifiers.0.id,identifiers.1.provider,identifiers.1.id,street.0,street.1
167890,Marion,Maltie,email,test@test.com,CRM,12313123,Ariosto street, Mozart rd.
234665,Jesse,Christopher,email,test@test.com,CRM,342567,Ariosto street, Mozart rd.
...
````

## uuid4 Generation
The script generates UUID4 automatically. It is not needed to be provided in the CSV input file.


## Multiple Values
While to generate a multivalue structure like `street` it is needed a column name with the following format:
````
<field>.<pos>
````

For example:
````
street.0, street.1
1st Rd, Another st.
````
will generate
````
"street":[
     "1 St",
     "Another st."
]
````


## Nested Values
To generate a nested structure like `identifiers` it is needed a column name with the following format:
````
<field>.<pos>.<subfield>
````

For example:
````
identifiers.0.id,identifiers.0.provider
test@test.com, email
````
will generate
````
"identifiers":[
    {
        "id": "test@test.com",
        "provider": "email"
    }
]
````

## Usage

It is a python3 script.

````
> python3 csv2usermodel.py inputfile.csv
````

or make it executable
````
> chmod +x csv2usermodel.py
> ./csv2usermodel.py inputfile.csv
````

The output is a file named `<inputfilename>.json`


## Exceptions

Not managed. TBD

# Limitations and Disclaimer
THE SOFTWARE IS PROVIDED “AS IS.” YOU BEAR THE RISK OF USING IT. PLEASE USE IT IN NON PRODUCTION ENVIRONMENTS.
