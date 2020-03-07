orig_info = []
file = open("list.txt", "r")
orig_info = file.readlines()
headers = " Group Email [Required],Member Email,Member Type,Member Role"
file.close()


with open('members_template.csv', 'w') as csvFile:
    csvFile.write(headers)
    csvFile.write('\n')
    for line in orig_info:
        csvFile.write("vilistlased@ituk.ee,")
        csvFile.write(line.strip('\n'))
        csvFile.write(",user,")
        csvFile.write("member")
        csvFile.write('\n')

csvFile.close()
