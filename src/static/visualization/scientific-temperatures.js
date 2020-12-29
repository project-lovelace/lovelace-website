function format_input(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: ${input[0]} °F <br>`
    return
}

function format_output(input, output, expected, n) {
    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: ${output[0]} °C (expected ${expected[0]} °C) <br>`
    return
}
