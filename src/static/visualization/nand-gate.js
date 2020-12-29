function format_input(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: A = ${input[0]}, B = ${input[1]} <br>`
    return
}

function format_output(input, output, expected, n) {
    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: ${output[0]} (expected ${expected[0]}) <br>`
    return
}
