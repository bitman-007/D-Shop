from django.contrib import admin
from .models import Item, Order, OrderItem, Payment, Address, Coupon, Refund


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'update to refund accepted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon',
                    ]
    list_display_links = ['user',
                          'shipping_address',
                          'billing_address',
                          'payment',
                          'coupon',
                          ]
    list_filter = ['ordered',
                   'shipping_address',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted',
                   ]
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default_address',
    ]
    list_filter = ['default_address', 'address_type', 'country']
    search_fields = [
        'user',
        'street_address',
        'apartment_address',
        'zip',
    ]


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
