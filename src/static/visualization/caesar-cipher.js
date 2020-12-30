function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: ciphertext = ${input[0]}, word = ${input[1]} <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: plaintext = ${output[0]} (expected: ${expected[0]}) <br>`

    return
}
