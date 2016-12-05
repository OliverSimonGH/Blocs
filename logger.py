filePath = "static/logs/log.txt"

def create_log():
    open(filePath, "w")

#Returning the logs in a list
def read_log():
    file = oepn(filePath, "r")
    result = file.read().split(',')
    file.close()
    return result


def write_email_to_log(data):
    file = open(filePath, "w")
    log_string = ""

    for item in data:
        log_string + item + ";"
