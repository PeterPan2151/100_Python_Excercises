# Assuming that we have some email addresses in the "username@companyname.com" format, please write program 
# to print the company name of a given email address. Both user names and company names are composed of letters only.
email = 'username@companyname.com'
att_position = email.index('@')
dot_position = email.index('.com')
company_name = email[att_position + 1: dot_position]
print(company_name)
