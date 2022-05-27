// hide buttons

window.onload = function () {
    console.log("dom is ready!");

    function clear() {
        $('#err_result').hide()
        $('#alert_result').hide()
        $('#result_text').hide()
    }

    function show_correct_result(result) {
        $('#logo').hide()
        clear()
        $('#alert_result').show()
        $('#result_text').show()
        $('#result_text').val(result['output'])
        $('#translated_text').show()
        $('#translated_text').val(result['translated'])
    }

    function show_err_result(result) {
        $('#logo').hide()
        clear()
        $('#err_result').show()
        $('#result_text').show()
        $('#result_text').val(result['error'])
    }

    clear()

    $("#upload_image").dropzone({
        maxFiles: 2000,
        success: function (file, response) {
            show_correct_result(response)
        }
    });

    console.log('CAI');

    $('#search').on('click', function (event) {
        $('#err_result').hide()
        $('#alert_result').hide()
        //$('#result_text').hide()

        const value = $('#image_url').val();
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: "/ocrit",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({"image_url": value}),
            success: function (result) {
                console.log(result);
                if (typeof (result['error']) != "undefined") {
                    show_err_result(result)
                } else {
                    show_correct_result(result)
                }
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
};

