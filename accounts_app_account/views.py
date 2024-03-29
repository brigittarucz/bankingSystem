from django.shortcuts import render

from .models import Account 
from transaction_app.models import Transaction
from auth_app.models import Profile

def accounts_view(request):
    user = request.user
    # path = request.path
    # print(path)
    profile = Profile.objects.get(user=user)
    user_account = Account.objects.filter(account_user_fk=profile)

    context = {
        "user": user,
        "user_accounts": user_account,
        "profile": profile
    }
    return render(request, "accounts_app_account/account.html", context)





