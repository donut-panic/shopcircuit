# link to how to set up variable
# https://www.youtube.com/watch?v=IolxqkL7cD8

import os
db_user = 'your login'
db_password = 'your password'


db_user = os.environ.get('db_user')
db_password = os.environ.get('db_password')