function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: blood type = ${input[0]} (available blood types = ${input[1]}) <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: survive = ${output[0]} (expected ${expected[0]}) <br>`

    return
}
