var updateBtn = document.getElementsByClassName('update-btn')

for (i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        if (user == 'AnonymousUser') {
            addCookieItem(productId, action)
        } else {
            updateUserOrder(productId, action)
            console.log("user is logged in")
        }
    })
}

function addCookieItem(productId, action) {
    console.log(cart[productId])
    if (action == "add") {
        if (cart[productId] == undefined) {
            cart[productId] = {"quantity": 1}

        } else {
            cart[productId]["quantity"] += 1
        }
    }
    if (action == "remove") {
        cart[productId]["quantity"] -= 1

        if (cart[productId]["quantity"] <= 0) {
            console.log("removing item")
            delete cart[productId]
        }

    }
    console.log("Cart: ", cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}

function updateUserOrder(product_id, action) {
    console.log("sending data user is logged in", product_id, action)

    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'productId': product_id, "action": action})
    }).then((response) => {
        return response.json();
    }).then((data) => {
        console.log("Data: ", data)
        location.reload()
    })
}