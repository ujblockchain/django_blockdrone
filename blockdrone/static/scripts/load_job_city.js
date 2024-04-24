$("#id_request_country").change(function(){
    const job_url = $("#jobRequestForm").attr("data-job-cities-url"); // get the url of the 'load_cities' view
    const countryId = $(this).val(); // get the selected country ID from the HTML input

    $.ajax({    // initialise an AJAX request
        url: job_url, // set the url of the request ()
        data: {
            "request_country_id": countryId // add the country id to the GET parameters
        },
        success: function (data){ // data is the return of the load_cities view function
            $("#id_request_city").html(data)// replace the contents of the city input with the data that came from the server 

        }


    })
})