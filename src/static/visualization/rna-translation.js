function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: RNA = "${input[0]}" <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: amino acid sequence = "${output[0]}" (expected "${expected[0]}") <br>`

    return
}
