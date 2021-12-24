from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models import Order
from django.contrib.auth.models import User
from store.models import Customer
from contact.models import FeedBack

# Create your views here.

def adminLte(request):
    order = Order.objects.filter(complete=True)
    all = 0
    days = {1: 0, 2: 0,
            3: 0, 4: 0,
            5: 0, 6: 0,
            7: 0, 8: 0,
            9: 0, 10: 0,
            11: 0, 12: 0}

    for i in order:
        month = i.date_ordered.month
        days[month] += int(i.get_cart_items)
        all += int(i.get_cart_items)
    customers = Customer.objects.all()

    context = {"order_count": all, "users_count": len(customers), "data": list(days.values())}
    return render(request, "adminLte/index.html", context)


def charts(request, name):
    cities = {
        'Andijon':
            {1: 0, 2: 0,
             3: 0, 4: 0,
             5: 0, 6: 0,
             7: 0, 8: 0,
             9: 0, 10: 0,
             11: 0, 12: 0},
        'Buxoro':
            {1: 0, 2: 0,
             3: 0, 4: 0,
             5: 0, 6: 0,
             7: 0, 8: 0,
             9: 0, 10: 0,
             11: 0, 12: 0},
        'Fargona':
            {1: 0, 2: 0,
             3: 0, 4: 0,
             5: 0, 6: 0,
             7: 0, 8: 0,
             9: 0, 10: 0,
             11: 0, 12: 0},
        'Jizzax':
            {1: 0, 2: 0,
             3: 0, 4: 0,
             5: 0, 6: 0,
             7: 0, 8: 0,
             9: 0, 10: 0,
             11: 0, 12: 0},
        'Xorazm':
            {1: 0, 2: 0,
             3: 0, 4: 0,
             5: 0, 6: 0,
             7: 0, 8: 0,
             9: 0, 10: 0,
             11: 0, 12: 0},
        'Namangan':
            {1: 0, 2: 0,
             3: 0, 4: 0,
             5: 0, 6: 0,
             7: 0, 8: 0,
             9: 0, 10: 0,
             11: 0, 12: 0},
        'Navoiy':
            {1: 0, 2: 0,
             3: 0, 4: 0,
             5: 0, 6: 0,
             7: 0, 8: 0,
             9: 0, 10: 0,
             11: 0, 12: 0},
        'Qashqadaryo':
            {1: 0, 2: 0,
             3: 0, 4: 0,
             5: 0, 6: 0,
             7: 0, 8: 0,
             9: 0, 10: 0,
             11: 0, 12: 0},
        'Qoraqalpogʻiston':
            {1: 0, 2: 0,
             3: 0, 4: 0,
             5: 0, 6: 0,
             7: 0, 8: 0,
             9: 0, 10: 0,
             11: 0, 12: 0},
        'Samarqand':
            {1: 0, 2: 0,
             3: 0, 4: 0,
             5: 0, 6: 0,
             7: 0, 8: 0,
             9: 0, 10: 0,
             11: 0, 12: 0},
        'Sirdaryo':
            {1: 0, 2: 0,
             3: 0, 4: 0,
             5: 0, 6: 0,
             7: 0, 8: 0,
             9: 0, 10: 0,
             11: 0, 12: 0},
        'Surxondaryo':
            {1: 0, 2: 0,
             3: 0, 4: 0,
             5: 0, 6: 0,
             7: 0, 8: 0,
             9: 0, 10: 0,
             11: 0, 12: 0},
        'Tashkent':
            {1: 0, 2: 0,
             3: 0, 4: 0,
             5: 0, 6: 0,
             7: 0, 8: 0,
             9: 0, 10: 0,
             11: 0, 12: 0}
    }
    orders = Order.objects.filter(complete=True)
    all_count = {
        1: 0, 2: 0,
             3: 0, 4: 0,
             5: 0, 6: 0,
             7: 0, 8: 0,
             9: 0, 10: 0,
             11: 0, 12: 0}
    for order in orders:
        month = order.date_ordered.month
        all_count[month] += order.get_cart_items
        cities[order.city][month] += order.get_cart_items
    
    all = list(all_count.values())
    andijon = {"list_data":list(cities['Andijon'].values()), "all_value":sum(list(cities['Andijon'].values()))}
    buxoro = {"list_data":list(cities["Buxoro"].values()), "all_value":sum(list(cities["Buxoro"].values()))}
    fargona = {"list_data":list(cities["Fargona"].values()), "all_value":sum(list(cities["Fargona"].values()))}
    jizzax = {"list_data":list(cities['Jizzax'].values()), "all_value":sum(list(cities['Jizzax'].values()))}
    xorazm = {"list_data":list(cities['Xorazm'].values()), "all_value":sum(list(cities['Xorazm'].values()))}
    namangan = {"list_data":list(cities['Namangan'].values()), "all_value":sum(list(cities['Namangan'].values()))}
    navoiy = {"list_data":list(cities['Navoiy'].values()), "all_value":sum(list(cities['Navoiy'].values()))}
    qashqadaryo = {"list_data":list(cities['Qashqadaryo'].values()), "all_value":sum(list(cities['Qashqadaryo'].values()))}
    qoraqalpogiston = {"list_data":list(cities['Qoraqalpogʻiston'].values()), "all_value":sum(list(cities['Qoraqalpogʻiston'].values()))}
    samarqand = {"list_data":list(cities['Samarqand'].values()), "all_value":sum(list(cities['Samarqand'].values()))}
    sirdaryo = {"list_data":list(cities['Sirdaryo'].values()), "all_value":sum(list(cities['Sirdaryo'].values()))}
    surxondaryo = {"list_data":list(cities['Surxondaryo'].values()), "all_value":sum(list(cities['Surxondaryo'].values()))}
    tashkent = {"list_data":list(cities['Tashkent'].values()), "all_value":sum(list(cities['Tashkent'].values()))}


    context = {'all_count': all, 'andijon': andijon, 'buxoro': buxoro, 'fargona': fargona, 'jizzax': jizzax,
               'xorazm': xorazm,
               'namangan': namangan, 'navoiy': navoiy, 'qashqadaryo': qashqadaryo, 'qoraqalpogiston': qoraqalpogiston,
               'samarqand': samarqand, 'sirdaryo': sirdaryo, 'surxondaryo': surxondaryo, 'tashkent': tashkent}
    print(context['tashkent'])
    return render(request, f"adminLte/pages/charts/{name}.html", context)


def mailbox(request, mailbox_name):
    messages = FeedBack.objects.all()
    context = {'messages': messages}
    return render(request, f"adminLte/pages/mailbox/{mailbox_name}.html", context)

from django.views.decorators.csrf import csrf_exempt

def mailbox_imbox_detail(request, inbox_id):

    print(inbox_id)
    messages = FeedBack.objects.all()

    message = FeedBack.objects.get(id=inbox_id)
    if request.method == "POST":

        message.delete()
        return redirect("mailbox", mailbox_name="mailbox")
    context = {'message_details': message, "max_num": len(messages)+1, "min_num": 0}
    return render(request, "adminLte/pages/mailbox/read-mail.html", context)





