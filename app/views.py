from django.shortcuts import render
from .models import Profile, Nft

#lista per far vedere tutti gli nft del singolo utente
def lista_nft(request):
    nfts = Nft.objects.filter(profile=request.user)
    return render(request, 'app/nfts.html', {'nfts': nfts})
#view per andare sul login
def login(request):
    return render(request, 'app/dist-web/index.html')