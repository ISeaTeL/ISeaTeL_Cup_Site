from contest.models import SignUp
signup = SignUp.objects.all()

ss = ""
for us in signup:
    ss += ', '+us.email

print ss
