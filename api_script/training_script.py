from xmlrpc import client

url = 'http://localhost:8069'
db = 'training_api'
username ='admin'
password = 'admin'

#Check the version of the DB trhough the url
common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print("Common Version: " + str(common.version()))



#Grab uid of the current user
uid = common.authenticate(db, username, password, {})
print("uid: " + str(uid))



#Check that the user has rights to access res.partner
models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
access = models.execute_kw(db, uid, password,
    'res.partner', 'check_access_rights',
    ['read'], {'raise_exception': False})

print("Access: " + str(access))



# Get all res.partnerts that are a company and a customer
cust_company = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[['is_company', '=', True], ['customer', '=', True]]])

print("Is a Customer Company: " + str(cust_company))



# Get the count of the res.partnerts that are a company and a customer
count = models.execute_kw(db, uid, password,
    'res.partner', 'search_count',
    [[['is_company', '=', True], ['customer', '=', True]]])

print("Number of Customers: " + str(count))



# Grab one company customer partner
ids = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[['is_company', '=', True], ['customer', '=', True]]],
    {'limit': 1})
# Grab the record of that partner
[record] = models.execute_kw(db, uid, password,
    'res.partner', 'read', [ids])
#printing the number of fields in that record
print("Length of Record" + str(len(record)))



# Use search_read to get only certain fields from the company customers
partners = models.execute_kw(db, uid, password,
    'res.partner', 'search_read',
    [[['is_company', '=', True], ['customer', '=', True]]],
    {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
print("Partners: " + str(partners))



# Create a new res.partner with name "New Partner"
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': "New Partner",
}])
print("New Partner's ID: " + str(id))



# Change the name of the partner to Newer Partner
models.execute_kw(db, uid, password, 'res.partner', 'write', [[id], {
    'name': "Newer partner"
}])
# get record name after having changed it
new_name = models.execute_kw(db, uid, password, 'res.partner', 'name_get', [[id]])
print("The New Partner Name:" + str(new_name))




# Delete the created records
models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[id]])
# check if the deleted record is still in the database
is_deleted = models.execute_kw(db, uid, password,
    'res.partner', 'search', [[['id', '=', id]]])
print("Is deleted: " + str(is_deleted))
