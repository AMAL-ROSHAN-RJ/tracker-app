def login(user, password):
    query = "SELECT * FROM users WHERE pw='%s'" % password
    return query
