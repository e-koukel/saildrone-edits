#!/usr/bin/env python
# coding: utf-8

# # python notebook that copies an xml file and removes unwanted variables
import os
import xml.etree.ElementTree as ET


#examples of potential filenames
#inputFilename = '/home/users/kobrien/saildrone/configs/saildrone_configs.xml'
#outputFilename = '/home/users/koukel/tomcat/content/erddap/metaedit_test_xmls/datasets_xmledit_selectvars.xml'


#asking for a filename to read and a filename to save out to
inputFilename = input('Enter a filename to read in: ')
outputFilename = input('Enter a filename to be saved out: ')
#makes space for a to-be-deleted xml file since things get weird with xml snippets and python
outputFilename_del = outputFilename.split('.')[0] + '_del' + '.' + outputFilename.split('.')[1]


#opens inputFilename and reads it out to another xml, which will be the one this code edits
with open(inputFilename) as inXML, open(outputFilename_del, 'w') as outXML:
    outXML.write('<toplevel>\n')#adds a top level node so that python can read the xml
    for line in inXML.readlines():
        outXML.write(line)
    outXML.write('</toplevel>\n')


#opens xml with new root, using a parser to keep comments
parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))

tree = ET.parse(outputFilename_del, parser)
root = tree.getroot()


#variables that we want to keep in the new xml file
#varskeep = ['latitude','longitude','time','trajectory','TEMP_AIR_MEAN','RH_MEAN','BARO_PRES_MEAN','TEMP_SBE37_MEAN','WIND_FROM_MEAN','WIND_SPEED_MEAN','SAL_SBE37_MEAN','WATER_CURRENT_SPEED_MEAN','WATER_CURRENT_DIRECTION_MEAN','WAVE_DOMINANT_PERIOD','WAVE_SIGNIFICANT_HEIGHT']


#finds all dataVariables not in varskeep and removes them
for dT in root.iter('dataset'):
    no_time = dT.findall('./dataVariable[sourceName="time"]')
    no_lat = dT.findall('./dataVariable[sourceName="latitude"]')
    no_lon = dT.findall('./dataVariable[sourceName="longitude"]')
    no_traj = dT.findall('./dataVariable[sourceName="trajectory"]')
    no_tam = dT.findall('./dataVariable[sourceName="TEMP_AIR_MEAN"]')
    no_rm = dT.findall('./dataVariable[sourceName="RH_MEAN"]')
    no_bpm = dT.findall('./dataVariable[sourceName="BARO_PRES_MEAN"]')
    no_tsm = dT.findall('./dataVariable[sourceName="TEMP_SBE37_MEAN"]')
    no_wfm = dT.findall('./dataVariable[sourceName="WIND_FROM_MEAN"]')
    no_wsm = dT.findall('./dataVariable[sourceName="WIND_SPEED_MEAN"]')
    no_ssm = dT.findall('./dataVariable[sourceName="SAL_SBE37_MEAN"]')
    no_wcsm = dT.findall('./dataVariable[sourceName="WATER_CURRENT_SPEED_MEAN"]')
    no_wcdm = dT.findall('./dataVariable[sourceName="WATER_CURRENT_DIRECTION_MEAN"]')
    no_wdp = dT.findall('./dataVariable[sourceName="WAVE_DOMINANT_PERIOD"]')
    no_wsh = dT.findall('./dataVariable[sourceName="WAVE_SIGNIFICANT_HEIGHT"]')
    
    noremlist = no_time + no_lat + no_lon + no_traj + no_tam + no_rm + no_bpm + no_tsm + no_wfm + no_wsm + no_ssm + no_wcsm + no_wcdm + no_wdp + no_wsh

    rem = dT.findall('./dataVariable')
    for x in range(len(rem)):    
        if rem[x] not in noremlist:
            #print('rem[x]',rem[x])
            #remx.append(rem[x])
            dT.remove(rem[x])


#prints your xml file so you can check that everything went okay before writing to your new xml file
#print(ET.tostring(root, encoding='unicode'))


#saves edits out to output file
tree.write(outputFilename_del)


#writes the edited xml to another xml, this time without the added <toplevel> node, back to original form
#outputFilename = outputFilename_del.split('.')[0][:-4] + '.' + outputFilename_del.split('.')[1]
with open(outputFilename_del) as inXML, open(outputFilename, 'w') as outXML:
    for line in inXML.readlines()[1:-1]:
        outXML.write(line)


#deletes the additionally created xml file
os.remove(outputFilename_del)
