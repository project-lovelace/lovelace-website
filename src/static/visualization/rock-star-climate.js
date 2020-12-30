function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: S = ${input[0]}, a = ${input[1]}, ε = ${input[2]} <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: T = ${output[0]} (expected ${expected[0]}) <br>`

    return
}
