import './App.css';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home'
import Header from './pages/Header'

function App() {
  return (
    <div>
      <Header />
        <Routes>
          <Route path="/" element={<Home />}/>
        </Routes>
    </div>
  );
}

export default App;
