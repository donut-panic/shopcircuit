$(".add-to-cart-button").click(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: "{% url 'add_product_to_cart_view' %}",
        data: serializedData,
        success: function (response) {
            var instance = JSON.parse(response["instance"]);
            var fields = instance[0]["fields"];
            $("#my_friends tbody").prepend(
                `<tr>
                <td>${fields["nick_name"]||""}</td>
                <td>${fields["first_name"]||""}</td>
                <td>${fields["last_name"]||""}</td>
                <td>${fields["likes"]||""}</td>
                <td>${fields["dob"]||""}</td>
                <td>${fields["lives_in"]||""}</td>
                </tr>`
            )
        },
        error: function (response) {
            // alert the error if any error occured
            alert(response["responseJSON"]["error"]);
        }
    })
})