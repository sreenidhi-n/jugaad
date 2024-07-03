import {React,useState} from 'react'
import Navbar from "../components/Navigation"
import Button from '../components/Button';
import  Checklist from '../components/Checkslit';
function Dirs() {
  const [hidden, setHidden] = useState(true)
  const [blur, setBlur] = useState(false)
  const check_list =()=>{
    setHidden(false)
    setBlur(true)
  }
  const call_by_check_to_reset = () => {
    setHidden(true)
    setBlur(false)
  }

  return (
		<div>
			<dir style={blur ? { filter: "blur(8px)" } : {}}>
				<Navbar  />
				<h3>This is Dirs page</h3>
				<Button
					val="Analyze Using AI"
					onClick={check_list}
				/>
			</dir>
			{!hidden && <Checklist reset={call_by_check_to_reset} />}
		</div>
	);
}

export default Dirs