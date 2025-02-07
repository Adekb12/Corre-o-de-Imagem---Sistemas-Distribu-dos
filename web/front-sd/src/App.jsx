import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import UploadButton from './assets/components/uploadButton/uploadButton'

function App() {


  return (
    <div className="App">
      <div className="card">
        <h1>Color Torra</h1>
        <h3>Bem vindo ao sistema de identificacao do ponto de torra do cafe, clique no botão abaixo para enviar a imagem</h3>
        <UploadButton/>
      </div>
    </div>
  )
}

export default App
