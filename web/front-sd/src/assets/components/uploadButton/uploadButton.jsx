import * as React from 'react';
import { styled } from '@mui/material/styles';
import Button from '@mui/material/Button';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
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
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setSelectedFile(file);
      handleUpload(file); // Chama a função de upload automaticamente após selecionar o arquivo
    }
  };

  const handleUpload = async (file) => {
    if (!file) {
      alert('Selecione uma imagem antes de enviar!');
      return;
    }

    const formData = new FormData();
    formData.append('image', file);

    setLoading(true);

    try {
      const response = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Erro ao enviar a imagem');
      }

      const data = await response.json();
      setResult(data.corrected_color);
    } catch (error) {
      console.error('Erro:', error);
      alert('Ocorreu um erro ao processar a imagem.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <Button
        component="label"
        role={undefined}
        variant="contained"
        tabIndex={-1}
        startIcon={<CloudUploadIcon />}
        disabled={loading}
      >
        {loading ? 'Enviando...' : 'Enviar Imagem'}
        <VisuallyHiddenInput
          type="file"
          onChange={handleFileChange}
          accept="image/*"
        />
      </Button>
      {result && (
        <div style={{ marginTop: '20px' }}>
          <h3>Cor Corrigida:</h3>
          <p>{JSON.stringify(result)}</p>
        </div>
      )}
    </div>
  );
}