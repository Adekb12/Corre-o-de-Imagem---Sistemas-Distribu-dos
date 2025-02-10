import * as React from 'react';
import { styled } from '@mui/material/styles';
import Button from '@mui/material/Button';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import CircularProgress from '@mui/material/CircularProgress';
import { useState } from 'react';

const VisuallyHiddenInput = styled('input')({
  clip: 'rect(0 0 0 0)',
  clipPath: 'inset(50%)',
  height: 1,
  overflow: 'hidden',
  position: 'absolute',
  bottom: 0,
  left: 0,
  whiteSpace: 'nowrap',
  width: 1,
});

export default function InputFileUpload() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [result, setResult] = useState(null);
  const [llamaResponse, setLlamaResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setSelectedFile(file);
      handleUpload(file);
    }
  };

  const handleUpload = async (file) => {
    if (!file) {
      alert('Selecione uma imagem antes de enviar!');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    setLoading(true);

    try {
      const response = await fetch('http://localhost:8000/process_image/', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Erro ao enviar a imagem');
      }

      const data = await response.json();
      setResult(data.corrected_colors);
      setLlamaResponse(data.llama_response);
    } catch (error) {
      alert('Ocorreu um erro ao processar a imagem.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ textAlign: 'center', padding: '20px' }}>
      <Button
        component="label"
        variant="contained"
        startIcon={<CloudUploadIcon />}
        disabled={loading}
      >
        {loading ? 'Enviando...' : 'Enviar Imagem'}
        <VisuallyHiddenInput type="file" onChange={handleFileChange} accept="image/*" />
      </Button>

      {loading && (
        <div style={{ marginTop: '20px' }}>
          <CircularProgress />
          <p>Processando imagem...</p>
        </div>
      )}

      {!loading && result && (
        <div style={{ marginTop: '20px', textAlign:"center" , display: "flex", flexDirection: "column", alignItems: "center" }}>
          <h3>Cor Corrigida:</h3>
          <p>{JSON.stringify(result)}</p>
          <h3>Resposta do Llama:</h3>
          <p>{llamaResponse}</p>
        </div>
      )}
    </div>
  );
}
