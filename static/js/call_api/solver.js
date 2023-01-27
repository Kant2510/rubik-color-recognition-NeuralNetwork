export default function solver(color_letter) {
    $.ajax({
        url: '/solve',
        type: 'POST',
        data: color_letter,
        success: response => {
            document.getElementById("solve-result").innerHTML = "Result: " + response.step.replace(/,/g, "")
        }
    })
}