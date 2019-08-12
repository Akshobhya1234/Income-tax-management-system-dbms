from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("account",views.account,name="account"),
    path("user123",views.user123,name = "user123"),
    path("tocg",views.tocg,name="tocg"),
    path("Its",views.Its,name="Its"),
    path("Salary123",views.Salary123,name="Salary123"),
    path("cg",views.cg,name="cg"),
    path("deduction",views.deduction,name="deduction"),
    path("oi",views.oi,name="oi"),
    path("fillform",views.fillform123,name="fillform"),
    path("userform123",views.userformview,name = "userform123"),
    path("tocgform123",views.tocgformview,name = "tocgform123"),
    path("Itsform123",views.Itsformview,name = "Itsform123"),
    path("Salaryform123",views.salaryformview,name="Salaryform123"),
    path("cgform123",views.cgformview,name="cgform123"),
    path("deductionform123",views.dformview,name="deductionform123"),
    path("calculation",views.calculationview,name="calculation"),
    path("oiform123",views.oiformview,name="oiform123")
    
]
