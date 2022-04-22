import sys
sys.path.append(r'C:\IIT_Palakkad\Projects\VIVA\Educational-Repository\backend\educationalRepository')

import databaseInterfaces.mongoDB_interface as mongoDBI

def validateUser(userDetails):
    userObject = mongoDBI.findSingleDocument("educationalRepository","User",userDetails)
    return userObject

def emailAuthentication(userDetails):
    return True

def authenticateUser(userDetails):
    if(emailAuthentication(userDetails)):
        return validateUser(userDetails)
    else:
        return None

# mongoDBI.saveSingleDocument("educationalRepository","User",{"email":"sample.iitpkd.ac.in","password":"sample123"})

# print(authenticateUser({"email":"sample.iitpkd.ac.in","password":"sample123"}))