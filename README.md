## A repo to edit the metadata and xml of saildrone files
To prepare a dataset for GTS by removing extraneous variables from the xml file, use `keepvars_GTS_xml_v3.py`. This step should be done <b>first</b> (for GTS).
<br>To prepare a dataset for serving via ERDDAP by editing the xml file, use `edit_xml_saildrone_newintake_v2.6.py`. This step should be done <b>after</b> 
`keepvars_GTS_xml_v*.py` if using, but can be done independently on an xml file.
<br><br> `edit_metadata_saildrone.ipynb` is for editing the metadata of individual saildrone files. This should largely be ignored, but is here if anyone is interested in my (Ellen's) process.
