let get_input_coefficients = function() {
    let a = $("#mtgformat option:selected").text()
    let b = $("input#b").val()
    let c = $("input#c").val()
    return {'mtgformat': a,
            'numplayers': parseInt(b),
            'c': parseInt(c)}
};

let send_coefficient_json = function(coefficients) {
    $.ajax({
        url: '/solve',
        contentType: "application/json; charset=utf-8",
        type: 'POST',
        success: function (data) {
            display_solutions(data);
        },
        data: JSON.stringify(coefficients)
    });
};

let display_solutions = function(solutions) {
    $("span#solution").html("Format: " + solutions.root_1 + " and Players: " + solutions.root_2)
};


$(document).ready(function() {

    $("button#solve").click(function() {
        let coefficients = get_input_coefficients();
        send_coefficient_json(coefficients);
    })

})
