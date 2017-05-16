var form = document.getElementById("code-submit-form");
var apiUrl =  "http://localhost:8000/submit";

function readCodeFile(event) {
    var file = document.querySelector('input[type=file]').files[0];
    var reader = new FileReader();

    reader.addEventListener("load", function () {
        console.log("Done reading file.");
        document.getElementById('result-text').innerHTML = "File read.<br>";

        rawResult = reader.result; // base64 encoded
        data = rawResult.substring(26) // discard substring "data:text/plain;base64,"     

        var payloadObj = new Object();
        payloadObj.code = data;
        payloadObj.problemID = 1;
        var payload = JSON.stringify(payloadObj);
        
        $.ajax({
            type: "POST",
            url: apiUrl,
            contentType: "text/plain",
            success: handleAjaxSuccess,
            error: handleAjaxError,
            data: payload
        });
    }, false);

    if (file) {
        console.log("Reading file...")
        reader.readAsDataURL(file);
    }
};

$('#code-submit-form').submit(function () {
    readCodeFile();
    return false;
});

function handleAjaxSuccess(response) {
    console.log("AJAX success!");
    console.log(response);
    if (response.success) {
        document.getElementById('result-text').innerHTML += "Success!";
    } else {
        document.getElementById('result-text').innerHTML += "Failed.";
    }
    document.getElementById('result-text').innerHTML += response.details;
}

function handleAjaxError(response) {
    console.log("AJAX error!");
    console.log(response);
    document.getElementById('result-text').innerHTML += "AJAX error!";
}