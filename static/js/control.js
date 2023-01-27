import { renderer, scene, camera, cube, texture_list } from "./init.js"
import { scan_btn } from "./DOM.js"

var SPEED = 0.03

const update = (cnt, order) => {
    if (document.getElementsByTagName("img")) {
        var url_img = document.getElementsByTagName("img")[cnt - 1].src
    }
    var texture = new THREE.TextureLoader().load(url_img, () => { renderer.render(scene, camera) })
    //rotate image for 6 times
    if (cnt == 6) {
        var img = new Image()
        img.src = url_img
        var mapCanvas = document.createElement('canvas')
        mapCanvas.width = mapCanvas.height = 300
        var ctx = mapCanvas.getContext('2d')
        ctx.translate(300 / 2, 300 / 2)
        ctx.rotate(-Math.PI / 2)
        ctx.translate(-300 / 2, -300 / 2)
        ctx.drawImage(img, 0, 0, 300, 300)
        texture = new THREE.Texture(mapCanvas)
        texture.needsUpdate = true
    }
    texture_list[order] = new THREE.MeshBasicMaterial({ map: texture })
}
const rotate_x = () => {
    var stop_x = cube.rotation.x
    var i = setInterval(function () {
        cube.rotation.x -= SPEED
        renderer.render(scene, camera)
        if (cube.rotation.x <= stop_x - Math.PI * 90 / 180) {
            stop_x = cube.rotation.x
            clearInterval(i)
            scan_btn.disabled = false
        }
    }, 30)
}
const rotate_y = () => {
    var stop_y = cube.rotation.y
    //requestAnimationFrame(render)
    var i = setInterval(function () {
        cube.rotation.y -= SPEED
        renderer.render(scene, camera)
        if (cube.rotation.y <= stop_y - Math.PI * 90 / 180) {
            stop_y = cube.rotation.y
            clearInterval(i)
            scan_btn.disabled = false
        }
    }, 30)
}
const rotate_z = () => {
    var stop_z = cube.rotation.z
    var i = setInterval(function () {
        cube.rotation.z -= SPEED
        renderer.render(scene, camera)
        if (cube.rotation.z <= stop_z - Math.PI * 90 / 180) {
            stop_z = cube.rotation.z
            clearInterval(i)
            scan_btn.disabled = false
        }
    }, 30)
}
export {
    update as update,
    rotate_x as rotateX,
    rotate_y as rotateY,
    rotate_z as rotateZ
}