function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: A = ${input[0]}, B = ${input[1]} <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: ${output[0]} (expected ${expected[0]}) <br>`

    return
}
