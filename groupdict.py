def group_per_user(group_dict):
    user_groups={}
    for group,users in group_dict.items():
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return user_groups


print(group_per_user({"local": ["admin", "userA"],"public":  ["admin", "userB"],"administrator": ["admin"]}))
