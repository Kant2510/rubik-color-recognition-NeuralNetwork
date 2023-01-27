const renderer = new THREE.WebGLRenderer({ antialias: true })

var WIDTH = 200
var HEIGHT = 200

var texture_list = []
var scene, camera, cube

const initScene = () => {
    scene = new THREE.Scene()
    var loader = new THREE.TextureLoader()
    loader.crossOrigin = true
}

const initCamera = () => {
    camera = new THREE.PerspectiveCamera(40, WIDTH / HEIGHT, 1, 10)
    camera.position.set(2, 2, 5)
    camera.lookAt(scene.position)
    scene.add(camera)
}
const initCube = () => {
    var texture0 = new THREE.TextureLoader().load("/static/img/0.jpg", () => { renderer.render(scene, camera) })
    for (var i = 0; i < 6; i++) {
        texture_list.push(new THREE.MeshBasicMaterial({ map: texture0 }))
    }
    cube = new THREE.Mesh(new THREE.BoxGeometry(2, 2, 2), texture_list)
    cube.rotation.x = Math.PI * 90 / 180
    scene.add(cube)
}
const initRender = () => {
    document.getElementById("container").appendChild(renderer.domElement)
    renderer.setSize(WIDTH, HEIGHT)
}
export default function initAll() {
    initScene()
    initCamera()
    initCube()
    initRender()
}
export { renderer, scene, camera, cube, texture_list }