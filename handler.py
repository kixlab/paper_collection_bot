import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def lambda_handler(event, context):

    message = event["event"]["text"]
    isPaper=False
    splt = re.split('<|>',message)
    shareword = " shared a file: "
    print(message)
    if (len(splt)>1):
        isPaper=True
    if shareword in splt:
        isPaper=False
    print(isPaper,splt)
    if isPaper:
        link=splt[1]
        comment=splt[2].strip()
        info=''
        if('/' in comment):
            info=comment
            append(link, info)
            print(link,info)
    return 200


def append(link, info):
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credential.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open("Paperbox").sheet1
    sheet.append_row([info, link])
