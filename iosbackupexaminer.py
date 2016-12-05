# iOS Backup Examiner v. 1.0
# Author: Jason Antrim (antrim111@gmail.com)
# https://github.com/jantrim/iosbackupexaminer
#
# -Parses the Info.plist property list file within an iOS backup file
# -Outputs important key/value pairs from Info.plist
# -Outputs file metadata
# -Calculates and outputs MD5, SHA1 and SHA256 hash values

# Import Python Standard Library modules:
#
# hashlib    Hashing
# os         Validating file exists and is readable
# sys        Exiting upon error
# time       Processing times
# plistlib   Parsing property list file
# argparse   Command line argument
#
import hashlib
import os
import sys
import time
import plistlib
import argparse

# Name:    ParseCommandLine() Function
#
# Desc:    Process and validate the command line argument
#  
# Actions: Uses the standard library argparse to process the command line
#
# 1 potential argument: -f, which defines the full path and file name of the property list file that will be parsed
#
def ParseCommandLine():

    # Create global variable for the argument 
    global gl_arg
    
    # Single argument -f expected. Argument is required. Help instruction provided
    parser = argparse.ArgumentParser(description='Parse an iOS backup\'s Info.plist file')
    parser.add_argument('-f', '--plistFile', type= ValidateFileRead, required=True, help="Info.plist file")    
    
    gl_arg = parser.parse_args()
    
    return

# End ParseCommandLine()

#
# Name:    ValidateFileRead Function
#
# Desc:    Function that will validate that a file exists and is readable
#
# Input:   Full path and filename
#  
# Actions: If valid it will return the path
#          If invalid it will raise an ArgumentTypeError within argparse,
#          which will inturn be printed to the user
#
#
def ValidateFileRead(theFile):

    # Validate the path is valid
    if not os.path.exists(theFile):
        raise argparse.ArgumentTypeError('File does not exist')

    # Validate the path is readable
    if os.access(theFile, os.R_OK):
        return theFile
    else:
        raise argparse.ArgumentTypeError('File is not readable')

#End ValidateFileRead()

#
# Name:    hashFile Function
#
# Desc:    Function that will hash the file, parse MAC times, and calcuate file size
#
# Input:   Full path and filename
#
# Actions: Hashing (MD5, SHA1, and SHA256) and identifying file metadata, then outputting this information
#
def hashFile(plistFile):
    
    try:
        
        # Open the file, read the contents into a buffer and then close the file
        # 'rb' opens the file in binary mode
        fp = open(plistFile,'rb')
        
        # Read the contents of the file
        fileContents = fp.read()
        
        # Close the file
        fp.close()
        
        # Create a hasher object of type sha256, sha1, md5
        hasher = hashlib.sha256()
        hasher2 = hashlib.sha1()
        hasher3 = hashlib.md5()
        
        # Hash the contents of the buffer
        hasher.update(fileContents)
        hasher2.update(fileContents)
        hasher3.update(fileContents)
        
        # Store file metadata
        theFileStats =  os.stat(plistFile)
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(plistFile)
    
        modifiedTime = time.ctime(mtime)
        accessTime = time.ctime(atime)
        createdTime = time.ctime(ctime)          

        # Print file metdata and calculated hash values
        print '\n\nFile Metadata'
        print '________________________________________________________________________________'        
        print 'File:\t\t\t',gl_arg.plistFile
        print 'File Modified:\t\t'+modifiedTime+'Z'
        print 'File Accessed:\t\t'+accessTime+'Z'
        print 'File Created:\t\t'+createdTime+'Z' 
        print 'File Size:\t\t',theFileStats.st_size,
        print 'bytes\n'       
        print 'MD5:\t\t\t'+hasher3.hexdigest()
        print 'SHA1:\t\t\t'+hasher2.hexdigest()
        print 'SHA256:\t\t\t'+hasher.hexdigest()
        
        # delete the hasher objects
        del hasher
        del hasher2
        del hasher3
        
    except:
        
        # If any exceptions occur notify the user and exit
        print('File Processing Error')
        sys.exit(0)
        
    return True

# End hashFile()

