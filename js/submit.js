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
        payloadObj.problemID = $('meta[name="problemID"]').attr('content');
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

    var nTestCases = response.testCaseDetails.length;
    var passes = 0;
    for (var i = 0; i < nTestCases; i++) {
        passes += response.testCaseDetails[i].passed ? 1 : 0;
    }
    document.getElementById('result-text').innerHTML
        += ' Passed ' + passes + '/' + nTestCases + ' test cases.<br><br>';

    // Print all the test case details.
    for (var i = 0; i < nTestCases; i++) {
        testCasePanelTitle = 'Test case ' + (i+1) + '/' + nTestCases
            + ' (' + response.testCaseDetails[i].testCaseType + '): ';
        if (response.testCaseDetails[i].passed) {
            testCasePanelTitle += 'passed!<br>';
        } else {
            testCasePanelTitle += 'failed.<br>';
        }

        processInfoString = 'Return code ' + response.testCaseDetails[i].processInfo.returnCode + ', '
            + 'utime: ' + response.testCaseDetails[i].processInfo.utime + ' s, '
            + 'stime: ' + response.testCaseDetails[i].processInfo.stime + ' s, '
            + 'maxrss: ' + response.testCaseDetails[i].processInfo.maxrss + ' kB.<br>';


        document.getElementById('result-text').innerHTML
            += '<div class="panel panel-default">'
            +  '<div class="panel-heading" style="font-size: medium;">' + testCasePanelTitle + '</div>'
            +  '<div class="panel-body" style="font-family: monospace; font-size: medium;">'
            +  processInfoString
            +  'Input:<br>' + response.testCaseDetails[i].inputString + '<br><br>'
            +  'Output:<br>' + response.testCaseDetails[i].outputString
            + '</div></div>';
    }
}

function handleAjaxError(response) {
    console.log("AJAX error!");
    console.log(response);
    document.getElementById('result-text').innerHTML += "AJAX error!";
}