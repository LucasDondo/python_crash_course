def build_profile(first, last, **user_info):
    ''' Build a dic. containing evth. we know about a usr. '''

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('lucas', 'dondo',
                             location='argentina',
                             field='informatics engineering',
                             university='itba')

print(user_profile)