#
# Name:    parseInfoPlist Function
#
# Desc:    Parses Info.plist property list file keys and values
#
# Input:   Full path and filename
#
# Actions: Parses specific keys and values, outputs the data
#          If key does not exist, outputs '[key does not exist]'
#
def parseInfoPlist(plistFile):
    
    # Define variable for plist read by plistlib
    pl = plistlib.readPlist(plistFile)
    
    # Define variables for specific keys of interest
    # Exception handling is necessary to handle a situation where a specific key does not exist
    # Pass instruction causes program to ignore the exception and move on
    try:
        buildVersion          = pl['Build Version']
    except:
        pass
    try:
        deviceName            = pl['Device Name']
    except:
        pass    
    try:
        displayName           = pl['Display Name']
    except:
        pass
    try:
        guid                  = pl['GUID']
    except:
        pass
    try:
        iccid                 = pl['ICCID']
    except:
        pass
    try:
        imei                  = pl['IMEI']
    except:
        pass
    try:
        meid                  = pl['MEID']
    except:
        pass    
    try:
        installedApplications = pl['Installed Applications']
    except:
        pass
    try:
        lastBackupDate        = pl['Last Backup Date']
    except:
        pass
    try:
        phoneNumber           = pl['Phone Number']
    except:
        pass
    try:
        productName           = pl['Product Name']
    except:
        pass
    try:
        productType           = pl['Product Type']
    except:
        pass
    try:
        productVersion        = pl['Product Version']
    except:
        pass
    try:
        serialNumber          = pl['Serial Number']
    except:
        pass
    try:
        targetIdentifier      = pl['Target Identifier']
    except:
        pass
    try:
        targetType            = pl['Target Type']
    except:
        pass
    try:
        uniqueIdentifier      = pl['Unique Identifier']
    except:
        pass
    try:
        iTunesVersion         = pl['iTunes Version']
    except:
        pass

    print '\n\nKey\t\t\tValue'
    print '________________________________________________________________________________'
    
    # Print keys and values
    # Exception handling is necessary to handle situation where a specific key does not exist
    # If key does not exist, print '[key does not exist]'
    try:
        print 'Last Backup Date:\t'+str(lastBackupDate)+'Z'     
    except:
        print 'Last Backup Date:\t'+'[key does not exist]'
    try:    
        print 'Device Name:\t\t'+deviceName.replace(u"\u2018", "'").replace(u"\u2019", "'") # Replace unicode ' character with ASCII equivalent, if not an exception will be thrown
    except:
        print 'Device Name:\t\t'+'[key does not exist]'
    try:
        print 'Display Name:\t\t'+displayName.replace(u"\u2018", "'").replace(u"\u2019", "'") # Replace unicode ' character with ASCII equivalent
    except:
        print 'Display Name:\t\t'+'[key does not exist]'
    try:
        print 'Product Name:\t\t'+productName
    except:
        print 'Product Name:\t\t'+'[key does not exist]' 
    try:    
        print 'Product Type:\t\t'+productType
    except:
        print 'Product Type:\t\t'+'[key does not exist]'
    try:
        print 'Phone Number:\t\t'+phoneNumber
    except:
        print 'Phone Number:\t\t'+'[key does not exist]' 
    try:    
        print 'Serial Number:\t\t'+serialNumber 
    except:
        print 'Serial Number:\t\t'+'[key does not exist]'
    try:
        print 'IMEI:\t\t\t'+imei
    except:
        print 'IMEI:\t\t\t'+'[key does not exist]'  
    try:
        print 'MEID:\t\t\t'+meid
    except:
        print 'MEID:\t\t\t'+'[key does not exist]'
    try:
        print 'ICCID:\t\t\t'+iccid
    except:
        print 'ICCID:\t\t\t'+'[key does not exist]'
    try:
        print 'Product Version:\t'+productVersion
    except:
        print 'Product Version:\t'+'[key does not exist]'
    try:
        print 'Build Version:\t\t'+buildVersion
    except:
        print 'Build Version:\t\t'+'[key does not exist]'
    try:
        print 'GUID:\t\t\t' +guid
    except:
        print 'GUID:\t\t\t'+'[key does not exist]'
    try:
        print 'Target Type:\t\t'+targetType
    except:
        print 'Target Type:\t\t'+'[key does not exist]'
    try:
        print 'Target Identifier:\t'+targetIdentifier
    except:
        print 'Target Identifier:\t'+'[key does not exist]'
    try:  
        print 'Unique Identifier:\t'+uniqueIdentifier
    except:
        print 'Unique Identifier:\t'+'[key does not exist]' 
    try:    
        print 'iTunes Version:\t\t'+iTunesVersion
    except:
        print 'iTunes Version:\t\t'+'[key does not exist]'
    # for loop to iterate through each of the Installed Applications values
    # Print each value on a separate line
    try:    
        print 'Installed Applications:'
        for application in installedApplications:
            print '\t\t\t'+application             
    except:
        print '\t\t\t[key does not exist]'
            
    return True    

# End parseInfoPlist()

#
# Main Program

if __name__=="__main__":
    
    # Parse the command line argument
    ParseCommandLine()
    
    # Store the start time
    startTime = time.time()
    
    # Print version, author and website information
    print 'iOS Backup Examiner v. 1.0\n'
    print 'Author: Jason Antrim (antrim111@gmail.com)'
    print 'https://github.com/jantrim/iosbackupexaminer\n'
    
    # Notify the user that the program is processing the file
    print 'Processing '+gl_arg.plistFile
    
    # Call the parseInfoPlist() and hashFile() functions
    parseInfoPlist(gl_arg.plistFile)
    hashFile(gl_arg.plistFile)
    
    # Store the end time
    endTime = time.time()
    
    # Print processing information (start time, end time, elapsed time)
    # Append examiner's timezone to the times so there is no mistaking whether times are local or UTC
    
    print '\n\nProcessing Info'
    print '________________________________________________________________________________' 
    print 'Start Time:\t\t',time.ctime(startTime),' ',time.tzname[time.localtime().tm_isdst]
    print 'End Time:\t\t',time.ctime(endTime),' ',time.tzname[time.localtime().tm_isdst]
    print 'Elapsed Time:\t\t',endTime-startTime,'seconds'

# End main program