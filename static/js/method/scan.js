import { scan_btn, scan_status } from '../DOM.js'
import creatImg from '../createImg.js'
import recognition from '../call_api/recognition.js'

scan_btn.onclick = () => {

    scan_btn.disabled = true
    scan_status.innerHTML = "Scanning..."
    scan_status.style.display = "block"

    const cameraOutput = creatImg()

    recognition(cameraOutput)

    cameraOutput.classList.add("taken");
    document.getElementById("image-list").appendChild(cameraOutput)
}