import './App.css';
import { BrowserRouter, Routes, Route, useNavigate } from "react-router-dom";
import Create from './create/create';
import Main from './main/main';
import Button from './ui-elements/button/button';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Main />} />
        <Route path="buttons" element={<Button shadow="shadow" size='big' title='Начать' />} />
        <Route path='create' element={<Create />} />
      </Routes>
      </BrowserRouter>
  );
}

export default App;
