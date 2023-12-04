from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('BienDoiAmBan/', views.BienDoiAmBan, name="BienDoiAmBan"),
    path('BienDoiHamSoMu/', views.BienDoiHamSoMu, name="BienDoiHamSoMu"),
    path('BienDoiLogarit/', views.BienDoiLogarit, name="BienDoiLogarit"),
    path('CanBangLuocDoXam/', views.CanBangLuocDoXam, name="CanBangLuocDoXam"),
    path('LocTrungVi/', views.LocTrungVi, name="LocTrungVi"),
    path('NangCaoChatLuongAnhSuDungToanTuDiem/', views.NangCaoChatLuongAnhSuDungToanTuDiem, name="NangCaoChatLuongAnhSuDungToanTuDiem"),
    path('PhanNguong/', views.PhanNguong, name="PhanNguong")
]
