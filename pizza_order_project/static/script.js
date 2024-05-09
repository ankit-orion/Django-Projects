// pizza_order/static/pizza_order/script.js
$(document).ready(function() {
    $('#pizza-order-form input[type="checkbox"]').change(function() {
        calculateTotalPrice();
    });

    $('#pizza-order-form input[type="radio"]').change(function() {
        calculateTotalPrice();
    });
});

function calculateTotalPrice() {
    var sizePrice = parseFloat($('input[name="size"]:checked').val());
    var crustPrice = parseFloat($('input[name="crust"]:checked').val());
    var toppingsPrice = 0;
    $('input[name="toppings"]:checked').each(function() {
        toppingsPrice += parseFloat($(this).val());
    });

    var totalPrice = sizePrice + crustPrice + toppingsPrice;
    $('#total-price').text('Total Price: $' + totalPrice.toFixed(2));
}
