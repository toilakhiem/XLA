from django.shortcuts import render
from django import forms
from .ThuatToan.BienDoiAmBan import *
from .ThuatToan.BienDoiHamSoMu import *
from .ThuatToan.BienDoiLogarit import *
from .ThuatToan.CanBangLuocDoXam import *
from .ThuatToan.LocTrungVi import *
from .ThuatToan.NangCaoChatLuongAnhSuDungToanTuDiem import *
from .ThuatToan.PhanNguong import *

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

def index(request):
    return render(request, "index.html")

def BienDoiAmBan(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']
            BDAB_process_image(uploaded_image)
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form})

def BienDoiHamSoMu(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']
            BDHSM_process_image(uploaded_image)
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form})

def BienDoiLogarit(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']
            BDL_process_image(uploaded_image)
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form})

def CanBangLuocDoXam(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']
            CBLDX_process_image(uploaded_image)
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form})

def LocTrungVi(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']
            LTV_process_image(uploaded_image)
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form})

def NangCaoChatLuongAnhSuDungToanTuDiem(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']
            NCCLA_process_image(uploaded_image)
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form})

def PhanNguong(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']
            PN_process_image(uploaded_image)
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form})