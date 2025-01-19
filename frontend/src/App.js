import './App.css';
import Box from './components/Box'
import Translated from './components/Translated'
import Banner from './components/Banner'
import {useState} from 'react';

function App() {
  const [showForm, setShowForm] = useState(true)
  const [showResults, setShowResults] = useState(false)
  const [translationData, setTranslationData] = useState({ text: '', translation: '' });

  const onStartOver = () => {
    setShowResults(false)
    setShowForm(true)
  }

  const translate = async (data) => {
    console.log(data)
    try {
      const response = await fetch('http://127.0.0.1:8000', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({message:data.text, language:data.selectedOption})
      });
  
      // if (!response.ok) {
      //   throw new Error('There was an error');
      // }
  
      const responseData = await response.json();
      console.log(responseData); 
      setShowForm(false)
      setTranslationData({ text: data.text, translation: responseData.response });
      setShowResults(true)
    } catch (error) {
      console.error('Error:', error);
    }
  }
  
  return (
    <>
    <Banner />
    { showForm && <Box translate={translate}/> }
    { showResults && <Translated text={translationData.text} onClick={onStartOver} translation={translationData.translation}/> }
    </>
  );
}

export default App;
