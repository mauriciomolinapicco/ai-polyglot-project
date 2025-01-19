import React from 'react'

const Translated = ({text, translation, onClick}) => {
  return (
    <div className='results'>
      <label>Original text 👇</label>
      <p className='result-p'>{text}</p>
      <label>Translation 👇</label>
      <p className='result-p'>{translation}</p>
      <button onClick={onClick}>Start Over</button>
    </div>
  )
}

export default Translated
