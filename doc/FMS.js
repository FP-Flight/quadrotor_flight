// fsm-config: {"rankdir": "UD"}
// fsm-begin  <------!important

// Note
// In VSCode, you can install an extension named "Power FSM Viewer."
// To use it, press Ctrl+Shift+P and input "FSM View: Open."

// arrow style
class Style {
    static dashed = 'dashed' //--
    bold = 'bold'
}

var Event = {
    complete:'complete',
    init:'init'

}

var State = {
    MANUAL_CTRL : 'MANUAL_CTRL',
    CMD_CTRL : 'CMD_CTRL',
    AUTO_LAND : 'AUTO_LAND',
    AUTO_TAKEOFF : 'AUTO_TAKEOFF',
    AUTO_HOVER : 'AUTO_HOVER'
}



let myFsm = new WhateverFSM({
    events: [
    {
        name: Event.init, 
        from: "system_start", 
        to: State.MANUAL_CTRL, 
        style: Style.dashed,
    },    
    {
        name: Event.complete, 
        from: State.MANUAL_CTRL, 
        to: State.AUTO_TAKEOFF, 
        style: Style.bold,
    },
    {
        name: Event.complete, 
        from: State.MANUAL_CTRL, 
        to: State.AUTO_HOVER, 
        style: Style.dotted,
    },
    {
        name: Event.complete, 
        from: State.AUTO_TAKEOFF, 
        to: State.AUTO_HOVER, 
        style: Style.solid,
    },
    {
        name: Event.complete, 
        from: State.CMD_CTRL, 
        to: State.MANUAL_CTRL, 
        style: Style.solid,
    },
    {
        name: Event.complete, 
        from: State.AUTO_HOVER, 
        to: State.AUTO_LAND, 
        style: Style.solid,
    },
    {
        name: Event.complete, 
        from: State.AUTO_LAND, 
        to: State.AUTO_HOVER, 
        style: Style.solid,
    },
    {
        name: Event.complete, 
        from: State.CMD_CTRL, 
        to: State.AUTO_HOVER, 
        style: Style.solid,
    },
    {
        name: Event.complete, 
        from: State.AUTO_HOVER, 
        to: State.MANUAL_CTRL, 
        style: Style.solid,
    },
    {
        name: Event.complete, 
        from: State.AUTO_LAND, 
        to: State.MANUAL_CTRL, 
        style: Style.solid,
    },





]
})

// fsm-end    <------!important