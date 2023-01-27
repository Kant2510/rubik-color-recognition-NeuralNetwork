import { capture_btn, dot, scan_status } from '../DOM.js'

color_obj = {
    yellow: "rgb(255, 255, 0)",
    blue: "rgb(0, 0, 255)",
    red: "rgb(255, 0, 0)",
    green: "rgb(0, 128, 0)",
    orange: "rgb(255, 165, 0)",
    white: "rgb(255, 0, 0)"
}
export default function recognition(cameraOutput) {
    $.ajax({
        url: '/recognition',
        type: 'POST',
        data: cameraOutput.src.replace("data:image/png;base64,", ""),
        success: response => {
            for (var i = 0; i < 9; i++) {
                dot[i].style.backgroundColor = color_obj[response.colors[i]]
            }
            scan_status.innerHTML = "Done!"
            capture_btn.disabled = false
        }
    })
}