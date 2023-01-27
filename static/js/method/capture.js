import { update, rotateX, rotateY } from '../control.js'
import { capture_btn, dot, scan_status, solve_btn } from '../DOM.js'

var click = 1
var color_letter = ''
function find_key(val) {
    for (const [key, value] of Object.entries(color_obj)) {
        if (value == val) {
            return key
        }
    }
}
capture_btn.onclick = () => {
    if (click == 6) {
        capture_btn.disabled = true
        solve_btn.disabled = false
    }
    capture_btn.disabled = true
    scan_status.style.display = "none"
    for (var i = 0; i < 9; i++) {
        if (click == 6) {
            color_letter += find_key(dot[8 - i].style.backgroundColor)[0]
        }
        else if (click == 1) {
            color_letter += find_key(dot[6 + (i - (i % 3)) / 3 - 3 * (i % 3)].style.backgroundColor)[0]
        }
        else {
            color_letter += find_key(dot[i].style.backgroundColor)[0]
        }
    }
    switch (click) {
        case 1:
            update(click, 2)
            break
        case 2:
            update(click, 4)
            break
        case 3:
            update(click, 0)
            break
        case 4:
            update(click, 5)
            break
        case 5:
            update(click, 1)
            break
        case 6:
            update(click, 3)
            break
    }
    if (click == 1 || click == 5) {
        rotateX()
    }
    if (click > 1 && click < 5) {
        rotateY()
    }
    click++
}
export { color_letter }