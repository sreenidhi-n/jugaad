import React from 'react'
function Button(Params) {
	
  return (
		<button
			type="button"
			className="btn btn-primary"
			id="rounded-rectangle_btn"
		  onClick={Params.onClick}
		  style={Params.style}
		>
			<h1>{Params.val}</h1>
		</button>
	);
}

export default Button   