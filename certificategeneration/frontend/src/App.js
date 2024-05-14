import { BrowserRouter, Route, Routes } from "react-router-dom";
import Templatelist from "./pages/templatelist";
import CertGen from "./pages/certgen";
import FormResults from "./components/formresults";
import Details from "./components/trailform";
import './App.css'



function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<Templatelist/>} />
          <Route path="/certgen" element={<CertGen />} />
          <Route path="/formresults" element={<FormResults />} />
          <Route path="/trailform" element={<Details />} />
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App;
