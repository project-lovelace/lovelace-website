function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: <br>` +
        `x = ${input[0]} <br>` +
        `y = ${input[1]} <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: correlation coefficient = ${output[0]} (expected ${expected[0]}) <br>`

    return
}
