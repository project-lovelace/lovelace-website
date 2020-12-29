function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: ${input[0]} m <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: ${output[0]} s (expected ${expected[0]} s) <br>`

    return
}
