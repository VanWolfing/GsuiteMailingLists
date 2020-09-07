orig_info = []
# Determine what the user wants to do
status = True
while status:
    action = input("Do you want to add accounts(1) or make a mailing list(2)? ")
    if action == 1:
        headers = "First Name [Required],Last Name [Required],Email Address [Required],Password [Required],Password Hash Function [UPLOAD ONLY],Org Unit Path [Required],New Primary Email [UPLOAD ONLY],Recovery Email,Home Secondary Email,Work Secondary Email,Recovery Phone [MUST BE IN THE E.164 FORMAT],Work Phone,Home Phone,Mobile Phone,Work Address,Home Address,Employee ID,Employee Type,Employee Title,Manager Email,Department,Cost Center,Building ID,Floor Name,Floor Section,Change Password at Next Sign-In,New Status [UPLOAD ONLY]"
        create_new_accounts(headers)
        status = False
        
    elif action == 2: 
        headers = " Group Email [Required],Member Email,Member Type,Member Role"
        create_mailing_list(headers)
        status = False
    else:
        print("Choose the correct number from the available options")
# Read the info
def create_new_accounts(headers):
    new_accounts = []
    generation_type = input("Do you have data in a txt file? Y/N ")
    if generation_type.capitalize() == "Y":
        file_name = input("Insert your filename here: ")
        generate(file_name, "new")
    elif generation_type.capitalize() == "N":
        answer = "Y"
        while answer.capitalize() == "Y":
            first_name = input("Add first name: ")
            new_accounts.append(first_name)
            last_name = input("Add last name: ")
            new_accounts.append(last_name)
            e_mail =
            password =
            org_unit_path =
            answer = input("Do you want to add more users? ")


def create_mailing_list(headers):


def generate(file_name, type):
    file = open(file_name, "r")
    orig_info = file.readlines()
    file.close()
    with open('output.csv', 'w') as csvFile:
        csvFile.write(headers)
        csvFile.write('\n')
        for line in orig_info:
    

    csvFile.close()
