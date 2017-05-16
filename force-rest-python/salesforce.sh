#!/bin/bash

'-------------------------------------starting the  script----------------- '
 '------------------------------------Running the apex_limit_get.py----------------------------------'
python apex_limit_get.py > hai.txt
'-------------------------------------written the data in to given text file'hai.txt'---------------------------------'
cat hai.txt
'------------------------------------------------------------------------------------Mapping the get values and formating them in required formate-------------------'
python Mapping_get.py > test.txt
'----------------------------------------------Dumped Mapped values to test.txt------------------------------------------------'
python ms.py
'-------------------------------------------Formating the final output--------------------------------'
'-------------------------------------Posting the data to Salesforce---------------------------------------------'
python apex_limit_post.py > output.txt
'-------------------------------------the out put of the Record Inserted is -------------------------------------------------------------------------------------------------------'
cat output.txt
'---------------------------------------------------Output of the Record Id----------------------------------------------------'
