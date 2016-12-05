# iOS Backup Examiner

Description

            Parses an iOS backup's Info.plist file to identify important information such as the backup 
            date and time, device name, phone number, serial number, installed applications, and more. 
            iOS 10 backups are supported. Compatible with Python 2.7.

iOS Backup Locations

            Windows 7, 8, 10:   C:\Users\<user>\AppData\Roaming\Apple Computer\MobileSync\Backup\
            Windows XP:         C:\Documents and Settings\<user>\Application Data\Apple Computer\MobileSync\Backup\
            Mac:                ~/Library/Application Support/MobileSync/Backup/
            
Help

            python iosbackupexaminer.py -h
                                
            usage: iosbackupexaminer.py [-h] -f PLISTFILE

            Parse an iOS backup's Info.plist file

            optional arguments:
              -h, --help      show this help message and exit
              -f PLISTFILE, --plistFile PLISTFILE
                              Info.plist file
                                    
Usage

            python iosbackupexaminer.py -f Info.plist
            
Example Output

            Key                     Value
            ________________________________________________________________________________

            Last Backup Date:       2015-09-26 14:57:41Z
            Device Name:            Daniel's iPhone
            Display Name:           Daniel's iPhone
            Product Name:           iPhone 5s
            Product Type:           iPhone6,1
            Phone Number:           (651) 354-9824
            Serial Number:          F98NG07GFMJM
            IMEI:                   35200906'7481292
            MEID:                   352009067481292
            ICCID:                  89148000001706526158
            Product Version:        9.0.1
            Build Version:          13A404
            GUID:                   FA8A4A7CB7950867B0F544D6A8F49063
            Target Type:            Device
            Target Identifier:      31e63128febc4a6956001193e595c0538dad8a7c
            Unique Identifier:      31E63128FEBC4A6956001193E595C0538DAD8A7C
            iTunes Version:         12.3.0.44
            Installed Applications:
                                    com.capitalone.enterprisemobilebanking
                                    com.ubercab.UberClient
                                    com.amazon.AMZNLocal
                                    [...]
                                    com.livingsocial.deals
                                    com.groupon.grouponapp
                                    com.google.Maps

            File Metadata
            ________________________________________________________________________________

            File:                   Info.plist
            File Modified:          Wed Aug 24 11:14:48 2016Z
            File Accessed:          Mon Dec 05 10:23:15 2016Z
            File Created:           Mon Dec 05 10:23:15 2016Z
            File Size:              1706318 bytes

            MD5:                    9463e8c06bf66e75fad0592a47742522
            SHA1:                   22b33261cadcdff0e39bf839c79a54dead519493
            SHA256:                 15cd7f20f93233f772b3509306655295de11683a94dcbd0dd8d8b2ac013a31a7

            Processing Info
            ________________________________________________________________________________

            Start Time:             Mon Dec 05 11:57:44 2016   Central Standard Time
            End Time:               Mon Dec 05 11:57:45 2016   Central Standard Time
            Elapsed Time:           0.233999967575 seconds
