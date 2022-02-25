key.
    varstripe = Stripe("pk_test_TYooMQauvdEDq54NiTphI7jx");
var purchase = {
    items: [{
        id: "xl-tshirt"
    }]
};

document.querySelector("button").disabled = true;
fetch("/create-payment-intent", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(purchase)
    })
    .then(function(result) {
        return result.json();
    })
    .then(function(data) {
        var elements = stripe.elements();
        var style = {
            base: {
                color: "#32325d",
                fontFamily: 'Arial, sans-serif',
                fontSmoothing: "antialiased",
                fontSize: "16px",
                "::placeholder": {
                    color: "#32325d"
                }
            },
            invalid: {
                fontFamily: 'Arial, sans-serif',
                color: "#fa755a",
                iconColor: "#fa755a"
            }
        };
        var card = elements.create("card", {
            style: style
        });
        card.mount("#card-element");
        card.on("change", function(event) {
            document.querySelector("button").disabled = event.empty;
            document.querySelector("#card-errors").textContent = event.error ? event.error.message :
                "";
        });
        var form = document.getElementById("paymentform");
        form.addEventListener("submit",
            function(event) {
                event.preventDefault();
                payWithCard(stripe, card, data.clientSecret);
            });
    });

page.
    varpayWithCard = function(stripe, card, clientSecret){
    loading(true);
    stripe
        .confirmCardPayment(clientSecret, {
            payment_method: {
                card: card
            }
        })
        .then(function(result) {
            if (result.error) {
                showError(result.error.message);
            } else {
                orderComplete(result.paymentIntent.id);
            }
        });
};

complete
var orderComplete = function(paymentIntentId) {
    loading(false);
    document
        .querySelector(".result-message a")
        .setAttribute(
            "href",
            "https://dashboard.stripe.com/test/payments/" + paymentIntentId);
    document.querySelector(".result-message").classList.remove("hidden");
    document.querySelector("button").disabled = true;
};

charge
var showError = function(errorMsgText) {
    loading(false);
    var errorMsg = document.querySelector("#carderrors");
    errorMsg.textContent = errorMsgText;
    setTimeout(function() {
        errorMsg.textContent =
            "";
    }, 4000);
};

var loading = function(isLoading) {
    if (isLoading) {
        document.querySelector("button").disabled = true;
        document.querySelector("#spinner").classList.remove("hidden");
        document.querySelector("#button-text").classList.add("hidden");
    } else {
        document.querySelector("button").disabled = false;
        document.querySelector("#spinner").classList.add("hidden");
        document.querySelector("#buttontext").classList.remove("hidden");
    }
};