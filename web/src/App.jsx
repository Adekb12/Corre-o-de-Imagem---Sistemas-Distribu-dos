import { useState } from 'react';
import './App.css';
import UploadButton from './assets/components/uploadButton/uploadButton';

function App() {
  return (
    <div className="App">
      <div className="card">
        <h1>Color Torra</h1>
        <h3>Bem vindo ao sistema de identificação do ponto de torra do café, clique no botão abaixo para enviar a imagem</h3>
        <UploadButton />
      </div>
    </div>
  );
}

export default App;
