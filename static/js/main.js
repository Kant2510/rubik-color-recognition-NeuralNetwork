import initAll from './init.js'


// Set constraints for the video stream
var constraints = {
    video: {
        facingMode: "environment"
    },
    audio: false
};
// Define constants
const cameraView = document.querySelector("#camera--view")
// Access the device camera and stream to cameraView
function cameraStart() {
    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(stream => {
            // const track = stream.getTracks()[0];
            cameraView.srcObject = stream;
        })
        .catch(error => {
            console.error("Oops. Something is broken.", error);
        });
}
initAll()


// Start the video stream when the window loads
window.addEventListener("load", cameraStart, false);
