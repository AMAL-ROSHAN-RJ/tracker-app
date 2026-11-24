def login(user, password):
    query = "SELECT * FROM users WHERE pw=?"
    return query, (password,)
