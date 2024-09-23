#Christian Brown

users = {
    'bernard' : {
        'username': 'Bernard',
        'securityQuestion' : 'What was the name of your first dog?',
        'securityAnswer' : 'Scully',
    },
    'charlotte' : {
        'username' : 'Charlotte',
        'securityQuestion' : 'What is your favorite color?',
        'securityAnswer' : 'Purple',
    },
    'david' : {
        'username' : 'David',
        'securityQuestion' : 'In which city were you born?',
        'securityAnswer' : 'Cullowhee',
    }
}

for user, user_info in users.items():
    print("\nUser: " + user)
    securityQuestion = user_info['securityQuestion']
    securityAnswer = user_info['securityAnswer']
    
    print("\tChoose the following security question: " + securityQuestion)
    print("\tAnswer to the security question: " + securityAnswer)
    try:
        email = users['emailAddress']
    except KeyError:
        print("\t Error finding emailAddress")
#    username = user_info['username']
    try:
        usernum = user_info['username']+ 920456483
    except TypeError:
        print("\t These two data types can't be added together! ")  
