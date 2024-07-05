import {React,useState} from 'react'
import Navbar from "../components/Navigation"
import Button from '../components/Button';
import  Checklist from '../components/Checkslit';
import FolderList from '../components/FolderList'
import Sidepanel from '../components/Sidepanel';
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
				<FolderList />
				<Button
					val="Analyze Using AI"
					onClick={check_list}
				/>
			</dir>
			{!hidden && <Checklist reset={call_by_check_to_reset} />}
			<Sidepanel>
				magu
			</Sidepanel>
		</div>
	);
}

export default Dirs