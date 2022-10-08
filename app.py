import requests


token = "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"

headers = {'Authorization': 'token ' + token}

user = input("Enter the user")

res = requests.get(f"https://api.github.com/users/{user}/repos" , headers = headers)
dat = res.json()

for i in dat:
    if i['fork'] == True:
        print(i['name'])
        res2 = requests.get(f"https://api.github.com/repos/{user}/{i['name']}",headers = headers)
        res2 = res2.json()
        print("Forked from  : " + res2['source']['full_name'])
        name = res2['source']['full_name'].split('/')
        res4 = requests.get(f"https://api.github.com/repos/{name[0]}/{name[1]}/branches" , headers = headers)
        res4 = res4.json()
        res3 = requests.get(f"https://api.github.com/repos/{name[0]}/{name[1]}/topics", headers = headers)
        res3 = res3.json()
        print(res3)
        shas = []
        for i in res4:
            shas.append((i['commit']['sha'],i['name']))
        for i,n in shas:
            res5 = requests.get(f"https://api.github.com/repos/{name[0]}/{name[1]}/commits?sha={i}", headers = headers)
            res5 = res5.json()
            branch = n
            print(f"People who got commits in branch {branch}: ")
            people = set()
            for j in res5:
                temp1 = (j['committer']['login'])
                if temp1 != 'web-flow':
                    people.add(temp1)
            print(people)
            print('\n')
        if user in people:
            print("User's Pr is merged")
                
            
        

