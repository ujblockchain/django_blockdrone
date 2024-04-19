$("#id_country").change(function(){
    const url = $("#profileForm").attr("data-cities-url"); // get the url of the 'load_cities' view
    const countryId = $(this).val(); // get the selected country ID from the HTML input

    $.ajax({    // initialise an AJAX request
        url: url, // set the url of the request ()
        data: {
            "country_id": countryId // add the country id to the GET parameters
        },
        success: function (data){ // data is the return of the load_cities view function
            $("#id_city").html(data)// replace the contents of the city input with the data that came from the server 

        }


    })
})