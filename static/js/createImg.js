import { cameraView, cameraSensor } from './DOM.js'

export default function creatImg() {
    var cameraOutput = document.createElement("img")
    cameraSensor.width = cameraView.videoWidth
    cameraSensor.height = cameraView.videoHeight
    cameraSensor.getContext("2d").drawImage(cameraView, 0, 0)
    // function aa(){
    //     var p = document.createElement("p")
    //     p.innerHTML = document.getElementsByClassName("nhac-in").value+""+document.getElementById("rgb01")
    //     document.getElementById("nhac-div").appendChild(p)}
    const canvass = document.createElement('canvas')
    canvass.width = 300
    canvass.height = 300
    canvass.getContext('2d').drawImage(cameraSensor, -90, -170)
    cameraOutput.src = canvass.toDataURL("image/jpg")
    return cameraOutput
}