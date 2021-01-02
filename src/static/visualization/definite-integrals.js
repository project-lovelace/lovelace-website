function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: rectangles = ${input[0]}, width = ${input[1]} <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: area = ${output[0]} (expected ${expected[0]}) <br>`

    return
}
