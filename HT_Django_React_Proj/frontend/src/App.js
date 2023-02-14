// react imports
import { BrowserRouter, Routes, Route } from 'react-router-dom';

// project imports
import Welcome from './pages/welcome/welcome.component';
import Login from './pages/login/login.component';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Welcome />}/>
        <Route path='login' element={<Login />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
