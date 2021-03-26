function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: ${input[0]} <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: classification = "${output[0]}" (expected "${expected[0]}"), strength = "${output[1]}" (expected "${expected[1]}") <br>`

    return
}
