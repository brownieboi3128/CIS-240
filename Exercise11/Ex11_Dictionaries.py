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

   
