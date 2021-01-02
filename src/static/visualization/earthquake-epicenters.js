function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: <br>` +
        `(x1, y1), t1 = (${input[0]}, ${input[1]}), ${input[2]} <br>` +
        `(x2, y2), t2 = (${input[3]}, ${input[4]}), ${input[5]} <br>` +
        `(x3, y3), t3 = (${input[6]}, ${input[6]}), ${input[7]} <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: <br>` +
        `(x0, y0) = (${output[0]}, ${output[1]}) [expected (${expected[0]}, ${expected[1]})] <br>`

    return
}
