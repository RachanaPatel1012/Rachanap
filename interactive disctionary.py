
import json
import difflib
from difflib import get_close_matches
def continu():
    ans = input("do you want to continue finding?")
    if ans == "yes":
        meaning(content)

def meaning(content):
    entry = input("enter the meaning of word you want to find")
    entry = entry.lower()
    if entry not in content:
        matche = get_close_matches(entry,content,cutoff=0.8)

        i = 0
        check = any(item in matche for item in content)
        if check is True:
            for i in range(len(matche)):
                con = input("did you mean{}true or false?".format(matche[i]))
                con = con.title()
                if con == "True":

                    print(content[matche[i]])
                    break
                else :
                    i = i + 1
            continu()

        else:
            print("invalid word")
            continu()

    else:
        print(content[entry])
        continu()

myfile = open("data.json",'r')
content = json.load(myfile)
meaning(content)
# print(content["rain"])
