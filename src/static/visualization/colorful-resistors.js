function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: band colors = ${input[0]} <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: <br>` +
        `nominal resistance = ${output[0]} (expected ${expected[0]}) <br>` +
        `minimum resistance = ${output[1]} (expected ${expected[1]}) <br>` +
        `maximum resistance = ${output[2]} (expected ${expected[2]})`

    return
}
