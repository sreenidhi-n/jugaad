import AnimatedGif from './holder';
import upload from './folder.gif'

function Image() {
  return (
      <AnimatedGif src={upload} alt="image upload"/>
  );
}

export default Image;