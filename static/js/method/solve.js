import solver from '../call_api/solver.js'
import { solve_btn } from '../DOM.js'
import { color_letter } from './capture.js'

solve_btn.onclick = () => {
    //color_letter = 'boobyowbgoogbbowyrrwwwrbyyroyyrgrwwrggywoybrbgrbgwgogy'
    solver(color_letter)
}