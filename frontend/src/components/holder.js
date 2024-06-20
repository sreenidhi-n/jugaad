import React from "react";

const AnimatedGif = ({src, alt}) =>{
    const divStyle = { 
        textAlign: 'center'
    };
    return(
    <div style={divStyle}>
        <img src={src} alt={alt} style={{width:"210px",height: "210px" ,animation: "rotate 2s infinite" }} />
    </div>
    );
};

export default AnimatedGif;
