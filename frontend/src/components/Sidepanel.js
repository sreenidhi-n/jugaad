import React from 'react'
import "./Sidepanel.css"
function Sidepanel(Params) {
  return (
    <div className='sticky-right'>
       {Params.children}
    </div>
  )
}

export default Sidepanel