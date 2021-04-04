import random
import string


letters = string.ascii_letters
print('Your brand new password is:')
print (''.join(random.choice(letters) for i in range(12)))
 