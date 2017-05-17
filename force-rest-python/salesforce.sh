#!/bin/bash

echo '********************starting the  script*********************************'
echo  '*******************Running the apex_limit_get.py************************'
python apex_limit_get.py > hai.txt
echo '********************written the data in to given text file hai.txt*******'
cat hai.txt
echo '********************Mapping the get values and formating them in required formate***************'
python Mapping_get.py > test.txt
echo '********************Dumped Mapped values to test.txt*********************'
python ms.py
echo '********************Formating the final output***************************'
echo '********************Posting the data to Salesforce***********************'
python apex_limit_post.py 'New ID' >> output.txt
echo '********************the out put of the Record Inserted is ***************'
cat  output.txt 
echo '********************Output of the Record Id*******************************'
