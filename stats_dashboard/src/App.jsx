import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Home from './pages/Home/Home';
import Pitchers from './pages/Pitchers/Pitchers';
import Hitters from './pages/Hitters/Hitters';
function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Home  />}/>
        <Route path='/pitchers' element={<Pitchers />}/>
        <Route path='/hitters' element={<Hitters />}/>

      </Routes>
    </Router>

    
  );
}

export default App;
