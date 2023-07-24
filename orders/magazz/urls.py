from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from magazz.views import PartnerUpdate, RegisterAccount,\
    ConfirmAccount, AccountDetails, LoginAccount, CategoryView,\
    ShopViewSet, ProductInfoView, BasketView, OrderView, ContactView,\
    PartnerOrders, PartnerState, ProductViewSet, PartnerNameUrl

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', ProductViewSet)
router.register('shops', ShopViewSet)
router.register('categories', CategoryView)



app_name = 'magazz'

urlpatterns = [
    path('user/register', RegisterAccount.as_view()),
    path('user/register/confirm', ConfirmAccount.as_view()),
    path('user/login', LoginAccount.as_view()),
    path('user/details', AccountDetails.as_view()),






    path('products', ProductInfoView.as_view()),



    path('basket', BasketView.as_view()),

    path('partner/update', PartnerUpdate.as_view()),
    path('partner/state', PartnerState.as_view()),
    path('partner/orders', PartnerOrders.as_view()),
    path('partner/nameurl', PartnerNameUrl.as_view()),

    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),

    path('order', OrderView.as_view(), name='order'),



] + router.urls

