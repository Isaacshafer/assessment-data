log_file = open("um-server-01.txt") #opening the um-server-01.txt file


def sales_reports(log_file): #naming a function
    for line in log_file: #looping through each line in the file
        line = line.rstrip() #trims off any extra space at the end of a line
        day = line[0:3] #setting variable day equal to what day is in the line
        if day == "Mon": #prints the line if the day in the line is tuesday/monday
            print(line)


sales_reports(log_file) #calls the function
