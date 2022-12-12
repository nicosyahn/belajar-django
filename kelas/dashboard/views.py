from django.shortcuts import render
from dashboard.forms import FormBarang
from dashboard.forms import FormMembership
from dashboard.models import Barang
from dashboard.models import Membership


def produk(request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produk.html', konteks)

def tambah_barang(request):
    form=FormBarang()
    konteks={
        'form':form,
    }
    return render(request, 'tambah_barang.html', konteks)

def tambah_membership(request):
    form=FormMembership()
    konteks={
        'form':form,
    }
    return render(request, 'tambah_membership.html', konteks)

def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }
    return render(request, 'tb_items.html', konteks)

def Membership_View(request):
    memberships=Membership.objects.all()

    konteks={
        'memberships':memberships,
    }
    return render(request, 'tb_member.html', konteks)